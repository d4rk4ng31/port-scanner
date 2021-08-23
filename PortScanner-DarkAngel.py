#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PortScanner")

print("<Author By DarkAngel>")
print("""
Port Tarama'ya Hosgeldiniz

1: 1.Port Tarama
2: 2.Ip Adresi Bulmak (url)
3: 3.Hizli Port Tarama
""")

islemnumara = raw_input("Tarama Hangi Seviyede Olsun? ")

if(islemnumara == "1"):
         hedefip = raw_input("Hedef Ip Giriniz: ")
         os.system("nmap " + hedefip)

elif(islemnumara == "2"):
        url = raw_input("Bir url giriniz: ")
        os.system("whatweb " + url)

elif(islemnumara == "3"):
    hedefip = raw_input("Hedef Ip Giriniz: ")
    os.system("nmap -F " + hedefip)

elif(islemnumara == "4"):
        hata = raw_input("Hata lutfen 1, 2, 3 seceneklerinden birisini secin.")
