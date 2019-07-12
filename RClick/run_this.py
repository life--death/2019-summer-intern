import sys,shutil,os
for i in range(1,len(sys.argv)):
    s=str(sys.argv[i])
    # print(s)
    ss=s.strip().split("\\")[-1]
    if os.path.exists(s):
        res=shutil.copy(s,f'C:\summer_camp\source\\{ss}')
    # print(res)
    # os.system("pause")
