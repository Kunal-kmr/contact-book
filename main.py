import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({
            'name': name,
            'phone': phone,
        })
        messagebox.showinfo("Success", "Contact added successfully.")

    def search_contact(self, search_key):
        results = []
        for contact in self.contacts:
            if (search_key.lower() in contact['name'].lower()) or (search_key in contact['phone']):
                results.append(contact)
        return results

    def update_contact(self, index, name, phone):
        self.contacts[index] = {
            'name': name,
            'phone': phone,
        }
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self, index):
        del self.contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully.")

    def get_all_contacts(self):
        return self.contacts


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Styling
        self.root.configure(bg="#cce6ff")
        self.label_font = ('Helvetica', 15, 'bold')
        self.entry_font = ('Helvetica', 12)
        self.button_font = ('Helvetica', 15, 'bold')
        self.listbox_font = ('Helvetica', 12)
        
        # Contact Book instance
        self.contact_book = ContactBook()

        # Labels and Entries
        self.name_label = tk.Label(root, text="Name:", font=self.label_font, bg="#f0f0f0")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(root, width=30, font=self.entry_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:", font=self.label_font, bg="#f0f0f0")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry = tk.Entry(root, width=30, font=self.entry_font)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", font=self.button_font, command=self.add_contact, bg="#1aa3ff", fg="black", relief=tk.RAISED)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

        self.search_label = tk.Label(root, text="Search:", font=self.label_font, bg="#f0f0f0")
        self.search_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.search_entry = tk.Entry(root, width=30, font=self.entry_font)
        self.search_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        self.search_button = tk.Button(root, text="Search", font=self.button_font, command=self.search_contact, bg="#ffff00", fg="black", relief=tk.RAISED)
        self.search_button.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.view_button = tk.Button(root, text="View All Contacts", font=self.button_font, command=self.view_contacts, bg="#FF9800", fg="white", relief=tk.RAISED)
        self.view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

        self.update_button = tk.Button(root, text="Update Contact", font=self.button_font, command=self.update_contact, bg="#00994d", fg="black", relief=tk.RAISED)
        self.update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

        self.delete_button = tk.Button(root, text="Delete Contact", font=self.button_font, command=self.delete_contact, bg="#F44336", fg="white", relief=tk.RAISED)
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

        # Contact Listbox
        self.contact_listbox = tk.Listbox(root, height=10, width=50, font=self.listbox_font, relief=tk.SUNKEN, borderwidth=2)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

        self.contact_listbox.bind("<Double-Button-1>", self.on_contact_select)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required.")
            return

        self.contact_book.add_contact(name, phone)
        self.clear_entries()
        self.view_contacts()

    def search_contact(self):
        search_key = self.search_entry.get().strip()
        if search_key:
            results = self.contact_book.search_contact(search_key)
            self.display_contacts(results)
        else:
            self.view_contacts()

    def view_contacts(self):
        contacts = self.contact_book.get_all_contacts()
        self.display_contacts(contacts)

    def display_contacts(self, contacts):
        self.contact_listbox.delete(0, tk.END)
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Select a contact to update.")
            return
        index = selected_index[0]
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required.")
            return

        self.contact_book.update_contact(index, name, phone)
        self.clear_entries()
        self.view_contacts()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Select a contact to delete.")
            return
        index = selected_index[0]
        self.contact_book.delete_contact(index)
        self.clear_entries()
        self.view_contacts()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def on_contact_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contact_book.get_all_contacts()[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact['phone'])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
