

import subprocess
import re
import sys

interface = None
new_mac = None

def get_logic():
    global interface
    global new_mac
    
    interface = raw_input("Add interface ")
    interface_search_result = re.search(r"\W", interface)
    print(interface_search_result)
    
    if interface_search_result is None:
        pass
    else:
        print("Illegal character used")
        sys.exit()
    
    new_mac = raw_input("Add new MAC address ")
    
    
    return interface, new_mac


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


get_logic()
current_mac = get_current_mac(interface)
print("Current MAC = " + str(current_mac))

change_mac(interface, new_mac)
