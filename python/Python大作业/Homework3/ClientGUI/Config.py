import yaml


class LoginFrameConfig:
    def __init__(self, root_height, root_width, label_width, username_x, username_y, password_x, password_y,
                 username_label_x, username_label_y, password_label_x, password_label_y, login_button_x, login_button_y,
                 ):
        self.root_height = root_height
        self.root_width = root_width
        self.label_width = label_width
        self.username_x = username_x
        self.username_y = username_y
        self.password_x = password_x
        self.password_y = password_y
        self.username_label_x = username_label_x
        self.username_label_y = username_label_y
        self.password_label_x = password_label_x
        self.password_label_y = password_label_y
        self.login_button_x = login_button_x
        self.login_button_y = login_button_y

    @classmethod
    def convert_dict_to_object(cls, dict_data):
        return cls(
            dict_data['root_height'],
            dict_data['root_width'],
            dict_data['label_width'],
            dict_data['username_x'],
            dict_data['username_y'],
            dict_data['password_x'],
            dict_data['password_y'],
            dict_data['username_label_x'],
            dict_data['username_label_y'],
            dict_data['password_label_x'],
            dict_data['password_label_y'],
            dict_data['login_button_x'],
            dict_data['login_button_y'],
        )


class SenderFrameConfig:
    def __init__(self, root_height, root_width, label_width,
                 state_label_x, state_label_y,
                 change_state_button_x, change_state_button_y,
                 sender_label_x, sender_label_y,
                 sender_x, sender_y, sender_height, sender_width,
                 receiver_label_x, receiver_label_y,
                 receiver_x, receiver_y, receiver_height, receiver_width,
                 subject_label_x, subject_label_y,
                 subject_x, subject_y, subject_height, subject_width,
                 text_label_x, text_label_y,
                 text_x, text_y, text_height, text_width,
                 send_button_x, send_button_y
                 ):
        self.root_height = root_height
        self.root_width = root_width
        self.label_width = label_width
        self.state_label_x = state_label_x
        self.state_label_y = state_label_y
        self.change_state_button_x = change_state_button_x
        self.change_state_button_y = change_state_button_y
        self.sender_label_x = sender_label_x
        self.sender_label_y = sender_label_y
        self.sender_x = sender_x
        self.sender_y = sender_y
        self.sender_height = sender_height
        self.sender_width = sender_width
        self.receiver_label_x = receiver_label_x
        self.receiver_label_y = receiver_label_y
        self.receiver_x = receiver_x
        self.receiver_y = receiver_y
        self.receiver_height = receiver_height
        self.receiver_width = receiver_width
        self.subject_label_x = subject_label_x
        self.subject_label_y = subject_label_y
        self.subject_x = subject_x
        self.subject_y = subject_y
        self.subject_height = subject_height
        self.subject_width = subject_width
        self.text_label_x = text_label_x
        self.text_label_y = text_label_y
        self.text_x = text_x
        self.text_y = text_y
        self.text_height = text_height
        self.text_width = text_width
        self.send_button_x = send_button_x
        self.send_button_y = send_button_y

    @classmethod
    def convert_dict_to_object(cls, dict_data):
        return cls(
            dict_data['root_height'], dict_data['root_width'], dict_data['label_width'],
            dict_data['state_label_x'], dict_data['state_label_y'],
            dict_data['change_state_button_x'], dict_data['change_state_button_y'],
            dict_data['sender_label_x'], dict_data['sender_label_y'],
            dict_data['sender_x'], dict_data['sender_y'], dict_data['sender_height'], dict_data['sender_width'],
            dict_data['receiver_label_x'], dict_data['receiver_label_y'],
            dict_data['receiver_x'], dict_data['receiver_y'], dict_data['receiver_height'], dict_data['receiver_width'],
            dict_data['subject_label_x'], dict_data['subject_label_y'],
            dict_data['subject_x'], dict_data['subject_y'], dict_data['subject_height'], dict_data['subject_width'],
            dict_data['text_label_x'], dict_data['text_label_y'],
            dict_data['text_x'], dict_data['text_y'], dict_data['text_height'], dict_data['text_width'],
            dict_data['send_button_x'], dict_data['send_button_y'],
        )


