import subprocess as sp
import time

output = []
proc = sp.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
	'GET-WMIOBJECT -Class Win32_ComputerSystem -Computer',
	'"localhost"',
	'|  select-Object Username'],
	stdout = sp.PIPE)
# output = proc.communicate()
time.sleep(3)
proc.kill()
output = proc.communicate()
print(output)
#print(Strip(proc.communicate()))


