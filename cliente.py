import socket
import threading

user = input("Escolhe um nome de user ai logo: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 9900))

def recebendo_msgs():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('ascii')
            if mensagem == 'USER':
                cliente.send(user.encode('ascii'))
            else:
                print(mensagem)
        except:
            print("deu erro seu maluco")
            cliente.close()
            break


def escrevendo_msg():
    while True:
        mensagem = f'{user}: {input("")}'
        cliente.send(mensagem.encode('ascii'))

recebendo_thread = threading.Thread(target=recebendo_msgs)
recebendo_thread.start()

escrevendo_thread = threading.Thread(target=escrevendo_msg)
escrevendo_thread.start()