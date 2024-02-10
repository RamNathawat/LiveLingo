from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from langdetect import detect

def translate_text():
    try:
        input_text = input_text_widget.get("1.0", END).strip()
        if input_text:
            input_lang = detect(input_text)
            translation = translator.translate(input_text, src=input_lang, dest=dest_lang_combobox.get())
            output_text_widget.delete(1.0, END)
            output_text_widget.insert(END, translation.text)
            detected_lang_label.config(text=f"Detected Language: {LANGUAGES.get(input_lang, 'Unknown')}")
        else:
            update_status_bar("Please enter text to translate.")
    except Exception as e:
        print(f"Translation error: {e}")

def update_status_bar(message):
    status_bar.config(text=message)

root = Tk()
root.geometry('1100x500')
root.resizable(0, 0)
root['bg'] = '#14213D'
root.title('LiveLingo - Simple Language Translator')

title_label = Label(root, text="Language Translator", font="Manrope 20 bold", bg='#14213D')
title_label.pack(pady=(20, 0))

Label(root, text="Enter Text", font='Manrope 13 bold', bg='#14213D').pack()
input_text_widget = Text(root, height=5, width=60, wrap=WORD)
input_text_widget.pack(pady=10)

trans_btn = Button(root, text='Translate', font='Manrope 12 bold', pady=5, command=translate_text, bg='#14213D', activebackground='green')
trans_btn.pack(pady=10)

Label(root, text="Output", font='Manrope 13 bold', bg='#14213D').pack()
output_text_widget = Text(root, font='Manrope 10', height=5, wrap=WORD, padx=5, pady=5, width=60)
output_text_widget.pack(pady=1)

detected_lang_label = Label(root, text="Detected Language: ", font='Manrope 10', bg='#14213D')
detected_lang_label.pack(pady=5)

language_names = list(LANGUAGES.values())
dest_lang_combobox = ttk.Combobox(root, values=language_names, width=22)
dest_lang_combobox.pack(pady=10)
dest_lang_combobox.set('Choose Language')

status_bar = Label(root, text="Ready", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

translator = Translator()
root.mainloop()
