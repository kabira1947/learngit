import subprocess

def change_mac(interface, new_mac):
    print("[+] Changing MAC for interface " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"]


options = getargumentsbyname()
change_mac(options.interface, options.new_mac)
