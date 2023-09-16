import tkinter
from tkinter import messagebox, StringVar
import tkmacosx
import time
import pyperclip
import password
from pwentry import PwEntry
from pwlabel import PwLabel

# Window background constant
BACKGROUND = '#FEF0F0'

# Label font type
FONT_NAME = 'Futura Std'

# Label and Entry font color
LABEL_FONT_COLOR = '#100809'

# Inline Warning message color
WARNING_COLOR = '#D2546F'

# UI Colors
DARK_BROWN = '#482B2F'
LIGHT_BROWN = '#B8B5B6'
# We should declare "White" because Tkmacosx doesn't accepts Tkinter color literals
WHITE = '#fff'
PASSWORD_BLUE = '#C4D1F0'

# UI Element's color
SAVE_BTN_NORMAL_STATE_BG = LIGHT_BROWN
SAVE_BTN_NORMAL_STATE_FG = DARK_BROWN
SAVE_BTN_ACTIVE_STATE_BG = LIGHT_BROWN
SAVE_BTN_ACTIVE_STATE_FG = WHITE
SAVE_BTN_DISABLED_STATE_BG = BACKGROUND
SAVE_BTN_DISABLED_STATE_FG = LIGHT_BROWN

ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_BG = LIGHT_BROWN
ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_FG = DARK_BROWN
ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_BG = LIGHT_BROWN
ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_FG = WHITE

# Main image per app state
START_IMAGE_PATH_STR = 'img/start.png'
GENERATING_DATA_IMAGE_PATH_STR = 'img/generating_data.png'
SUCCESS_IMAGE_PATH_STR = 'img/success.png'


# ---------------------------- UI SETUP ------------------------------- #

# ---------------------------- Window ---------------------------- #

root = tkinter.Tk()
root.title("Password Manager")
root.config(padx=75, pady=25, bg=BACKGROUND)

# ---------------------------- CONSTANTS and Global variables that needs the root ---------------------------- #

main_image = tkinter.PhotoImage()


# ---------------------------- UI SETUP continues ------------------------------- #

# ---------------------------- Title Label ---------------------------- #

title_label = PwLabel("The Favorite", 32, 25)
title_label.grid(row=0, column=0, columnspan=4)


# ---------------------------- Canvas/Image ---------------------------- #

canvas = tkinter.Canvas(width=400, height=230, bg=BACKGROUND, highlightthickness=0)
main_img = tkinter.PhotoImage(file=START_IMAGE_PATH_STR)
canvas.create_image(202, 115, image=main_img)
canvas.grid(row=1, column=0, columnspan=4)

# ---------------------------- Website Row + common Entry commands before first Entry ---------------------------- #

url_label = tkinter.Label(text="Website:", bg=BACKGROUND, font=(FONT_NAME, 16, ""), pady=20)

# Sampling for know system theme and color, before set foreground
ORIGINAL_SYSTEM_TEXT_COLOR = url_label.cget("foreground")

url_label.config(fg=LABEL_FONT_COLOR)
url_label.grid(row=2, column=0)


def on_click(event):
    # Delete all warning, we are editing now, don't know the result to validate
    inline_warning_message_placeholder_label["text"] = ""

    # Checks if Entry contains its placeholder text
    # If yes, delete it and set the system foreground color
    if event.widget.is_placeholder():
        event.widget.delete(0, tkinter.END)
        event.widget.config(fg=ORIGINAL_SYSTEM_TEXT_COLOR)


# ---------------------------- URL Entry ---------------------------- #

url_entry = PwEntry("url")

# binding on_click() command by button behavior for check is it's default text
url_entry.bind("<Button-1>", on_click)
url_entry.grid(row=2, column=1, columnspan=3)

url_entry.focus()

# TODO Changing foreground color when an element get focus

# ---------------------------- Username Row ---------------------------- #

# ---------------------------- Username Label ---------------------------- #

username_label = PwLabel("Email/Username:",16, 20)
username_label.grid(column=0, row=3)

# ---------------------------- Username Entry ---------------------------- #

username_entry = PwEntry("username")

# binding on_click() command by button behavior for check is it's default text
username_entry.bind("<Button-1>", on_click)

username_entry.grid(row=3, column=1, columnspan=3)


# ---------------------------- Password Row ---------------------------- #

# ---------------------------- Password Label ---------------------------- #

password_label = PwLabel("Password:", 16, 20)
password_label.grid(row=4, column=0)

# ---------------------------- Password Entry ---------------------------- #

password_entry = PwEntry("password")

# binding on_click() command by button behavior for check is it's default text
password_entry.bind("<Button-1>", on_click)

password_entry.grid(row=4, column=1, columnspan=3)

# Generating password preferred:
password_entry.configure(state="disabled")

