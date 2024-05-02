# ExamenCiberseguridad

Son pequeños programas para encriptar una imagen y recibirla para desencriptarla en formato AES, "servidorImagen.py" se ejecutaría en el servidor y "usuarioImagen.py" de parte del usuario.
Primero instalamos la biblioteca "pycryptodome" en las instancias de python, tanto la computadora como el servidor y se utiliza una imagen llamada "imagenEncriptada.jpg" para que pueda utilizar el path configurado.

Se ejecuta "servidorImagen.py" desde un servidor y se establece conexión desde una computadora y se ejecuta "usuarioImagen.py", así el servidor debería mostrar que guardo la imagen "imagenEncriptada.jpg"
