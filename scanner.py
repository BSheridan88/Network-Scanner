import socket
class HostScanner:
    def ping(self,ip):
        if 7 <= len(ip) <= 15:
            return True
            #possible ip range
        else:
            return False
class Port_Scanner:
    def __init__(self):
        self.detector = Service_Detector()

    def scan(self,ip,port):
        print()

    def scan_range(self,ip,start_port,end_port):
        print()
        current_port = ""
        #go through all ips from start to end
        self.scan(ip,current_port)

class Service_Detector:
    def __init__(self):
        self.services = {}

    def lookup(self,port):
        print()

