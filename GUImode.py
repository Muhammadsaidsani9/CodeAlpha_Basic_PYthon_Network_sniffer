import tkinter as tk
from tkinter import ttk,messagebox
from scapy.all import sniff, UDP, IP, TCP, ICMP, conf
import threading






def process_packet(packet,packet_table, root):
	
	if not packet.haslayer(IP):
			
		return
	
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
	root.after(0, lambda:
						packet_table.insert("",tk.END,	
													values=(src , dst, protocol, sport, dport)))

def GraphicalUinterface():
	print("start in gui")
	Sniffing = False
	root=tk.Tk()	
	root.title("PYthon GUI network ")
	root.geometry("900x500")

	columns=("source ip", "Destination ip", "protocol", "src port", "dst port")
	packet_table=ttk.Treeview(root, columns=columns, show="headings")

	for col in columns:
		packet_table.heading(col,text=col)
		packet_table.column(col,width=150)

	packet_table.pack(fill=tk.BOTH, expand=True)

	status_label = tk.Label(root, text="Status: stopped", anchor="w")
	status_label.pack(fill=tk.X, padx=5, pady=(0, 5))

	def startsniffing():
		nonlocal Sniffing 
		Sniffing = True
		try:
			ssniff = sniff(iface=conf.iface,
				prn=lambda P: process_packet(P, packet_table, root),
				store=False,
				stop_filter=lambda x: not Sniffing)
		except Exception as e:
			root.after(0, lambda: messagebox.showerror("error", f"sniffing failed {e}"))

	def run_sniffer():
		nonlocal Sniffing
		if Sniffing:
			return 
		thread=threading.Thread(target=startsniffing, daemon=True)	
		thread.start()
		start_btn.config(state="disabled",text="sniffing")
		stop_btn.config(state="normal")
		status_label.config(text="Status: sniffing")
	


		
		
	def stop_sniffer():
		nonlocal Sniffing
		Sniffing= False
		start_btn.config(state="normal",text="start sniffing")
		stop_btn.config(state="disabled")
		status_label.config(text="Status: stopped")


	start_btn=tk.Button(root, text="Start sniffing",command=run_sniffer)
	start_btn.pack(pady=5)

	stop_btn=tk.Button(root, text="Stop sniffing",command=stop_sniffer)
	stop_btn.pack(pady=5)
	stop_btn.config(state="disabled")

	def stop_and_exit():
		stop_sniffer()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", stop_and_exit)

	root.mainloop()
if __name__=="__main__":
	GraphicalUinterface()
		
					