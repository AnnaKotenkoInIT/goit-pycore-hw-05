#decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please, print a name and a phone."
        except KeyError:
            return "Contact does not exist :("
        except IndexError:
            return "Only a name is required."
    return inner

#fuctions for the bot
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args       
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact updated :)"

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name  not in contacts:
         raise KeyError
    return contacts[name]

@input_error
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts found."

#main function
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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()