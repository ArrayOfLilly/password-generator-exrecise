import tkinter

# Window background constant
BACKGROUND = '#FEF0F0'

# Label font type
FONT_NAME = 'Futura Std'

# Label and Entry font color
LABEL_FONT_COLOR = '#100809'

# Inline Warning message color
WARNING_COLOR = '#D2546F'


class PwLabel(tkinter.Label):
    def __init__(self, text, font_size, pady):
        super().__init__()
        self.configure(text=text)
        self.configure(bg=BACKGROUND)
        self.configure(fg=LABEL_FONT_COLOR)
        self.configure(font=(FONT_NAME, font_size, ""))
        self.configure(pady=pady)

