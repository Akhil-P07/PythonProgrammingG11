books = dict()
end = 1
while (end == 1):
    book_nm = input("Enter Book's Name: ")
    book_pr = int(input("Enter price of book (in USD): "))
    books[book_nm] = book_pr
    end = int(input("Press 1 to Continue or 0 to exit: "))
print(books)
