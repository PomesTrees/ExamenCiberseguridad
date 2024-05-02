import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_data = image.tobytes()

    # Encriptar imagen
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(image_data, AES.block_size)
    encrypted_image = cipher.encrypt(padded_data)

    return encrypted_image

def main():
    # Ruta de la imagen a enviar
    image_path = "imagenEncriptada.jpg"

    # Clave de encriptado (debería ser la misma que se usará para desencriptar en el servidor)
    key = b'16bytessecretkey'

    # Encriptar imagen
    encrypted_image = encrypt_image(image_path, key)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Enviar imagen encriptada al servidor
    client_socket.sendall(encrypted_image)

    print("Image sent to server.")
    client_socket.close()

if __name__ == "__main__":
    main()
