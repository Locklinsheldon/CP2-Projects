# Function to display the menu options to the user and get their choice
def display_menu():
    print("Personal Library Catalog")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

# Function to add a new book to the library
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    book = {"title": title, "author": author}
    library.append(book)
    print(f"'{title}' by {author} has been added to your library.")

# Function to display all books in the library
def display_books(library):
    if len(library) == 0:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")

# Function to search for a book by title or author
def search_books(library):
    search_term = input("Enter the title or author to search: ").lower()
    found_books = [book for book in library if search_term in book['title'].lower() or search_term in book['author'].lower()]
    if len(found_books) == 0:
        print("No matching books found.")
    else:
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}")

# Function to remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"'{title}' has been removed from your library.")
            return
    print(f"No book found with the title '{title}'.")

# Main function to run the library catalog program
def main():
    library = []
    while True:
        choice = display_menu()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            display_books(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            remove_book(library)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
