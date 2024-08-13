import json
from models import Book, load_books, save_books
from view import display_books, add_book_prompt

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
