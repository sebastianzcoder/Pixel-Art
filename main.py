"""

Copyright (c) Sebastian Chetroni "Tee N'Tee" 2023.05.27
Email: sebastianchetroni@gmail.com

"""

from time import sleep

from guizero import *
from guizero.dialog import *

from consts import *

currentColor = red


def levelClicked(x, y):
    global lvl, levelWindow
    if (x, y) == (0, 0):
        lvl = 1
    if (x, y) == (1, 0):
        lvl = 2
    if (x, y) == (0, 1):
        lvl = 3
    if (x, y) == (1, 1):
        lvl = 4
    if (x, y) == (0, 2):
        lvl = 5
    if (x, y) == (1, 2):
        lvl = 6

    levelWindow = Window(root, f"Level {lvl}", 600, 800)

    makeLevel(lvl, levelWindow)


def makeLevel(lvl, levelWindow):
    global currentColor

    def pixelClicked(x, y):
        print("[DEBUG]:: ~ Player clicked playableWaffle on ({},{})".format(x, y))
        # if playableWaffle.get_pixel(event.x//20, event.y//20) == currentColor:
        #     playableWaffle.set_pixel(event.x//20, event.y//20, white)
        #     sleep(.1)
        #     return
        sleep(.1)
        playableWaffle.set_pixel(x, y, currentColor)

    def changeColor(x, y):
        global currentColor
        currentColor = colorPalette.get_pixel(x, y)

        print("[DEBUG]:: ~ Successfully changed color to " + colorPalette._waffle_pixels[x, y].color)
        # print("[DEBUG]:: ~ Successfully changed color")

    def checkLevel():
        ready = True
        for x in range(rows):
            for y in range(cols):
                if playableWaffle.get_pixel(x, y) == levelWaffle.get_pixel(x, y): continue
                ready = False
        if ready:
            info("Level finished", "Well done!", levelWindow)
            levelWindow.destroy()
        else:
            if yesno("Not finished", "You didn't finished your level! Exit?"):
                levelWindow.destroy()

    if lvl == 1:
        import level.lvl1 as level
    if lvl == 2:
        import level.lvl2 as level
    if lvl == 3:
        import level.lvl3 as level

    print("[DEBUG]:: ~ Successfully imported level.lvl{}".format(lvl))

    levelWindow.resize(340, 820)
    levelWindow.bg = woody
    Text(levelWindow, "", size=10)
    levelWaffle = Waffle(levelWindow, rows, cols, dotty=False, color=white, command=lambda x, y: None, dim=20, pad=0)
    print("[DEBUG]:: ~ Successfully created levelWaffle")

    Text(levelWindow, "", size=10)

    for y in range(rows):
        for x in range(cols):
            levelWaffle.set_pixel(x, y, level.matrix[y][x])

    playableWaffle = Waffle(levelWindow, command=pixelClicked, height=rows, width=cols, dotty=False, color=white,
                            dim=20, pad=0)
    # playableWaffle.when_mouse_dragged = pixelClicked
    Text(levelWindow, "", size=10)
    print("[DEBUG]:: ~ Successfully created playableWaffle")

    colorPalette = Waffle(levelWindow, 1, 10, dotty=True, command=changeColor, dim=20, pad=10)
    print("[DEBUG]:: ~ Successfully created colorPalette")

    for i in range(10):
        colorPalette.set_pixel(i, 0, [n, k, t, w, d, b, l, r, o, g][i])

    checkButton = PushButton(levelWindow, command=checkLevel, text="CHECK", pady=0, padx=10)
    checkButton.bg = woody
    checkButton.text_color = bluey


if __name__ == '__main__':
    root = App("Pixel Art", 460, 500, bg=bluey)
    # root.icon = "./PixelArt.gif"

    lvl = None
    boox = Box(root, height=60, width=400)
    name = Text(boox, text="ᴘɪx\u0332eʟ ⲁʀт", size=40)
    levelsWaffle = Waffle(root, 3, 2, dotty=True, color=blood, command=levelClicked, dim=100, pad=20)
    root.display()
