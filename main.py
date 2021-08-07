import pyqrcode
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("QR Generator")

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(300, 340, window=image_label)

canvas = Canvas(root, width=600, height=750 )
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="green", font=("Arial",30))
canvas.create_window(300, 50, window=app_label)

name_label = Label(root, text="Link Name", fg = "blue", font=("Arial",15))
link_label = Label(root, text="Link", fg = "blue", font=("Arial",15))
canvas.create_window(300, 160, window=name_label)
canvas.create_window(300, 250, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(300, 200, window=name_entry)
canvas.create_window(300, 290, window=link_entry)

button = Button(text="Generate QR Code", font=("Arial",15), command=generate)
canvas.create_window(300, 390, window=button)

root.mainloop()