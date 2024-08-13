Voici un exemple simple de mise en œuvre du modèle MVC (Modèle-Vue-Contrôleur) en Python sans utiliser de framework. Nous allons créer une application de gestion de livres en utilisant des fichiers JSON pour stocker les données.

### Structure du projet

```
mvc_example/
│
├── app.py
├── models.py
└── views.py
```

### 1. Code des fichiers

**app.py** (le contrôleur)

```python
import json
from models import Book, load_books, save_books
from views import display_books, add_book_prompt

def main():
    # Charger les livres existants depuis le fichier JSON
    books = load_books()

    while True:
        print("\nOptions:")
        print("1. Afficher les livres")
        print("2. Ajouter un livre")
        print("3. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            title = input("Titre du livre: ")
            author = input("Auteur du livre: ")
            book = Book(title, author)
            books.append(book)
            save_books(books)
            print("Livre ajouté avec succès!")
        elif choice == '3':
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == '__main__':
    main()
```

**models.py** (le modèle)

```python
import json
import os

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author
        }

def load_books(filename='books.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        books_data = json.load(file)
        return [Book(**book) for book in books_data]

def save_books(books, filename='books.json'):
    with open(filename, 'w') as file:
        json.dump([book.to_dict() for book in books], file, indent=4)
```

**views.py** (la vue)

```python
def display_books(books):
    if not books:
        print("Aucun livre à afficher.")
    else:
        print("\nListe des livres:")
        for i, book in enumerate(books):
            print(f"{i + 1}. Titre: {book.title}, Auteur: {book.author}")

def add_book_prompt():
    title = input("Titre du livre: ")
    author = input("Auteur du livre: ")
    return title, author
```

### 2. Explication du code

- **Modèle (`models.py`)** :
  - La classe `Book` représente le modèle de données, avec des attributs `title` et `author`.
  - Les fonctions `load_books` et `save_books` gèrent la lecture et l'écriture des données dans un fichier JSON.

- **Vue (`views.py`)** :
  - La fonction `display_books` affiche la liste des livres. Si la liste est vide, un message est affiché.
  - La fonction `add_book_prompt` permet de saisir les détails d'un nouveau livre (elle n'est pas utilisée dans cet exemple, car nous saisissons les détails directement dans `app.py`).

- **Contrôleur (`app.py`)** :
  - Le fichier `app.py` gère le flux de l'application. Il affiche un menu permettant d'afficher les livres, d'en ajouter ou de quitter l'application.
  - Les livres sont chargés à partir d'un fichier JSON au démarrage et sont sauvegardés après l'ajout d'un nouveau livre.

### 3. Exécution de l'application

Pour exécuter l'application, ouvre un terminal, navigue jusqu'au dossier contenant `app.py`, et exécute :

```bash
python app.py
```

### 4. Interaction avec l'application

Tu devrais voir un menu te permettant d'afficher les livres, d'en ajouter ou de quitter l'application. Les livres ajoutés seront sauvegardés dans le fichier `books.json`.

