import json
import os


class ContactManager:
    def __init__(self, file_name="contacts.json"):
        self.file_name = file_name
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as file:
            return json.load(file)

    def save_contacts(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter student name: ").strip()
        email = input("Enter student email: ").strip()

        contact = {
            "name": name,
            "email": email
        }

        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully.")

    def list_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
            return

        print("\nStudent Contacts")
        print("----------------")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['email']}")

    def search_contact(self):
        search_name = input("Enter a name to search for: ").strip().lower()

        found = False
        for contact in self.contacts:
            if search_name in contact["name"].lower():
                print(f"Found: {contact['name']} - {contact['email']}")
                found = True

        if not found:
            print("No matching contact found.")

    def delete_contact(self):
        self.list_contacts()

        if len(self.contacts) == 0:
            return

        try:
            number = int(input("Enter the contact number to delete: "))
            if 1 <= number <= len(self.contacts):
                removed = self.contacts.pop(number - 1)
                self.save_contacts()
                print(f"Deleted: {removed['name']}")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    manager = ContactManager()

    while True:
        print("\nCommands: add, list, search, delete, exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            manager.add_contact()
        elif command == "list":
            manager.list_contacts()
        elif command == "search":
            manager.search_contact()
        elif command == "delete":
            manager.delete_contact()
        elif command == "exit":
            print("Goodbye.")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()