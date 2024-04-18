def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
def input_error(func):
    def inner(args, kwargs):
        try:
            return func(args, kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command."

    return inner
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")
class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

class Record:
    def __init__(self):
        self.fields = []

    def add_field(self, name, value):
        field = Field(name, value)
        self.fields.append(field)

    def remove_field(self, name):
        for field in self.fields:
            if field.name == name:
                self.fields.remove(field)
                break

    def edit_field(self, name, value):
        for field in self.fields:
            if field.name == name:
                field.set_value(value)
                break

class ContactBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, name):
        for record in self.records:
            if record.name == name:
                self.records.remove(record)
                break

    def search(self, criteria):
        results = []
        for record in self.records:
            match = True
            for criterion in criteria:
                found = False
                for field in record.fields:
                    if field.name == criterion:
                        found = True
                        if field.value != criteria[criterion]:
                            match = False
                            break
                if not found:
                    match = False
                    break
            if match:
                results.append(record)
        return results

if __name__ == "__main__":
    main()

