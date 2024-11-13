import requests
import time
import sys
import pyfiglet
from urllib.parse import urlparse
from colorama import init, Fore
import socket
from datetime import datetime

init(autoreset=True)

def get_user_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException:
        return "Unavailable"

def check_website(website, status_dict, user_ip, save_file=None):
    try:
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Make the HTTP request to check the website status
        response = requests.get(website, timeout=1)
        
        # Get the destination IP address
        dst_ip = socket.gethostbyname(urlparse(website).hostname)
        
        # Display the formatted output with time, URL, status, code, and IPs
        if response.status_code == 200:
            status_dict["UP"] += 1
            output = f"{current_time} | {website} | {Fore.GREEN}UP | {response.status_code} | SrcIP: {user_ip} | DstIP: {dst_ip}"
            print(output)
            
            # Save output if requested
            if save_file:
                with open(save_file, "a") as file:
                    file.write(output + "\n")
        else:
            status_dict["DOWN"] += 1
            print(f"{current_time} | {website} | {Fore.RED}DOWN | {response.status_code} | SrcIP: {user_ip} | DstIP: {dst_ip}")
    except requests.RequestException as e:
        dst_ip = "Unavailable"
        status_dict["ERROR"] += 1
        print(f"{current_time} | {website} | {Fore.YELLOW}ERROR | {str(e)} | SrcIP: {user_ip} | DstIP: {dst_ip}")

def safe_input(prompt):
    return input(prompt).encode(sys.stdin.encoding, errors='replace').decode('utf-8', errors='replace')

def read_websites_from_file(filename):
    try:
        with open(filename, 'r') as file:
            websites = file.readlines()
        return [url.strip() for url in websites]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []

def print_summary(status_dict):
    print("\nSummary:")
    print(f"{Fore.GREEN}UP: {status_dict['UP']}")
    print(f"{Fore.RED}DOWN: {status_dict['DOWN']}")
    print(f"{Fore.YELLOW}ERROR: {status_dict['ERROR']}")

def main():
    # Display the header
    header = pyfiglet.figlet_format("UpRobot")
    print(header)
    
    # Tool description and credits
    print("====================================================")
    print(Fore.CYAN + "Website Monitoring Tool - Check the UP/DOWN status of websites.")
    print("====================================================")
    print("Tool created by Yahya El Ourdighi")
    print("https://www.linkedin.com/in/yahya-el-ourdighi-175028244/")
    print("https://github.com/yahyaelourdighi\n")
    
    choice = safe_input("Input websites manually or from a file? (manual/file): ").lower().strip()

    if choice == "file":
        filename = safe_input("Enter file name with URLs: ").strip()
        websites = read_websites_from_file(filename)
        if not websites:
            print("No websites found in the file.")
            return
    elif choice == "manual":
        websites_input = safe_input("Enter websites to monitor (comma-separated): ").split(',')
        websites = [url.strip() for url in websites_input]
    else:
        print("Invalid input. Exiting...")
        return

    for i in range(len(websites)):
        if not urlparse(websites[i]).scheme:
            websites[i] = 'https://' + websites[i]

    scan_speed = safe_input("Choose scan speed (fast/slow): ").lower().strip()
    delay = 0.3 if scan_speed == "fast" else 1

    # Ask if the user wants to save "UP" statuses to a file
    save_up_only = safe_input("Save only 'UP' statuses to a file? (yes/no): ").lower().strip()
    save_file = None
    if save_up_only == "yes":
        save_file = safe_input("Enter file name to save 'UP' statuses: ").strip()

    user_ip = get_user_ip()
    status_dict = {"UP": 0, "DOWN": 0, "ERROR": 0}

    print("\nStarting website monitoring...")

    for website in websites:
        check_website(website, status_dict, user_ip, save_file)
        time.sleep(delay)

    print_summary(status_dict)

if __name__ == "__main__":
    main()

