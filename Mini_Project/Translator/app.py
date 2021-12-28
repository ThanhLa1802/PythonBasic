from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# text = "Bạn đẹp trai quá!"
# init_trans = Translator()
# before_trans = init_trans.translate(text, src="vi", dest="en")
# after_trans = before_trans.text
# print(after_trans)

root = Tk()
root.title("Super Translator")
root.geometry("1280x720")
root.iconbitmap("db.ico")
load_img = Image.open("background.jpg")
render_img = ImageTk.PhotoImage(load_img)
background_img = Label(root, image=render_img)
background_img.place(x=10, y=10)

root.resizable(False, False)
root.mainloop()
