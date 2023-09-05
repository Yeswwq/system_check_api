<<<<<<< Updated upstream
import wmi
import re
w = wmi.WMI()

def ram_shuju():
    ram_zhuangtai = w.Win32_PhysicalMemory() #获取内存状态
    ram_guanjianzi = re.compile(r'(Physical Memory [0-9])') #建立正则表达式检测内存槽位
    ram_shaixuan = ram_guanjianzi.findall(str(ram_zhuangtai)) #根据规则筛选获取到的内存状态
    ram_shuliang = len(ram_shaixuan) #检查内存数量
    return ram_shuliang

def disk_shuju():
    disk_zhuangtai = w.Win32_DiskDrive()
    disk_guanjianzi = re.compile(r'(PHYSICALDRIVE[0-9])') #建立正则表达式检测硬盘数量
    disk_shaixuan = disk_guanjianzi.findall(str(disk_zhuangtai))
    disk_shuliang = len(disk_shaixuan)
    return disk_shuliang

def gpu_shuju():
    gpu_zhuangtai = w.Win32_VideoController()
    gpu_guangjianzi = re.compile(r'(VideoController[0-9])') #建立正则表达式检测显卡数量
    gpu_shaixuan = gpu_guangjianzi.findall(str(gpu_zhuangtai))
    gpu_shuliang = len(gpu_shaixuan)
    return gpu_shuliang

=======
import wmi
import re
from datetime import datetime
import socket
w = wmi.WMI()

def ram_shuju():
    ram_zhuangtai = w.Win32_PhysicalMemory() #获取内存状态
    ram_guanjianzi = re.compile(r'(Physical Memory [0-9])') #建立正则表达式检测内存槽位
    ram_shaixuan = ram_guanjianzi.findall(str(ram_zhuangtai)) #根据规则筛选获取到的内存状态
    ram_shuliang = len(ram_shaixuan) #检查内存数量
    return ram_shuliang

def disk_shuju():
    disk_zhuangtai = w.Win32_DiskDrive()
    disk_guanjianzi = re.compile(r'(PHYSICALDRIVE[0-9])') #建立正则表达式检测硬盘数量
    disk_shaixuan = disk_guanjianzi.findall(str(disk_zhuangtai))
    disk_shuliang = len(disk_shaixuan)
    return disk_shuliang

def gpu_shuju():
    gpu_zhuangtai = w.Win32_VideoController()
    gpu_guangjianzi = re.compile(r'(VideoController[0-9])') #建立正则表达式检测显卡数量
    gpu_shaixuan = gpu_guangjianzi.findall(str(gpu_zhuangtai))
    gpu_shuliang = len(gpu_shaixuan)
    return gpu_shuliang

def printMain_board():
    boards = []
    for board_id in w.Win32_BaseBoard():
        tmpmsg = {}
        tmpmsg["id"] = "0"
        tmpmsg["type"] = "board"
        tmpmsg['UUID'] = board_id.qualifiers['UUID'][1:-1]   #主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        tmpmsg['SerialNumber'] = board_id.SerialNumber                #主板序列号
        tmpmsg['Manufacturer'] = board_id.Manufacturer       #主板生产品牌厂家
        tmpmsg['Product'] = board_id.Product                 #主板型号
        boards.append(tmpmsg)
    return boards

system_data = datetime.strptime(w.Win32_OperatingSystem()[0].InstallDate.split('.')[0], "%Y%m%d%H%M%S")

#获取计算机名称和IP
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("计算机名称: %s" %hostname)
print("IP地址: %s" %ip)
>>>>>>> Stashed changes
