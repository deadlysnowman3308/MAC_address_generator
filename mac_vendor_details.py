import requests 
import argparse 

print("[~] Welcome") 
def get_arguments(): 
	parser = argparse.ArgumentParser() 
	parser.add_argument("-m", "--macaddress", 
						dest="mac_address", 
						help="MAC Address of the device. "
						) 
	options = parser.parse_args() 
	if options.mac_address: 
		return options.mac_address 
	else: 
		parser.error("[!] Invalid Syntax. "
					"Use --help for more details.") 
def get_mac_details(mac_address): 
	url = "https://api.macvendors.com/"
	response = requests.get(url+mac_address) 
	if response.status_code != 200: 
		raise Exception("[!] Invalid MAC Address!") 
	return response.content.decode() 
if __name__ == "__main__": 
	mac_address = get_arguments() 
	print("[+] Checking Details...") 
	try: 
		vendor_name = get_mac_details(mac_address) 
		print("[+] Device vendor is "+vendor_name) 
	except: 
		print("[!] An error occured. Check ", 
			"your Internet connection.") 
