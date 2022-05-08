import tkinter
from tkinter import messagebox
from ClientGUI import Config


class ReceiverFrame:
    def __init__(self):
        config = Config.Config().ReceiverFrameConfig
        self.root = tkinter.Tk()
        self.root.title('Receiving Emails...')
        self.root.geometry("%sx%s" % (config.root_width, config.root_height))
        self.state_label = tkinter.Label(self.root, text='Receiver Box')
        self.state_label.place(x=config.state_label_x, y=config.state_label_y)
        self.mail_num_label = tkinter.Label(self.root)
        self.mail_num_label.place(x=config.mail_num_label_x, y=config.mail_num_label_y)
        self.change_state_button = tkinter.Button(self.root, text='To Sender Box')
        self.change_state_button.place(x=config.change_state_button_x, y=config.change_state_button_y)
        self.sender_label = tkinter.Label(self.root, text='Sender:')
        self.sender_label.place(x=config.sender_label_x, y=config.sender_label_y)
        self.sender = tkinter.Text(self.root, height=config.sender_height, width=config.sender_width)
        self.sender.place(x=config.sender_x, y=config.sender_y)
        self.receiver_label = tkinter.Label(self.root, text='Receiver:')
        self.receiver_label.place(x=config.receiver_label_x, y=config.receiver_label_y)
        self.receiver = tkinter.Text(self.root, height=config.receiver_height, width=config.receiver_width)
        self.receiver.place(x=config.receiver_x, y=config.receiver_y)
        self.subject_label = tkinter.Label(self.root, text='Subject:')
        self.subject_label.place(x=config.subject_label_x, y=config.subject_label_y)
        self.subject = tkinter.Text(self.root, height=config.subject_height, width=config.subject_width)
        self.subject.place(x=config.subject_x, y=config.subject_y)
        self.text_label = tkinter.Label(self.root, text='Text:')
        self.text_label.place(x=config.text_label_x, y=config.text_label_y)
        self.text = tkinter.Text(self.root, height=config.text_height, width=config.text_width)
        self.text.place(x=config.text_x, y=config.text_y)
        self.mail_choose_label = tkinter.Label(self.root, text='Choose Mail:')
        self.mail_choose_label.place(x=config.mail_choose_label_x, y=config.mail_choose_label_y)
        self.mail_choose = tkinter.Text(self.root, height=config.mail_choose_height, width=config.mail_choose_width)
        self.mail_choose.place(x=config.mail_choose_x, y=config.mail_choose_y)
        self.send_button = tkinter.Button(self.root, text='Choose')
        self.send_button.place(x=config.send_button_x, y=config.send_button_y)

    def show(self):
        self.root.mainloop()

    @staticmethod
    def show_success(msg: str):
        messagebox.showinfo(title='Success!', message=msg)

    @staticmethod
    def show_error(msg: str):
        messagebox.showerror(title='Error!', message=msg)