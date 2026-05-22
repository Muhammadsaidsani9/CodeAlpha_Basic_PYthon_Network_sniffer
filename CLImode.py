
from scapy.all import sniff, UDP, IP, TCP, Raw, ICMP, conf


def process_packet(packet,):
	print("new packet")
	if packet.haslayer(IP):

		sourceIP=packet[IP].src
		destinationIP=packet[IP].dst
		
		print(f"source ip Address : {sourceIP}")
		print(f"destination ip Address : {destinationIP}")
		
		if packet.haslayer(TCP):
				
				protocol="TCP"
				sourceport= packet[TCP].sport
				destinationport=packet[TCP].dport
				print(f"TCP source port: {sourceport}")
				print(f"TCP destination port: {destinationport}")

		elif packet.haslayer(UDP):
			
			protocol="UDP"
			sourceport=packet[UDP].sport
			destinationport=packet[UDP].dport
			print(f"UDP source port : {sourceport}")
			print(f"UDP destination port : {destinationport}")
	if packet.haslayer(Raw):
		payload=packet[Raw].load
		print(f"payload:{payload[:50]}")

def CommandLinterface():
	try:
		sniff( iface=conf.iface, prn=process_packet, store=False)
	except KeyboardInterrupt:
		print("sniffing is stop by user")
if __name__=="__main__":
	CommandLinterface()