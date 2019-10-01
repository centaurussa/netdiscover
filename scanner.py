def module_settings():
	global live, arp, cast

	parse = argparse.ArgumentParser()
	parse.add_argument("-l", "--live", dest="live", help="Keep checking for devices.")
	parse.add_argument("-n", "--network", dest="network", help="Scan the wanted network.")
	data = parse.parse_args()

	network = data.network
	if data.live != None:
		live = int(data.live)
	else:
		live = None


	if network in [None, ""] and not live:
		network = input("Network (Ex: 192.168.1.1/24): ")
		if len(network) < 8 or "/" not in network or len(network.split(".")) != 4:
			print("\nSomething went wrong checking your network. Please try again.")
			print("Exiting...")
			sleep(3)
			sys.exit()
		live = int(input("Live (1 or 0): "))
	elif network is not None and live is not None:
		if len(network) < 8 or "/" not in network or len(network.split(".")) != 4:
			print("\nSomething went wrong checking your network range. Please try again.")
			print("Exiting...")
			sleep(3)
			sys.exit()
	else:
		print("Something went wrong. Please, check your arguments.")
		print("Exiting...")
		sleep(3)
		sys.exit()

	arp = scapy.ARP(pdst=network)
	cast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")



def header():
	print("\tIP\t\t\tMAC\t\t\t\tVendor")
	print("____________________________________________________________________________________________\n")


def clear():
	pass #os.system('cls' if os.name == 'nt' else 'clear')

def getter():
	global devices
	answers = scapy.srp(cast/arp, timeout=0.5, verbose=False)[0]

	mac_lst = []

	for answer in answers:
		if answer[-1].hwsrc not in [i['MAC'] for i in devices]:
			devices.append({'IP':answer[-1].psrc, 'MAC':answer[-1].hwsrc})

	with open('macs.txt', 'r', encoding="utf8") as f:
		for i in f.readlines():
			if len(i) > 3:
				mac_lst.append({'MAC':i[:9], 'Vendor':i[9:].rstrip("\n")})

	for index, device in enumerate(devices):
		for mac_vendor in mac_lst:
			if mac_vendor['MAC'][0:8].lower() == device['MAC'][0:8]:
				devices[index]['Vendor'] = mac_vendor['Vendor']
				break
		if len(devices[index]) == 2:
			devices[index]['Vendor'] = 'Unknown'
	return devices


def method_one():
	global devices
	clear()
	header()
	printed = []
	while 1:
		sleep(1)
		devices = getter()
		for device in devices:
			if device not in printed:
				printed.append(device)
				print(device['IP'] + "\t\t" + device['MAC'] + "\t\t" + device['Vendor'])


def method_two():
	global devices
	devices = getter()
	clear()
	header()
	for device in devices:
		print(device['IP'] + "\t\t" + device['MAC'] + "\t\t" + device['Vendor'])
	sleep(3.3)


def main():
	global devices
	devices = []
	clear()
	module_settings()

	if not live:
		method_one()
	elif live:
		while 1:
			method_two()


if __name__ == "__main__":
	print("Please wait...")

	import sys
	import os
	from time import sleep

	import scapy.all as scapy
	import argparse

	main()
