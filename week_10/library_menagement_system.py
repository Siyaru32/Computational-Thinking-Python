import time

# 1. Outer Loop: Processes library members one by one
while True:
    print("\n--- Welcome to the Library Management System ---")
    user = input("Enter your name (or type 'exit' to quit): ")
    user_exit = user.lower()
    
    if user_exit == "exit":
        print("Exiting system. Goodbye!")
        break

    # 2. Return Section: Handles book returns with a countdown timer (FOR Loop)
    returning = input("Are you returning a book today? (y/n): ").lower()

    if returning == "y":
        print("Processing your return. Please wait...")
        for seconds in range(3, 0, -1):
            print(seconds)
            time.sleep(1)  # Pauses the program for 1 second
        print("Book returned successfully!")
    else:
        print("No returns to process.")

    # 3. Checkout Section: Handles book checkouts (WHILE Loop)
    get_book = True
    book_count = 0  # Tracker to count total checked out books
    
    while get_book:
        book_name = input("Enter the name of the book to check out: ")
        book_count += 1  # Add 1 to the count for every book entered
        
        get_book_check = input("Do you want to add another book? (y/n): ").lower()
        if get_book_check == "n":
            get_book = False

    # 4. Conditional Messages Section: Shows different messages based on outcomes
    print(f"\nThank you, {user}!")
    if book_count > 3:
        print(f"Wow, you checked out {book_count} books! That is a heavy load. Enjoy your reading!")
    elif book_count > 0:
        print(f"You successfully checked out {book_count} book(s). Happy reading!")
    else:
        print("No books were checked out today.")
