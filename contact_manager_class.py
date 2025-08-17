import json

class ContactManager:
    def __init__(self):
        print("creating Contact Manager@")
        self.contacts = []
        self.load_from_file()

    def add_contacts(self,name,phone,email):
        new_contact = {"name" : name, "phone" : phone, "email" : email}
        self.contacts.append(new_contact)
        self.save_to_file()
        print(f"Contact with name: {name} has been successfully created")



    def show_all_contacts(self):
        if not self.contacts:
            print(" No contact")

        print("\n...ALL Contacts>>")
        for i, contact in enumerate(self.contacts, 1):
            print(F"{i} . {contact['name']} - {contact['phone']}")

    def count_contacts(self):
        return len(self.contacts)

    def save_to_file(self):
        with open("contacts.json","w") as file:
            json.dump(self.contacts, file, indent=2)

    def load_from_file(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
                print(f"loaded {len(self.contacts)} Contacts")
        except FileNotFoundError:
            print("Yoo bro, I can't find that Contact")






manager = ContactManager()
manager.add_contacts("Harsh", "123456", "harsh@gmail.com")
manager.add_contacts("Swathi", "789012", "swathi@gmail.com")
manager.show_all_contacts()
print(f"Total contacts: {manager.count_contacts()}")



