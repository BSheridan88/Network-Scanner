from scanner import *
from utils import *

def main():

    host = HostScanner()
    port = Port_Scanner
    print()
    ip = input("Enter your IP: ")
    valid_ip = validate_ip(ip)
    if valid_ip == False:
        print("Invalid IP Format")
        print("IP Is Either Too Long Or Too Short")
        eligible = False
    else:
        print("valid ip")
        eligible = True

    if eligible == True:
        try:
            print("Network Scanner Dashboard")
            print("1. Scan Port")
            print("2. Scan Range of Ports")
            print("3. Lookup Port")
            print("4. Exit Dashboard")
            choice = int(input(""))

            try:
                if choice == 1:
                    port = int(input("What Port Would You Like To Scan"))
                    report = port.scan(ip,port)
                    print(f'Report for {port}: {report}')
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                else:
                    print("Invalid Number")
                    print("Please Select 1-4")
            except ValueError:
                print("Invalid Value")

        except TimeoutError:
            print("The Scan Timed Out")
        except OSError:
            print("Network Error Occured")





if __name__ == "__main__":
    main()