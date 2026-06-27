class Logger:
    def log(self,results):
        print()

    def save(self,file_name):
        try:
            with open(file_name, "w") as file:
                file.write() #log data
        except FileNotFoundError:
            print("Error: File not able to be found")




def validate_ip(ip):
    print() #check if ip is a real one

def generate_ip_range(start_ip,end_ip):
    print()