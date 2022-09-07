import qrcode
from PIL import Image

cadena = input("Introduzca lo que desea Generar a QR: ")
imagen = qrcode.make(cadena)

nombre_imagen = input("Introduzca el nombre de la imagen: ") + '.pdf'
archivo_imagen = open(nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = './'+nombre_imagen
Image.open(ruta_imagen).show()
