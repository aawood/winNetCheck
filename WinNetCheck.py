from windows_toasts import WindowsToaster, ToastText1
import requests
import socket
import time
import yaml

wintoaster = WindowsToaster('Python')
newToast = ToastText1()

with open('settings.yml', 'r') as file:
    settings = yaml.safe_load(file)

def toast(message):
    if settings['active'] == True:
        newToast = ToastText1()
        newToast.SetBody(message)
        wintoaster.show_toast(newToast)
    else:
        print(message)

def main():
    time.sleep(settings['startDelay'])
    faults = 0
    
    # Check for servers off network
    for serverIP in open(settings['serverFile'], "r"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((serverIP.strip('\n'), 80))

        if result != 0:
            toast(serverIP.strip('\n') + " is not on the network.")
            faults = 1

    # Check if External IP has changed
    with open(settings['externalIPFile']) as f:
        expectedExtIP = f.readline().strip('\n')

    actualExtIP = requests.get('https://api.ipify.org')

    if actualExtIP.text != expectedExtIP:
        toast("IP Changed.\nExpected IP: " + expectedExtIP + "\nCurrent IP: " + actualExtIP.text)
        faults = 1

    # If no issues found, send alert
    if faults == 0:
        toast("No server issues detected.")

main()
