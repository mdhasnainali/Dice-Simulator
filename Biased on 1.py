import tkinter
from PIL import Image, ImageTk
import random

# Top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# Adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Dice Simulator",
                             fg="#B22222",
                             bg="#EA9090",
                             font="Helvetica 16 bold")
HeadingLabel.pack()

# Working with image
dice = ['Image/Dic1.png', 'Image/Dic2.png', 'Image/Dic3.png',
        'Image/Dic4.png', 'Image/Dic5.png', 'Image/Dic6.png', 'Image/Dic1.png', 'Image/Dic1.png', 'Image/Dic1.png']

# simulating the dice with random numbers between 0 to 6
DiceNumber = random.choice(dice)

# generating image
DiceImage = ImageTk.PhotoImage(Image.open(DiceNumber))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget
ImageLabel.pack(expand=True)


# function activated by button
def rolling_dice():
    dicenewimage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=dicenewimage)
    # keep a reference
    ImageLabel.image = dicenewimage


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='Red', command=rolling_dice, bd=1, activebackground='#E6E4E4')

# pack a widget in the parent widget
button.pack(expand=True)
root.mainloop()
