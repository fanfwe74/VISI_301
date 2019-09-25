from PIL import Image

def convert_to_tab(im):
    """
    Entrée : Fichier image
    Sortie : Tableau à deux dimensions
    Chaque pixels blancs deviennent des 1 dans le tableau, sinon des 0.
    La deuxième dimension du tableau correspond aux lignes de pixels.
    """

    im_RGB = im.convert('RGB')
    size = ( im_RGB.size[0], im_RGB.size[1] )
    tab = []

    for j in range(0, size[1],1):

        line = []

        for i in range(0, size[0],1):

            pix = im_RGB.getpixel((i, j))

            if pix[0]>=245 and pix[1]>=245 and pix[2]>=245:
                line.append(1)
            else:
                line.append(0)

        tab.append(line)

    return(tab)


tab1 = Image.open('Tableau_Template.jpg')
print(convert_to_tab(tab1))