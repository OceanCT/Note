import zmail


class ClientServer:
    def __init__(self):
        self.username = ''
        self.authentication_string = ''
        self.server = None

    def change_info(self, new_username='', new_authentication_string=''):
        if new_username:
            self.username = new_username
        if new_authentication_string:
            self.authentication_string = new_authentication_string

    def connect_to_server(self):
        try:
            self.server = zmail.server(self.username, self.authentication_string)
            if not self.server.smtp_able() or not self.server.pop_able():
                print("Error happened when connecting to server")
                return "Connection Failed"
        except Exception as e:
            print("Error happened when connecting to server")
            print(e)
            return e

    def send_message(self, mail: dict, mail_receiver: list):
        try:
            self.server.send_mail(mail_receiver, mail)
        except Exception as e:
            print("Error happened when sending message")
            print(e)

    def get_mail(self, num: int):
        try:
            msg = self.server.get_mail(num)
            msg['Content_text'] = ''.join(msg['Content_text'])
            return msg
        except Exception as e:
            print("Error happened when getting email")
            print(e)
            return None

    def get_mail_num(self):
        print(self.server.stat()[0])
        return self.server.stat()[0]
