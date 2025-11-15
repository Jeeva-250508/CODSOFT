contacts = {}
def add_contact():
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    
    for name, data in contacts.items():
        print(name, "-", data["phone"])


def search_contact():
    query = input("Search by name or phone: ")
    match_found = False

    for name, data in contacts.items():
        if query.lower() in name.lower() or query in data["phone"]:
            print("------ Contact Found ------")
            print("Name:", name)
            print("Phone:", data["phone"])
            print("Email:", data["email"])
            print("Address:", data["address"])
            match_found = True

    if not match_found:
        print("No contact matched your search.")


def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name not in contacts:
        print("That contact does not exist.")
        return

    print("Leave any field empty if you do not want to change it.")

    new_phone = input("New Phone Number: ")
    new_email = input("New Email: ")
    new_address = input("New Address: ")

    if new_phone != "":
        contacts[name]["phone"] = new_phone
    if new_email != "":
        contacts[name]["email"] = new_email
    if new_address != "":
        contacts[name]["address"] = new_address

    print("Contact updated successfully!")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("No contact found with that name.")


while True:
    print("CONTACT BOOK ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1–6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the contact book")
        break
    else:
        print("Invalid option. Please try again.")