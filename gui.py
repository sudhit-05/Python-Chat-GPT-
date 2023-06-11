from pdb import set_trace as bp
from tkinter import *
import time
import tkinter.messagebox
from bot import chat
import pyttsx3
import threading
window_size = "400x400"
class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
        # Menu bar

        # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        # file.add_command(label="Save Chat Log", command=self.save_chat)
        file.add_command(label="Clear Chat", command=self.clear_chat)
        #  file.add_separator()
        file.add_command(label="Exit", command=self.chatexit)

        # Options
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

        # font
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default", command=self.font_change_default)
        font.add_command(label="Algerian", command=self.font_change_Algerian)
        font.add_command(label="System", command=self.font_change_system)
        font.add_command(label="Helvetica", command=self.font_change_helvetica)
        font.add_command(label="Fixedsys", command=self.font_change_fixedsys)

        # color theme
        color_theme = Menu(options, tearoff=0)
        options.add_cascade(label="Color Theme", menu=color_theme)
        color_theme.add_command(label="Default", command=self.color_theme_default)
        color_theme.add_command(label="Dark", command=self.color_theme_dark)
        color_theme.add_command(label="Grey", command=self.color_theme_grey)
        color_theme.add_command(label="Green", command=self.color_theme_green)
        color_theme.add_command(label="Blue", command=self.color_theme_blue)
        color_theme.add_command(label="Red", command=self.color_theme_red)
        color_theme.add_command(label="Hacker", command=self.color_theme_hacker)
        color_theme.add_command(label="Hacker 2",command=self.color_theme_hacker_2)
        color_theme.add_command(label="Hacker 3",command=self.color_theme_hacker_3)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        # help_option.add_command(label="Features", command=self.features_msg)
        help_option.add_command(label="About", command=self.msg)
        help_option.add_command(label="Developer", command=self.about)

        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)

        self.last_sent_label(date="No messages sent.")
        # t2 = threading.Thread(target=self.send_message_insert(, name='t1')
        # t2.start()

        user_input = self.entry_field.get()
        pr1 = str(input("What's your name? "))
        global user_name
        user_name = pr1

    def playResponce(self, responce):
        x = pyttsx3.init()
        # print(responce)
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')
                # print(b)

        x.setProperty('rate', 120)
        x.setProperty('volume', 75)
        x.say(responce)
        x.runAndWait()
        # print("Played Successfully......")

    def last_sent_label(self, date):
        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("Chat GPT v1.0",
                                    'Chat GPT is a chatbot for answering the meaning of english words and python queries\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter\nIt can answer questions regarding python language and meaning of english words for new learners')

    def about(self):
        tkinter.messagebox.showinfo("Chat GPT Developer", "Sudhit")

    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        global user_name
        pr1 = user_name + ": " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        # t1 = threading.Thread(target=self.playResponce, args=(user_input,))
        # t1.start()
        # time.sleep(1)
        ob = chat(user_input)
        pr = "GPT : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.last_sent_label(str(time.strftime("Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.entry_field.delete(0, END)
        time.sleep(0)
        #self.playResponce(ob)
        t2 = threading.Thread(target=self.playResponce, args=(ob,))
        t2.start()
        # return ob

    def font_change_default(self):
        self.text_box.config(font="Verdana 10")
        self.entry_field.config(font="Verdana 10")
        self.font = "Verdana 10"

    def font_change_Algerian(self):
        self.text_box.config(font="Algerian")
        self.entry_field.config(font="Algerian")
        self.font = "Algerian"

    def font_change_system(self):
        self.text_box.config(font="System")
        self.entry_field.config(font="System")
        self.font = "System"

    def font_change_helvetica(self):
        self.text_box.config(font="helvetica 10")
        self.entry_field.config(font="helvetica 10")
        self.font = "helvetica 10"

    def font_change_fixedsys(self):
        self.text_box.config(font="fixedsys")
        self.entry_field.config(font="fixedsys")
        self.font = "fixedsys"

    def color_theme_default(self):
        self.master.config(bg="#EEEEEE")
        self.text_frame.config(bg="#EEEEEE")
        self.entry_frame.config(bg="#EEEEEE")
        self.text_box.config(bg="#EEEEEE", fg="#000000")
        self.entry_field.config(bg="#EEEEEE", fg="#000000", insertbackground="#000000")
        self.send_button_frame.config(bg="#EEEEEE")
        self.send_button.config(bg="#EEEEEE", fg="#000000", activebackground="#EEEEEE", activeforeground="#000000")
        # self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.sent_label.config(bg="#EEEEEE", fg="#000000")

        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"

    # Dark
    def color_theme_dark(self):
        self.master.config(bg="#232323")
        self.text_frame.config(bg="#232323")
        self.text_box.config(bg="#000000", fg="#FFFFFF")
        self.entry_frame.config(bg="#232323")
        self.entry_field.config(bg="#000000", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#232323")
        self.send_button.config(bg="#000000", fg="#FFFFFF", activebackground="#000000", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#232323", fg="#FFFFFF")

        self.tl_bg = "#000000"
        self.tl_bg2 = "#232323"
        self.tl_fg = "#FFFFFF"

    # Green
    def color_theme_green(self):
        self.master.config(bg="#005C29")
        self.text_frame.config(bg="#005C29")
        self.text_box.config(bg="#013220", fg="#FFFFFF")
        self.entry_frame.config(bg="#005C29")
        self.entry_field.config(bg="#013220", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#005C29")
        self.send_button.config(bg="#013220", fg="#FFFFFF", activebackground="#013220", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#005C29", fg="#FFFFFF")

        self.tl_bg = "#013220"
        self.tl_bg2 = "#005C29"
        self.tl_fg = "#FFFFFF"

    # Grey
    def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.text_frame.config(bg="#444444")
        self.text_box.config(bg="#4f4f4f", fg="#ffffff")
        self.entry_frame.config(bg="#444444")
        self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
        self.send_button_frame.config(bg="#444444")
        self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        # self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.sent_label.config(bg="#444444", fg="#ffffff")

        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"

    # Blue
    def color_theme_blue(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        # self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    # Red
    def color_theme_red(self):
        self.master.config(bg="#BF0000")
        self.text_frame.config(bg="#BF0000")
        self.text_box.config(bg="#800000", fg="#FFFFFF")
        self.entry_frame.config(bg="#BF0000")
        self.entry_field.config(bg="#800000", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#BF0000")
        self.send_button.config(bg="#800000", fg="#FFFFFF", activebackground="#800000", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#BF0000", fg="#FFFFFF")

        self.tl_bg = "#800000"
        self.tl_bg2 = "#BF0000"
        self.tl_fg = "#FFFFFF"

    # Hacker
    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#33FF33")
        self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        # self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#33FF33"

    #Hacker 2
    def color_theme_hacker_2(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#00FFAA")
        self.entry_field.config(bg="#0F0F0F", fg="#00FFAA", insertbackground="#00FFAA")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#00FFAA")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#00FFAA"

    #Hacker 3
    def color_theme_hacker_3(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#A020F0")
        self.entry_field.config(bg="#0F0F0F", fg="#A020F0", insertbackground="#A020F0")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg=f"#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#A020F0")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#A020F0"

    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()

root = Tk()
a = ChatInterface(root)
root.geometry(window_size)
root.title("Chat GPT")
root.iconbitmap('i.ico')
root.mainloop()
