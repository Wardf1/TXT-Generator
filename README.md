
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

Pliki *.png powinny mieć format dla txt i txt-shiny: ``<pokemon>-<forma>.png`` oraz dla sprite i sprite-shiny: ``<dex-number-###>-<forma>.png``. Jeśli jest to forma bazowa to nie trzeba stosować ``-<forma>`` w nazwie pliku graficznego.</br></br>
Upewnij się, że masz folder `images/` z poniższymi podfolderami:

```
images/
├── pokemon/              # źródła dla txt.png (np. pikachu-cap.png)
├── pokemon-shiny/        # źródła dla txt-shiny.png
├── sprite/               # źródła dla sprite.png (np. 025-cap.png)
├── sprite-shiny/         # źródła dla sprite-shiny.png
```

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

| Preset                 | Styl                                                            |
|------------------------|-----------------------------------------------------------------|
| **Forma Letnia**           | Ciepłe, jasne kolory z podbitą nasyceniem                      |
| **Forma Nocna**            | Chłodne, przyciemnione barwy                                   |
| **Forma Jesienna**         | Żółto-pomarańczowe tony, lekko stonowane                       |
| **Forma Księżycowa**       | Fioletowo-niebieska tonacja, wysoka jasność                    |
| **Forma Tropikalna**       | Zielono-turkusowy filtr, bardzo żywa kolorystyka               |
| **Forma Wiosenna**         | Pastelowe róże, średnia jasność, niska nasycenie               |
| **Forma Cieniowana**       | Mroczne fiolety i zielenie, średnia saturacja                  |
| **Forma Niebieska Mgła**   | Błękitno-biała mgła, niskie nasycenie, wysoka jasność          |
| **Forma Upiorna**          | Zgaszone chłodne barwy z niską nasyceniem                      |
| **Forma Cukierkowa**       | Jaskrawe magenty i róże, wysoka jasność                        |
| **Forma Dzika**            | Ekstremalnie nasycone kolory, przesunięty hue                  |
| **Forma Lodowa**           | Jasny chłodny odcień błękitu z naturalną jasnością             |

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
