import os
import json
import requests
import re
from PIL import Image
import colorsys

# === Przetwarzanie HLS ===

def apply_hls_adjustment(image, hue_shift=0.0, lightness_mul=1.0, saturation_mul=1.0):
    img = image.convert("RGB")
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = [v / 255.0 for v in pixels[x, y]]
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            h = (h + hue_shift) % 1.0
            l = max(0.0, min(1.0, l * lightness_mul))
            s = max(0.0, min(1.0, s * saturation_mul))
            r, g, b = colorsys.hls_to_rgb(h, l, s)
            pixels[x, y] = tuple(int(c * 255) for c in (r, g, b))
    return img

# === Presety kolorystyczne ===

PRESETS = [
    ("Forma Letnia", lambda img: apply_hls_adjustment(img, hue_shift=0.04, lightness_mul=1.1, saturation_mul=1.3)),
    ("Forma Nocna", lambda img: apply_hls_adjustment(img, hue_shift=0.60, lightness_mul=0.6, saturation_mul=0.6)),
    ("Forma Jesienna", lambda img: apply_hls_adjustment(img, hue_shift=0.08, lightness_mul=0.9, saturation_mul=0.8)),
    ("Forma Księżycowa", lambda img: apply_hls_adjustment(img, hue_shift=0.7, lightness_mul=1.2, saturation_mul=0.9)),
    ("Forma Tropikalna", lambda img: apply_hls_adjustment(img, hue_shift=0.3, lightness_mul=1.1, saturation_mul=1.4)),
    ("Forma Wiosenna", lambda img: apply_hls_adjustment(img, hue_shift=0.9, lightness_mul=1.0, saturation_mul=0.6)),
    ("Forma Cieniowana", lambda img: apply_hls_adjustment(img, hue_shift=0.75, lightness_mul=0.7, saturation_mul=1.2)),
    ("Forma Niebieska Mgła", lambda img: apply_hls_adjustment(img, hue_shift=0.6, lightness_mul=1.3, saturation_mul=0.4)),
    ("Forma Upiorna", lambda img: apply_hls_adjustment(img, hue_shift=0.66, lightness_mul=0.8, saturation_mul=0.3)),
    ("Forma Cukierkowa", lambda img: apply_hls_adjustment(img, hue_shift=0.95, lightness_mul=1.2, saturation_mul=1.6)),
    ("Forma Dzika", lambda img: apply_hls_adjustment(img, hue_shift=0.2, lightness_mul=1.0, saturation_mul=1.8)),
    ("Forma Lodowa", lambda img: apply_hls_adjustment(img, hue_shift=0.55, lightness_mul=1.3, saturation_mul=1.0))
]

def fetch_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1025"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        mapping = {str(i + 1).zfill(3): p["name"] for i, p in enumerate(data["results"])}
        with open("pokemon_names.json", "w", encoding="utf-8") as f:
            json.dump(mapping, f, indent=4)
        return mapping
    else:
        print("❌ Błąd przy pobieraniu nazw Pokémonów.")
        return {}

def load_pokemon_names(json_file):
    return fetch_pokemon_names() if not os.path.exists(json_file) else json.load(open(json_file, encoding="utf-8"))

def process_images(input_folder, process_fn, output_folder):
    folders = {
        "txt": os.path.join(input_folder, "pokemon"),
        "txt-shiny": os.path.join(input_folder, "pokemon-shiny"),
        "sprite": os.path.join(input_folder, "sprite"),
        "sprite-shiny": os.path.join(input_folder, "sprite-shiny")
    }

    mapping = load_pokemon_names("pokemon_names.json")
    skipped_sprites = []
    folder_contents = {}

    for key, folder in folders.items():
        if not os.path.exists(folder):
            print(f"⚠️ Folder '{folder}' nie istnieje — pomijam.")
            continue

        print(f"📁 Przetwarzanie: {folder}")
        for filename in os.listdir(folder):
            if not filename.endswith(".png"):
                continue
            file_path = os.path.join(folder, filename)
            name, _ = os.path.splitext(filename)

            # SPRITE: przemapuj numer na nazwę
            if key.startswith("sprite"):
                match = re.match(r"^(\d{3})(?:-(.*))?$", name)
                if not match:
                    print(f"⏭️ Pominięto: {filename}")
                    skipped_sprites.append(filename)
                    continue
                number = match.group(1)
                suffix = match.group(2) if match.group(2) else ""
                poke_name = mapping.get(number)
                if not poke_name:
                    print(f"⚠️ Brak nazwy dla numeru {number}")
                    skipped_sprites.append(filename)
                    continue
                final_name = f"{poke_name.lower()}-{suffix}" if suffix else poke_name.lower()
            else:
                final_name = name  # txt/txt-shiny

            target_dir = os.path.join(output_folder, final_name)
            os.makedirs(target_dir, exist_ok=True)
            output_file = os.path.join(target_dir, f"{key}.png")

            try:
                img = Image.open(file_path)
                processed = process_fn(img)
                processed.save(output_file)
                print(f"✅ Zapisano: {output_file}")
                folder_contents.setdefault(final_name, []).append(f"{key}.png")
            except Exception as e:
                print(f"❌ Błąd: {file_path} — {e}")

    # === RAPORTY KOŃCOWE ===
    print("\n📋 Raport:")
    if skipped_sprites:
        print("⚠️ Pominięte sprite’y (błędna nazwa lub brak mapowania):")
        for fname in skipped_sprites:
            print(f"   - {fname}")
    else:
        print("✅ Wszystkie sprite’y zostały poprawnie przetworzone.")

    print("\n📦 Sprawdzenie kompletności folderów Pokémonów:")
    expected = {"txt.png", "txt-shiny.png", "sprite.png", "sprite-shiny.png"}
    for folder, files in folder_contents.items():
        missing = expected - set(files)
        if missing:
            print(f"⚠️ {folder} — brak plików: {', '.join(sorted(missing))}")
    print("\n✅ Przetwarzanie zakończone.\n")

def show_menu():
    print("🎨 Wybierz formę kolorystyczną:")
    for i, (name, _) in enumerate(PRESETS, 1):
        print(f"{i}. {name}")
    while True:
        try:
            choice = int(input(f"Wybierz formę (1–{len(PRESETS)}): "))
            if 1 <= choice <= len(PRESETS):
                return PRESETS[choice - 1]
            print("❗ Podaj poprawny numer.")
        except ValueError:
            print("❗ Podaj numer jako liczbę.")

def ask_output_folder():
    while True:
        name = input("📂 Podaj nazwę folderu wynikowego (np. 'formy-test-1'): ").strip()
        if name:
            return os.path.join("images", name)
        print("❗ Nazwa folderu nie może być pusta.")

if __name__ == "__main__":
    input_dir = "images"
    effect_name, effect_fn = show_menu()
    output_dir = ask_output_folder()
    print(f"\n🔧 Przetwarzanie: {effect_name}")
    process_images(input_dir, effect_fn, output_dir)
