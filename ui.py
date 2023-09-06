from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel
import psutil

from check_module import *
from disk import *
from ram import *
from gpu import *

system_jiagou = w.Win32_ComputerSystem()[0]
system_shuju = w.Win32_OperatingSystem()[0]
ww = w.Win32_Processor()[0] #获取处理器详细信息
print(ww)
cpu_name = ww.Name #cpu型号
cpu_NumberOfCores = ww.NumberOfCores #cpu核心数
cpu_NumberOfLogicalProcessors = ww.NumberOfLogicalProcessors #cpu线程数
cpu_pinlv = psutil.cpu_freq() #基准频率


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize())
        self.setWindowTitle("当前登录:" + system_jiagou.UserName)

        #输出结果到UI界面

        win_banben = QLabel(system_shuju.Caption
                             + "\r" + system_shuju.OSArchitecture +"操作系统"
                             + "\n运行内存:" + str("%.2fGB"%(int(system_shuju.TotalVisibleMemorySize)/1024**2))
                             + "\n设备名称:" + system_jiagou.Name
                             + "\n制造商:" + system_jiagou.Manufacturer
                             + "\n系统安装时间:" + str(system_data)
                             + "\nCPU型号:" + str(cpu_name) 
                             + "\n核心数:" + str(cpu_NumberOfCores) + "\t线程数:"+ str(cpu_NumberOfLogicalProcessors) + "\t基准频率:" + str("%.2f"%(cpu_pinlv[2]/1000))+ "GHz"
                             + "\n"
                             + "\n第一条" + str(ram_daxiao0)
                             + "\n"
                             + "\n第二条" + str(ram_daxiao1)
                             + "\n"
                             + "\n第三条" + str(ram_daxiao2)
                             + "\n"
                             + "\n第四条" + str(ram_daxiao3)
                             + "\n"
                             + "\n第一块为：" + str(disk_leixin_out0)
                             + "\n" + str(disk_daxiao0)
                             + "\n"
                             + "\n第二块为：" + str(disk_leixin_out1)
                             + "\n" + str(disk_daxiao1)
                             + "\n"
                             + "\n第三块为：" + str(disk_leixin_out2)
                             + "\n" + str(disk_daxiao2)
                             + "\n"
                             + "\n第四块为：" + str(disk_leixin_out3)
                             + "\n" + str(disk_daxiao3)
                             + "\n"
                             + "\n" + gpu_daxiao0
                             + "\n"
                             + "\n" + gpu_daxiao1
                             + "\n" + "计算机名称: %s" %hostname
                             + "\n" + "IP地址: %s" %ip
                             )


        self.setCentralWidget(win_banben)


        # Set the central widget of the Window.
        