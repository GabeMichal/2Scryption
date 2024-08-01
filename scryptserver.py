import socket
from _thread import *
from Scrypt_player import Player
from scrypkle import picklificate, unpickle
from Scrypt_comms import *
from Scrypt_game import Game
from Scrypt_card import *
import pickle

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(240,290,10,10,(255,0,0)), Player(240,290, 10,10, (0,0,255))]
scryption = Game(*players)

def threaded_client(conn, player):
    scryption.players[player].playerNum = player
    conn.send(picklificate(player))
    scryption.players[player].cards = unpickle(conn)
    scryption.setDefault()
    wPress = False
    aPress = False
    sPress = False
    dPress = False
    reply = ""
    while True:
            #print("Sending:", scryption)
            conn.sendall(picklificate(scryption))

            data = unpickle(conn)
            #print("Received:", data)

            if data is None:
                print("Disconnected")
                break

            if data[1][pygame.K_ESCAPE]:
                break

            scryption.players[player].mousePos = data[0]

            if scryption.screen in ["battle", "battleswap", "hoard"] or "Boss" in scryption.screen or "cut" in scryption.screen:
                scryption.battleMoment2(player)

            if isinstance(data[1], tuple):
                if scryption.screen == "overworld":
                    scryption.switch = 0
                    wPress = True
                    players[player].move(data[1], scryption.map[0])
                    if players[player].playerNum:
                        mapPlayer = players[player]
                    else:
                        mapPlayer = players[1-player]
                    if mapPlayer.y <= 255:
                        spotLen = len(scryption.map[0].spots[1])
                        for m in range(spotLen):
                            if spotLen == 1:
                                scryption.screen = scryption.map[0].spots[1][0]
                            elif spotLen == 2:
                                scryption.screen = scryption.map[0].spots[1][int(mapPlayer.x/240)]
                            elif spotLen == 3:
                                scryption.screen = scryption.map[0].spots[1][int((mapPlayer.x-120)/80)]
                        scryption.setDefault()
                else:
                    if data[2]:
                        scryption.getClick(player)
                    if data[1][pygame.K_w]:
                        if not wPress:
                            players[player].deckShow = True
                            wPress = True
                    else:
                        wPress = False
                    if data[1][pygame.K_s]:
                        if not sPress:
                            players[player].deckShow = False
                            players[player].ruleb = ""
                            sPress = True
                    else:
                        sPress = False
                    if data[1][pygame.K_a]:
                        if isinstance(players[player].ruleb, int):
                            if not aPress:
                                players[player].ruleb -= 2
                                if players[player].ruleb < 0:
                                    players[player].ruleb = len(rulebook)-len(rulebook)%2
                                aPress = True
                    else:
                        aPress = False
                    if data[1][pygame.K_d]:
                        if isinstance(players[player].ruleb, int):
                            if not dPress:
                                players[player].ruleb += 2
                                if players[player].ruleb >= len(rulebook):
                                    players[player].ruleb = 0
                                dPress = True
                    else:
                        dPress = False

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
