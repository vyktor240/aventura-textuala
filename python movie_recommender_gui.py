import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

# Extindem baza de date a filmelor
movies = pd.DataFrame([
    {'id': 1, 'title': 'Inception', 'genres': ['Sci-Fi', 'Thriller'], 'image': r'C:\Users\Admin\Desktop\1.JPG', 'description': 'A mind-bending thriller about dreams within dreams.'},
    {'id': 2, 'title': 'The Matrix', 'genres': ['Sci-Fi', 'Action'], 'image': r'C:\Users\Admin\Desktop\2.JPG', 'description': 'A computer hacker learns that reality is a simulation.'},
    {'id': 3, 'title': 'Interstellar', 'genres': ['Sci-Fi', 'Drama'], 'image': r'C:\Users\Admin\Desktop\3.JPG', 'description': 'A team of explorers travel through a wormhole in space to ensure humanity\'s survival.'},
    {'id': 4, 'title': 'Blade Runner 2049', 'genres': ['Sci-Fi', 'Action'], 'image': r'C:\Users\Admin\Desktop\4.JPG', 'description': 'A young blade runner uncovers a long-buried secret that could change the course of humanity.'},
    {'id': 5, 'title': 'Titanic', 'genres': ['Romance', 'Drama'], 'image': r'C:\Users\Admin\Desktop\5.jpg', 'description': 'A love story set during the ill-fated voyage of the RMS Titanic.'},
    {'id': 6, 'title': 'The Notebook', 'genres': ['Romance', 'Drama'], 'image': r'C:\Users\Admin\Desktop\6.jpg', 'description': 'A young couple falls in love, but their relationship is tested by circumstances.'},
    {'id': 7, 'title': 'Pride and Prejudice', 'genres': ['Romance', 'Drama'], 'image': r'C:\Users\Admin\Desktop\7.jpg', 'description': 'An early 19th-century romance set in England, based on the famous novel.'},
    {'id': 8, 'title': 'La La Land', 'genres': ['Romance', 'Comedy'], 'image': r'C:\Users\Admin\Desktop\8.jpg', 'description': 'A jazz musician and an aspiring actress fall in love but struggle to keep their relationship intact.'},
    {'id': 9, 'title': 'Avatar', 'genres': ['Action', 'Fantasy'], 'image': r'C:\Users\Admin\Desktop\9.jpg', 'description': 'A paraplegic former Marine is dispatched to the moon Pandora on a unique mission.'},
    {'id': 10, 'title': 'The Avengers', 'genres': ['Action', 'Sci-Fi'], 'image': r'C:\Users\Admin\Desktop\10.jpg', 'description': 'Earth\'s mightiest heroes join forces to stop an alien invasion.'},
    {'id': 11, 'title': 'Mad Max: Fury Road', 'genres': ['Action', 'Adventure'], 'image': r'C:\Users\Admin\Desktop\11.jpg', 'description': 'In a post-apocalyptic wasteland, a lone drifter teams up with a group of rebels to overthrow a tyrannical warlord.'},
    {'id': 12, 'title': 'Gladiator', 'genres': ['Action', 'Drama'], 'image': r'C:\Users\Admin\Desktop\12.jpg', 'description': 'A betrayed Roman general seeks revenge against the corrupt emperor who murdered his family.'},
    {'id': 13, 'title': 'Forrest Gump', 'genres': ['Drama', 'Comedy'], 'image': r'C:\Users\Admin\Desktop\13.jpg', 'description': 'The life story of a man with low intelligence who inadvertently influences major events in U.S. history.'},
    {'id': 14, 'title': 'The Godfather', 'genres': ['Drama', 'Crime'], 'image': r'C:\Users\Admin\Desktop\14.jpg', 'description': 'The story of a powerful Italian-American crime family set in New York City.'},
    {'id': 15, 'title': 'Schindler\'s List', 'genres': ['Drama', 'History'], 'image': r'C:\Users\Admin\Desktop\15.jpg', 'description': 'The true story of Oskar Schindler, who saved more than a thousand Jewish lives during the Holocaust.'},
    {'id': 16, 'title': '12 Angry Men', 'genres': ['Drama', 'Crime'], 'image': r'C:\Users\Admin\Desktop\16.jpg', 'description': 'Twelve jurors deliberate the fate of a young man accused of murder.'},
    {'id': 17, 'title': 'Parasite', 'genres': ['Thriller', 'Drama'], 'image': r'C:\Users\Admin\Desktop\17.jpg', 'description': 'A poor family schemes to infiltrate a wealthy household, with unexpected consequences.'},
    {'id': 18, 'title': 'Shutter Island', 'genres': ['Thriller', 'Mystery'], 'image': r'C:\Users\Admin\Desktop\18.jpg', 'description': 'A U.S. Marshal investigates the disappearance of a patient from a mental institution.'},
    {'id': 19, 'title': 'Seven', 'genres': ['Thriller', 'Crime'], 'image': r'C:\Users\Admin\Desktop\19.jpg', 'description': 'Two detectives hunt down a serial killer who uses the seven deadly sins as his modus operandi.'},
    {'id': 20, 'title': 'Gone Girl', 'genres': ['Thriller', 'Drama'], 'image': r'C:\Users\Admin\Desktop\20.jpg', 'description': 'A man becomes the prime suspect in the disappearance of his wife.'},
    {'id': 21, 'title': 'The Conjuring', 'genres': ['Horror', 'Thriller'], 'image': r'C:\Users\Admin\Desktop\21.jpg', 'description': 'Paranormal investigators work to help a family terrorized by dark forces.'},
    {'id': 22, 'title': 'Get Out', 'genres': ['Horror', 'Thriller'], 'image': r'C:\Users\Admin\Desktop\22.jpg', 'description': 'A young African-American man visits his white girlfriend\'s family, where his unease grows.'},
    {'id': 23, 'title': 'A Quiet Place', 'genres': ['Horror', 'Sci-Fi'], 'image': r'C:\Users\Admin\Desktop\23.jpg', 'description': 'A family must live in silence to avoid blind monsters with acute hearing.'},
    {'id': 24, 'title': 'It', 'genres': ['Horror', 'Thriller'], 'image': r'C:\Users\Admin\Desktop\24.jpg', 'description': 'A group of young misfits must confront a monster that takes the form of a clown.'},
])

