set PM=C:\Users\WDAGUtilityAccount\Desktop\ProcessMonitor\procmon.exe
start %PM% /AcceptEula /quiet /minimized
%PM% /waitforidle /AcceptEula
start /wait notepad.exe
%PM% /terminate /AcceptEula