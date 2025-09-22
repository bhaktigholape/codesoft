import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact list
contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_entries()
    view_contacts()


def view_contacts():
    listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts, 1):
        listbox.insert(tk.END, f"{i}. {contact['name']} | 📞 {contact['phone']}")


def search_contact():
    keyword = simpledialog.askstring("Search", "Enter Name or Phone:")
    if not keyword:
        return

    listbox.delete(0, tk.END)
    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            listbox.insert(tk.END, f"{contact['name']} | 📞 {contact['phone']}")
            found = True

    if not found:
        messagebox.showinfo("Search Result", "No contact found.")


def update_contact():
    try:
        index = listbox.curselection()[0]
        contact = contacts[index]

        new_name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact["name"])
        new_phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contact["phone"])
        new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact["email"])
        new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact["address"])

        contacts[index] = {
            "name": new_name or contact["name"],
            "phone": new_phone or contact["phone"],
            "email": new_email or contact["email"],
            "address": new_address or contact["address"]
        }

        messagebox.showinfo("Success", "Contact updated successfully!")
        view_contacts()

    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")


def delete_contact():
    try:
        index = listbox.curselection()[0]
        removed = contacts.pop(index)
        messagebox.showinfo("Deleted", f"Contact '{removed['name']}' deleted successfully!")
        view_contacts()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("📒 Contact Management System")
root.geometry("500x500")

# Labels & Entry fields
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Address:").pack()
entry_address = tk.Entry(root, width=40)
entry_address.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

root.mainloop()
