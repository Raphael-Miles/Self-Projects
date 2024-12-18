import tkinter as tk
from googletrans import Translator
from time import *  # Not currently used, but included

# widgets = GUI elements: buttons, textboxes, labels, images, text, entry

'''Organisation is necessary, functions that link to other functions go everywhere, also google translate seems to be pretty poorly optimised
Aesthetic choices need to be re-evalued lol

May have to change everything from pack to grid or a better alternative down the line cause of stylistic conflicts
'''

# Start menu
window = tk.Tk()  # Instantiates window but doesn't display it
translator = Translator()  # Init translator
window.geometry("400x400")
window.title("コンビニ")  # Might stick with this name

window.config(background='gray')

'''Keeping this section for simple reusable functions'''


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()  # Uses return button to clear window of current widgets and place new widgets or start screen, otherwise overlap issue


def return_home():  # Return button, goes to main screen
    clear_window()
    app_widgets()


def tester():
    print('Working')  # My best testing tool lol


new_dict = []  # Dictionary for holding saved translations

'''END OF SIMPLE FUNCS'''


def trans_click():
    print('Loading translator')
    clear_window()

    # Label for instructions
    l1 = tk.Button(window, text='En to Jp', command=lambda: set_src_lang("en")) # SHOULDNT HAVE TO CHOOSE LANGUAGE EVERYTIME, HAVE IT SAVED AUTOMATICALLY AS JP TO EN
    l1.pack(pady=10, side=tk.TOP)
    l2 = tk.Button(window, text='Jp to En', command=lambda: set_src_lang("ja"))
    l2.pack(pady=10, side=tk.TOP)

    # Text widget for user input
    b6 = tk.Text(window, height=5, width=30)
    b6.pack(pady=10)

    # Button to submit the text
    b7 = tk.Button(window, text='Submit', activebackground='red',
                   command=lambda: trans_text(b6.get("1.0", tk.END).strip()))
    b7.pack(pady=10)

    return_b = tk.Button(window, text='Return', command=return_home)
    return_b.pack(side=tk.BOTTOM)


def set_src_lang(lang):
    global src_lang
    src_lang = lang
    print(f"Source language set to: {src_lang}")
    # lan_label = tk.Label(window, text=f'Translating from {src_lang}') # Need to Add an indicator to show which one theyve clicked
    # lan_label.pack(pady=10)


def trans_text(user_text):  # Function takes user text inside text bubble and prints it to show original and translated
    global saved_text
    global src_lang

    if not user_text:
        # Handle empty input
        result_label = tk.Label(window, text="Please enter some text to translate.")
        result_label.pack(pady=10)
        return

    # Translate text
    dest_lang = "en" if src_lang == "ja" else "ja"  # Set destination language based on source language
    translated = translator.translate(user_text, src=src_lang, dest=dest_lang)
    b4 = tk.Label(window, text=f"Original: {user_text}")
    b5 = tk.Label(window, text=f"Translated: {translated.text}")
    b4.pack(pady=5)
    b5.pack(pady=5)

    saved_text = user_text + " | " + translated.text

    save_b = tk.Button(window, text='Save', activebackground='blue',
                       command=lambda: saving_text(saved_text))  # Pass saved_text as argument
    save_b.pack(padx=10)
    print(new_dict)

    discard_b = tk.Button(window, text='Discard', command=discard_text)
    discard_b.pack(pady=10)


def discard_text():
    trans_click()  # Go back to the translate screen


def saving_text(text):
    global new_dict
    new_dict.append(text)
    print(new_dict)
    discard_text()


def flash_click():  # Flashcard button clicked and gives some options
    clear_window()
    return_b = tk.Button(window, text='Return', command=return_home)
    return_b.pack(side=tk.BOTTOM)
    F_LABEL = tk.Label(window, text='Folders')
    F_LABEL.pack(padx=10)
    add_b = tk.Button(window, text='Add folder', command=add_folder)
    add_b.pack(side=tk.LEFT)
    add_b2 = tk.Button(window, text='Manage folders')
    add_b2.pack(side=tk.LEFT)
    add_b3 = tk.Button(window, text='Delete folder')
    add_b3.pack(side=tk.LEFT)
    add_b4 = tk.Button(window, text='Recently Saved', command=recent_folder)
    add_b4.pack(side=tk.LEFT)


def add_folder():  # Currently just adds a label with saved text, will need to actually make folders, allow you to customise name
    clear_window()
    return_b = tk.Button(window, text='Return', command=return_home)
    return_b.pack(side=tk.BOTTOM)
    F_LABEL = tk.Label(window, text='Folders')
    F_LABEL.pack(padx=10)
    add_b3 = tk.Button(window, text='Delete folder')
    add_b3.pack(side=tk.BOTTOM)

def recent_folder():
    clear_window()
    return_b = tk.Button(window, text='Return', command=return_home)
    return_b.pack(side=tk.BOTTOM)
    
    global saved_text
    new_label = tk.Label(window, text=new_dict)
    new_label.pack(side=tk.LEFT)



def new_window():
    New_window = tk.Tk()
    New_window.mainloop()  # just testing some widgets, opens a brand new window


def app_widgets():  # Also the main start screen

    label_og = tk.Label(text="Learning App")
    label_og.pack(side=tk.TOP)

    b1 = tk.Button(window, text='Translate', command=trans_click)
    b1.pack(side=tk.LEFT)
    b1.config(height=5, width=10)

    b2 = tk.Button(window, text='Flashcards', command=flash_click)
    b2.pack(side=tk.LEFT)
    b2.config(height=5, width=10)

    b3 = tk.Button(window, text='Settings', command=new_window)  # Unsure how to make settings really but added it anyway
    b3.pack(side=tk.LEFT)
    b3.config(height=5, width=10)

    bE = tk.Button(window, text='Testing', command=tester)  # Not too sure, just incase i need it??
    bE.pack(side=tk.LEFT)

app_widgets()  # Calls entire start screen

window.mainloop()  # Place window on computer screen, listen for events
