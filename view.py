def display_books(books):
    if not books:
        print("Aucun livre à afficher.")
    else:
        print("\nListe des livres:")
        for i, book in enumerate(books):
            print(f"{i + 1}. Titre: {book.title}, Auteur: {book.author}")

def view_book_details(books):
    if not books:
        print("Aucun livre à afficher.")
        return None
    display_books(books)
    index = int(input("Choisissez le numéro du livre à voir (ou 0 pour annuler): ")) - 1
    if 0 <= index < len(books):
        return index
    else:
        print("Sélection invalide.")
        return None

def delete_book_prompt(books):
    if not books:
        print("Aucun livre à supprimer.")
        return None
    display_books(books)
    index = int(input("Choisissez le numéro du livre à supprimer (ou 0 pour annuler): ")) - 1
    if 0 <= index < len(books):
        return index
    else:
        print("Sélection invalide.")
        return None
    
def add_book_prompt():
    title = input("Titre du livre: ")
    author = input("Auteur du livre: ")
    return title, author
