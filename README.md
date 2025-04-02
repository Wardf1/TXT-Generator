
# 🎨 Pokemon Texture Generator

Skrypt do przetwarzania grafik Pokémonów przy użyciu stylizowanych presetów kolorystycznych dla Pixelmon Generations. Obsługuje jednocześnie:
```markdown
- `txt.png` z folderu `pokemon/`
- `txt-shiny.png` z folderu `pokemon-shiny/`
- `sprite.png` z folderu `sprite/`
- `sprite-shiny.png` z folderu `sprite-shiny/`
```
Każdy preset modyfikuje barwę (Hue), jasność (Lightness) i nasycenie (Saturation) obrazu, tworząc unikalny efekt stylistyczny.

---

## 🧰 Wymagania

- Python 3.8+
- Pillow:  
  ```bash
  pip install pillow
  ```
- requests:  
  ```bash
  pip install requests
  ```
- Plik Pokemon Database Json
```html
https://github.com/Wardf1/TXT-Generator/blob/main/pokemon_names.json
```
---

## 📁 Struktura wejściowa

Pliki ``*.png`` powinny mieć format dla <b>txt</b> i <b>txt-shiny</b>: ``<pokemon>-<forma>.png`` oraz dla <b>sprite</b> i <b>sprite-shiny</b>: ``<dex-number-###>-<forma>.png``. Jeśli jest to forma bazowa to nie trzeba stosować ``-<forma>`` w nazwie pliku graficznego.</br></br>
Upewnij się, że masz folder `images/` z poniższymi podfolderami:

