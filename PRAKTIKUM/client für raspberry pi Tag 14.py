# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:34:32 2024

@author: Administrator
"""
import socket
import random
import math
from datetime import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def createList(lst, x):
    lst.append(x)
    return lst

def Primnumber(lst):
    global x
    x = 2
    while x <= 10000:
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i) == 0:
                is_prime = False
                break
        if is_prime:
            createList(lst, x)
        x += 1

def to_ascii(message):
    ascii_values = [ord(character) for character in message]
    return ascii_values

def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def finde_teilerfremden(CODE1):
    for i in range(2, CODE1):
        if ggT(i, CODE1) == 1:
            return i
    return None

def from_ascii(CODE2):
    charListe = [chr(ascii_int) for ascii_int in CODE2]
    return ''.join(charListe)

xl = 'lo'
ne = 'ne'
x = 'print' #print befehl
liste = []  #liste erstellen, zur Speicherung und analysierung von Nachrichten
m = 'OK'  #check ob der Befehl richtig verstanden wurde
COE = 'ne'  #Nachricht mit dem öffentlichen code verschlüsseln
c = 'code'  #die verschlüsselte Nachricht entschlüsseln
ledA = 'ledA'  #LED an
ledAU = 'ledAU'  #LED aus

commands = [xl, ne, x, m, COE, c , ledA, ledAU]

def client_program():
    
    
    lst = []
    Primnumber(lst)
    random.shuffle(lst)
    a = lst[random.randint(0, len(lst))]
    b = lst[random.randint(0, len(lst))]
    CODE1 = a * b
    n1 = (a - 1) * (b - 1)
    
    ergebnis = finde_teilerfremden(n1)
    if ergebnis:
        if ergebnis < n1:
            e = ergebnis
    else:
        print(f"Es gibt keinen teilerfremden Wert für {n1}, du musst alles nochmal versuchen.")
    d = pow(e, -1, (a - 1) * (b - 1))
    CF = f'{CODE1} {e}'
    
    msg = 'start'
    h = 0
    
    host = '192.168.1.100'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    skipInput = False
    
    message = input(" PW: ")  # take input
    if message == '1234':
        message = 'start'
        client_socket.send(message.encode())
    skipInput = True
    while message.lower().strip() != 'bye':
        jetzt = datetime.now().replace(microsecond=0)
        data = client_socket.recv(1024).decode()  # receive response
        liste = data.split()
        
        if liste[0] != 'OK':
            print('Received from client: ' + data)  # show in terminal
        
        if liste[0] == x:
            print(liste[1:])
            client_socket.send(bytes('OK ' + liste[0], 'utf-8'))
            skipInput = True
        elif liste[0] == 'OK':
            print(f'{Fore.GREEN}----------------------->>{jetzt}<<-----------------------{Style.RESET_ALL}')
            h = h + 1
            if h >= 2:
                skipInput = True
        elif COE == liste[0]:
            na = liste[1]
            ea = liste[2]
            client_socket.send(bytes(f'ne {CF}', 'utf-8'))
        elif c == liste[0]:
           CODE2 = liste[1:] 
           CODE2 = [pow(int(m), int(d), int(CODE1)) for m in CODE2]
           CODE2 = from_ascii(CODE2)
           print('MESSAGE: ' + CODE2)
           client_socket.send(bytes('OK ' + liste[0], 'utf-8'))
        elif ledA == liste[0]:
            xl is True
            client_socket.send(bytes('OK ' + liste[0], 'utf-8'))
            skipInput = True
        elif ledAU == liste[0]:
            xl is False
            client_socket.send(bytes('OK ' + liste[0], 'utf-8'))
            skipInput = True
        else:
            print('Befehl nicht verstanden!! ' + liste[0])

        if  not skipInput:
            message = input(' -> ')
            liste1 = message.split(" ")
            
            if liste1[0] in commands:
                client_socket.send(message.encode())
            else:
                message = to_ascii(message)
                message = [pow(int(m), int(ea), int(na)) for m in message]
                message = [str(m) for m in message]
                message = ' '.join(message)
                client_socket.send(bytes('code ' + message, 'utf-8'))#Message to ascii
                print(f'SEND-> {message}')
        skipInput = False

        
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()