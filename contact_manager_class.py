import json

class ContactManager:
    def __init__(self):
        print("creating Contact Manager@")
        self.contacts = []

    def add_contacts(self,name,phone,email):
        new_contact = {"name" : name, "phone" : phone, "email" : email}
        self.contacts.append(new_contact)
        print(f"Contact with name: {name} has been successfully created")


    def show_all_contacts(self):
        if not self.contacts:
            print(" No contact")

        print("\n...ALL Contacts>>")
        for i, contact in enumerate(self.contacts, 1):
            print(F"{i} . {contact['name']} - {contact['phone']}")

    def count_contacts(self):
        return len(self.contacts)


manager = ContactManager()
manager.add_contacts("Harsh", "123456", "harsh@gmail.com")
manager.add_contacts("Swathi", "789012", "swathi@gmail.com")
manager.show_all_contacts()
print(f"Total contacts: {manager.count_contacts()}")



