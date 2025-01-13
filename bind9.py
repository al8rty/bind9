import os
import subprocess
import requests

def is_bind9_installed():
    try:
        subprocess.run(["dpkg", "-s", "bind9"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_bind9():
    if is_bind9_installed():
        print("bind9 is already installed.")
        return
    try: 
        print("Updating package list...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        print("Instlalling bind9...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "bind9"], check=True)

        print("bind9 installed successfully.")

def download_config(url, output_path):
    try:
        print("Downloading configuration file...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(output_path, 'w') as file:
            file.write(response.text)
        print(f"Configuration file downloaded to {output_path}")
    
    except Exception as E:
        print(f"Error donloading configuration file: {E}")
        exit(1)

def confirm_bind9():
    if not is_bind9_installed():
        print("bind9 is not installed. Installing now...")
        install_bind9()

    config_url = "https://github.com/al8rty/bind9.git"
    config_path = "/etc/bind/"

    download_config(config_url, config_url)

    try:
        subprocess.run(["sudo", "systemctl", "restart", "bind9"], check=True)
        print("bind9 configured and restarted successfully.")
    except subprocess.CalledProcessError as g:
        print(f"Error restarting bind9: {g}")

if __name__ == "__main__":
    if os.geteuid() !=0:
        print("This script requires superuser privileges. Pleace run as root or use sudo.")
    else:
        confirm_bind9()

