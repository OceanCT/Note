import smtplib
import poplib
import email
from email.parser import Parser
from email.message import EmailMessage



class Client:
    def __init__(self):
        self.mail_sender_host = 'smtp.163.com'
        self.mail_receiver_host = 'pop.163.com'
        self.mail_num = 0
        self.username = ''
        self.authentication_string = ''
        self.send_server = None
        self.recv_server = None
        self.mail_list = None

    def change_info(self, new_username='', new_authentication_string='', new_mail_sender_host='',
                    new_mail_receiver_host=''):
        if new_username:
            self.username = new_username
        if new_authentication_string:
            self.authentication_string = new_authentication_string
        if new_mail_sender_host:
            self.mail_sender_host = new_mail_sender_host
        if new_mail_receiver_host:
            self.mail_receiver_host = new_mail_receiver_host

    def connect_to_server(self):
        try:
            self.send_server = smtplib.SMTP(host=self.mail_sender_host)
            self.recv_server = poplib.POP3(host=self.mail_receiver_host)
        except Exception as e:
            print(e)
            return e
        try:
            self.send_server.login(self.username, self.authentication_string)
            self.recv_server.user(self.username)
            self.recv_server.pass_(self.authentication_string)
            self.mail_list = self.recv_server.list()
            self.mail_num = len(self.mail_list[1])
        except Exception as e:
            print(e)
            return e

    def send_message(self, msg_str: str, subject: str, mail_receiver: str):
        try:
            msg = email.message_from_string(msg_str)
            msg['Subject'] = subject
            msg['To'] = mail_receiver
            msg['From'] = self.username
            msg.set_charset('utf-8')
            self.send_server.send_message(msg, self.username, mail_receiver)
        except Exception as e:
            print(e)
            return e

    def get_mail(self, num: int):
        lines = self.recv_server.retr(num)[1]
        msg_content = b'\r\n'.join(lines).decode()
        msg = Parser().parsestr(msg_content)
        return msg

    @staticmethod
    def get_mail_subject(msg: EmailMessage):
        return msg['Subject']

    @staticmethod
    def get_mail_From(msg: EmailMessage):
        return msg['From']

    @staticmethod
    def get_mail_content_type(msg: EmailMessage):
        return msg['Content-type']

    @staticmethod
    def get_mail_text(msg: EmailMessage):
        res = []
        if msg.is_multipart():
            parts = msg.get_payload()
            for _, part in enumerate(parts):
                if part.get_content_type() == 'text/plain':
                    res.extend(Client.get_mail_text(part))
        elif msg.get_content_maintype() == 'text':
            res.append(msg.get_payload())
        return res

        # help_info = {}
        # help_info['Subject'] = msg['Subject']
        # print(msg['Subject'])
        # print(msg['To'])
        # print(msg['From'])
        # print(msg['Content-type'])
        # if msg.is_multipart():
        #     parts = msg.get_payload()
        #     for _, part in enumerate(parts):
        #         if part.get_content_type() == 'text/plain':
        #             content1 = part.get_payload(decode=True)
        #             # print(content1)
        #             content1 = content1.decode('utf-8')
        #             print(content1)
        # else:
        #     print(msg.get_payload())


if __name__ == '__main__':
    mail_user = '123213@163.com'
    mail_pass = ''
    receiver = '2io012371230@qq.com'
    title = '2021,hello'
    content = '2021'
    subject1 = 'test.py'
    client = Client()
    client.change_info(mail_user, mail_pass)
    client.connect_to_server()
    mesg = client.get_mail(2)
    print(client.get_mail_From(mesg))
    print(client.get_mail_text(mesg))
