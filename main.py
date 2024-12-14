# Import des bibliothèques nécessaires
import tkinter as tk

# Fonction principale de l'application
def main():
    app = tk.Tk()  # Crée une fenêtre Tkinter
    app.title("Mon Application")  # Définit le titre
    app.geometry("800x600")  # Définit la taille de la fenêtre

    # Ajoute un label simple
    label = tk.Label(app, text="Bienvenue dans mon application !")
    label.pack(pady=20)

    # Lancement de la boucle principale
    app.mainloop()

# Point d'entrée du programme
if __name__ == "__main__":
    main()

