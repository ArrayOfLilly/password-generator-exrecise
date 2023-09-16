import tkinter

PLACEHOLDER_TEXT_COLOR = '#888888'  # Entry placeholder text's color (foreground)
FONT_NAME = 'Futura Std'  # Label font type
LABEL_FONT_COLOR = '#100809'  # Label and Entry font color

URL_ENTRY_PLACEHOLDER_TEXT = "Type the Website URL Here"
USERNAME_ENTRY_PLACEHOLDER_TEXT = "Type your Email/Username Here"
PASSWORD_ENTRY_PLACEHOLDER_TEXT = "Your Password"

MISSING_URL_WARNING_TEXT = "You'll forget the URL!'\n"
MISSING_USERNAME_WARNING_TEXT = "You won't remember your own name!'\n"
MISSING_PASSWORD_WARNING_TEXT = "You didn't even set the password!\n"

MISSING_URL_WARNING_IMAGE_PATH_STR = 'img/missing_url_warning.png'
MISSING_USERNAME_WARNING_IMAGE_PATH_STR = 'img/missing_username_warning.png'
MISSING_PASSWORD_WARNING_IMAGE_PATH_STR = 'img/missing_password_warning.png'


class PwEntry(tkinter.Entry):
    def __init__(self, object_type):
        super().__init__()
        self.object_type = object_type  # url, username or password
        self.original_system_color = self.cget("foreground")
        self.placeholder_color = PLACEHOLDER_TEXT_COLOR
        self.textvariable = tkinter.StringVar()
        self.placeholder_text = tkinter.StringVar()
        self.set_placeholder_text()
        self.copy_placeholder_text_to_textvariable()
        self.state = self.cget("state")
        self.inline_warning_text = ""
        self.missing_content_warning_image_path = ""
        self.set_warning()
        self.configure(width=48)
        self.configure(font=(FONT_NAME, 16, ""))

    def set_placeholder_text(self):
        if self.object_type == "url":
            self.placeholder_text.set(URL_ENTRY_PLACEHOLDER_TEXT)
        if self.object_type == "username":
            self.placeholder_text.set(USERNAME_ENTRY_PLACEHOLDER_TEXT)
        if self.object_type == "password":
            self.placeholder_text.set(PASSWORD_ENTRY_PLACEHOLDER_TEXT)

    def copy_placeholder_text_to_textvariable(self):
        self.textvariable.set(self.placeholder_text.get())
        self.configure(textvariable=self.textvariable)
        self.configure(foreground=self.placeholder_color)
        self.configure(disabledforeground=self.placeholder_color)

    def is_placeholder(self):
        if self.textvariable.get() == str(self.placeholder_text.get()):
            return True
        return False

    def set_warning(self):
        if self.object_type == "url":
            self.inline_warning_text = MISSING_URL_WARNING_TEXT
            self.missing_content_warning_image_path = MISSING_URL_WARNING_IMAGE_PATH_STR
        if self.object_type == "username":
            self.inline_warning_text = MISSING_USERNAME_WARNING_TEXT
            self.missing_content_warning_image_path = MISSING_USERNAME_WARNING_IMAGE_PATH_STR
        if self.object_type == "password":
            self.inline_warning_text = MISSING_PASSWORD_WARNING_TEXT
            self.missing_content_warning_image_path = MISSING_PASSWORD_WARNING_IMAGE_PATH_STR

    def set_to_placeholder_color(self):
        self.configure(foreground=self.placeholder_color)

    def set_textvariable(self, param: tkinter.StringVar):
        '''
        Set the parent's textvariable attribute
        :param param:
        :return:
        '''
        self.textvariable = param
        self.configure(textvariable=self.textvariable)

    def get_original_system_color(self):
        return self.ORIGINAL_SYSTEM_TEXT_COLOR