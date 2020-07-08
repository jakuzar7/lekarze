import tkinter as tk
import graphicalSwap as gs

root = tk.Tk()

# orzeczenie lekarskie do badan kierowcow
# left up corner XY, width, height
nameBox = [155, 22, 621, 253]
miejscowoscDataBox = [952, 208, 468, 70]

originalDocImg = gs.loadImg(
    'orignalImg/OrzeczenieLekarskieDoBadanKierocow1.png')

# importing all doc properties and settings
# make doc class and change all variables to object properties
labelObjs, inputObjs = [], []
docTexts = [['Podaj imię i nazwisko pacjenta', 'imię i nazwisko'], []]
docBoxes = [nameBox, miejscowoscDataBox]


def reloadDoc(inputObjs, docBoxes):
    font = gs.makeFont('font/manuale/Manuale-Regular.ttf', textSize=70)
    # make here a loop
    inputText = inputObjs[0].get()
    docImg = gs.addText(inputText, docBoxes[0], originalDocImg, textFont=font)

    gs.saveFile(docImg, 'PILprawojazdy.pdf')
    gs.saveFile(docImg, 'PILprawojazdy.png')
    return


# make label + input, returning [labelObject, inputObject] without placement
def makeLabelInput(labelText, inputText):
    inputObj = tk.Entry(root)
    inputObj.insert(0, inputText)
    labelObj = tk.Label(text=labelText)

    return [labelObj, inputObj]


# making label and input objects
labelObj, inputObj = makeLabelInput(docTexts[0][0], docTexts[0][1])
inputObjs.append(inputObj)
labelObjs.append(labelObj)


# UI - grid managment of widgets --> loop
reloadButton = tk.Button(root, text="Zatwierdź",
                         command=(lambda: reloadDoc(inputObjs, docBoxes)))

labelObjs[0].grid(row=0, column=0)
inputObjs[0].grid(row=0, column=1)
reloadButton.grid(row=1, column=0, columnspan=2)

root.mainloop()
