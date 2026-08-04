# from scapy.all import sniff

# print("Network Sniffer Started...")
# print("Waiting for packets...\n")

# packets = sniff(count=5)

# print("Packet Capture Completed!")
# print(f"Total Packets Captured: {len(packets)}")







# from scapy.all import sniff

# print("Network Sniffer Started...")
# print("Capturing Packets...\n")

# packets = sniff(count=5)

# print("\nCaptured Packets:\n")

# for packet in packets:

#     if packet.haslayer("IP"):

#         print("----------------------------------")
#         print("Source IP      :", packet["IP"].src)
#         print("Destination IP :", packet["IP"].dst)









# from scapy.all import sniff

# print("Network Sniffer Started...")
# print("Capturing Packets...\n")

# packets = sniff(count=5)

# print("\nCaptured Packets:\n")

# for packet in packets:

#     if packet.haslayer("IP"):

#         protocol = "Other"

#         if packet.haslayer("TCP"):
#             protocol = "TCP"

#         elif packet.haslayer("UDP"):
#             protocol = "UDP"

#         elif packet.haslayer("ICMP"):
#             protocol = "ICMP"

#         print("--------------------------------------")
#         print("Source IP      :", packet["IP"].src)
#         print("Destination IP :", packet["IP"].dst)
#         print("Protocol       :", protocol)







# from scapy.all import sniff

# print("Network Sniffer Started...")
# print("Capturing Packets...\n")

# packets = sniff(count=5)

# print("\nCaptured Packets:\n")

# for packet in packets:

#     if packet.haslayer("IP"):

#         protocol = "Other"

#         if packet.haslayer("TCP"):
#             protocol = "TCP"

#         elif packet.haslayer("UDP"):
#             protocol = "UDP"

#         elif packet.haslayer("ICMP"):
#             protocol = "ICMP"

#         if packet.payload:
#             payload = str(packet.payload)
#         else:
#             payload = "No Payload"

#         print("----------------------------------------")
#         print("Source IP      :", packet["IP"].src)
#         print("Destination IP :", packet["IP"].dst)
#         print("Protocol       :", protocol)
#         print("Payload        :", payload)



# create a function 


from scapy.all import sniff
from datetime import datetime

def detect_protocol(packet):

    if packet.haslayer("TCP"):
        return "TCP"

    elif packet.haslayer("UDP"):
        return "UDP"

    elif packet.haslayer("ICMP"):
        return "ICMP"

    return "Other"


def get_payload(packet):

    if packet.payload:
        return str(packet.payload)[:100]

    return "No Payload"


def display_packet(packet, index):

    print("\n" + "=" * 60)
    print(f"Packet #{index}")
    print("=" * 60)
    print("Time           :", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Source IP      :", packet["IP"].src)
    print("Destination IP :", packet["IP"].dst)
    print("Protocol       :", detect_protocol(packet))
    print("Payload        :", get_payload(packet))

print("=" * 60)
print("         BASIC NETWORK SNIFFER")
print("=" * 60)
print("Project   : CodeAlpha Cyber Security Internship")
print("Developer : Ankit Shivhare")
print("Status    : Capturing Live Network Packets")
print("=" * 60)

print("\nNetwork Sniffer Started...")
print("Capturing Packets...\n")

packets = sniff(count=10)

tcp_count = 0
udp_count = 0
icmp_count = 0

for index, packet in enumerate(packets, start=1):

    if packet.haslayer("IP"):

        protocol = detect_protocol(packet)

        if protocol == "TCP":
            tcp_count += 1

        elif protocol == "UDP":
             udp_count += 1

        elif protocol == "ICMP":
             icmp_count += 1
        display_packet(packet, index)
print("\n" + "=" * 60)
print("CAPTURE SUMMARY")
print("=" * 60)
print(f"Total Packets Captured : {len(packets)}")
print(f"TCP Packets            : {tcp_count}")
print(f"UDP Packets            : {udp_count}")
print(f"ICMP Packets           : {icmp_count}")
print("Status                 : Success")
print("=" * 60)

print("\nNetwork Sniffing Completed Successfully.")