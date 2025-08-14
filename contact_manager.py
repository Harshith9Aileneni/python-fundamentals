import json
from random import choice


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]


def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contacts():
    contacts = load_contacts()

    name = input("enter the name")
    phone = input("enter the phone number")
    email = input("enter the email ID")

    new_contact = {"name" : name, "phone": phone, "email" : email}
    contacts.append(new_contact)
    save_contacts(contacts)

    print(f" contact {name} is successfully added")

def view_contact():
    contacts = load_contacts()
    if not contacts:
        print("contact not found!")
        return
    print("\n All Contacts")
    for i, contact in enumerate(contacts, 1):  # Use 'contact' (singular)
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def main():
    while True:
        print("Contact Manager")
        print("1.add contacts")
        print("2.view contacts")
        print("3.exit")

        choice = input("choose an option from (1-3)")

        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            print("goodbye")
            break
        else:
            print("invalid choice")
main()

