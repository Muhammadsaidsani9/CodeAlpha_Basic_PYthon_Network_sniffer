from scapy.all import sniff, UDP, IP, TCP, Raw, ICMP, conf


def process_packet(packet):
	print("New packet")
	if not packet.haslayer(IP):
		print("Non-IP packet ignored")
		return

	source_ip = packet[IP].src
	destination_ip = packet[IP].dst
	
	print(f"source ip Address : {source_ip}")
	print(f"destination ip Address : {destination_ip}")
	
	protocol = "UNKNOWN"
	sourceport = "_"
	destinationport = "_"

	if packet.haslayer(TCP):
		protocol = "TCP"
		sourceport = packet[TCP].sport
		destinationport = packet[TCP].dport
		print(f"TCP source port: {sourceport}")
		print(f"TCP destination port: {destinationport}")
	elif packet.haslayer(UDP):
		protocol = "UDP"
		sourceport = packet[UDP].sport
		destinationport = packet[UDP].dport
		print(f"UDP source port : {sourceport}")
		print(f"UDP destination port : {destinationport}")
	elif packet.haslayer(ICMP):
		protocol = "ICMP"
		print("ICMP packet detected")
	
	print(f"protocol: {protocol}")

	if packet.haslayer(Raw):
		payload = packet[Raw].load
		print(f"payload: {payload[:50]!r}")


def CommandLinterface():
	print(f"Starting CLI sniffing on interface: {conf.iface}")
	try:
		sniff(iface=conf.iface, prn=process_packet, store=False)
	except KeyboardInterrupt:
		print("Sniffing stopped by user")


if __name__=="__main__":
	CommandLinterface()