class ReceiverFrameConfig:
    def __init__(self, root_height, root_width, label_width,
                 state_label_x, state_label_y,
                 change_state_button_x, change_state_button_y,
                 mail_num_label_x,mail_num_label_y,
                 sender_label_x, sender_label_y,
                 sender_x, sender_y, sender_height, sender_width,
                 receiver_label_x, receiver_label_y,
                 receiver_x, receiver_y, receiver_height, receiver_width,
                 subject_label_x, subject_label_y,
                 subject_x, subject_y, subject_height, subject_width,
                 text_label_x, text_label_y,
                 text_x, text_y, text_height, text_width,
                 mail_choose_label_x, mail_choose_label_y,
                 mail_choose_x, mail_choose_y, mail_choose_height, mail_choose_width,
                 send_button_x, send_button_y
                 ):
        self.root_height = root_height
        self.root_width = root_width
        self.label_width = label_width
        self.state_label_x = state_label_x
        self.state_label_y = state_label_y
        self.change_state_button_x = change_state_button_x
        self.change_state_button_y = change_state_button_y
        self.mail_num_label_x = mail_num_label_x
        self.mail_num_label_y = mail_num_label_y
        self.sender_label_x = sender_label_x
        self.sender_label_y = sender_label_y
        self.sender_x = sender_x
        self.sender_y = sender_y
        self.sender_height = sender_height
        self.sender_width = sender_width
        self.receiver_label_x = receiver_label_x
        self.receiver_label_y = receiver_label_y
        self.receiver_x = receiver_x
        self.receiver_y = receiver_y
        self.receiver_height = receiver_height
        self.receiver_width = receiver_width
        self.subject_label_x = subject_label_x
        self.subject_label_y = subject_label_y
        self.subject_x = subject_x
        self.subject_y = subject_y
        self.subject_height = subject_height
        self.subject_width = subject_width
        self.text_label_x = text_label_x
        self.text_label_y = text_label_y
        self.text_x = text_x
        self.text_y = text_y
        self.text_height = text_height
        self.text_width = text_width
        self.mail_choose_label_x = mail_choose_label_x
        self.mail_choose_label_y = mail_choose_label_y
        self.mail_choose_x = mail_choose_x
        self.mail_choose_y = mail_choose_y
        self.mail_choose_height = mail_choose_height
        self.mail_choose_width = mail_choose_width
        self.send_button_x = send_button_x
        self.send_button_y = send_button_y

    @classmethod
    def convert_dict_to_object(cls, dict_data):
        return cls(
            dict_data['root_height'], dict_data['root_width'], dict_data['label_width'],
            dict_data['state_label_x'], dict_data['state_label_y'],
            dict_data['change_state_button_x'], dict_data['change_state_button_y'],
            dict_data['mail_num_label_x'], dict_data['mail_num_label_y'],
            dict_data['sender_label_x'], dict_data['sender_label_y'],
            dict_data['sender_x'], dict_data['sender_y'], dict_data['sender_height'], dict_data['sender_width'],
            dict_data['receiver_label_x'], dict_data['receiver_label_y'],
            dict_data['receiver_x'], dict_data['receiver_y'], dict_data['receiver_height'], dict_data['receiver_width'],
            dict_data['subject_label_x'], dict_data['subject_label_y'],
            dict_data['subject_x'], dict_data['subject_y'], dict_data['subject_height'], dict_data['subject_width'],
            dict_data['text_label_x'], dict_data['text_label_y'],
            dict_data['text_x'], dict_data['text_y'], dict_data['text_height'], dict_data['text_width'],
            dict_data['mail_choose_label_x'], dict_data['mail_choose_label_y'],
            dict_data['mail_choose_x'], dict_data['mail_choose_y'], dict_data['mail_choose_height'], dict_data['mail_choose_width'],
            dict_data['send_button_x'], dict_data['send_button_y'],
        )


class Config:
    def __init__(self):
        yaml_path = r'./config.yaml'
        with open(yaml_path, mode='rb') as f:
            infos = yaml.load(f, Loader=yaml.FullLoader)
        self.loginFrameConfig = LoginFrameConfig.convert_dict_to_object(infos['loginFrameConfig'])
        self.SenderFrameConfig = SenderFrameConfig.convert_dict_to_object(infos['senderFrameConfig'])
        self.ReceiverFrameConfig = ReceiverFrameConfig.convert_dict_to_object(infos['receiverFrameConfig'])
