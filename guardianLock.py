'''
Author: Diego Campos
Version: 1.0
Date: 09/28/24
Assignment: Final Project 
Description:
This is the final project for Introduction to Software Development class
at IvyTech Fall 24. This project has been developed using Tkinter as GUI
using Python as language. The main goal of this app is to help people to
choose a secure password every time that the user requires it.
'''

import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage
import random
import string

# Main Application Class
class GuardianLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Maker Helper")
        self.root.geometry("500x400")
        self.root.resizable(0,0)
        
        #Background-image
        self.imagePath = tk.PhotoImage(file="bg2.png")
        self.img_copy= self.imagePath.copy()
        self.background = tk.Label(self.root, image= self.imagePath)
        self.background.place(relx=0.4, rely=0.35, anchor="center")
        
        # Header
        self.header_label = tk.Label(root, text="Password Maker Helper", font=("Arial", 16))
        self.header_label.pack(pady=10)

        # Password Generation
        self.createPasswordGeneration()

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
    
    def createPasswordGeneration(self):
        # Password Length
        tk.Label(self.root, text="Password Length:").pack(pady=5)
        self.lengthEntry = tk.Entry(self.root)
        self.lengthEntry.pack(pady=5)

        # Complexity Checkboxes
        self.includeUppercase = tk.BooleanVar()
        self.includeLowercase = tk.BooleanVar()
        self.includeNumbers = tk.BooleanVar()
        self.includeSpecial = tk.BooleanVar()

        tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.includeUppercase).pack()
        tk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.includeLowercase).pack()
        tk.Checkbutton(self.root, text="Include Numbers", variable=self.includeNumbers).pack()
        tk.Checkbutton(self.root, text="Include Special Characters", variable=self.includeSpecial).pack()

        # Generate Button
        self.generateButton = tk.Button(self.root, text="Generate Password", command=self.generatePassword)
        self.generateButton.pack(pady=10)

        # Display Generated Password
        self.passwordDisplay = tk.Entry(self.root, width=50)
        self.passwordDisplay.pack(pady=5)

        # Copy Button
        self.copyButton = tk.Button(self.root, text="Copy to Clipboard", command=self.copyToClipboard)
        self.copyButton.pack(pady=5)

    def generatePassword(self):
        length = self.getPasswordLength()
        if length is None:
            return

        characters = ""
        if self.includeUppercase.get():
            characters += string.ascii_uppercase
        if self.includeLowercase.get():
            characters += string.ascii_lowercase
        if self.includeNumbers.get():
            characters += string.digits
        if self.includeSpecial.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "At least one character type must be selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.passwordDisplay.delete(0, tk.END)
        self.passwordDisplay.insert(0, password)

    def getPasswordLength(self):
        try:
            length = int(self.lengthEntry.get())
            if length <= 0:
                raise ValueError
            return length
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
            return None

    def copyToClipboard(self):
        password = self.passwordDisplay.get()
        if password == "":
            messagebox.showerror("Error", "You must create a password to use this feature.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Info", "Password copied to clipboard.")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = GuardianLockApp(root)
    root.mainloop()