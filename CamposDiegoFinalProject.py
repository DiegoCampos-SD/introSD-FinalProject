'''
Author: Diego Campos
Version: 1.0
Date: 10/09/24
Assignment: Final Project 
Description:
This is the final project for Introduction to Software Development class
at IvyTech Fall 24. This project has been developed using Tkinter as GUI
using Python as language. The main goal of this app is to help people to
choose a secure password every time that the user requires it.
'''

import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage, Frame,Toplevel
import random
import string

# Main Application Class
class guardianLockApp:
#This function will be crating the first app window (welcome window) .  
    def __init__(self, root):
        self.root = root
        self.root.attributes('-toolwindow', True)
        self.root.title("Password Maker Helper")
        self.root.geometry("400x200+400+300")
        self.root.resizable(0,0)
        
        #Background-image
        self.imagePath = tk.PhotoImage(file="bg1.png")
        self.background1 = tk.Label(self.root, image= self.imagePath)
        self.background1.place(relx=0.2, rely=0.75, anchor="center")
        
        # Header
        self.header_label = tk.Label(root, text="Welcome to Password Maker Helper", font=("Arial", 16), background="#d5eafd")
        self.header_label.pack(pady=10)
        
        # Button frame to contain buttons
        self.buttonFrame = tk.Frame(root, background="#caf0f8")
        self.buttonFrame.pack(pady=20)

        # Buttons creation
        # Start app button
        self.generateButton = tk.Button(self.buttonFrame, text="Start", height=1, width=4, font=("Arial", 12), fg='white', background="#588157", command=self.createPasswordGeneration) #Button to start the app
        self.generateButton.pack(side="left", padx=5)
        
        # Information button
        self.generateButton = tk.Button(self.buttonFrame, text="Info", height=1, width=4, font=("Arial", 12), fg="white", background="#669bbc", command=self.showInfo) #Button to show app information
        self.generateButton.pack(side="left", padx=5)
        
        # Exit button
        self.generateButton = tk.Button(self.buttonFrame, text="Exit", height=1, width=4, font=("Arial", 12), fg="white", background="#780000", command=self.root.destroy) #Button to exit the app
        self.generateButton.pack(side="left", padx=5)


#This function will be populate when the user clicks the info button in the main window.
    def showInfo(self): 
        messagebox.showinfo("App information", "A password maker app is a tool designed " +
                            "to generate strong, unique passwords for users. This app " + 
                            "offers features like customizable length, inclusion of special " +
                            "characters, uppercase letters, lowercase letters and numbers. Also " +
                            "this app includes a copy to clipboard option, so the user don't have " +
                            "to memorize the generated app. This helps users enhance their online security " + 
                            "and simplifies the process of managing multiple accounts.")
        
    
#This function will be crating the second window when the user clicks the start button in the main window.  
    def createPasswordGeneration(self):
        
        # Creats new window
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.attributes('-toolwindow', True)
        self.newWindow.overrideredirect()
        self.newWindow.geometry("500x350+400+300")
        self.newWindow.resizable(0,0)
        self.root.iconify()
        
        # Background image
        self.imagePath = tk.PhotoImage(file="bg2.png")
        self.background2 = tk.Label(self.newWindow, image= self.imagePath)
        self.background2.place(relx=0.25, rely=0.25, anchor="center")
        
        # Password Length
        tk.Label(self.newWindow, text="Password Length:", font=("Arial", 16), background="#e2d0fd").pack(pady=5)
        self.lengthEntry = tk.Entry(self.newWindow)
        self.lengthEntry.pack(pady=5)

        # Complexity Checkboxes
        self.includeUppercase = tk.BooleanVar()
        self.includeLowercase = tk.BooleanVar()
        self.includeNumbers = tk.BooleanVar()
        self.includeSpecial = tk.BooleanVar()

        tk.Checkbutton(self.newWindow, text="Include Uppercase Letters", font=("Arial", 12), background="#e2d0fd", variable=self.includeUppercase).pack()
        tk.Checkbutton(self.newWindow, text="Include Lowercase Letters", font=("Arial", 12),background="#e2d0fd", variable=self.includeLowercase).pack()
        tk.Checkbutton(self.newWindow, text="Include Numbers", font=("Arial", 12), background="#e2d0fd", variable=self.includeNumbers).pack()
        tk.Checkbutton(self.newWindow, text="Include Special Characters", font=("Arial", 12), background="#e2d0fd", variable=self.includeSpecial).pack()

        # Generate Button
        self.generateButton = tk.Button(self.newWindow, text="Generate Password", font=("Arial", 12), background="#e2d0fd", command=self.generatePassword)
        self.generateButton.pack(pady=10)

        # Display Generated Password
        self.passwordDisplay = tk.Entry(self.newWindow, width=50)
        self.passwordDisplay.pack(pady=5)

        # Copy Button
        self.copyButton = tk.Button(self.newWindow, text="Copy to Clipboard", font=("Arial", 12), background="#e2d0fd", command=self.copyToClipboard)
        self.copyButton.pack(pady=5)
        
        # Exit Button
        self.generateButton = tk.Button(self.newWindow, text="Exit", height=1, width=4, font=("Arial", 12), fg="white", background="dark red", command=self.root.destroy) #Button to exit the app
        self.generateButton.pack(side="right", padx=10, pady=10)

#This function will be generating the password with all the condition from the checkboxes selected.  
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
        

#This function will be getting the length chosen by the user and also will do 
#the validation of the input; not empty and at least 8 characters length password.
    def getPasswordLength(self):
        try:
            length = int(self.lengthEntry.get())
            if length < 8 :
                raise ValueError
            return length
        except ValueError:
            messagebox.showerror("Error", "Password length must be at least 8 characters.")
            return None
        
#This function will copy the generated password to the clipboard so the user doesn't have to memorize it 
    def copyToClipboard(self):
        password = self.passwordDisplay.get()
        if password == "":
            messagebox.showerror("Error", "You must create a password to use this feature.")
            return
        self.newWindow.clipboard_clear()
        self.newWindow.clipboard_append(password)
        messagebox.showinfo("Info", "Password copied to clipboard.")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = guardianLockApp(root)
    root.mainloop()
