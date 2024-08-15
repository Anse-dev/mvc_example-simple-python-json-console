
from models import Book, load_books, save_books
from view import display_books,add_book_prompt ,view_book_details, delete_book_prompt

def main():

    books = load_books()

    while True:
        print("\nOptions:")
        print("1. Afficher les livres")
        print("2. Ajouter un livre")
        print("3. Voir un livre")
        print("4. Supprimer un livre")
        print("5. Quitter")

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
            index = view_book_details(books)
            if index is not None:
                print(f"Détails du livre: Titre: {books[index].title}, Auteur: {books[index].author}")

        elif choice == '4':
            index = delete_book_prompt(books)
            if index is not None:
                del books[index]
                save_books(books)
                print("Livre supprimé avec succès!")

        elif choice == '5':
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == '__main__':
    main()
