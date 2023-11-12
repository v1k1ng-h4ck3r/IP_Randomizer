import os
import time
import socket

def clear_screen():
    os.system('cls')

def get_ipv4_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def set_google_dns(interface_name):
    os.system(f'netsh interface ip set dns name="{interface_name}" static 8.8.8.8 primary')
    os.system(f'netsh interface ip add dns name="{interface_name}" 8.8.4.4 index=2')

def renew_ip():
    os.system('ipconfig /release')  # Release the current IP
    os.system('ipconfig /renew')  # Renew the IP

def main_menu():
    while True:
        clear_screen()
        print("IP Randomizer")
        time.sleep(1)
        print("A Global Bug Hunters Program")
        time.sleep(1)
        print(f"Your current IPv4 Address is: {get_ipv4_address()}")
        time.sleep(1)
        
        print("""
1) Change DNS to Google and Randomize IP Address
2) Exit
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            print("IP Randomizer")
            time.sleep(1)
            print("A Global Bug Hunters Program")
            time.sleep(1)
            print(f"Your current IPv4 Address is: {get_ipv4_address()}")
            time.sleep(1)
            interface_name = input("Please enter the name of the network interface (e.g., 'Wi-Fi'): ")
            print("Setting Google DNS servers...")
            set_google_dns(interface_name)
            print("Please wait while I randomize your IP Address...")
            renew_ip()
            print(f"Your new IPv4 Address is: {get_ipv4_address()}")
            input("Press ENTER to return to the main screen...")
        elif choice == '2':
            break

if __name__ == "__main__":
    main_menu()
