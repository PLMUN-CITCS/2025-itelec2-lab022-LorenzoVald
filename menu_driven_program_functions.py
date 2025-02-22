while True:
    # Display menu
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")
    
    # Get user choice
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        print("Hello! Welcome!")
    elif choice == 2:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(num, "is an Even number.")
        else:
            print(num, "is an Odd number.")
    elif choice == 3:
        print("Exiting program. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")