import tkinter
from tkinter import messagebox
from ClientGUI import Config


class SenderFrame:
    def __init__(self):
        config = Config.Config().SenderFrameConfig
        self.root = tkinter.Tk()
        self.root.title('Sending Emails...')
        self.root.geometry("%sx%s" % (config.root_width, config.root_height))
        self.state_label = tkinter.Label(self.root, text='Sender Box')
        self.state_label.place(x=config.state_label_x, y=config.state_label_y)
        self.change_state_button = tkinter.Button(self.root, text='To Receiver Box')
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
        self.send_button = tkinter.Button(self.root, text='Send')
        self.send_button.place(x=config.send_button_x, y=config.send_button_y)

    def show(self):
        self.root.mainloop()

    @staticmethod
    def show_success(msg: str):
        messagebox.showinfo(title='Success!', message=msg)
