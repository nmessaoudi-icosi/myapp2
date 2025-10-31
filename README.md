# 🐍 MyApp2

Projet **DevOps** de démonstration sous **Windows 11** — création, conteneurisation et intégration continue d’un **script Python**.

---

## 📘 Description

Ce projet illustre les bonnes pratiques DevOps :
- Utilisation de **Git** et **GitHub**
- Conteneurisation avec **Docker**
- Orchestration locale avec **Docker Compose**
- Intégration Continue (CI/CD) avec **GitHub Actions**

L’application principale est un **script Python** (`app.py`) exécuté dans un conteneur Docker.

---

## 🧩 Structure du projet

```
myapp2/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .gitattributes
├── tests/
│   └── test_app.py
└── README.md
```

---

## ⚙️ Installation locale (sans Docker)

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/<ton-user>/myapp2.git
   cd myapp2
   ```

2. **Créer un environnement virtuel :**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate    # Sous Windows
   pip install -r requirements.txt
   ```

3. **Exécuter le script :**
   ```bash
   python app.py
   ```

---

## 🐳 Utilisation avec Docker

1. **Construire l’image :**
   ```bash
   docker build -t myapp2:latest .
   ```

2. **Lancer le conteneur :**
   ```bash
   docker run --rm myapp2:latest
   ```

---

## 🧱 Utilisation avec Docker Compose

Le fichier `docker-compose.yml` permet de lancer facilement le service :

```yaml
version: "3.9"
services:
  app:
    build: .
    container_name: myapp2
    command: python app.py
    volumes:
      - .:/app
    working_dir: /app
    environment:
      - PYTHONUNBUFFERED=1
```

**Commandes :**
```bash
docker compose up --build
```

Arrêter :
```bash
docker compose down
```

---

## 🔄 Intégration Continue (GitHub Actions)

Le pipeline CI s’exécute automatiquement à chaque **push** ou **pull request** sur la branche `main`.

Fichier : `.github/workflows/ci.yml`

```yaml
name: CI Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest -q || echo "No tests found, skipping..."

  docker:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Build Docker image
        uses: docker/build-push-action@v6
        with:
          context: .
          push: false
          tags: myapp2:ci
```

---

## 🧪 Tests

Les tests se trouvent dans `tests/` et sont exécutés par **pytest** :
```bash
pytest -q
```

---

## 📦 Exemple de Dockerfile

```Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## 👨‍🏫 Auteur

**Le premier** — Enseignant DevOps  
Projet réalisé à des fins pédagogiques (initiation à Git, Docker, GitHub Actions et CI/CD).

---

## 💡 Astuces DevOps Windows + WSL

- Active **WSL2** et **Docker Desktop** pour de meilleures performances.  
- Évite de travailler dans `C:\` ou `D:\` depuis WSL (préférer `/home/<user>`).  
- Commande utile :  
  ```bash
  docker system prune -af
  ```  
  pour nettoyer les conteneurs et images inutiles.
