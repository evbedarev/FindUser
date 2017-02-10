# import subprocess as sp
# import time
# def Run_command(ip):
# 	output = []
# 	proc = sp.Popen([r'C:\Windows\System32\cmd.exe',
# 		' WMIC /NODE:',
# 		'"' + ip + '"',
# 		' COMPUTERSYSTEM GET USERNAME'],
# 		stdout = sp.PIPE)
# 	time.sleep(3)
# 	proc.kill()
# 	output = proc.communicate()
# 	print(output)
# 	string = output[0].decode('utf-8')
# 	string = string[string.find("SBT"):string.find("SBT")+40]
# 	return string
# Run_command("127.0.0.1")

import wmi

c = wmi.WMI('172.29.96.35')
for process in c.Win32_Process(name='explorer.exe'):
	print (process.GetOwner())