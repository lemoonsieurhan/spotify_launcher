Spotify Playlist Launcher (Windows)
Petit launcher type rofi pour lancer rapidement ses playlists Spotify via un raccourci clavier sous Windows.

Fonctionnalités
Ctrl + Alt + S ouvre le launcher

Liste toutes vos playlists Spotify

Lance la lecture sur le device actif

Interface simple via Tkinter

Installation
1. Cloner le repository
bash
git clone https://github.com/TonPseudo/spotify-launcher.git
cd spotify-launcher
2. Installer Python
Téléchargez la dernière version de Python depuis : https://www.python.org/downloads/windows/

Lors de l’installation, cochez “Add Python to PATH”

3. Installer les dépendances
Dans le dossier du projet, ouvrez PowerShell et tapez :

powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
4. Créer un fichier .env
Créez un fichier .env à la racine du projet avec vos identifiants Spotify :

env
CLIENT_ID=ton_client_id
CLIENT_SECRET=ton_client_secret
REDIRECT_URI=http://localhost:8888/callback
Remplacez ton_client_id et ton_client_secret par vos valeurs récupérées depuis le Spotify Developer Dashboard.

5. Créer une application Spotify
Aller sur : https://developer.spotify.com/dashboard

Créer une nouvelle application

Ajouter le Redirect URI : http://localhost:8888/callback

Récupérer le CLIENT_ID et le CLIENT_SECRET

Lancement
Lancer le script directement
bash
python spotify_launcher.py
Générer un exécutable (.exe) — optionnel
bash
pyinstaller --onefile spotify_launcher.py
Le fichier .exe sera disponible dans le dossier dist/.

Ne pas push le .exe sur GitHub : il est déjà dans le .gitignore.

Lancer automatiquement au démarrage de Windows
Pour que le raccourci clavier fonctionne dès le démarrage :

Appuyer sur Win + R

Taper shell:startup

Coller un raccourci vers le .exe dans ce dossier

Le launcher se lancera automatiquement à chaque démarrage.

Important
Ne jamais commit le fichier .env

Vérifier qu’il est bien dans votre .gitignore

Support
En cas de problème :

Vérifiez que Python est installé et accessible (python --version)

Verifiez que les dependances s’installent correctement :

bash
python -m pip install -r requirements.txt
Vérifiez que votre .env contient les bons identifiants Spotify