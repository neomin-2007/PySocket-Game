import socket

loaded_players = []

def start_server():

    global loaded_players, players_count

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('', 25570))

    print("O servidor está iniciando...")

    while True:

        message, address = server.recvfrom(4096)
        decoded_message = message.decode()

        if decoded_message.startswith("/connect"):
            username = decoded_message.split(":")[1]
            print(f"O usuário ({username}) entrou...")
            loaded_players.append(username)

        print(decoded_message)

start_server()