set PM=C:\ProcessMonitor\procmon.exe
start %PM% /AcceptEula /quiet /minimized /backingfile c:\netease.exe.pml 
%PM%  /waitforidle /AcceptEula
start /wait C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\source\netease.exe
%PM% /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs c:\write-action.pmc.csv /Openlog c:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\write-action.pmc 
%PM% /minimized /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs c:\write-reg.pmc.csv /Openlog c:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\write-reg.pmc 
%PM% /minimized /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs c:\TCP-catch.pmc.csv /Openlog c:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\TCP-catch.pmc 
%PM% /minimized /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs c:\process-create.pmc.csv /Openlog c:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\process-create.pmc 
%PM% /minimized /terminate /AcceptEula 
exit