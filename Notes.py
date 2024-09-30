import time
from datetime import datetime  #Imports libraries, datetime to track each notes creation time, and time to add a little more realism to my programme

AllNotes = {}

def view_note():
    print("Viewing all notes...")
    time.sleep(1)
    if AllNotes: 
        for title, note_data in AllNotes.items():
            print(f"Title: {title}\nDate: {note_data['date']}\nContent: {note_data['content']}\n")
    else:
        print("No notes available.") #Prints notes if there are notes available

def write_note():
    print("Writing a new note...")
    time.sleep(1)
    Title = input('Title: ')
    
    if Title in AllNotes:
        print(f"A note with the title '{Title}' already exists.")
    else:
        Date = datetime.now().strftime('%d/%m/%Y') 
        Content = input('Content of Note: ')
        AllNotes[Title] = {
            'date': Date,
            'content': Content
        }
        print(f"Note titled '{Title}' saved successfully!") #Input title, adds date to note then input content and prints a confirmation sentence for you once its worked

def edit_note():
    print("Editing an existing note...")
    time.sleep(1)
    Title = input('Enter the title of the note you want to edit: ')
    
    if Title in AllNotes:
        print(f"Current content of '{Title}': {AllNotes[Title]['content']}")
        new_content = input('Enter the new content: ')
        AllNotes[Title]['content'] = new_content
        print(f"Note titled '{Title}' has been updated successfully!")
    else:
        print(f"No note found with the title '{Title}'.") # Enter title of note you want edited, then input new content and it gets saved. 

def main():
    while True:
        print('Notes App: ')
        print('V for viewing | W to write a new note | E to edit a pre-existing note | X to exit program')
        UI = input('What would you like to do? -->  ').upper()

        if UI == 'V':
            view_note()
        elif UI == 'W':
            write_note()
        elif UI == 'E':
            edit_note()
        elif UI == 'X':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Character not recognised, Please try again.") # Creates a system which allows programme to always start from here and accesses each function straight from here


main()
