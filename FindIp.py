import subprocess as sp
import time

def Run_command(ip):
	output = []
	proc = sp.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
		'GET-WMIOBJECT -Class Win32_ComputerSystem -Computer',
		'"' + ip +'"',
		'|  select-Object Username'],
		stdout = sp.PIPE)
	time.sleep(3)
	proc.kill()
	output = proc.communicate()
	# print(output)
	return output