# All Entry for batch managing, after that creation finished
ENTRY_WIDGETS = [url_entry, username_entry, password_entry]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- Choose Own Password ---------------------------- #


def change_main_image(file_path: str):
    global main_img
    main_img = tkinter.PhotoImage(file=file_path)
    canvas.create_image(202, 115, image=main_img)


def choose_my_own_password():
    # set the password generating phase's blue lock image as main image
    change_main_image(GENERATING_DATA_IMAGE_PATH_STR)

    # Enable manual editing on password Entry
    password_entry.config(state="normal")
    password_entry.copy_placeholder_text_to_textvariable()
    password_entry.config(fg=ORIGINAL_SYSTEM_TEXT_COLOR)

    password_entry.focus()
    password_entry.delete(0, tkinter.END)


    # Enables saving without generating password and WARNING about the lack of validation
    # TODO Basic Validation:
    #    Duplicated password (easy)
    #    Most commonly used passwords (easy)
    #       (Get the list first)
    #   Pattern (length, patterns, personal data, etc)

    save_button.configure(state="normal", fg=SAVE_BTN_NORMAL_STATE_FG, bg=SAVE_BTN_NORMAL_STATE_BG)
    inline_warning_message_placeholder_label[
        "text"] += "Be aware that you're an adult, \nthere's no validation! (yet)'\n"


# ---------------------------- Random Password Generation ---------------------------- #


def generate_random_password():
    change_main_image(GENERATING_DATA_IMAGE_PATH_STR)

    # Disables manual password editing and delete the manual editing related warning
    # with all other warning because we continues the editing

    password_entry.configure(state="disabled")
    password_entry.configure(disabledforeground=PASSWORD_BLUE)
    inline_warning_message_placeholder_label["text"] = ""

    # Enables saving
    save_button.configure(state="normal", fg=SAVE_BTN_NORMAL_STATE_FG, bg=SAVE_BTN_NORMAL_STATE_BG)

    # Password generation (by @Alex V's Generator)
    random_password = tkinter.StringVar()
    random_password.set(password.random_pass())
    password_entry.set_textvariable(random_password)


# ---------------------------- Memorable Password Generation ---------------------------- #

# Uses word list stored in pass_word.txt
# words are from 10 000 most frequently used English words, 4 < length < 8
# all 10 000 words stored in dictionary.txt
# changing the selected length you can use filter.py

# Memorable password structure: Word_1-Word_2-Word_3-53,
# Where 53 is just for validation, not for increase entropy
# 53 is constant for better memorability

def generate_memorable_password():
    change_main_image(GENERATING_DATA_IMAGE_PATH_STR)

    # Disables manual password editing and delete the manual editing related warning
    # with all other warning because we continue the editing

    password_entry.configure(state="disabled")
    password_entry.configure(disabledforeground=PASSWORD_BLUE)
    inline_warning_message_placeholder_label["text"] = ""

    # Enables saving
    save_button.configure(state="normal", fg=SAVE_BTN_NORMAL_STATE_FG, bg=SAVE_BTN_NORMAL_STATE_BG)

    memorable_password = tkinter.StringVar()
    memorable_password.set(password.memorable())
    password_entry.set_textvariable(memorable_password)


# ---------------------------- Password Generating Row ---------------------------- #

# ---------------------------- Choose My Own Password Button ---------------------------- #

own_password_button = tkmacosx.Button(root, text="Choose \nmy Own",
                                      command=choose_my_own_password, width=140,
                                      bg=ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_BG,
                                      fg=ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_FG,
                                      activebackground=ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_BG,
                                      activeforeground=ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_FG,
                                      borderless=1, focuscolor='', font=(FONT_NAME, 16, ""), justify="left", padx=15,
                                      pady=4)

own_password_button.grid(row=5, column=1)

# ---------------------------- Random Password Button ---------------------------- #

random_button = tkmacosx.Button(root, text="Generate \nRandom", command=generate_random_password,
                                width=140, bg=ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_BG,
                                fg=ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_FG,
                                activebackground=ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_BG,
                                activeforeground=ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_FG,
                                borderless=1, focuscolor='', font=(FONT_NAME, 16, ""), justify="left", padx=10, pady=4)
random_button.grid(row=5, column=2)

# ---------------------------- Memorable Password Button ---------------------------- #

memorable_button = tkmacosx.Button(root, text="Generate \nMemorable", command=generate_memorable_password,
                                   width=140, bg=ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_BG,
                                   fg=ALL_PASSWORD_GENERATING_BTN_NORMAL_STATE_FG,
                                   activebackground=ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_BG,
                                   activeforeground=ALL_PASSWORD_GENERATING_BTN_ACTIVE_STATE_FG,
                                   borderless=1, focuscolor='', font=(FONT_NAME, 16, ""), justify="left", padx=10,
                                   pady=4)
