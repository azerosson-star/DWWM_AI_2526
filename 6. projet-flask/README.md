# Projet Flask

Description
- Petit projet Flask d'exemple avec quelques routes simples et une petite animation JavaScript sur la page `hello`.

Structure du projet
- `app.py` : application Flask principale.
- `templates/hello.html` : template qui affiche le `h1` cliquable.
- `static/css/style.css` : styles globaux et styles pour l'animation du `h1`.
- `static/js/main.js` : script qui gère l'animation (clic pour centrer le `h1`).

Prérequis
- Python 3.8+ installé
- PowerShell (Windows)

Installation et exécution (PowerShell)
1. Créer un environnement virtuel dans le répertoire du projet :

```
python -m venv .venv
```

2. Activer l'environnement virtuel (PowerShell) :

```
& .\.venv\Scripts\Activate.ps1
```

3. Installer les dépendances (Flask) :

```
pip install flask
```

Ou, si vous avez fourni un `requirements.txt` :

```
pip install -r requirements.txt
```

4. Lancer l'application avec la CLI Flask (PowerShell) :

```
$env:FLASK_APP = "app.py";
$env:FLASK_ENV = "development";
flask run --host=127.0.0.1 --port=5000
```

Test de l'animation `h1`
- Ouvrez `http://127.0.0.1:5000` (ou la route appropriée si votre app sert `hello` à une autre route).
- Sur la page `hello`, cliquez sur le texte `Hello ...` (`<h1>`). Le texte doit se déplacer au centre avec une transition douce.
- Cliquez de nouveau pour le remettre à sa place.

Fichiers modifiés pour l'animation
- `static/css/style.css` : styles ajoutés pour `h1` et la classe `.to-center`.
- `static/js/main.js` : script ajouté pour animer le `h1` au clic.

Personnalisation possible
- Ajouter un effet de scale/agrandissement lors du centrage.
- Centrer d'autres éléments en adaptant le sélecteur dans `main.js`.

Conseils utiles
- Générer un `requirements.txt` après installation des dépendances :

```
pip freeze > requirements.txt
```
- Désactiver l'environnement virtuel :

```
deactivate
```

Contact
- Questions / améliorations : créer une issue ou me contacter.

Licence
- Ajoutez une licence si nécessaire.
