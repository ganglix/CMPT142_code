# Topic(s): Writing Files
# DEMO
# records of books to write to file
books = [
    {"title": "The Cat in the Hat", "author": "Dr. Seuss",
     "year_published": 1605},
    {"title": "The Cat in the Hat Comes Back", "author": "Dr. Seuss",
     "year_published": 1859},
    {"title": "The Adventures of Tom Sawyer", "author": "Mark Twain",
     "year_published": 1876},
    {"title": "The Prince and the Pauper", "author": "Mark Twain",
     "year_published": 1881},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
     "year_published": 1960},
    {"title": "Animal Farm", "author": "George Orwell",
     "year_published": 1945},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger",
     "year_published": 1951},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
     "year_published": 1813}
]

# create a file
f = open('my_books.txt', 'w')  # create the file, write mode
# f = open('my_books.txt', 'a')  # create the file, write-appending mode

# get the book info from a list of dictionary
for book in books:   # book is dict
    #book_info = book['title'] + "," + book['author'] + "," + str(book['year_published'])
    book_info = ','.join([book['title'], book['author'], str(book['year_published'])])
    # write the book info into a line of text in the file
    f.write(book_info)
    f.write("\n")  # go to next line

# save the file and close it at the same time
f.close()
