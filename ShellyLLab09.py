
# Lab 09 - Socket Functions
# Name: Luke Shelly

import socket


class SocketTools:

    def GetServByPort(self, port):
        """Finds the service name for a port number."""
        return socket.getservbyport(port)

    def GetHostName(self):
        """Gets the computer name."""
        return socket.gethostname()

    def GetHostByName(self, hostname):
        """Gets the IP address of a hostname."""
        return socket.gethostbyname(hostname)

    def GetFQDN(self, hostname):
        """Gets the full domain name."""
        return socket.getfqdn(hostname)

    def GetAddressInfo(self, hostname):
        """Gets address information for a hostname."""
        return socket.getaddrinfo(hostname, 80)

    def ConvertIP(self, ip):
        """Converts an IPv4 address into bytes."""
        socket.inet_aton(ip)
        return socket.inet_aton(ip)


# Driver functions

def RunServByPort(tools):
    try:
        print("Service:", tools.GetServByPort(80))
    except OSError as error:
        print("Error:", error)


def RunHostName(tools):
    try:
        print("Computer name:", tools.GetHostName())
    except OSError as error:
        print("Error:", error)


def RunHostByName(tools):
    try:
        print("IP address:", tools.GetHostByName("google.com"))
    except OSError as error:
        print("Error:", error)


def RunFQDN(tools):
    try:
        print("Full domain name:", tools.GetFQDN("google.com"))
    except OSError as error:
        print("Error:", error)


def RunAddressInfo(tools):
    try:
        results = tools.GetAddressInfo("google.com")
        print("Address information:")
        for result in results[:3]:
            print(result)
    except OSError as error:
        print("Error:", error)


def RunConvertIP(tools):
    try:
        print("Packed IP:", tools.ConvertIP("8.8.8.8"))
    except OSError as error:
        print("Error:", error)


def main():
    tools = SocketTools()

    while True:
        print("\n===== SOCKET MENU =====")
        print("1. Get service by port")
        print("2. Get computer name")
        print("3. Get IP address")
        print("4. Get full domain name")
        print("5. Get address information")
        print("6. Convert IP address")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            RunServByPort(tools)
        elif choice == "2":
            RunHostName(tools)
        elif choice == "3":
            RunHostByName(tools)
        elif choice == "4":
            RunFQDN(tools)
        elif choice == "5":
            RunAddressInfo(tools)
        elif choice == "6":
            RunConvertIP(tools)
        elif choice == "7":
            print("Program finished.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
