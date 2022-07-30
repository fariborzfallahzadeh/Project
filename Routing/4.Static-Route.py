import telnetlib
import time

IP = "192.168.2.201"
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
telnet.write("ip route 0.0.0.0 0.0.0.0 10.1.1.1\n".encode())
time.sleep(1)
telnet.write("end\n".encode())
time.sleep(1)
telnet.write("exit\n".encode())


