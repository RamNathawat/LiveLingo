from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate():
    try:
        # Create a Translator object
        translator = Translator()

        # Get the input text from the Text widget
        input_text = Input_text.get("1.0", END).strip()

        if input_text:  # Check if input_text is not empty
            # Translate the input text to the selected destination language
            translation = translator.translate(input_text, dest=dest_lang.get())

            # Clear the output text and insert the translation
            Output_text.delete(1.0, END)
            Output_text.insert(END, translation.text)
        else:
            update_status_bar("Please enter text to translate.")
    except Exception as e:
        print(f"Translation error: {e}")

# Create the main window
root = Tk()
root.geometry('1100x400')  
root.resizable(0, 0)  
root['bg'] = '#14213D'  
root.title('LiveLingo - Simple Language Translator')

# Create a label for the title
title_label = Label(root, text="Language Translator", font="Manrope 20 bold", bg='#14213D')
title_label.pack(pady=(20, 0))

# Create a label for the input text
Label(root, text="Enter Text", font='Manrope 13 bold', bg='#14213D').pack()

# Create a text widget for multiline user input
Input_text = Text(root, height=5, width=60, wrap=WORD)
Input_text.pack(pady=10)

# Create a button for triggering translation
trans_btn = Button(root, text='Translate', font='Manrope 12 bold', pady=5, command=translate, bg='#14213D', activebackground='green')
trans_btn.pack(pady=10)

# Create a label for the output
Label(root, text="Output", font='Manrope 13 bold', bg='#14213D').pack()

# Create a text widget for displaying the translation
Output_text = Text(root, font='Manrope 10', height=5, wrap=WORD, padx=5, pady=5, width=60)
Output_text.pack(pady=10)

# Get the list of supported languages
language = list(LANGUAGES.values())

# Create a Combobox for selecting the destination language
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.pack(pady=10)
dest_lang.set('Choose Language')  

# Add a status bar
status_bar = Label(root, text="Ready", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

# Function to update status bar
def update_status_bar(message):
    status_bar.config(text=message)

# Start the Tkinter event loop
root.mainloop()
