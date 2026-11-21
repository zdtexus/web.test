# Win Reinstalling

A single page of download links for setting up a fresh Windows install: drivers, browsers, basic programs, coding tools and games, grouped by category.

## Overview

The page can be used in two ways:

| Mode | How it works |
|---|---|
| Website | Hosted on Firebase Hosting; GitHub Actions deploys it on every push to `main` |
| Desktop app | A small Flask server, packaged with PyInstaller, that opens the page in your browser |

## Getting started

### Static site

Open `public/index.html` in a browser.

### Flask app

```bash
pip install flask
python app.py
```

The page opens at `http://localhost:5000`.

### Building the executable

```bash
pip install pyinstaller
pyinstaller app.spec
```

## Deployment

| Workflow | Trigger | Result |
|---|---|---|
| [`firebase-hosting-merge.yml`](.github/workflows/firebase-hosting-merge.yml) | Push to `main` | Deploys to production |
| [`firebase-hosting-pull-request.yml`](.github/workflows/firebase-hosting-pull-request.yml) | Pull request | Deploys a preview channel |

## Project structure

```text
public/      Static site served by Firebase
templates/   The same page, served by Flask
app.py       Flask launcher
app.spec     PyInstaller build config
```
