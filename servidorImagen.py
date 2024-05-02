import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def decrypt_image(encrypted_image, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_image = cipher.decrypt(encrypted_image)
    return decrypted_image

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Waiting for connections...")

    client_socket, address = server_socket.accept()
    print("Connection established with:", address)

    # Recibir imagen encriptada
    encrypted_image = client_socket.recv(4096)

    # Clave de desencriptado (debería ser la misma que se usó para encriptar en el cliente)
    key = b'16bytessecretkey'

    # Desencriptar imagen
    decrypted_image = decrypt_image(encrypted_image, key)

    # Guardar la imagen desencriptada
    with open('decrypted_image.jpg', 'wb') as file:
        file.write(decrypted_image)

    print("Image decrypted and saved as 'decrypted_image.jpg'")
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
