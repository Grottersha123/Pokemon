from PIL import Image
def slpiting(pic):
    p = 0
    z = 0
    x = 0
    for i in pic:
        im1 = Image.open(i+'.bmp')
        x,y = im1.size
        p += y
    im = Image.new('RGB', (x, p))
    for i in pic:
        im1 = Image.open(i+'.bmp')
        x,y = im1.size
        im.paste(im1, (0,z))
        z+= y
    im.show()
    
    print(p,x)

slpiting(['004'])
