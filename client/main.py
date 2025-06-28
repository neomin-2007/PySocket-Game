import socket
from player import Player;

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    player = Player()
    player.set_name("Neomin")
    player.move(3, 6)
    logged = False

    print("Digite /connect para se conectar!")

    while True:
        if not logged:
            message = input()
            client.sendto(f"{message}:{player.p_encode()}".encode(), (('', 25570)))
            logged = True

        input()
        client.sendto(player.p_encode().encode(), (('', 25570)))

start_client()