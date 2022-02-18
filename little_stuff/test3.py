from scapy.all import *

# print(sr1(IP(dst="192.168.95.155")/ICMP(), timeout=2).summary())
# print(sr(IP(dst="192.168.95.155")/ICMP(), timeout=2))
# print(sr(IP(dst="192.168.95.153")/ICMP(), timeout=2))


# for ip in range(152,154):
#      DST = "192.168.95." + str(ip)
#      print({DST})
#      ans, unans = sr(IP(dst=DST)/ICMP(), retry=0, timeout=1)
#      if DST in ans:
#           print("Alive")
#      else:
#           print("Dead")


# for ip in range(152,154):
#      DST = "192.168.95." + str(ip)
#      print(DST)

scan_hosts = "192.168.95.153"
inactive_hosts = []
active_hosts = []
try:
        ans, unans = sr(IP(dst=scan_hosts)/ICMP(), retry=0, timeout=1)
        for inactive in unans:
          #   print ("%s is inactive" %inactive.dst)
            inactive_hosts.append(inactive)
        for active in ans:
          #    print ("%s is active" %active.dst)
             active_hosts.append(active)

        
        print ("Total %d hosts are inactive" %(len(inactive_hosts)))
        print(f"inactive {inactive_hosts}")
        print ("Total %d hosts are active" %(len(active_hosts)))
        print(f"active{active_hosts}")
             
            
        
except KeyboardInterrupt:
     exit(0) 

print( "192.168.95.153" in ans) 
