import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from tkinter import messagebox
import threading
import keyboard

# ------------------- CONFIGURATION SPOTIFY -------------------
# Remplace ces valeurs avec tes propres clés avant de lancer le script
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = ""

SCOPE = "playlist-read-private playlist-read-collaborative user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# ------------------- FONCTION LAUNCHER -------------------
def launch_spotify_launcher():
    playlist_dict = {}

    results = sp.current_user_playlists(limit=50)
    
    while True:
        for p in results['items']:
            playlist_dict[p['name']] = p['uri']
        
        if results['next']:
            results = sp.next(results)
        else:
            break

    root = tk.Tk()
    root.title("Spotify Launcher")
    root.geometry("400x400")
    root.resizable(False, False)

    label = tk.Label(root, text="Sélectionne une playlist et appuie sur Entrée")
    label.pack(pady=10)

    listbox = tk.Listbox(root, width=50, height=20)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    for name in sorted(playlist_dict.keys()):
        listbox.insert(tk.END, name)

    def play_selected(event=None):
        selected = listbox.get(tk.ACTIVE)
        if not selected:
            return

        uri = playlist_dict[selected]
        devices = sp.devices()

        if not devices['devices']:
            messagebox.showerror("Erreur", "Aucun appareil actif détecté.")
            return

        device_id = devices['devices'][0]['id']

        try:
            sp.start_playback(device_id=device_id, context_uri=uri)
            messagebox.showinfo("Lecture", f"Lancement de : {selected}")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    listbox.bind("<Return>", play_selected)
    listbox.bind("<space>", play_selected)

    root.mainloop()

# ------------------- HOTKEY -------------------
keyboard.add_hotkey('ctrl+alt+s', lambda: threading.Thread(target=launch_spotify_launcher).start())

if __name__ == "__main__":
    keyboard.wait()