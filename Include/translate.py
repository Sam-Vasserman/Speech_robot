import tkinter
from PIL import ImageTk, Image
from google_trans_new import google_translator

translator = google_translator()

class TRAN:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Translation")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.img = ImageTk.PhotoImage(Image.open('C:/Users/Sweet/Desktop/julie/london-taste-of-england-hero.jpg'))
        self.panel = tkinter.Label(self.root, image = self.img)
        self.rus = tkinter.Entry(self.root, font="Consolas 20",
                                 fg="#fff",
                                 bg="#3c3c3c",
                                 relief="solid",
                                 justify="center", text=input)
        text_to = self.text.get(tkinter.Entry)
        self.eng = tkinter.Entry(self.root, font="Consolas 20",
                                 fg="#fff",
                                 bg="#3c3c3c",
                                 relief="solid",
                                 justify="center"
)
        self.translate = tkinter.Button(self.root, text = "Translate", font = "Consolas 13", fg = "#fff", bg ="#ff0d66", activeforeground = "#fff", activebackground = "#9e9e9e",)
        self.rus.place(x = 50, y = 68)
        self.eng.place(x = 50, y = 158)
        self.translate.place(x = 151, y = 210)
        self.panel.pack()
        tkinter.mainloop()
gui = TRAN()
