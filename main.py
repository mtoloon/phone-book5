contacts = []

while False:
    ch = input("""Enter a choice:
    0: exit
    1=>new
    2=>list
    3=>search
    """)

    if ch == '0':
        break
    if ch == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contact = [name, phone]
        contacts.append(contact)
    elif ch == '2':
        print(contacts)
    elif ch == '3':
        name = input("Enter name: ")
        for contact in contacts:
            if contact[0] == name:
                contact[1]
     
        
