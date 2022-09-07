##########################GENERATOR QR###################################

import qrcode
from PIL import Image

cadena = input("Introduzca lo que desea Generar a QR: ")
imagen = qrcode.make(cadena)

nombre_imagen = input("Introduzca el nombre del archivo: ") + '.pdf'
archivo_imagen = open(nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = './'+nombre_imagen
Image.open(ruta_imagen).show()

########################GENERATOR QR WIFI (PROBAR)#####################

"""import subprocess 
import wifi_qrcode_generator 
  
try: 
    
    Id = subprocess.check_output( 
        ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n') 
      
    id_results = str([b.split(":")[1][1:-1] 
                      for b in Id if "Profile" in b])[2:-3] 
  
    
    password = subprocess.check_output( 
        ['netsh', 'wlan', 'show', 'profiles',  
         id_results, 'key=clear']).decode('utf-8').split('\n') 
      
    pass_results = str([b.split(":")[1][1:-1] 
                        for b in password if "Key Content" in b])[2:-2] 
    print("User name :", id_results) 
    print("Password :", pass_results) 
      
except: 
    print("something wrong") 
      
wifi_qrcode_generator.wifi_qrcode(id_results, False, 'WPA', pass_results)"""