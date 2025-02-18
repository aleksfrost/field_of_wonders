from tkinter import Button, Entry, Label, Tk

from game.users import auth_user


root = Tk()

root.title("Field of Wonders")
root.geometry("300x300+300+300")

font_header = ("Arial", 15)
font_entry = ("Arial", 12)
label_font = ("Arial", 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def clicked():
    login = login_entry.get()
    password = password_entry.get()
    user = auth_user(login, password)


def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='Show Password')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='Hide Password')

frame_label = Label(root, text="Authorisation", font=font_header, justify="center")
frame_label.pack(**header_padding)
login_entry = Entry(root, font=font_entry)
login_entry.pack(**base_padding)
label_login = Label(root, text="login", font=label_font)
label_login.pack(**base_padding)
password_entry = Entry(root, font=font_entry, show="*")
password_entry.pack(**base_padding)
label_password = Label(root, text="password", font=label_font)
label_password.pack(**base_padding)

send_btn = Button(root, text='Войти', command=clicked)
send_btn.pack(**base_padding)
toggle_btn = Button(root, text='Show Password', width=15, command=toggle_password)
toggle_btn.pack(**base_padding)

root.mainloop()