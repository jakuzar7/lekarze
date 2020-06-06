import tkinter as tk
import graphicalSwap as gs

root = tk.Tk()

# input widget
e = tk.Entry(root, width=50 )
e.pack()
e.insert(0, "Enter your name here")

# e.get() gets the input
#print(e.get())

def myClick():
    nameText = e.get()
    font = gs.makeFont('font/manuale/Manuale-Regular.ttf',textSize=70)
    docImg = gs.addText(nameText, nameBox, originalDocImg,textFont=font)
    gs.saveFile(docImg,'PILprawojazdy.pdf')
    gs.saveFile(docImg,'PILprawojazdy.png')
    return 


myButton = tk.Button(root, text="Enter name", command=myClick)
myButton.pack()


# orzeczenie lekarskie do badan kierowcow
# left up corner XY, width, height
nameBox = [155, 22, 621, 253]
miejscowoscDataBox = [952, 208, 468, 70]
#nameText = 'dr med. Jan Kowalski\nPrzychodnia XYZ\nąźćżęąóÓŻŹĆŚĘĄŃ'
originalDocImg = gs.loadImg('orignalImg/OrzeczenieLekarskieDoBadanKierocow1.png')

#docImg = gs.addText(nameText, nameBox, originalDocImg,textFont=gs.stdFont)





root.mainloop()
