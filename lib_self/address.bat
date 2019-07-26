set PM=C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\lib_self\ProcessMonitor\procmon.exe
start %PM% /AcceptEula /quiet /minimized /backingfile C:\netease.exe.pml 
%PM%  /waitforidle /AcceptEula
start /wait C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\source\netease.exe
%PM% /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs C:\netease.exewrite-action.pmc.csv /Openlog C:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\lib_self\filter_library\write-action.pmc 
%PM% /minimized /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs C:\netease.exewrite-reg.pmc.csv /Openlog C:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\lib_self\filter_library\write-reg.pmc 
%PM% /minimized /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs C:\netease.exeTCP-catch.pmc.csv /Openlog C:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\lib_self\filter_library\TCP-catch.pmc 
%PM% /minimized /terminate /AcceptEula 
%PM% /SaveApplyFilter  /SaveAs C:\netease.exeprocess-create.pmc.csv /Openlog C:\netease.exe.pml /quiet /minimized /AcceptEula /LoadConfig C:\Users\WDAGUtilityAccount\Desktop\2019-summer-intern\lib_self\filter_library\process-create.pmc 
%PM% /minimized /terminate /AcceptEula 
