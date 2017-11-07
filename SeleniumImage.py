import numpy
from PIL import Image
import scipy.misc


def screeshopElement(browser,element,nameRef='ref.jpg',nameScreenshot='screenshot.jpg'):
    location = element.location
    size = element.size

    try:
        open(nameRef)
        namefile = nameScreenshot
    except:
        namefile = nameRef

    browser.save_screenshot(namefile)

    im = Image.open(namefile)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))

    if(namefile == nameRef):
        im.save(namefile)
        im.save(nameScreenshot)
    else:
        im.save(namefile)

    return Image.open(namefile)

def tamanhoMatriz(matriz):
    x, y = len(matriz), len(matriz[0])
    return x * y

def compareImage(screeshop,referencia, margem=None, nameDiff='diff.jpg'):
    screenshot = numpy.asarray(Image.open(screeshop).convert('L'))
    ref = numpy.asarray(Image.open(referencia).convert('L'))

    dif = screenshot - ref
    tam_matriz = tamanhoMatriz(dif)
    scipy.misc.imsave(nameDiff, dif)
    diferenca = 100 * float(numpy.count_nonzero(dif)) /float(tam_matriz)

    if (margem == None):
        if(diferenca == 0):
            resultado = True
        else:
            resultado = False
    elif(diferenca <= margem):
        resultado = True
    else:
        resultado = False


    retorno = {
        "diff": str("%.2f" % diferenca)+'%',
        "Image_file": nameDiff,
        "resultado": resultado
    }

    return retorno
