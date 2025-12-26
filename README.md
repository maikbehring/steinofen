# Steinofenbäcker Produkt-Website

Eine statische Website zur Anzeige aller Steinofenbäcker-Produkte von DataNature.de.

## Features

- 📦 Anzeige aller Produkte mit Bildern und Zutaten
- 🌱 Markierung veganer Produkte
- 🔍 Suchfunktion nach Produktnamen
- 📱 Responsive Design
- 🎨 Moderne, benutzerfreundliche Oberfläche

## Website-Struktur

Die Website befindet sich im Verzeichnis `website_datanature/`:

```
website_datanature/
├── index.html          # Haupt-HTML-Datei
├── style.css           # Stylesheet
├── products.json       # Produktdaten (JSON)
├── images/             # Produktbilder
│   └── [Produktname]/
│       └── datanature_bild_1.jpg
└── serve.py            # Lokaler Entwicklungsserver (optional)
```

## Lokale Entwicklung

### Voraussetzungen

- Python 3.x

### Lokalen Server starten

```bash
cd website_datanature
python3 serve.py
```

Die Website ist dann unter `http://localhost:8000` erreichbar.

Alternativ können Sie auch den integrierten Python HTTP-Server verwenden:

```bash
cd website_datanature
python3 -m http.server 8000
```

## Deployment auf Netlify

### Automatisches Deployment

1. Verbinden Sie das GitHub-Repository mit Netlify:
   - Gehen Sie zu [Netlify](https://www.netlify.com)
   - Klicken Sie auf "New site from Git"
   - Wählen Sie GitHub und das Repository `maikbehring/steinofen`

2. Build-Einstellungen:
   - **Build command:** (leer lassen - statische Website)
   - **Publish directory:** `website_datanature`

3. Deploy!

Die Website wird automatisch bei jedem Push ins `main`-Branch neu deployed.

### Manuelles Deployment

Falls Sie die Website manuell hochladen möchten:

1. Laden Sie den gesamten Inhalt des `website_datanature/` Verzeichnisses hoch
2. Netlify erkennt automatisch `index.html` als Einstiegsseite

## Datenaktualisierung

Die Produktdaten werden durch Scraping-Scripts aktualisiert (nicht im Repository enthalten):

- `download_datanature_all.py` - Lädt alle Produkte von DataNature.de herunter
- `build_datanature_website.py` - Erstellt die statische Website aus den heruntergeladenen Daten

Nach dem Ausführen dieser Scripts muss die Website neu gebaut werden:

```bash
python3 build_datanature_website.py
```

Anschließend die Änderungen committen und pushen:

```bash
git add website_datanature/
git commit -m "Update: Neue Produktdaten"
git push
```

## Technologien

- **HTML5** - Struktur
- **CSS3** - Styling
- **JavaScript** - Suchfunktion
- **Python** - Datenverarbeitung (nicht im Repository)

## Lizenz

Dieses Projekt ist für den internen Gebrauch bestimmt.

## Kontakt

Bei Fragen oder Problemen wenden Sie sich bitte an den Repository-Maintainer.
