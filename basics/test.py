show_arp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.10.20.48             -   0050.56bb.e99c  ARPA   GigabitEthernet1
Internet  10.10.20.200           14   0050.56bb.8be2  ARPA   GigabitEthernet1
Internet  10.10.20.254            0   0896.ad9e.444c  ARPA   GigabitEthernet1
"""

arp_table = dict()
for arp_line in show_arp.splitlines():
    #print(f"{arp_line}\n")
    arp_line_strip = arp_line.strip()
    print(arp_line_strip)