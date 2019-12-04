# Code Kata: "the tree"
# Original concept by Seb-Lee Delisle  @seblee
# Adapted to Python by Pedro Dias @digitaldias December 4, 2019
# Revision 1.0

from tkinter import *
import math
import random
import time

# Initial junk, set up a window to put the tree in
window = Tk()
window.title("A Tree")
window.configure(background='black')
window.geometry("1024x768")

instructions = "Click the left mousebutton to draw a tree.\nRepeat until bored sick.\nHit <ESC> to end the misery"

# Create a canvas to draw on
canvas = Canvas(window, bd=0, highlightthickness=0, relief='ridge')
canvas.configure(background='black', bd=0)
canvas.create_text(10, 10, text=instructions, fill='white', font="arial 12", anchor=NW)
canvas.pack(fill=BOTH, expand=True)

# Get our Canvas dimensions
window.update()
width, height = canvas.winfo_width(), canvas.winfo_height()
print("Window width: {}, height: {}".format(width, height))

def randomDegree(min, max):
    """ Return a random degree between min and max """

    return min + random.randint(min, max)

def reduce_branch_length(size):
    """ Reduce the branch by a random length of 60-95% """

    factor = round(random.uniform(0.6, 0.95), 2)
    return size * factor


def drawTree(size, lastX, lastY, angle):
    """ Recursively draws the tree, branch by branch, until the branches are shorter than 15 in length """

    lineWidth      = size * 0.1
    angleInRadians = angle * math.pi / 180
    nextY          = lastY - size * math.cos(angleInRadians)
    nextX          = lastX + size * math.sin(angleInRadians)

    canvas.create_line(lastX, lastY, nextX, nextY, fill='yellow', width=lineWidth)

    if size > 15:
        branchLength = reduce_branch_length(size)
        drawTree(branchLength, nextX, nextY, angle + randomDegree(0, 35))

        branchLength = reduce_branch_length(size)
        drawTree(branchLength, nextX, nextY, angle - randomDegree(0, 35))

def start_over(_):
    """ Empties the current canvas and draws a new tree """

    canvas.delete("all")
    t0 = time.time()
    lastX, lastY = canvas.winfo_width() / 2, canvas.winfo_height() - 10  # Calculate the starting positions bottom center
    treeSize = canvas.winfo_height() * (1/7.68)                          # Height of the tree is in the ratio 768pix height goes to 100pix tall tree
    drawTree(treeSize, lastX, lastY, 0)
    finished = "{}ms.".format(round(1000* (time.time() - t0), 1))
    canvas.create_text(lastX + 12, lastY -12, text=finished, fill='green', anchor=NW ) # informal "grass" with time taken to render :D

def end_program(_):
    """ Terminate the program """

    print("Program ended.")
    window.destroy()

def configure(event):
    """ When the window resizes, make sure to update """

    window.update()
    canvas.update()
    canvas.delete("all")
    width, height = canvas.winfo_width(), canvas.winfo_height()
    print("Resize event to: {}x{}".format(width, height))

    # Find our starting position at the middle of the bottom of the screen
    lastX = width/2
    lastY = height - 10
    canvas.create_text(10, 10, text=instructions, fill='white', font="arial 12", anchor=NW)


if __name__ == '__main__':
    canvas.bind("<Button-1>", start_over) # Bind left button to redrawing the tree
    window.bind("<Escape>", end_program)  # Let the program finish when ESC is pressed
    canvas.bind("<Configure>", configure) # What to do when the window resizes
    window.mainloop()
