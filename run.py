import os,sys
if sys.version[0:3]=="3.9":
	os.system("python 39.py")
elif sys.version[0:3]=="3.8":
	os.system("python 38.py")
elif sys.version[0:3]=="2.7" or sys.version[0:3]=="2.8":
	exit("[!] Gunakan Python Versi 3")
else:
	exit("[!] Versi Python Yang Lu Miliki Gak Support")