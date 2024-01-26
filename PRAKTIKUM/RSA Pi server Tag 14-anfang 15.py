import socket
import random
import math
from datetime import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

import RPi.GPIO as GPIO
import time

ledPin = 11    # RPI Board pin11

def blink():
    GPIO.output(ledPin, GPIO.HIGH)  # led on
    print ('...led on')
  
def blinknein():
    GPIO.output(ledPin, GPIO.LOW) # led off
    print ('led off...')

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
    GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to off led
    print ('using pin%d'%ledPin)

def loop():
    while xl == True:
        blink(1)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     # led off
    GPIO.cleanup()  

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

def to_ascii(NACHRICHT_VER1):
    ascii_values = [ord(character) for character in NACHRICHT_VER1]
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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def power_mod(base: int, exponent: int, mod: int) -> int:
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

    
start = 'start'
xl = 'lo'
ne = 'ne'
x = 'print' #print befehl
liste = []  #liste erstellen, zur Speicherung und analysierung von Nachrichten
m = 'OK'  #check ob der Befehl richtig verstanden wurde
COE = 'ne'  #Nachricht mit dem öffentlichen code verschlüsseln
c = 'code'  #die verschlüsselte Nachricht entschlüsseln
ledA = 'ledA'  #LED an
ledAU = 'ledAU'  #LED aus

commands = [xl, ne, x, m, COE, c , "led"]

def server_program():
    setup()
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
        print('Es gibt keinen teilerfremden Wert für' + str(n1) + ', du musst alles nochmal versuchen.')
    d = modinv(e, (a - 1) * (b - 1))
    CF = str(CODE1) + ' ' + str(e)
    # get the hostname
    host = "192.168.1.100"
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    print("Socket created" + str(host) + " port: " + str(port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    skipInput = False
    h = 0
    data = ''
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        jetzt = datetime.now().replace(microsecond=0)
        jetzt = jetzt.strftime("%Y-%m-%d %H:%M:%S")
        data = conn.recv(1024).decode()
        print('Received from client: ' + data)  # show in terminal
        if not data:
            # if data is not received break
            break
        liste = data.split(' ')
        if liste[0] == x:
            print(liste[1:])
            conn.send(bytes('OK ' + liste[0], 'utf-8'))
        elif liste[0] == m:
            print('----------------------->>' + jetzt + '<<-----------------------')
            skipInput = True
        elif COE == liste[0]:
            na = liste[1]
            ea = liste[2]
            conn.send('connection secure')
            data = conn.recv(1024).decode()
            print(data)
        elif c == liste[0]:
            CODE2 = liste[1:]
            CODE2 = [power_mod(int(m), int(d), int(CODE1)) for m in CODE2]
            CODE2 = from_ascii(CODE2)
            print('MESSAGE: ' + CODE2)
            conn.send(bytes('OK ' + liste[0], 'utf-8'))
            skipInput = False
        elif ledA == liste[0]:
            xl = True
            conn.send(bytes('OK ' + liste[0], 'utf-8'))
            blink()
        elif ledAU == liste[0]:
            xl = False
            conn.send(bytes('OK ' + liste[0], 'utf-8'))
            blinknein()
        elif start == liste[0]:
            lok = input('PW: ')
            if lok == '4321':
                conn.send(bytes('ne ' + CF, 'utf-8'))
            data = conn.recv(1024).decode()
            print('Received from client: ' + data)
            liste = data.split(' ')
            if COE == liste[0]:
                na = liste[1]
                ea = liste[2]
                conn.send(bytes('OK connection secure', 'utf-8'))
                print('connection secure')
                skipInput = True
        else:
            print('Befehl nicht verstanden!!' + liste[0])
            
            
        if  not skipInput:
            data = input(' -> ')
            liste1 = data.split(" ")
            
            if liste1[0] in commands:
                conn.send(data.encode())
            else:
                data = to_ascii(data)
                data = [pow(int(m), int(ea), int(na)) for m in data]
                data = [str(m) for m in data]
                data = ' '.join(data)
                conn.send(bytes('code ' + data, 'utf-8'))#Message to ascii
                print('SEND-> ' + data)
        skipInput = False    


    conn.close()  # close the connection





if __name__ == '__main__':
    server_program()