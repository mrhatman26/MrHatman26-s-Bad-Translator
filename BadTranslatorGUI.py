from googletrans import Translator
import random
from random import randrange
import tkinter as t
from tkinter.ttk import *
from tkinter import messagebox
import threading
import pyperclip as p
prog_ver = "1.1.0"
def translations():
    translate_misc_copy_button['state'] = t.DISABLED
    translate_input_submit['state'] = t.DISABLED
    translate_input_textbox.configure(state="disabled")
    translate_output_log_textbox.configure(state="normal")
    translate_output_out_textbox.configure(state="normal")
    translate_output_log_textbox.delete("1.0", "end")
    translate_output_out_textbox.delete("1.0", "end")
    translate_output_log_textbox.configure(state="disabled")
    translate_output_out_textbox.configure(state="disabled")
    print("\nUpdate: User clicked translate button.\nUpdate: Getting trans_amnt from translate_input_amnt_entry...", end="")
    failure = True
    try:
        trans_amnt = int(translate_input_amnt_entry.get())
        print("Done!\nUpdate: trans_amnt ==", trans_amnt)
        failure = False
    except:
        print("Failed!\nError: User either did enter an integer or the program failed to parse the input.\nUpdate: Alerting user to error...", end="")
        t.messagebox.showerror("Error!", "Error: The translation amount must be a number!")
        print("Done!")
    if failure is False and trans_amnt > 1:
        failure = True
        print("\nUpdate: Getting original_text from translate_input_textbox...", end="")
        try:
            original_text = translate_input_textbox.get("1.0", "end")
            print("Done!\nUpdate: original_text ==", original_text)
            failure = False
        except:
            print("Failed!\nError: Unable to parse entered text. User may not have entered any.\nUpdate: Alerting user to error...", end="")
            t.messagebox.showerror("Error!", "Error: Unable to read entered text. Text box may be empty.")
            print("Done!")
        if failure is False:
            print("Update: Begining bad translation...")
            translator = Translator()
            trans_amnt -= 1
            languages = ["af", "sq", "am", "ar", "el", "fr", "ru", "pl", "de", "en"]
            lang_length = len(languages)
            translated_text = ""
            current_translation = 0
            x = 0
            rando = 0
            result = ""
            while x <= trans_amnt:
                rando = randrange(0, lang_length)
                current_translation = x + 1
                if x <= 0:
                    result = translator.translate(original_text, dest=languages[rando])
                else:
                    result = translator.translate(translated_text, dest=languages[rando])
                if current_translation == 1:
                    output_temp = "" + str(x + 1) + ": " + result.text
                else:
                    output_temp = "\n\n" + str(x + 1) + ": " + result.text
                print("Translation #", current_translation, ": ", result.text)
                translate_output_log_textbox.configure(state="normal")
                translate_output_log_textbox.insert("end", output_temp)
                translate_output_log_textbox.see("end")
                translate_output_log_textbox.configure(state="disabled")
                translated_text = result.text
                translate_progress_label.configure(text="Translating... (" + str(current_translation) + "/" + str(trans_amnt + 1) + ")")
                x = x + 1
                progress_amnt = x / trans_amnt
                progress_amnt = progress_amnt * 100
                progress_amnt = int(progress_amnt)
                translate_misc_progress['value'] = (progress_amnt)
            translate_output_log_textbox.configure(state="disabled")
            translate_output_out_textbox.configure(state="normal")
            translated_text = translator.translate(translated_text, dest='en')
            translate_output_out_textbox.insert("end", translated_text.text)
            translate_output_out_textbox.configure(state="disabled")
            print("Update: Translation finished!")
            translate_progress_label.configure(text="Done! (" + str(trans_amnt + 1) + "/" + str(trans_amnt + 1) + ")")
    if failure is False and trans_amnt <= 1:
        print("\nWarning!: User entered number less than or equal to one! Alerting user...", end="")
        t.messagebox.showwarning("Warning!", "The number of translations cannot be one or lower!")
        print("Done!")
    print("\n\nWaiting for user input...")
    translate_input_submit['state'] = t.NORMAL
    translate_input_textbox.configure(state="normal")
    translate_input_amnt_entry.configure(state="normal")
    translate_misc_copy_button['state'] = t.NORMAL
