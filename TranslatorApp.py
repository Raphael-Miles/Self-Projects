import tkinter as tk

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = servers as a container to hold or contain these widgets

# Start menu
window = tk.Tk() # Instantiates window but doesnt display it
window.geometry("400x400")
window.title("コンビニ")

window.config(background='white')

label = tk.Label(text="Learning App")
label.pack(side=tk.TOP)

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def trans_click():
    print('Loading translator')
    clear_window()
    b4 = tk.Label(window, text='translating')
    b4.pack()

def flash_click():
    print('Loading flashcards')

def new_window():
    New_window = tk.Tk()
    New_window.mainloop()

def app_widgets():

    
    b1 = tk.Button(window, text='Translate', command=trans_click)
    b1.pack(side=tk.LEFT)
    b1.config(height= 5, width= 10)
    
    b2 = tk.Button(window, text='Flashcards', command=flash_click)   
    b2.pack(side=tk.LEFT)    
    b2.config(height= 5, width= 10)

    b3 = tk.Button(window, text='Settings', command=new_window)   
    b3.pack(side=tk.LEFT)    
    b3.config(height= 5, width= 10)


app_widgets()


window.mainloop() # Place window on computer screen, listen for events
