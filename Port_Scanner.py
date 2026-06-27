from scanner import *
from utils import *

def main():

    host = HostScanner()
    port = Port_Scanner
    logs = Logger()
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
            print("4. Save Results")
            print("5. Exit Dashboard")
            choice = int(input(""))

            try:
                if choice == 1:
                    port = int(input("What Port Would You Like To Scan"))
                    report = port.scan(ip,port)
                    logs.log(report) # add this to all so data can be saved
                    print(f'Report for {port}: {report}')
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    output_file = input("What is the full file path of where you log saved:")
                    logs.save(output_file)
                elif choice == 5:
                    pass
                #find some way to check if log is empty and if they saved.
                #if not then prompt them to ask if they want to if no exit
                #if yes save then exit them
                else:
                    print("Invalid Number")
                    print("Please Select 1-4")
            except ValueError:
                print("Invalid Value")

        except TimeoutError:
            print("The Scan Timed Out")
        except OSError:
            print("Network Error Occurred")





if __name__ == "__main__":
    main()