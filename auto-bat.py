def xml_out(req:int,address:str):
    name = address.split("\\")[-1]
    filter_dict = {0:"write-action.pmc",1:"write-reg.pmc",2:"TCP-catch.pmc",3:"process-create.pmc"}
    new_file = open("C:\\address.bat","w")
    new_file.write("set PM=C:\\Users\\WDAGUtilityAccount\\Desktop\\ProcessMonitor\\procmon.exe\n")
    new_file.write("start %PM% /AcceptEula /quiet /minimized /backingfile C:\\" + name +".pml \n")
    new_file.write("%PM%  /waitforidle /AcceptEula\n")
    new_file.write("start /wait "+ address + "\n")
    new_file.write("%PM% /terminate /AcceptEula \n")
    for temp in range(4):
        if req[temp] == 1:
            new_file.write("%PM% /SaveApplyFilter  /SaveAs C:\\" + name + filter_dict[temp] +".csv " + "/Openlog C:\\" + name + ".pml " +  "/quiet /minimized /AcceptEula /LoadConfig C:\\Users\\WDAGUtilityAccount\\Desktop\\"  + filter_dict[temp] + " \n")
            new_file.write("%PM% /minimized /terminate /AcceptEula \n")
            new_file.close() 
