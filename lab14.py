books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = set()
for book in books:
    library_categories.add(book[3])

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("==================================================")
print("         LIBRARY BOOK & CATEGORY MANAGER")
print("==================================================")

while True:
    print("")
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    print("")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("")
        print("--- Current Library Catalog (Fixed Records) ---")
        for i in range(len(books)):
            title, author, year, category = books[i]
            print(f'{i + 1}. "{title}" by {author} ({year}) | Genre: {category}')
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        print("")
        print("--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")
        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)
            print("")
            print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("[ERROR] All fields are required.")

    elif choice == "3":
        print("")
        print("--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f"- {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        print("")
        print("--- Add to Student Wishlist ---")
        req_cat = input("Enter requested category: ")
        student_wishlist.add(req_cat)
        print(f'[SUCCESS] "{req_cat}" added to student wishlist.')

    elif choice == "5":
        print("")
        print("============= CATEGORY GAP ANALYSIS =============")
        print(f"Library Holdings (Set): {sorted(library_categories)}")
        print(f"Student Wishlist (Set): {sorted(student_wishlist)}")

        in_stock = library_categories & student_wishlist
        needed = student_wishlist - library_categories
        combined = library_categories | student_wishlist

        print("")
        print("1. Already in Stock (Intersection &):")
        print(sorted(in_stock))

        print("")
        print("2. Purchase Order Needed (Difference -):")
        print(sorted(needed))

        print("")
        print("3. Full Combined Genre Coverage (Union |):")
        print(sorted(combined))
        print("=================================================")

    elif choice == "6":
        print("")
        print("Thank you for using the Library Manager. Goodbye!")
        break

    else:
        print("")
        print("[ERROR] Invalid choice! Please enter a number between 1 and 6.")
