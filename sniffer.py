# import sniff, IP, UDP , TCP from scapy
from scapy.all import sniff , IP , UDP , TCP
import datetime
def process_packet(packet): # define function
  if packet.haslayer(IP):   #checks if packet has an IP layer
    ip = packet[IP]
    
    if packet.haslayer(TCP):  #checks if the protocol is tcp and add source and destination for the same
      tcp = packet[TCP]
      time = datetime.datetime.now().strftime("%H:%M:%S")
      output = f"[{time}] [TCP] {ip.src}:{tcp.sport} -> {ip.dst}:{tcp.dport}"
      print(output)

      #store data in a file
      with open("packets.txt", "a") as f:
        f.write(output + "\n")

    elif packet.haslayer(UDP): #checks if the protocol is udp and add source and destination for the same
      udp = packet[UDP]
      time = datetime.datetime.now().strftime("%H:%M:%S")
      output = f"[{time}] [UDP] {ip.src}:{udp.sport} -> {ip.dst}:{udp.dport}"
      print(output)

      #store data in a file
      with open("packets.txt", "a") as f:
        f.write(output + "\n")

sniff(prn=process_packet,filter="tcp", count = 10)  #core engine. for every packet captured you pass this function. count tell the no. of packets to capture