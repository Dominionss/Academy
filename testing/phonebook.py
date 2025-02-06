from pathlib import Path
"""
This module can help you in creating and maintaining a phonebook.
"""


def create_phonebook(name_of_phonebook):
    with open(name_of_phonebook, "w") as phonebook:
        pass

def create_contact(name_of_phonebook, first_name, last_name, telephone_number, country):
    with open(name_of_phonebook, "a") as phonebook:
        phonebook.writelines(f"{first_name} {last_name} {telephone_number} {country}\n")


def get_contacts(name_of_phonebook, first_name="None", last_name="None", telephone_number="None", country="None"):
    target = [first_name, last_name, telephone_number, country]
    result = []
    with open(name_of_phonebook, "r") as phonebook:
        contacts = phonebook.readlines()
        for contact in contacts:
            if bool(set(contact.split()) & set(target)):
                result.append(contact)
    return result


def delete_contacts(name_of_phonebook, first_name="None", last_name="None", telephone_number="None", country="None"):
    target = get_contacts(name_of_phonebook, first_name, last_name, telephone_number, country)
    with open(name_of_phonebook, "r") as phonebook:
        contacts = phonebook.readlines()

    with open(name_of_phonebook, "w") as phonebook:
        for contact in contacts:
            if contact not in target:
                phonebook.write(contact)


def update_contacts(name_of_phonebook, first_name="None", last_name="None", telephone_number="None", country="None", new_first_name="None", new_last_name="None", new_telephone_number="None", new_country="None"):
    target = get_contacts(name_of_phonebook, first_name, last_name, telephone_number, country)
    changes = [new_first_name, new_last_name, new_telephone_number, new_country]

    with open(name_of_phonebook, "r") as phonebook:
        contacts = phonebook.readlines()

    with open(name_of_phonebook, "w") as phonebook:
        for contact in contacts:
            if contact in target:
                changed_contact = contact.split()

                for element in changed_contact:
                    index = changed_contact.index(element)
                    if changes[index] != "None":
                        changed_contact[index] = changes[index]

                changed_contact = " ".join(changed_contact) + "\n"
                phonebook.write(changed_contact)
            else:
                phonebook.write(contact)
