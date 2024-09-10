
# Book Records
# Problem Statement:
# You are building a simple library management system where each book is represented by a record containing 
# its title, author, and ISBN number. Since these details about a book should not change once they are set, 
# you should use tuples to store this information.

# Your task is to write a function that accepts a list of book records 
# and a specific author’s name, and then returns a list of all book titles by that author.

# "The Great Gatsby", "F. Scott Fitzgerald", "9780743273565",
# "To Kill a Mockingbird", "Harper Lee", "9780061120084",
# "1984", "George Orwell", "9780451524935",
# "Animal Farm", "George Orwell", "9780451526342",
# "The Catcher in the Rye", "J.D. Salinger", "9780316769488"


books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"),
    ("To Kill a Mockingbird", "Harper Lee", "9780061120084"),
    ("1984", "George Orwell", "9780451524935"),
    ("Animal Farm", "George Orwell", "9780451526342"),
    ("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
]


def get_books(books, author):
    return [book[0] for book in books if book[1] == author]


print(get_books(books, "George Orwell"))

