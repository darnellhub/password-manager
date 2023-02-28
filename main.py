from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WHITE = "#FFFFFF"
BLACK = "#000000"
window = Tk()
password = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def search_db():
    website = website_entrybox.get()
    try:
        with open("dat.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Password Manager", message="Database cannot be found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Password Manger", message=f"Login: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Entry Unknown")





def password_gen():
    global password
    global letters
    global numbers
    global symbols
    password_entrybox.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = str("".join(password_list))

    pyperclip.copy(password)

    password_entrybox.insert(END, password)


def save_info():
    website = website_entrybox.get()
    email = email_entrybox.get()
    password = password_entrybox.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Password Generator", message="You made an error")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror("Password Manager", "Database Missing, will create a new one now")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entrybox.delete(0, END)
            password_entrybox.delete(0, END)
            email_entrybox.delete(0, END)
            messagebox.showinfo("Password Manager", "Info Saved")


window.title("Password Manager")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", fg=BLACK)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Website:", fg=BLACK)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg=BLACK)
password_label.grid(row=3, column=0)

search_button = Button(text="Search", width="13", command=search_db)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=password_gen)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="ADD", width=36, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

website_entrybox = Entry(width=20)
website_entrybox.grid(column=1, row=1)
website_entrybox.focus()
email_entrybox = Entry(width=38)
email_entrybox.grid(row=2, column=1, columnspan=2)
password_entrybox = Entry(width=20)
password_entrybox.grid(column=1, row=3)


window.mainloop()