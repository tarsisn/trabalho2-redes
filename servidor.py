import threading
import socket

host = '127.0.0.1'
port = 9900

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, port))
servidor.listen()

clientes = []
users = []


def broadcast(mensagem):
    for cliente in clientes:
        cliente.send(mensagem)


#essa function vai lidar com as mensagens
def servico(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            broadcast(mensagem)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            user = users[index]
            broadcast(f"{user} acabou de sair do chat!!".encode('ascii'))
            users.remove(user)
            break

def recebendo_msgs():
    while True:
        cliente, ip = servidor.accept()
        print(f"estamos conectados agora com {str(ip)} nessa budega")

        cliente.send('USER'.encode('ascii'))
        user = cliente.recv(1024).decode('ascii')
        users.append(user)
        clientes.append(cliente)

        print(f"o user do cara que se conectou é {user}")
        broadcast(f"{user} acabou de entrar nessa budega".encode('ascii'))
        cliente.send("se conectamo ao servidor caramba!".encode('ascii'))

        thread = threading.Thread(target=servico, args=(cliente,))
        thread.start()

print("O servidor está no grau e esperando...")
recebendo_msgs()



