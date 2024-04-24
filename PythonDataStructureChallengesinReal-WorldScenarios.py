library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_new(library):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    book = (title, author,)
    if book in library:
        print("That book already exist in the library")
    else:
        library.append(book)

add_new(library)
print(library)