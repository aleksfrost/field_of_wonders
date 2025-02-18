from tkinter import Button, Entry, Label
import tkinter as tk

from main import main_game
from users import User, auth_user

font_header = ("Arial", 15)
font_entry = ("Arial", 12)
label_font = ("Arial", 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class AuthWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Field of Wonders")
        self.root.geometry("300x300+300+300")

        self.frame_label = Label(root, text="Authorisation", font=font_header, justify="center")
        self.frame_label.pack(**header_padding)
        self.login_entry = Entry(root, font=font_entry)
        self.login_entry.pack(**base_padding)
        self.label_login = Label(root, text="login", font=label_font)
        self.label_login.pack(**base_padding)
        self.password_entry = Entry(root, font=font_entry, show="*")
        self.password_entry.pack(**base_padding)
        self.label_password = Label(root, text="password", font=label_font)
        self.label_password.pack(**base_padding)

        self.login_btn = Button(root, text='Войти', command=self.login)
        self.login_btn.pack(**base_padding)
        self.toggle_btn = Button(root, text='Show Password', width=15, command=self.toggle_password)
        self.toggle_btn.pack(**base_padding)


    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        user = auth_user(login, password)
        if user:
            self.root.destroy()
            main_window = MainWindow(user)
            #main_game(user) отсюда запуск игры идет

    def toggle_password(self):
        if self.password_entry.cget('show') == '':
            self.password_entry.config(show='*')
            self.toggle_btn.config(text='Show Password')
        else:
            self.password_entry.config(show='')
            self.toggle_btn.config(text='Hide Password')


class MainWindow:
    def __init__(self, user: User):
        self.root = tk.Tk()
        self.root.title(f"Main window")
        self.label = Label(self.root, text=f"Hello {user.user_name}", font=font_header, justify="center")
        self.label.pack(**header_padding)
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    auth_window = AuthWindow(root)
    root.mainloop()
