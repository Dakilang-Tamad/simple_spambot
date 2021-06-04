import pyautogui, time
import tkinter as tk
from tkinter import*
from tkinter.ttk import*
import tkinter.messagebox


class Inator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(S0)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class S0(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scroll = Scrollbar(master, orient="vertical")
        self.scroll.pack(side=RIGHT, fill=Y)

        self.t_box = Text(master, height=10, width=50, bg="light cyan", yscrollcommand=self.scroll.set)
        self.t_box.place(x=50, y=60)

        self.label = Label(master, text="Please enter spam text", bg=None, justify=CENTER)
        self.label.config(font=("Courier", 20))
        self.label.pack()

        self.scroll.config(command=self.t_box.yview)

        self.next = Button(master, text="Proceed", command=lambda: self.proceed(master))
        self.next.place(x=190, y=235, height=50, width=100)

    def proceed(self, master):
        file = open("spam.txt", "w")
        byline = self.t_box.get('1.0', END).splitlines()
        for i in byline:
            file.write(i + "\n")
        Inator.switch_frame(master, S1)


class S1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = Label(master, text="Please click your cursor \n"
                                        "to your chatbox input \n"
                                        "after clicking spam. \n"
                                        , bg=None, justify=CENTER)
        self.label.config(font=("Courier", 15))
        self.label.place(x=100, y=100)

        self.next = Button(master, text="Spam", command=lambda: self.spam())
        self.next.place(x=190, y=235, height=50, width=100)

    def spam(self):
        self.f = open("spam.txt", "r")
        time.sleep(5)
        for word in self.f:
            pyautogui.typewrite(word)
            self.label.config(text="sending" + word)

            pyautogui.press("enter")






if __name__ == "__main__":
    app = Inator()
    app.title("Chat Spammer Inator")
    app.geometry("500x300")
    app.resizable(False, False)
    icon = PhotoImage(file=r"doof.png")
    app.iconphoto(False, icon)
    app.mainloop()
