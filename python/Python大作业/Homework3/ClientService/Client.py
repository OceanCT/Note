from ClientService import ClientServer
from ClientGUI import LoginFrame
from ClientGUI import SenderFrame
from ClientGUI import ReceiverFrame


class Client:
    def __init__(self):
        self.client_server = ClientServer.ClientServer()
        self.login_frame = LoginFrame.LoginFrame()
        self.login_frame.login_button.configure(command=lambda: [
            self.login(self.login_frame.get_username(), self.login_frame.get_password()),
        ])
        self.sender_frame = None
        self.receiver_frame = None
        self.receiver = None
        self.text = None
        self.subject = None
        self.sender = None
        self.Text = None

    def login(self, username: str, password: str):
        self.client_server.change_info(username, password)
        if self.client_server.connect_to_server():
            self.login_frame.error_message = 'Connection Failed'
            self.login_frame.show_err()
            print(self.login_frame.error_message)
        else:
            self.login_frame.error_message = ""
            self.login_frame.destroy()
            self.receiver_frame = ReceiverFrame.ReceiverFrame()
            self.receiver_frame.mail_num_label.configure(
                text="You have %d mails." % self.client_server.get_mail_num())
            self.receiver_frame.send_button.configure(command=lambda: [
                self.receive_mail()
            ])
            self.receiver_frame.change_state_button.configure(command=lambda: [
                self.receiver_frame.root.destroy(),self.to_sender_frame()
            ])

    def show(self):
        self.login_frame.show()

    def get_sending_info(self):
        self.sender = self.sender_frame.sender.get('0.0', 'end')
        self.receiver = self.sender_frame.receiver.get('0.0', 'end')
        self.subject = self.sender_frame.subject.get('0.0', 'end')
        self.text = self.sender_frame.text.get('0.0', 'end')
        self.sender_frame.sender.delete('1.0', 'end')
        self.sender_frame.receiver.delete('1.0', 'end')
        self.sender_frame.subject.delete('1.0', 'end')
        self.sender_frame.text.delete('1.0', 'end')

    def send_mail(self):
        self.get_sending_info()
        mail = {
            'Subject': self.subject,
            'Context_text': self.text,
            'From': self.sender,
            'To': self.receiver,
        }
        self.client_server.send_message(mail, self.receiver)
        self.sender_frame.show_success('Have sent the email.')

    def receive_mail(self):
        target_num = self.receiver_frame.mail_choose.get('0.0', 'end')
        try:
            target_num = int(target_num)
        except Exception as e:
            print("Error happened receiving mail.")
            print(e)
            self.receiver_frame.show_error('Please input a number.')
            return
        self.receiver_frame.mail_choose.delete('1.0', 'end')
        self.receiver_frame.receiver.delete('1.0', 'end')
        self.receiver_frame.subject.delete('1.0', 'end')
        self.receiver_frame.sender.delete('1.0', 'end')
        self.receiver_frame.text.delete('1.0', 'end')
        mail = self.client_server.get_mail(target_num)
        self.receiver_frame.receiver.insert('1.0', mail['to'])
        self.receiver_frame.sender.insert('1.0', mail['from'])
        self.receiver_frame.subject.insert('1.0', mail['subject'])
        self.receiver_frame.text.insert('1.0', mail['content_text'])

    def to_sender_frame(self):
        self.sender_frame = SenderFrame.SenderFrame()
        self.sender_frame.send_button.configure(command=lambda: [
            self.send_mail()
        ])
        self.sender_frame.change_state_button.configure(command=lambda: [
            self.sender_frame.root.destroy(),self.to_receiver_frame()
        ])

    def to_receiver_frame(self):
        self.receiver_frame = ReceiverFrame.ReceiverFrame()
        self.receiver_frame.send_button.configure(command=lambda: [
            self.receive_mail()
        ])
        self.receiver_frame.change_state_button.configure(command=lambda: [
            self.receiver_frame.root.destroy(),self.to_sender_frame()
        ])
