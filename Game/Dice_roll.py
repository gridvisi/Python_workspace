
from tkinter import *
from PIL import Image, ImageTk
import random
def Roll() :
    randomImg = random.choice(diceImg)
    img_1 = Image.open(randomImg)
    img_2 = ImageTk.PhotoImage(img_1)
    imgLabel.configure(image = img_2)
    imgLabel.image = img_2

if __name__ == "__main__" :
    window = Tk()
    window.configure(background = 'black')
    window.geometry("500x510")
    window.title("Dice Roll")
    diceImg = ['11.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
    randomImg = random.choice(diceImg)
    img_1 = Image.open(randomImg)
    img_2 = ImageTk.PhotoImage(img_1)
    imgLabel = Label(window, image = img_2)
    imgLabel.grid(row = 2, column = 2,
                 padx = "50", pady = "50")
    rollButton = Button(window, text = "Roll Dice",
                    bg = "red", fg = "black",
                    command = Roll)
    rollButton.grid(row = 3, column = 2,
                     padx = "25", ipadx = "10")

    window.mainloop()