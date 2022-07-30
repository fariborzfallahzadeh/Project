import telnetlib
import time

IP = "192.168.2.240"
USERNAME = "admin"
PASSWORD = "cisco"
ENABLE_PASS = "cisco"

telnet = telnetlib.Telnet(IP)
telnet.read_until("Username: ".encode())
time.sleep(2)
telnet.write(USERNAME.encode() + "\n".encode())
time.sleep(3)
telnet.read_until("Password: ".encode())
telnet.write(PASSWORD.encode() + "\n".encode())
time.sleep(1)
telnet.write("en\n".encode())
time.sleep(1)
telnet.write(ENABLE_PASS.encode() + "\n".encode())
time.sleep(1)
telnet.write("conf t\n".encode())
time.sleep(1)
telnet.write("int range ethernet 0/1 - 3\n".encode())
time.sleep(1)
telnet.write("switchport mode access\n".encode())
time.sleep(1)
telnet.write("switchport access vlan 2\n".encode())
time.sleep(1)
telnet.write("end\n".encode())
time.sleep(1)
telnet.write("exit\n".encode())


