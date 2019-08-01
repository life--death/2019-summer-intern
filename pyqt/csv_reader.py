import csv

#This is an easy to use tool cooperate using with the record from process monitor
#Which take the .csv record which filtered already output a readable txt to show the process tree

class information():
    def __init__(self, process_name=None,pid=None, operation=None, path=None, result=None, detail=None):
        self.name = process_name
        self.pid = pid
        self.job = operation
        self.path = path
        self.result = result
        self.detail = detail
    
class process():
    def __init__(self,name = None, father = None,pid = None,father_pid = None):
        self.name = name
        self.pid = pid
        self.father = father
        self.father_pid= father_pid
        

class node():
    def __init__(self,process_name,pid):
        self.name = process_name
        self.pid = pid
        self.child = set()
    def BFS(self,pid:str):
        mem = list()
        mem.append(self)
        while len(mem) != 0:
            if mem[0].pid != pid:
                mem = mem + list(mem[0].child)
                mem.pop(0)
            else:
                return mem[0]
        return -1
    def BFS_name(self,name:str):
        mem = list()
        mem.append(self)
        while len(mem) != 0:
            if mem[0].name != name:
                mem = mem + list(mem[0].child)
                mem.pop(0)
            else:
                return mem[0]
        return -1
    def find(self,pid:str):
        if self.BFS(pid) != -1:
            return True
        else:
            return False
    def add_node(self,process:str,pid:str,father_pid:str):
        process = node(process,pid)
        target = self.BFS(father_pid)
        if target != -1:
            target.child.add(process)

def reader(name:str):
    #row 2 里的内容需要拆解 2  PM","Explorer.EXE","3448","RegCreateKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModel\StateRepository\Cache\Metadata","SUCCESS","Desired
    result = []
    with open(name, newline='',encoding="UTF-8") as csvfile:
        temp = csv.reader(csvfile)
        for row in temp:
            #print(len(row))
            #print(spliter(row[1]))
            #print("1 ",row[0],"2 ",row[1],"3 ",row[2],"4 ",row[3])
            result.append(information(row[1],row[2],row[3],row[4],row[5],row[6]))
    return result

def listfilter(target_list:list,name:str):
    result = []
    for event in target_list:
        if event.name == name:
            result.append(event)
    return result

def process_tool(target:information):
    father = target.name
    temp = target.path.split("\\")
    name = temp[-1]
    pid = target.detail.split(",")[0].split(": ")[1]
    father_pid = target.pid
    result = process(name,father,pid,father_pid)
    return result


def process_analysis_main(material:str):                                         #csv address
    templist = reader(material)
    templist.pop(0)
    root_list = []
    temp = process_tool(templist.pop(0))
    root_list.append(node(temp.father,temp.father_pid))
    root_list[0].add_node(temp.name,temp.pid,temp.father_pid)
    for element in templist:
        flag = 0
        temp = process_tool(element)
        for tree in root_list:
            if tree.find(temp.father_pid):
                tree.add_node(temp.name,temp.pid,temp.father_pid)
                flag = 1
                break
        if flag == 0:
            root = node(element.name,element.pid)
            root.add_node(temp.name,temp.pid,temp.father_pid)
            root_list.append(root)
    return root_list

def print_helper(target_list:list,helper=0): 
    for element in target_list:
        if len(element.child) != 0:
            result = open("C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\test.txt","a")                                         #txt address
            print("  "*helper + "|" + "--"*helper + element.name + "( pid: " + element.pid + " )")
            result.write("  "*helper + "|" + "--"*helper + element.name + "( pid: " + element.pid + " )\n")
            result.close()
            print_helper(element.child,helper + 1)
        else:
            result = open("C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\test.txt","a")                                         #txt address
            print("  "*helper + "|" + "--"*helper + element.name + "( pid: " + element.pid + " )")
            result.write("  "*helper + "|" + "--"*helper + element.name + "( pid: " + element.pid + " )\n")
            result.close()
            
def fake_main(name:str,material:str):
    templist = reader(material)
    templist = listfilter(templist,name)

def DFS_pid(root_node:node,result:list):
    result.append(root_node.pid)
    if len(root_node.child) != 0:
        for element in root_node.child:
            result = result + DFS_pid(element,result)
    return result

def find_main_tree(root_list:list,name:str):
    result = []
    for root in root_list:
        if root.BFS_name(name) != -1:
            result.append(root.BFS_name(name))
    return result

def write_action_analysis(info_list:list):
    result = open("C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\write_action_report.txt","w",encoding="UTF-8")  #地址
    result.write("the total write action that the process made is " + str(len(info_list)) +"\n")
    address_list = set()
    for info in info_list:
        temp_path = info.path
        temp_list = temp_path.split("\\")
        legal_path = ""
        for number in range(len(temp_list) - 1):
            legal_path = legal_path + temp_list[number] + "\\"
            address_list.add(legal_path)
    result.write("The write actions were happened here: \n")
    for address in address_list:
        result.write(address + "\n")
    result.close()

def write_reg_analysis(info_list:list):
    result = open("C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\write_reg_report.txt","w",encoding="UTF-8")  #地址
    result.write("the total write action that the process made is " + str(len(info_list)) +"\n")
    address_list = set()
    for info in info_list:
        temp_path = info.path
        temp_list = temp_path.split("\\")
        legal_path = ""
        for number in range(len(temp_list) - 1):
            legal_path = legal_path + temp_list[number] + "\\"
            address_list.add(legal_path)
    result.write("The write actions were happened here: \n")
    for address in address_list:
        result.write(address + "\n")
    result.close()

def tcp_connect_analysis(info_list:list):
    result = open("C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\tcp_report_report.txt","w",encoding="UTF-8")  #地址
    result.write("the total write action that the process made is " + str(len(info_list)) +"\n")
    address_list = set()
    for info in info_list:
        temp_path = info.path
        temp_list = temp_path.split("->")
        address_list.add(temp_list[1])
    result.write("The visit actions were happened here: \n")
    for address in address_list:
        result.write(address + "\n")
    result.close()

def analysis_main(material:str,name:str):
    filter_dict = {0:"write-action.pmc",1:"write-reg.pmc",2:"TCP-catch.pmc",3:"process-create.pmc"}
    signal = 111
    templist = process_analysis_main(material+"\\" +filter_dict[3]+".csv")
    templist = find_main_tree(templist,name)
    core_process = []
    for root in templist:
        core_process =DFS_pid(root,core_process)
    for number in range(3):
        with open(material+"\\" +filter_dict[number]+".csv", newline='',encoding="UTF-8") as csvfile:
            temp = csv.reader(csvfile)
            result =[]
            for row in temp:
                if row[2] in core_process:
                    result.append(information(row[1],row[2],row[3],row[4],row[5],row[6]))
            if number == 0:
                write_action_analysis(result)
            elif number == 1:
                write_reg_analysis(result)
            else:
                tcp_connect_analysis(result)    
    return 0
                    
# analysis_main('C:\\summer_camp\\2019-summer-intern\\lib_self\\pmc\\','netease.exe')
#至此数据处理完成，后面要对与细节（detail）和路径（path）进行分析
  