def copy_button():
    print("\nUpdate: User clicked copy button.\nUpdate: Getting text from translate_output_out_textbox...", end="")
    try:
        p.copy(translate_output_out_textbox.get("1.0", "end"))
        print("Done!\nUpdate: Translation copied to user's clipboard")
    except:
        print("Failed!\nError: Unable to parse text in translate_output_out_textbox! Textbox may be empty?\nUpdate: Alerting user to error...", end="")
        t.messagebox.showerror("Error!", "Error: Something when wrong while copying from the output textbox.\nThe textbox may be empty?")
        print("Done!")
    print("\n\nWaiting for user input...")
def exit_button():
    print("\nUpdate: User clicked exit button.\nUpdate: Exiting...", end="")
    window.destroy()
thread = threading.Thread(target=translations)
def start_thread():
    thread = None
    thread = threading.Thread(target=translations)
    try:
        thread.start()
    except:
        thread.join()
def about_button():
    print("\nUpdate: User clicked about button.\nUpdate: Showing program information...")
    mesg = "This program was made by MrHatman26 AKA nobody important.\n\nWhat is this?: This is a simple program that takes some text and translates it multiple times making the text (hopefully) a funny nonsensical mess.\n\nThis program was made using Python and uses the following libraries: -googletrans -random -tkinter -threading -pyperclip\n\nCurrent Version: " + prog_ver
    t.messagebox.showinfo("About", mesg)
    print("Done!\n\nWaiting for user input...")
resolution = "700x600"
title = "MrHatman26's Bad Translator " + prog_ver
print("Update: Creating main window...", end="")
window = t.Tk()
print("Done!\nUpdate: Setting window resolution to " + resolution + "...", end="")
window.geometry(resolution)
print("Done!\nUpdate: Setting window title to " + title + "...", end="")
window.title(title)
print("Done!\nUpdate: Setting icon...", end="")
window.iconbitmap("Icon.ico")
print("Done!\nUpdate: Creating GUI elements...", end="")
#Text entry frame
translate_input_frame = t.Frame(window)
translate_input_label = t.Label(translate_input_frame, text="Enter original text here:").pack(side=t.TOP)
translate_input_textbox = t.Text(translate_input_frame, height=10, width=40)
translate_input_textbox.pack()
translate_input_amnt_label = t.Label(translate_input_frame, text="Enter the amount of times you want to translate the text:").pack()
translate_input_amnt_entry = t.Entry(translate_input_frame, width=40, justify='center')
translate_input_amnt_entry.pack()
translate_input_submit = t.Button(translate_input_frame, text="Translate", width=45, command=start_thread)
translate_input_submit.pack(side=t.BOTTOM, pady=6)#To Do: Give the button a function!
translate_input_frame.pack()
#Translation log and output frame
translate_output_frame = t.Frame(window)
translate_output_log_label = t.Label(translate_output_frame, text="Log").grid(column=0, row=0)
translate_output_out_label = t.Label(translate_output_frame, text="Output").grid(column=1, row=0)
translate_output_log_textbox = t.Text(translate_output_frame, height=10, width=40)
translate_output_log_textbox.grid(column=0, row=1, padx=10)
translate_output_out_textbox = t.Text(translate_output_frame, height=10, width=40)
translate_output_out_textbox.grid(column=1, row=1, padx=10)
translate_output_frame.pack()
translate_output_log_textbox.configure(state="disabled")
translate_output_out_textbox.configure(state="disabled")
#Progress frame
translate_progress_frame = t.Frame(window)
translate_progress_label = t.Label(translate_progress_frame, text="Waiting for input...")
translate_progress_label.pack(side=t.TOP, pady=8)
translate_misc_progress = Progressbar(translate_progress_frame, orient='horizontal', length=675, mode='determinate')
translate_misc_progress.pack(side=t.BOTTOM)
translate_progress_frame.pack()
#Misc frame
translate_misc_frame = t.Frame(window)
translate_misc_copy_button = t.Button(translate_misc_frame, text="Copy", width=45, command=copy_button)
translate_misc_copy_button.pack(pady=4, side=t.TOP)
translate_misc_about_button = t.Button(translate_misc_frame, text="About", width=45, command=about_button).pack()
translate_misc_exit_button = t.Button(translate_misc_frame, text="Exit", width=45, command=exit_button).pack(side=t.BOTTOM, pady=4)
translate_misc_frame.pack()
translate_misc_copy_button['state'] = t.DISABLED
log_scrollbar = t.Scrollbar(window, command=translate_output_log_textbox.yview, width=15)
log_scrollbar.place(x=325, y=284, height=164)
translate_output_log_textbox['yscrollcommand'] = log_scrollbar.set
window.resizable(False, False)
print("Done!\n\nWaiting for input...")
window.mainloop()
print("Done!")
