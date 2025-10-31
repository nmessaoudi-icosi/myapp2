Parfait — on va faire ça en 3 étapes :

1. compléter **README.md**, 2) commenter/améliorer **app.py**, 3) **commit & push**.

---

# 1) Remplacer/compléter `README.md`

Ouvre ton fichier (au choix) :

```powershell
cd D:\myapp2
notepad README.md
# ou avec VS Code :
# code README.md
```

Colle ce **modèle complet** (tu peux adapter `<ton-user>` si tu veux afficher l’URL exacte) :

````markdown
# 🐍 MyApp2

Projet **DevOps** de démonstration (Windows 11 + WSL2) : script Python conteneurisé avec **Docker**, orchestration locale **Docker Compose**, et **CI GitHub Actions**.

> Auteur : **Le premier** (Enseignant DevOps)

---

## 📦 Prérequis
- Python 3.11+
- Git & GitHub Desktop (ou CLI)
- Docker Desktop (WSL2 activé recommandé)

---

## 🚀 Démarrage rapide (Windows)
```bash
git clone https://github.com/<ton-user>/myapp2.git
cd myapp2
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
````

---

## 🐳 Docker

Construire et exécuter :

```bash
docker build -t myapp2:latest .
docker run --rm myapp2:latest
```

### Docker Compose (dev)

```bash
docker compose up --build
# Arrêter
docker compose down
```

---

## 🧪 Tests

Les tests sont dans `tests/` et exécutés par **pytest** :

```bash
pytest -q
```

---

## 🧱 Structure

```
myapp2/
├── app.py                # Script principal (voir docstring)
├── requirements.txt      # Dépendances Python
├── Dockerfile            # Image de l’app
├── docker-compose.yml    # Orchestration locale
├── .github/workflows/ci.yml  # Pipeline CI
├── tests/test_app.py     # Tests unitaires
├── .gitignore
├── .gitattributes
└── README.md
```

---

## 🔄 CI/CD (GitHub Actions)

Chaque **push/PR vers `main`** déclenche :

1. Installation de Python et dépendances
2. Exécution des **tests**
3. **Build Docker** (sans push d’image par défaut)

Le workflow est défini dans `.github/workflows/ci.yml`.

---

## 🧰 Commandes utiles

```bash
# Nettoyer Docker
docker system prune -af

# Lister conteneurs / images
docker ps -a
docker images
```

---

## 🤝 Contribution (exemple pour les étudiants)

* Créer une branche : `git checkout -b feature/mon-sujet`
* Commit conventionnel : `feat: ajoute X` / `fix: corrige Y`
* Ouvrir une **Pull Request** vers `main`

---

````

Enregistre et ferme le fichier.

---

# 2) Ajouter des commentaires/docstrings dans `app.py`
Ouvre ton script, puis remplace son contenu par cette version **documentée** (compatible avec tes tests existants) :

```python
"""
MyApp2 — Script de démonstration DevOps.

Usage:
    python app.py [nom]

Si aucun nom n'est fourni, le script salue "world".
Le cœur de l'app est la fonction `greet`, testée par pytest.
"""

from __future__ import annotations
import sys
import logging

# Configuration simple du logging pour tracer l'exécution
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp2")


def greet(name: str = "world") -> str:
    """
    Retourne un message de salutation.

    Args:
        name: Nom de la personne/entité à saluer (par défaut "world").

    Returns:
        Message formaté "Hello from MyApp2, <name>!"
    """
    return f"Hello from MyApp2, {name}!"


def main(argv: list[str] | None = None) -> int:
    """
    Point d'entrée du script.
    Lit un éventuel argument de ligne de commande et affiche le message.

    Args:
        argv: Liste des arguments (utile pour les tests/CI). Par défaut, sys.argv.

    Returns:
        Code de sortie du processus (0 = succès).
    """
    if argv is None:
        argv = sys.argv

    name = argv[1] if len(argv) > 1 else "world"
    msg = greet(name)
    logger.info(msg)
    print(msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
````

> Cette version ajoute : docstrings, annotations de types, logging, et une fonction `main` – tout en gardant la sortie identique pour ne pas casser `tests/test_app.py`.

*(Optionnel)* Tu peux aussi commenter le test pour l’expliquer aux étudiants :

```python
# tests/test_app.py
from app import greet

def test_greet_default():
    # Par défaut, la fonction doit saluer "world"
    assert greet() == "Hello from MyApp2, world!"

def test_greet_custom():
    # Elle doit accepter un nom personnalisé
    assert greet("DevOps") == "Hello from MyApp2, DevOps!"
```

---

# 3) Commit & push des modifications

Dans PowerShell à la racine du projet :

```powershell
cd D:\myapp2

# Vérifier les changements
git status

# Ajouter les fichiers modifiés
git add README.md app.py tests/test_app.py

# Créer un commit clair et conventionnel
git commit -m "docs: complète README; refactor(app): ajoute docstrings, types et logging"

# (Première fois uniquement) Lier le dépôt distant :
# git remote add origin https://github.com/<ton-user>/myapp2.git
# git branch -M main

# Envoyer sur GitHub
git push -u origin main
```

Ensuite :

* Va sur **GitHub → Actions** pour voir la **CI** s’exécuter.
* Ouvre la page du dépôt pour vérifier le **README** et les fichiers mis à jour.

---

Si tu veux, dis-moi ton **nom d’utilisateur GitHub** et je te renvoie les **2 commandes exactes** `git remote add origin …` + `git push` prêtes à coller. Je peux aussi ajouter au workflow CI le **push automatique d’image Docker vers GHCR**.
