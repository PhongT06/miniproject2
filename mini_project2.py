import re

# Initialize contact data
contacts = {}

# Regular expressions for input validation
phone_pattern = re.compile(r'^\d{10}$')
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Function to add a new contact
def add_contact():
    print("Adding a new contact:")
    contact_id = input("Enter unique identifier (phone number or email address): ")
    if contact_id in contacts:
        print("Contact already exists!")
        return
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    while not phone_pattern.match(phone_number):
        print("Invalid phone number format!")
        phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    while not email_pattern.match(email):
        print("Invalid email address format!")
        email = input("Enter email address: ")
    address = input("Enter address (optional): ")
    notes = input("Enter additional notes (optional): ")
    contacts[contact_id] = {'Name': name, 'Phone': phone_number, 'Email': email, 'Address': address, 'Notes': notes}
    print("Contact added successfully!")

# Function to edit an existing contact
def edit_contact():
    print("Editing an existing contact:")
    contact_id = input("Enter unique identifier of the contact to edit: ")
    if contact_id not in contacts:
        print("Contact not found!")
        return
    print("Current details:")
    print_contact(contact_id)
    name = input("Enter new name (leave blank to keep current): ")
    if name:
        contacts[contact_id]['Name'] = name
    phone_number = input("Enter new phone number (leave blank to keep current): ")
    if phone_number:
        while not phone_pattern.match(phone_number):
            print("Invalid phone number format!")
            phone_number = input("Enter new phone number: ")
        contacts[contact_id]['Phone'] = phone_number
    email = input("Enter new email address (leave blank to keep current): ")
    if email:
        while not email_pattern.match(email):
            print("Invalid email address format!")
            email = input("Enter new email address: ")
        contacts[contact_id]['Email'] = email
    address = input("Enter new address (leave blank to keep current): ")
    contacts[contact_id]['Address'] = address
    notes = input("Enter new additional notes (leave blank to keep current): ")
    contacts[contact_id]['Notes'] = notes
    print("Contact updated successfully!")

# Function to delete a contact
def delete_contact():
    print("Deleting a contact:")
    contact_id = input("Enter unique identifier of the contact to delete: ")
    if contact_id not in contacts:
        print("Contact not found!")
        return
    del contacts[contact_id]
    print("Contact deleted successfully!")

# Function to search for a contact
def search_contact():
    print("Searching for a contact:")
    contact_id = input("Enter unique identifier of the contact to search for: ")
    if contact_id not in contacts:
        print("Contact not found!")
        return
    print_contact(contact_id)

# Function to display all contacts
def display_contacts():
    print("All contacts:")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact_id in enumerate(contacts, start=1):
        print(f"{i}. {contact_id}: {contacts[contact_id]['Name']}")

# Function to export contacts to a text file
def export_contacts():
    print("Exporting contacts to text file.")
    with open("contacts.txt", "w") as file:
        for contact_id in contacts:
            file.write(f"{contact_id}\n")
            for key, value in contacts[contact_id].items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    print("Contacts exported successfully!")

# Function to print contact details
def print_contact(contact_id):
    print(f"Name: {contacts[contact_id]['Name']}")
    print(f"Phone: {contacts[contact_id]['Phone']}")
    print(f"Email: {contacts[contact_id]['Email']}")
    print(f"Address: {contacts[contact_id]['Address']}")
    print(f"Notes: {contacts[contact_id]['Notes']}")

# Main function to display menu and handle user input
def main():
    print("Welcome to the Contact Management System!")
    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 7.")

main()
