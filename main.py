from tkinter import *
from tkinter import messagebox
import pyperclip
import json


def save_password():
    w = website_input.get()
    p = password_input.get()
    e = email_input.get()
    
    new_data = {
        w: {
            "email": e,
            "password": p,
        }
    }
    
    if  w and p and e:

        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
                    
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else: 
            data.update(new_data)
                
            with open("data.json", "w") as f:
                json.dump(new_data, f)          
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
        
        messagebox.showinfo(message="Saved Successfully")
    else:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

def password_generator():
    import random
    import string
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    
    password_letters = [random.choice(string.ascii_letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(string.punctuation) for _ in range(nr_symbols)]
    password_digits = [random.choice(string.digits) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_digits
    
    random.shuffle(password_list)

    password = "".join(password_list)

    if password_input:
        password_input.delete(0, END)
        
    password_input.insert(0, password)
    
    pyperclip.copy(password)

def search():
    name = website_input.get()
    
    try:
        with open('data.json') as f:
            websites = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found, save some information first.")  
    
    else:
        if name in websites:
            messagebox.showinfo(title=name, message=f"Email: {websites[name]['email']}\npassword: {websites[name]['password']}")
        else:
            messagebox.showerror(message="Data not found")
        
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
email_input.insert(0, "mrboomed99@gmail.com")
password_input = Entry(width=35)
password_input.grid(row=3, column=1, columnspan=2, padx=10)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, padx=10, pady=10)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10 )

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, padx=10)

window.mainloop()