memorable_button.grid(row=5, column=3)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- Checking conditions for saving ---------------------------- #


def is_copy_checkbox_used():
    global is_copy_checkbox_checked
    is_copy_checkbox_checked = is_copy_checkbox_checked_state.get()


def if_exit_checkbox_used():
    global is_exit_checkbox_checked
    is_exit_checkbox_checked = is_exit_checkbox_checked_state.get()


# ---------------------------- Copy to Clipboard Checkbox ---------------------------- #

is_copy_checkbox_checked = 0  # set default state
is_copy_checkbox_checked_state = tkinter.IntVar()
is_copy = tkinter.Checkbutton(text="Copy to the Clipboard", variable=is_copy_checkbox_checked_state,
                              command=is_copy_checkbox_used, bg=BACKGROUND, fg=LABEL_FONT_COLOR,
                              font=(FONT_NAME, 16, ""), pady=20)
is_copy_checkbox_checked_state.get()
is_copy.grid(row=6, column=2)

# ---------------------------- Exit on Save Checkbox ---------------------------- #

is_exit_checkbox_checked = 0
is_exit_checkbox_checked_state = tkinter.IntVar()
is_exit = tkinter.Checkbutton(text="Exit on Save", variable=is_exit_checkbox_checked_state,
                              command=if_exit_checkbox_used, bg=BACKGROUND, fg=LABEL_FONT_COLOR,
                              font=(FONT_NAME, 16, ""), pady=20)
is_exit_checkbox_checked_state.get()
is_exit.grid(row=6, column=3)


# ---------------------------- Save ---------------------------- #


def save():
    # checking if ready to save
    # TODO make PwEntry class to hold attributes like it's own placeholder text
    # TODO PwLabels class with default attribute values also simplified a lot...
    # TODO after creating classes rewrite this (save) function for readability

    for entry_widget in ENTRY_WIDGETS:

        # First check: widget's content is placeholder text or it's empty
        if entry_widget.is_placeholder() or entry_widget.get() == "":

            # if it's empty set to placeholder for better understanding/visibility then back to editing
            if entry_widget.get() == "":
                entry_widget.copy_placeholder_text_to_textvariable()
                entry_widget.set_to_placeholder_color()

            inline_warning_message_placeholder_label["text"] += entry_widget.inline_warning_text
            change_main_image(entry_widget.missing_content_warning_image_path)
            return

    if is_copy_checkbox_checked == 1:
        pyperclip.copy(password_entry.get())

    # Confirmation (Messagebox)
    messagebox.showwarning(title="", message="Sure?",
                           icon="question")

    # TODO Proper JSON format
    # Effective saving
    new_entry = ('{\n"URL": ' + url_entry.get() + ',\n"username": ' + username_entry.get() + ',\n"password": ' +
                 password_entry.get() + '\n},\n')

    with open("save/save.txt", 'a') as save_file:
        save_file.write(new_entry)

    # Success Status
    inline_warning_message_placeholder_label["text"] = ""
    change_main_image(SUCCESS_IMAGE_PATH_STR)

    # TODO would be better operating asynchronous,
    #  it's just finish for showing again the start screen, doesn't worth 2 sec
    time.sleep(1.5)

    # Reset UI/app
    save_button.configure(state="disabled", fg=SAVE_BTN_DISABLED_STATE_FG, bg=SAVE_BTN_DISABLED_STATE_BG)
    for entry_widget in ENTRY_WIDGETS:
        entry_widget.copy_placeholder_text_to_textvariable()

    change_main_image(START_IMAGE_PATH_STR)

    # Exit
    if is_exit_checkbox_checked == 1:
        root.destroy()


# ---------------------------- Save Button -------------------------------- #

save_button = tkmacosx.Button(root, text="Save", command=save, width=365, bg=SAVE_BTN_DISABLED_STATE_BG,
                              fg=SAVE_BTN_NORMAL_STATE_FG, activebackground=SAVE_BTN_ACTIVE_STATE_BG,
                              activeforeground=SAVE_BTN_ACTIVE_STATE_FG, disabledbackground=SAVE_BTN_DISABLED_STATE_BG,
                              disabledforeground=SAVE_BTN_DISABLED_STATE_FG, font=(FONT_NAME, 16, ""), borderless=1,
                              focuscolor='', state="disabled", padx=50, pady=4)
save_button.grid(row=7, column=2, columnspan=2, )

# ---------------------------- Placeholder label for validation ---------------------------- #

inline_warning_message_placeholder_label = PwLabel("", 20, 10)
inline_warning_message_placeholder_label.configure(fg=WARNING_COLOR, justify="left")
inline_warning_message_placeholder_label.grid(row=8, column=2, columnspan=2)


root.mainloop()