set PM=C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\lib_self\ProcessMonitor\procmon.exe
start %PM% /AcceptEula /quiet /minimized
%PM% /waitforidle /AcceptEula
start /wait notepad.exe
%PM% /terminate /AcceptEula