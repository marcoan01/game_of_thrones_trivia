from tkinter import *
from playsound import playsound
from PIL import ImageTk, Image
import got_trivia_tools as tools

root = Tk()
root.title("Game of Thrones Trivia")
root.eval("tk::PlaceWindow . center")
root.geometry("500x700")

bg = Image.open("./media/images/westeros_background.jpg")
bg = bg.resize((500, 700), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)

def load_frame_1():
    label_1 = Label(root, image=bg, bg="black")
    label_1.pack(fill="both", expand=True)
    
    
    Frame_1.pack(pady=20, fill="both", expand=True)
    
    text_label = Label(Frame_1, text="Are you ready to answer some questions?", bg="#3d6466", fg="white")
    text_label.pack()


Frame_1 = Frame(root)
load_frame_1()

root.resizable(False, False)
root.mainloop()
