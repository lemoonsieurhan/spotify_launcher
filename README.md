## spotify_launcher
Launcher Spotify pour windows permettant de lancer ses playlists rapidement avec un raccourci clavier.

---

###  Fonctionnalités

- **Raccourci clavier** : `Ctrl + Alt + S` ouvre le launcher.
- **Liste les playlists** : récupère toutes vos playlists Spotify.
- **Lecture instantanée** : lance la lecture sur le device actif.
- **Interface simple** : développée avec Tkinter.

---

###  Installation

1. **Cloner le dépôt**
	```bash
	git clone https://github.com/TonPseudo/spotify-launcher.git
	cd spotify-launcher
	```
2. **Installer Python**
	- Téléchargez la dernière version de Python depuis : https://www.python.org/downloads/windows/
	- Pendant l'installation, cochez « Add Python to PATH ».
3. **Installer les dépendances**
	```powershell
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	```
4. **Configurer l’application Spotify**
	- Rendez-vous sur : https://developer.spotify.com/dashboard
	- Créez une nouvelle application.
	- Ajoutez la **Redirect URI** : `http://localhost:8888/callback`.
	- Récupérez le `CLIENT_ID` et le `CLIENT_SECRET`.

5. **Créer un fichier `.env`**
	À la racine du projet, créez un fichier `.env` contenant :
	```env
	CLIENT_ID=ton_client_id
	CLIENT_SECRET=ton_client_secret
	REDIRECT_URI=http://localhost:8888/callback
	```
	Remplacez `ton_client_id` et `ton_client_secret` par vos valeurs obtenues sur le [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

### Lancement

- **Exécuter le script** :
  ```bash
  python spotify_launcher.py
  ```

- **Générer un exécutable Windows (optionnel)** :
  ```bash
  pyinstaller --onefile spotify_launcher.py
  ```
  Le fichier `.exe` se trouvera dans le dossier `dist/`.
  **Ne poussez pas l’exécutable sur GitHub ; il est déjà dans `.gitignore`.**

---

### Démarrage automatique

Pour que le raccourci fonctionne au démarrage de Windows :
1. Appuyez sur **Win + R**.
2. Tapez `shell:startup`.
3. Collez un raccourci vers l’exécutable `.exe` dans ce dossier.

Le launcher s’exécutera à chaque démarrage.

---

### Important

- Ne **jamais** commiter le fichier `.env`.
- Assurez-vous qu’il est bien listé dans `.gitignore`.

---

### Support

En cas de problème :

- Vérifiez que Python est installé et accessible : `python --version`.
- Assurez-vous que les dépendances s’installent correctement :
  ```bash
  python -m pip install -r requirements.txt
  ```
- Vérifiez que votre `.env` contient les bons identifiants Spotify.

---

*Bonne utilisation !* 