# Funcție pentru a obține recomandări
def get_recommendations():
    # Preluarea preferințelor din input și normalizarea lor
    raw_input = entry_genres.get()
    genres = [genre.strip().capitalize() for genre in raw_input.split(",")]

    if not genres:
        messagebox.showerror("Eroare", "Introdu genurile preferate!")
        return

    # Filtrare filme care conțin toate genurile selectate
    recommended = movies[movies['genres'].apply(lambda g: all(genre in g for genre in genres))]

    # Afișare rezultate
    if recommended.empty:
        result_label.config(text="Nu s-au găsit filme care să includă toate genurile selectate.")
        canvas.delete("all")  # Curățăm canvas-ul
    else:
        result_label.config(text="Recomandări:")
        canvas.delete("all")  # Curățăm canvas-ul înainte de a adăuga rezultatele

        # Creăm un frame pentru filmele orizontale
        movie_frame = tk.Frame(canvas, bg="#f0f0f0")
        movie_frame.place(x=20, y=20)

        # Afișăm fiecare film pe frame, plasându-le orizontal
        x_offset = 20  # Offset orizontal pentru fiecare film
        for _, row in recommended.iterrows():
            title = row['title']
            image_path = row['image']
            genres = ', '.join(row['genres'])
            description = row['description']

            film_card = tk.Frame(movie_frame, width=180, height=350, bg="#fff", bd=2, relief="solid")
            film_card.grid(row=0, column=x_offset, padx=10)

            # Titlu film
            title_label = tk.Label(film_card, text=title, font=("Arial", 10, "bold"), bg="#fff", fg="#333")
            title_label.grid(row=0, column=0, pady=5)

            # Încărcăm și redimensionăm imaginea
            try:
                img = Image.open(image_path)
                img.thumbnail((180, 270))  # Redimensionăm imaginea menținând proporțiile
                img = ImageTk.PhotoImage(img)

                # Afișăm imaginea
                image_label = tk.Label(film_card, image=img, bg="#fff")
                image_label.image = img  # Păstrăm referința la imagine
                image_label.grid(row=1, column=0, rowspan=2, pady=5)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")

            # Genuri film
            genres_label = tk.Label(film_card, text=f"Genuri: {genres}", font=("Arial", 8), bg="#fff", fg="#555")
            genres_label.grid(row=1, column=1, padx=10, sticky="w")

            # Descrierea filmului
            description_label = tk.Label(film_card, text=f"Descriere: {description}", font=("Arial", 8), bg="#fff", fg="#555", wraplength=180)
            description_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

            # Actualizăm offset-ul pentru următorul film
            x_offset += 220  # Ajustăm pentru a lăsa spațiu între filme

# Creare fereastră principală
root = tk.Tk()
root.title("Recomandări Filme")
root.attributes("-fullscreen", True)  # Activăm modul pe ecran complet

# Încarcă și afișează imaginea de fundal
background_image = Image.open(r'C:\Users\Admin\Desktop\1234.jpg')  # Calea imaginii de fundal
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Redimensionează la dimensiunea ecranului
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Titlu
title_label = tk.Label(root, text="Recomandări de Filme", font=("Helvetica", 24, "bold"), fg="#ffeb3b", bg="#2c3e50")
title_label.pack(pady=20)

# Instrucțiuni
instruction_label = tk.Label(root, text="Introdu genurile preferate (ex: Sci-Fi, Thriller):", font=("Arial", 14), bg="#34495e", fg="#ecf0f1")
instruction_label.pack(pady=10)

# Input pentru genuri
entry_genres = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="solid", justify="center", bg="#ecf0f1")
entry_genres.pack(pady=10)

# Buton pentru generarea recomandărilor
recommend_button = tk.Button(root, text="Recomandă Filme", command=get_recommendations, bg="#3498db", fg="white", font=("Arial", 14, "bold"), relief="raised", activebackground="#2980b9")
recommend_button.pack(pady=20)

# Etichetă pentru afișarea rezultatelor
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#34495e", fg="#ecf0f1")
result_label.pack(pady=10)

# Canvas pentru afișarea recomandărilor
canvas = tk.Canvas(root, bg="#ecf0f1", scrollregion=(0, 0, 5000, 1000))
canvas.pack(pady=20, expand=True, fill=tk.BOTH)

# Buton de ieșire
exit_button = tk.Button(root, text="Ieșire", command=root.quit, bg="#e74c3c", fg="white", font=("Arial", 14, "bold"), relief="raised", activebackground="#c0392b")
exit_button.pack(pady=20)

# Rularea aplicației
root.mainloop()
