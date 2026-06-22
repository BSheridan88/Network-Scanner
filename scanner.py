import socket
class HostScanner:
    def ping(self,ip):
        if 7 <= len(ip) <= 15:
            print()
            #possible ip range
        else:
            print("Invalid IP Format")
            print("IP Is Either Too Long Or Too Short")


class Port_Scanner:
    def __init__(self):
        self.detector = Service_Detector()

    def scan(self,ip,port):
        print()

    def scan_range(self,ip,start_port,end_port):
        print()

class Service_Detector:
    def __init__(self):
        self.services = {}

    def lookup(self,port):
        print()

