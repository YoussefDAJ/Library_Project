# Step1 = SetUp
library = []
wishlist = []

# Step2 = Adding Individual Books
book_name = input("Enter the name of a book you own: ").lower()

library.append(book_name)

book_name = input(
    "Enter the name of another book your own (or press 'Enter' to skip) :"
).lower()

if book_name:
    library.append(book_name)
    print("\n Your library : ", library)


# Step 3: Managment wishlist
book_name = input("\nEnter the name of a book you wish to have in the future: ").lower()

wishlist.append(book_name)

book_name = input(
    "\nEnter the name of an other book you wish to have (or press 'Enter' to skip) "
).lower()

if book_name:
    wishlist.append(book_name)
    print("\nYour wishlist: ", wishlist)

# Step 4: Mergin wishlist into library
acquired_book = input(
    "\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip) :"
).lower()
if acquired_book in wishlist:
    library.append(acquired_book)
    wishlist.remove(acquired_book)

print("\nUpdated library: ", library)
print("\nUpdated wishlist: ", wishlist)

# Donation books:

donated_book = input(
    "\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip) :"
).lower()
if donated_book in library:
    library.remove(donated_book)

print("\nFinal library after Donation: ", library)
