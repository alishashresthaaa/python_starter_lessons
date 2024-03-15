# Question 4: Combining Concepts (20 Points)
# Scenario: You are creating a Python script for a library that keeps track of books. Each book has a title and an author. Write a Python script that:
# •	Uses a list to store books, where each book is represented as a dictionary with keys "title" and "author".
# •	Continuously prompts the user to enter a book title and author or type 'exit' to stop.
# •	Adds each book to the list.
# •	After the user types 'exit', print all books in the list in the format "Title by Author".

inputted_books = []

while True:
    book_title = input("Enter the title of the book: (Type 'exit' to stop the program)\n")
    if not book_title:
        print("Please enter a valid book title")
        continue
    if book_title.lower() == 'exit':
        print("You have exited from the program")
        break

    book_author = input("Please enter the author of the book:\n")
    if not book_author:
        print("Please enter a valid book author")
        continue

    book = {"title": book_title, "author": book_author}
    inputted_books.append(book)


if inputted_books:
    print("The list of books are:")
    for book in inputted_books:
        print(book['title'].capitalize(), "by", book['author'].capitalize())