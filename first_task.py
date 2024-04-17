def main():
    contacts = {}
    print("Welcome to the console bot assistant!")
    while True:
        command = input("\nEnter a command: ").strip().lower()
        if command in {"close", "exit"}:
            print("Goodbye!")
            exit(0)
        elif command == "help":
            print("Available commands:")
            print("  - 'hello': Start a conversation with the bot")
            print("  - 'add [name] [phone number]': Add a new contact")
            print("  - 'change [name] [new phone number]': Update a contact's phone number")
            print("  - 'phone [name]': Get a contact's phone number")
            print("  - 'all': Show all contacts")
            print("  - 'close' or 'exit': Quit the bot")
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            try:
                name, phone_number = command.split(" ", 2)
                contacts[name] = phone_number
                print("Contact added.")
            except ValueError:
                print("Invalid syntax. Please try again.")
        elif command.startswith("change "):
            try:
                name, phone_number = command.split(" ", 2)
                if name in contacts:
                    contacts[name] = phone_number
                    print("Contact updated.")
                else:
                    print("Name not found.")
            except ValueError:
                print("Invalid syntax. Please try again.")
        elif command.startswith("phone "):
            try:
                name = command.split(" ", 1)[1]
                if name in contacts:
                    print(contacts[name])
                else:
                    print("Name not found.")
            except ValueError:
                print("Invalid syntax. Please try again.")
        elif command == "all":
            for name, phone_number in contacts.items():
                print(f"{name}: {phone_number}")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()