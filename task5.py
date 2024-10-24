class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.name} | Phone: {self.phone} | Email: {self.email} | Address: {self.address}"


contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.\n")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact.name} | Phone: {contact.phone}")
    else:
        print("No contacts found.\n")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
    
    if found_contacts:
        for contact in found_contacts:
            print(contact)
    else:
        print(f"No contact found for '{search_term}'.\n")

def update_contact():
    search_term = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact.name.lower() == search_term.lower():
            print(f"Updating contact: {contact.name}")
            contact.phone = input("Enter new phone number: ") or contact.phone
            contact.email = input("Enter new email: ") or contact.email
            contact.address = input("Enter new address: ") or contact.address
            print("Contact updated successfully.\n")
            return
    print(f"No contact found with name '{search_term}'.\n")


def delete_contact():
    search_term = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact.name.lower() == search_term.lower():
            contacts.remove(contact)
            print(f"Contact '{contact.name}' deleted successfully.\n")
            return
    print(f"No contact found with name '{search_term}'.\n")
def contact_manager():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
contact_manager()
