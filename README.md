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

1. **Repository verbinden:**
   - Gehen Sie zu [Netlify](https://www.netlify.com)
   - Klicken Sie auf **"Add new site"** → **"Import an existing project"**
   - Wählen Sie **GitHub** als Git-Provider
   - Autorisiere Netlify für den Zugriff auf Ihr GitHub-Konto
   - Wählen Sie das Repository **`maikbehring/steinofen`**

2. **Build-Einstellungen konfigurieren:**
   
   **WICHTIG:** Diese Einstellungen müssen Sie setzen:
   
   - **Branch to deploy:** `main` (oder `master`, je nachdem)
   - **Build command:** *(leer lassen - keine Build-Schritte nötig)*
   - **Publish directory:** `website_datanature`
   
   ⚠️ **Wichtig:** Das Publish directory muss `website_datanature` sein, da sich die Website-Dateien dort befinden!

3. **Deploy starten:**
   - Klicken Sie auf **"Deploy site"**
   - Netlify erstellt automatisch eine URL (z.B. `https://random-name-123.netlify.app`)
   - Die Website ist sofort live!

4. **Automatische Updates:**
   - Bei jedem Push ins `main`-Branch wird die Website automatisch neu deployed
   - Sie können auch manuell über das Netlify-Dashboard deployen

### Optionale Einstellungen

- **Custom Domain:** Sie können eine eigene Domain hinzufügen (z.B. `produkte.steinofenbaecker.de`)
- **Branch Deploys:** Aktivieren Sie "Deploy previews" für Pull Requests
- **Build Hooks:** Für manuelle Deployments via API

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
