  
# Author: Aniket Dinda
# Site: https://hackingivla.wordpress.com
#!/usr/bin/python
# -*- coding: utf-8 -*-

from randmac import RandMac
import os, sys, time

def start():
    pass
    start_time = time.time()
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        num = int(input("\n\n\tEnter an number: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Number of generated keys: ", num)
        print("\n")
        for _ in range(0, num):
            example_mac = "00-00-00-00-00-00"
            generated_mac = RandMac(example_mac)            
            print("[+] Generated 6-byte mac address: ",generated_mac)
            
        end = round(time.time() - start_time ,2)
        print("\n\n\t[*] Total time elapsed:>  ", end ,"sec")
            
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n\t[/] Input number only...")  
        print("\n\n\n\t[*] Try Agian [*]")
        time.sleep(2)
        start()
    except KeyboardInterrupt:
        print("[+] CTRL+C detected [+]")
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
start()
input("\n\n\n\tPress enter for exit")
os.system('cls' if os.name == 'nt' else 'clear')
sys.exit()
