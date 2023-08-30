class Contacts:
    def __init__(self, name , phone ,email ):
        self.name = name
        self.phone = phone
        self.email = email 

    def __str__(self) :
        return f"Contact name is: {self.name} ⏭  Contact phone number is: {self.phone}  ⏭  Contact E-mail is: {self.email}"

class ContactManager (Contacts):
    def __init__(self ):
        self.contactsList =[] 

    def add_contact (self , contact):
        self.contactsList.append(contact) 

    def remove_contact (self ,contact):
        if contact in self.contactsList:
            self.contactsList.remove(contact)
            print("contact remove_contactd:) ")
        else :
            return "There is no Contact with This name:("
       
    def search_contact(self , name):
        
        for contact in self.contactsList:
            if contact.name.lower()== name.lower():
                return contact
            else:
                return "None"
                
    def display_contact(self):
        for contact in self.contactsList:
            print (contact)




def Checklist():
    
    print("Contact Manager: \n 1. add_contact Contact \n 2. Remove Contact \n 3. search_contact Contact \n 4. display_contact Contact \n 5. Exit ")


ContactManager=ContactManager()
var = True
while var == True:
    Checklist()
    operation_number = input("Enter your choice: ")
    if operation_number == "1":
        name = input("Enter the Contact name: ")
        phone = input("Enter the Contact phone number: ")
        email= input("Enter the Contact E-mail: ")
        contact=Contacts(name,phone,email)
        ContactManager.add_contact(contact)
        print ("Contact add_contacted successfully")
    elif operation_number == "2":
        name = input("Enter the name of the contact that you want to remove: ")
        contact=ContactManager.search_contact(name)

        if contact:
            ContactManager.remove_contact(contact)
        else :
            print ("Contact not founded")
    elif operation_number == "3":
        name = input("Enter the name of the contact that you want to search_contact for: ")
        if contact:
            contact=ContactManager.search_contact(name)
            print (contact)
        else :
            print ("Contact not founded")    
    elif operation_number == "4":
        ContactManager.display_contact()
    elif operation_number == "5":
        break
    else:
        print("Error please enter number from the list, try another number:) ")