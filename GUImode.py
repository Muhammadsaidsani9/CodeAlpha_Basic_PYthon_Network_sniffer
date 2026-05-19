import tkinter as tk
from tkinter import ttk
from scapy.all import sniff, UDP, IP, TCP, Raw, ICMP, conf
import threading

Sniffing = False

def process_packet(packet):
	print("new packet")
	if packet.haslayer(IP):

		src=packet[IP].src
		dst=packet[IP].dst

		protocol="others"
		sport="_"
		dport="_"
	
		if packet.haslayer(TCP):
				
				protocol="TCP"
				sport= packet[TCP].sport
				dport=packet[TCP].dport
			
		elif packet.haslayer(UDP):
			
			protocol="UDP"
			sport=packet[UDP].sport
			dport=packet[UDP].dport
		elif packet.haslayer(ICMP):
			protocol="ICMP"
		packet_table.insert("",tk.END,	values=(src , dst, protocol, sport, dport))

def startsniffing():
	 
 global Sniffing
Sniffing = True 
sniff(prn=process_packet, store=False, stop_filter=lambda x:not Sniffing)

def run_sniffer():
	thread=threading.Thread(target=startsniffing)	
	thread.daemon=True
	thread.start()

def stop_sniffer():
	 global Sniffing
Sniffing= False

root=tk.Tk()	
root.title("PYthon GUI network ")
root.geometry("900x500")
start_btn=tk.Button(root, text="startsniffing",command=run_sniffer)
start_btn.pack(pady=5)

stop_btn=tk.Button(root, text="stopsniffer",command=stop_sniffer)

start_btn.pack(pady=5)
columns=("source ip", "Destination ip", "protocol", "src port", "dst port")
packet_table=ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
	packet_table.heading(col,text=col)
	packet_table.column(col,width=150)
packet_table.pack(fill=tk.BOTH, expand=True)
root.mainloop()
			