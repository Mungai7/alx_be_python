def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping
    _list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_add = input ("enter the item you want to add :")  
            shopping_list.append(item_add)

        elif choice == '2':
            # Prompt for and remove an item
            item_remove = input ("enter the item you want to remove:")
            shopping_list.remove(str(item_remove))

        elif choice == '3':
            # Display the shopping list 
            for display in shopping_list:
                print(display)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()