phone_book = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name is not in the phone book. Please enter a valid name."
        except ValueError:
            return "Please enter a valid phone number."
    return inner

@input_error
def add_contact(name, phone):
    phone_book[name] = phone
    return "Contact added successfully."

@input_error
def change_phone(name, phone):
    phone_book[name] = phone
    return "Phone number updated successfully."

@input_error
def find_phone(name):
    return f"The phone number for {name} is {phone_book[name]}."

def show_all_contacts():
    if not phone_book:
        return "The phone book is empty."
    else:
        contacts = "\n".join([f"{name}: {phone}" for name, phone in phone_book.items()])
        return f"List of contacts:\n{contacts}"

def handle_command(command):
    parts = command.split()
    if parts[0].lower() == "hello":
        return "How can I help you?"
    elif parts[0].lower() == "add":
        name = parts[1]
        phone = parts[2]
        return add_contact(name, phone)
    elif parts[0].lower() == "change":
        name = parts[1]
        phone = parts[2]
        return change_phone(name, phone)
    elif parts[0].lower() == "phone":
        name = parts[1]
        return find_phone(name)
    elif parts[0].lower() == "show":
        return show_all_contacts()
    else:
        return "Sorry, I don't understand. Please try again."

while True:
    command = input("Enter command: ")
    response = handle_command(command)
    print(response)
