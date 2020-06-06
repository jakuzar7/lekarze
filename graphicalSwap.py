from PIL import Image, ImageDraw, ImageFont, ImageColor

stdFont = ImageFont.truetype(
    'font/newStandardRegular/NewStandardRegular.otf', size=45)
manualeFont = ImageFont.truetype(
    'font/manuale/Manuale-Regular.ttf', size=45)



# box [x, y, w, h] left up corner XY, width, height
def addText(text, box, docImg, textFont=stdFont, textColor=(0, 0, 0), textSpacing=24, downMarginPct=0.85):


    #drawing box and calculating text position
    textImg = Image.new('RGB', (box[2], box[3]), color=(255, 255, 255))
    ImgDrw = ImageDraw.Draw(textImg)
    TextSizeX, TextSizeY = ImgDrw.multiline_textsize(
        text, font=textFont, spacing=textSpacing)
    # middle pos
    TextPosX = (box[2]-TextSizeX)/2
    # down border, with margin from below
    TextPosY = (box[3]-TextSizeY) * downMarginPct

    ImgDrw.text((TextPosX, TextPosY), text, fill=textColor,
                    font=textFont, align='center', spacing=textSpacing)

    docImg.convert('RGB')

    # paste box with text onto document
    docImg.paste(textImg, (box[0], box[1], box[0] + box[2], box[1]+box[3]))

    return docImg


def makeFont(textFontPath, textSize=45):
    if textFontPath == '':
        textFontPath = 'font/newStandardRegular/NewStandardRegular.otf'
    return ImageFont.truetype(textFontPath, size=textSize)
    
def saveFile(file, filePath):
    file.save(filePath)
    pass

def loadImg(imgPath):
    return Image.open(imgPath).convert('RGB')
    
    
'''
nameImg = Image.new('RGB', (name[2], name[3]), color=(255, 255, 255))

nameImgDrw = ImageDraw.Draw(nameImg)
nameTextSizeX, nameTextSizeY = nameImgDrw.multiline_textsize(
    nameText, font=stdFont, spacing=24)

# middle
nameTextPosX = (name[2]-nameTextSizeX)/2
# down border, with margin below
nameTextPosY = (name[3]-nameTextSizeY) * 0.85

nameImgDrw.text((nameTextPosX, nameTextPosY), nameText, fill=(0, 0, 0),
                font=stdFont, align='center', spacing=24)

#nameImg.save('pil_text.png')

doc = Image.open(
    'orignalImg/OrzeczenieLekarskieDoBadanKierocow1.png').convert('RGB')

# paste box with text onto document
doc.paste(nameImg, (name[0], name[1], name[0] + name[2], name[1]+name[3]))

doc.save('PILprawojazdy.png')
doc.save('PILprawojazdy.pdf')
'''
