import tkinter
from ClientGUI import Config
from tkinter import messagebox


class LoginFrame:
    def __init__(self):
        config = Config.Config().loginFrameConfig
        self.root = tkinter.Tk()
        self.root.title("Login")
        self.root.geometry("%sx%s" % (config.root_width, config.root_height))
        self.username_label = tkinter.Label(self.root, text="Username:")
        self.username_label.place(x=config.username_label_x, y=config.username_label_y)
        self.username_entry = tkinter.Entry(self.root, width=config.label_width)
        self.username_entry.place(x=config.username_x, y=config.username_y)
        self.password_label = tkinter.Label(self.root, text="Password:")
        self.password_label.place(x=config.password_label_x, y=config.password_label_y)
        self.password_entry = tkinter.Entry(self.root, width=config.label_width)
        self.password_entry.place(x=config.password_x, y=config.password_y)
        self.login_button = tkinter.Button(self.root, text="Login")
        self.login_button.place(x=config.login_button_x, y=config.login_button_y)
        self.error_message = "waiting"

    def get_username(self):
        username = self.username_entry.get()
        return username

    def get_password(self):
        password = self.password_entry.get()
        return password

    def show(self):
        self.root.mainloop()

    def show_err(self):
        messagebox.showerror(title=self.error_message,message='please check your username and authentication_string')

    def destroy(self):
        if not self.error_message:
            self.root.destroy()
            