```
images/
├── pokemon/              # źródła dla txt.png (np. pikachu-cap.png)
├── pokemon-shiny/        # źródła dla txt-shiny.png
├── sprite/               # źródła dla sprite.png (np. 025-cap.png)
├── sprite-shiny/         # źródła dla sprite-shiny.png
```
Gotowa biblioteka TXT - [Pobierz z LimeWire](https://limewire.com/d/3cCxb#5OI0bhsxCG)

---

## 🚀 Uruchomienie

1. Uruchom skrypt:

```bash
python txt-generator.py
```

2. Wybierz preset kolorystyczny z listy:

```
🎨 Wybierz formę kolorystyczną:
1. Forma Letnia
2. Forma Nocna
3. Forma Jesienna
...
```

3. Podaj nazwę folderu wynikowego:

```
📂 Podaj nazwę folderu wynikowego: formy-lodowe
```

4. Skrypt przetworzy wszystkie dostępne obrazy i zapisze wyniki w:

```
images/formy-lodowe/<nazwa-pokemona-forma>/
├── txt.png
├── txt-shiny.png
├── sprite.png
├── sprite-shiny.png
```

---

## 🧪 Dostępne formy kolorystyczne

| Preset                   | Opis techniczny                                                                                             | Czy jest na serwerze? |
|--------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------|
| **Forma Letnia**         | Niewielkie przesunięcie odcienia (Hue +0.04), delikatne rozjaśnienie (x1.1), wyraźnie zwiększona intensywność (x1.3)       |                       |
| **Forma Nocna**          | Znaczny przesuw odcienia (Hue +0.60), silne przyciemnienie (x0.6), obniżona intensywność kolorów (x0.6)                  |                       |
| **Forma Jesienna**       | Małe przesunięcie odcienia (Hue +0.08), lekkie przyciemnienie (x0.9), częściowe odbarwienie (x0.8)                        |                       |
| **Forma Księżycowa**     | Duży przesuw odcienia (Hue +0.70), wyraźne rozjaśnienie (x1.2), lekka redukcja nasycenia (x0.9)                            |                       |
| **Forma Tropikalna**     | Średni przesuw odcienia (Hue +0.3), rozjaśnienie (x1.1), silne podbicie nasycenia (x1.4)                                  |                       |
| **Forma Wiosenna**       | Znaczny przesuw (Hue +0.9), brak zmiany jasności, niska nasycenie (x0.6)                                              |                       |
| **Forma Cieniowana**     | Znaczny przesuw (Hue +0.75), ciemniejsze kolory (x0.7), zwiększona intensywność (x1.2)                                    |                       |
| **Forma Niebieska Mgła** | Przesunięcie do chłodniejszego odcienia (Hue +0.6), duże rozjaśnienie (x1.3), mocne osłabienie koloru (x0.4)               | ✅                    |
| **Forma Upiorna**        | Chłodny przesuw (Hue +0.66), lekkie przyciemnienie (x0.8), bardzo niskie nasycenie (x0.3)                                 |                       |
| **Forma Cukierkowa**     | Przesunięcie w górę (Hue +0.95), rozjaśnienie (x1.2), bardzo wysokie nasycenie (x1.6)                                   |                       |
| **Forma Dzika**          | Średni przesuw (Hue +0.2), brak zmiany jasności, ekstremalne nasycenie (x1.8)                                          |                       |
| **Forma Lodowa**         | Chłodny przesuw (Hue +0.55), silne rozjaśnienie (x1.3), bez zmiany nasycenia                                          | ✅                    |
| **Forma Toxic**          | Przesunięcie w stronę zieleni (Hue +0.33), rozjaśnienie (x1.2), brak zmiany intensywności                               | ✅                    |
| **Forma Radioaktywna**   | Podobny przesuw jak wyżej (Hue +0.33), lekkie rozjaśnienie (x1.1), silne nasycenie (x1.4)                                |                       |
| **Forma Zatruta Mgła**   | Lekki przesuw (Hue +0.25), lekkie przyciemnienie (x0.9), niskie nasycenie (x0.5)                                       |                       |
| **Forma Cyberpunk**      | Silny przesuw (Hue +0.85), rozjaśnienie (x1.2), bardzo wysokie nasycenie (x1.6)                                        |                       |
| **Forma Neonowa**        | Lekki przesuw (Hue +0.1), bardzo silne rozjaśnienie (x1.3), maksymalne nasycenie (x1.8)                                |                       |
| **Forma Pastelowa**      | Niewielki przesuw (Hue +0.05), bardzo wysokie rozjaśnienie (x1.4), bardzo niskie nasycenie (x0.5)                        |                       |
| **Forma Duchowa**        | Przesuw (Hue +0.75), lekkie rozjaśnienie (x1.1), bardzo słabe kolory (x0.3)                                           |                       |
| **Forma Jadowita Noc**   | Przesunięcie ku zieleniom (Hue +0.35), przyciemnienie (x0.7), lekka redukcja nasycenia (x0.8)                           |                       |
| **Forma Technomagiczna** | Przesuw (Hue +0.58), rozjaśnienie (x1.2), podbite kolory (x1.3)                                                        |                       |
| **Forma Kryształowa**    | Przesuw do czystego niebieskiego (Hue +0.5), bardzo silne rozjaśnienie (x1.4), obniżone nasycenie (x0.7)                 |                       |
| **Forma Piekielna**      | Bardzo lekki przesuw (Hue +0.02), lekkie przyciemnienie (x0.9), bardzo wysokie nasycenie (x1.7)                         |                       |



---

## 📋 Raportowanie

Po zakończeniu przetwarzania skrypt automatycznie:

- wypisuje listę sprite’ów, które zostały **pominięte** (np. błędna nazwa pliku, brak mapowania numeru Pokémona),
- sprawdza kompletność każdego folderu z przetworzonym Pokémonem (czy ma wszystkie 4 pliki: `txt.png`, `txt-shiny.png`, `sprite.png`, `sprite-shiny.png`) i wypisuje brakujące pliki.

---

## 👀 Przykładowy raport:

```
📋 Raport:
⚠️ Pominięte sprite’y (błędna nazwa lub brak mapowania):
   - 999-a.png
   - 998.png

📦 Sprawdzenie kompletności folderów Pokémonów:
⚠️ pikachu-hat — brak plików: sprite-shiny.png
✅ Przetwarzanie zakończone.
```
