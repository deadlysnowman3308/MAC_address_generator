  
# Author: Aniket Dinda
# Site: https://hackingivla.wordpress.com
#!/usr/bin/python
# -*- coding: utf-8 -*-

from randmac import RandMac
import os, sys, time

def start():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        num = int(input("\n\n\tEnter an number: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Number of generated keys: ", num)
        print("\n")
        for _ in range(0, num):
            example_mac = "00-00-00-00-00-00"
            generated_mac = RandMac(example_mac)            
            print("Generated 6-byte mac address: ",generated_mac)
            
    except ValueError:
        print("Please input number only...")  
        start()
    except KeyboardInterrupt:
        print("[+] CTRL+C detected [+]")
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
start()
input("\n\n\n\tPress enter for exit")
os.system('cls' if os.name == 'nt' else 'clear')
sys.exit()