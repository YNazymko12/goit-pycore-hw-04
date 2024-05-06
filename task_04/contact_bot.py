def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return f"The name {name} is already exists on your contacts list."
        else:
            contacts[name] = phone
            return "Contact added."
    except ValueError as ve:
        return str(ve)   

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f"The name {name} is not on your contacts list yet."
    except ValueError as ve:
        return str(ve)       

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else: 
            return f"The name {name} is not on your contacts list yet."
    except ValueError as ve:
        return str(ve)       
    
def show_all(contacts):
    res = ""  

    if len(contacts) == 0:
        return "Your contact list is empty."
    else:
        for name, phone in contacts.items():
            res += f"{name}: {phone} \n"
        return res.rstrip("\n")  