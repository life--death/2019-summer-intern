set PM=C:\Users\WDAGUtilityAccount\Desktop\ProcessMonitor\procmon.exe
start %PM% /AcceptEula /quiet /minimized /backingfile C:\notepad.exe.pml 
%PM%  /waitforidle /AcceptEula
start /wait notepad.exe
%PM% /terminate /AcceptEula
%PM% /SaveApplyFilter /SaveAs1 C:\notepad-write-reg.exe.xml /Openlog C:\notepad.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\Users\WDAGUtilityAccount\Desktop\write-reg.pmc
%PM% /minimized /terminate /AcceptEula
%PM% /SaveApplyFilter /SaveAs1 C:\notepad1.exe.xml /Openlog C:\notepad.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\Users\WDAGUtilityAccount\Desktop\empty.pmc
%PM1% /minimized /terminate /AcceptEula 
