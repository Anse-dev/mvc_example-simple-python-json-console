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
