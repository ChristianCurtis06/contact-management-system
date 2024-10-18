import re

def add_new_contact(contacts):
    number_input = input("Enter the contact's phone number (XXX-XXX-XXXX): ").strip()
    if re.search(r'\b\d{3}-\d{3}-\d{4}\b', number_input):
        if number_input not in contacts:
            name_input = input("Enter the contact's first and last name: ").strip().title()
            if re.search(r'\b[a-zA-Z]+\b\s\b[a-zA-Z]+\b', name_input):
                email_input = input("Enter the contact's email address: ").strip()
                if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', email_input):
                    address_choice = input("Would you like to add the contact's home address? (yes/no) ").lower()
                    if address_choice == 'yes':
                        address_input = input("Enter the contact's home address: ").strip()
                    else:
                        address_input = "None"
                    note_choice = input("Would you like to add a note for the contact? (yes/no) ").lower()
                    if note_choice == 'yes':
                        note_input = input("Enter the contact's note: ").strip()
                    else:
                        note_input = "None"

                    contacts[number_input] = {'name': name_input, 'phone_number': number_input, 'email_address': email_input, 'home_address': address_input, 'note': note_input}
                    print(f"{name_input}'s contact added to contacts.")
                else:
                    print("Invalid email address. Please enter valid email.")
            else:
                print("Invalid name. Please enter first and last name.")
        else:
            print("Phone number already exists in contacts. Please try again.")
    else:
        print("Invalid phone number. Please use 'XXX-XXX-XXXX' format.")

def edit_existing_contact(contacts):
    old_number_input = input("Enter the contact's original phone number (XXX-XXX-XXXX): ").strip()
    if re.search(r'\b\d{3}-\d{3}-\d{4}\b', old_number_input):
        if old_number_input in contacts:
            new_number_input = input("Enter the contact's updated phone number (XXX-XXX-XXXX): ").strip()
            if re.search(r'\b\d{3}-\d{3}-\d{4}\b', new_number_input): 
                name_input = input("Enter the contact's updated first and last name: ").strip().title()
                if re.search(r'\b[a-zA-Z]+\b\s\b[a-zA-Z]+\b', name_input):
                    email_input = input("Enter the contact's updated email address: ").strip()
                    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', email_input):
                        address_choice = input("Would you like to edit the contact's home address? (yes/no) ").lower()
                        if address_choice == 'yes':
                            address_input = input("Enter the contact's updated home address: ").strip()
                        else:
                            address_input = contacts[old_number_input]['home_address']
                        note_choice = input("Would you like to edit a note for the contact? (yes/no) ").lower()
                        if note_choice == 'yes':
                            note_input = input("Enter the contact's updated note: ").strip()
                        else:
                            note_input = contacts[old_number_input]['note']

                        contacts[new_number_input] = {'name': name_input, 'phone_number': new_number_input, 'email_address': email_input, 'home_address': address_input, 'note': note_input}
                        print(f"{contacts[old_number_input]['name']}'s contact edited in contacts.")
                        contacts.pop(old_number_input)
                    else:
                        print("Invalid email address. Please enter valid email.")
                else:
                    print("Invalid name. Please enter first and last name.")
            else:
                print("Invalid phone number. Please use 'XXX-XXX-XXXX' format.")
        else:
            print("Phone number not found in contacts. Please try again.")
    else:
        print("Invalid phone number. Please use 'XXX-XXX-XXXX' format.")

def delete_contact(contacts):
    number_input = input("Enter the contact's phone number (XXX-XXX-XXXX): ").strip()
    if re.search(r'\b\d{3}-\d{3}-\d{4}\b', number_input) and number_input in contacts:
        print(f"{contacts[number_input]['name']}'s contact deleted from contacts.")
        contacts.pop(number_input)
    else:
        print("Invalid phone number. Please use 'XXX-XXX-XXXX' format.")

def search_for_contact(contacts):
    number_input = input("Enter the contact's phone number (XXX-XXX-XXXX): ").strip()
    if re.search(r'\b\d{3}-\d{3}-\d{4}\b', number_input):
        if number_input in contacts:
            print(f"\nName: {contacts[number_input]['name']}\n- Phone Number: {number_input}\n- Email Address: {contacts[number_input]['email_address']}\n- Home Address: {contacts[number_input]['home_address']}\n- Note: {contacts[number_input]['note']}")
        else:
            print("Phone number not found in contacts. Please try again.")
    else:
        print("Invalid phone number. Please use 'XXX-XXX-XXXX' format.")

def display_contacts(contacts):
    if contacts:
        print("Contacts:")
        for number, details in contacts.items():
            print(f"\nName: {details['name']}\n- Phone Number: {number}\n- Email Address: {details['email_address']}\n- Home Address: {details['home_address']}\n- Note: {details['note']}")
    else:
        print("Contacts are empty. Please add a contact before displaying them.")

def export_contacts(filename, contacts):
    try:
        with open(filename, 'w') as file:
            for number, details in contacts.items():
                file.write(f"{details['name']}, {number}, {details['email_address']}, {details['home_address']}, {details['note']}\n")
            print("Contacts exported to file.")
    
    except FileNotFoundError:
        print("FileNotFoundError: Invalid file or path.")
    except PermissionError:
        print("PermissionError: Unable to access file.")

def import_contacts(filename, contacts):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number, email, address, note = line.strip().split(', ')
                if number not in contacts:
                    contacts[number] = {'name': name, 'phone_number': number, 'email_address': email, 'home_address': address, 'note': note}
                else:
                    continue
            print("Contacts imported from file.")

    except FileNotFoundError:
        print("FileNotFoundError: Invalid file or path.")
    except PermissionError:
        print("PermissionError: Unable to access file.")

contacts = {
    '123-123-1234': {'name': 'John Doe', 'phone_number': '123-123-1234', 'email_address': 'email@address.com', 'home_address': 'None', 'note': 'None'}
}

print("Welcome to the Contact Management System!")
while True:
    print("\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")
    user_input = input("Enter your choice: ").strip()
    
    try:
        if user_input == '1':
            add_new_contact(contacts)
        elif user_input == '2':
            edit_existing_contact(contacts)
        elif user_input == '3':
            delete_contact(contacts)
        elif user_input == '4':
            search_for_contact(contacts)
        elif user_input == '5':
            display_contacts(contacts)
        elif user_input == '6':
            export_contacts(r'contact-management-system\contacts_file.txt', contacts)
        elif user_input == '7':
            import_contacts(r'contact-management-system\contacts_file.txt', contacts)
        elif user_input == '8':
            print("Quitting the system...")
            break
        else:
            print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")