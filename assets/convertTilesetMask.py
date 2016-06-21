from PIL import Image

im = Image.open('tileset_mask.png')
pix = im.load()

offset = 16
        
for y in range(0,34) :
        
    mask = []
    
    for x in range(0,50) :

        (r, g, b, a) = pix[ x*32 + offset, y*32 + offset]

        if   (a == 0) : mask.append('0')
        elif (r == 0) : mask.append('1')
        else          : mask.append('2')

    print ','.join(mask)




