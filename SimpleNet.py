import socket

# SimpleNet
# It 's a simple list of tools for network
# That is just the start of the project
# -------------------------------------------

def getHostname():
    print("Hostname : ", socket.gethostname())
    return socket.gethostname()

def getNameFromHost():
    print("Address : ", socket.gethostbyname(socket.gethostname()))
    return socket.gethostbyname(socket.gethostname())

def getAddrInfo(port):
    print("Info : ", socket.getaddrinfo(socket.gethostname(), port, 0, 0, 0, 0))
    return socket.getaddrinfo(socket.gethostname(), port, 0, 0, 0, 0)

def menu():
    print("""
   _____   _                       _          _   _          _   
  / ____| (_)                     | |        | \ | |        | |  
 | (___    _   _ __ ___    _ __   | |   ___  |  \| |   ___  | |_ 
  \___ \  | | | '_ ` _ \  | '_ \  | |  / _ \ | . ` |  / _ \ | __|
  ____) | | | | | | | | | | |_) | | | |  __/ | |\  | |  __/ | |_ 
 |_____/  |_| |_| |_| |_| | .__/  |_|  \___| |_| \_|  \___|  \__|
                          | |                                    
                          |_|                                    

Simple Network Tools

1. Hostname
2. Name form host
3. Address info

-------------------------------------------------------------------------------
""")

    opt = input("OPTION --> ")

    if(opt == "1"):
        getHostname()
        input("PRESS ANY KEY . . .")
        menu()
    if(opt == "2"):
        getNameFromHost()
        input("PRESS ANY KEY . . .")
        menu()
    if(opt == "3"):
        port = int(input("PORT --> "))
        getAddrInfo(port)
        input("PRESS ANY KEY . . .")
        menu()

menu()
