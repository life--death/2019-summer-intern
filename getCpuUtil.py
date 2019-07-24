import logging
import psutil
import time

# while(True):
cpu=psutil.cpu_percent(interval=0.5,percpu=False)
memory=psutil.virtual_memory().percent
t=time.time()
# print('time',t,'cpu:',cpu,'memory:',memory)
with open('C:\\Users\\WDAGUtilityAccount\\Desktop\\2019-summer-intern\\cpu_util.txt','a') as f:
    f.write(f'{t} {cpu} {memory}\n')



# ##设置一个日志输出文件
# # log_filename = "logging.txt"
#
# # 设置日志输出格式
# # log_format = ' [%(asctime)s]   %(message)s'
#
# # 日志文件基本设置
# # logging.basicConfig(format=log_format, datafmt='%Y-%m-%d %H:%M:%S %p', level=logging.DEBUG, filename=log_filename, filemode='w')
#
# # logging.debug('日志输出! ')
#
# # 获取当前运行的pid
# p1 = psutil.Process(os.getpid())
#
# # 打印本机的内存信息
# print('直接打印内存占用： ' + (str)(psutil.virtual_memory))
#
# # 打印内存的占用率
# print('获取内存占用率： ' + (str)(psutil.virtual_memory().percent) + '%')
#
# # 本机cpu的总占用率
# print('打印本机cpu占用率： ' + (str)(psutil.cpu_percent(0)) + '%')
#
# # 该进程所占cpu的使用率
# print(" 打印该进程CPU占用率: " + (str)(p1.cpu_percent(None)) + "%")
#
# # 直接打印进程所占内存占用率
# print(p1.memory_percent)
#
# # 格式化后显示的进程内存占用率
# print("percent: %.2f%%" % (p1.memory_percent()))
#
