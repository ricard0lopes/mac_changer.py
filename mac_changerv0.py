#!usr/bin/env python

import subprocess


subprocess.call(["ifconfig", "eth0", "down"])
subprocess.call(["ifconfig", "eth0", "hw", "ether", "00:11:22:33:44:44"])
subprocess.call(["ifconfig", "eth0", "up"])
subprocess.call(["ifconfig"])