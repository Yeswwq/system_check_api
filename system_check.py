import sys
import psutil
import subprocess
import pandas as pd
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel
from check_module import *
from datetime import datetime
import socket


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
                             + "\n核心数:" + str(cpu_NumberOfCores) + "   线程数:"+ str(cpu_NumberOfLogicalProcessors) + "  基准频率:" + str("%.2f"%(cpu_pinlv[2]/1000))+ "GHz"
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

if __name__ == '__main__':
    system_jiagou = w.Win32_ComputerSystem()[0]
    system_shuju = w.Win32_OperatingSystem()[0]
    system_data = datetime.strptime(system_shuju.InstallDate.split('.')[0], "%Y%m%d%H%M%S")

    print(system_shuju)
    ww = w.Win32_Processor()[0] #获取处理器详细信息
    cpu_name = ww.Name #cpu型号
    cpu_NumberOfCores = ww.NumberOfCores #cpu核心数
    cpu_NumberOfLogicalProcessors = ww.NumberOfLogicalProcessors #cpu线程数
    cpu_pinlv = psutil.cpu_freq() #基准频率

    #循环获取每条内存详细规格
    ram_sifang = ram_shuju()
    ram_daxiao0 = "不存在"
    ram_daxiao1 = "不存在"
    ram_daxiao2 = "不存在"
    ram_daxiao3 = "不存在"
    while ram_sifang >=1:
        ram_sifang -= 1
        if ram_sifang == 3:
            ram_loop3 = w.Win32_PhysicalMemory()[ram_sifang]
            ram_daxiao3 = "内存大小:" + str("%.2f"%(int(ram_loop3.Capacity)/1024/1024/1024))  + "GB" + "\n内存最大可用频率:" + str(ram_loop3.Speed) + "Hz"+ "\n内存当前工作频率:" + str(ram_loop3.ConfiguredClockSpeed) + "Hz"+ "\n内存厂商:"+ str(ram_loop3.Manufacturer)+ "\n内存编号:"+ str(ram_loop3.PartNumber)
            print("内存插槽:"+ str(ram_loop3.Tag))


        elif ram_sifang == 2:
            ram_loop2 = w.Win32_PhysicalMemory()[ram_sifang]
            ram_daxiao2 = "内存大小:" + str("%.2f"%(int(ram_loop2.Capacity)/1024/1024/1024))  + "GB" + "\n内存最大可用频率:" + str(ram_loop2.Speed) + "Hz"+ "\n内存当前工作频率:" + str(ram_loop2.ConfiguredClockSpeed) + "Hz"+ "\n内存厂商:"+ str(ram_loop2.Manufacturer)+ "\n内存编号:"+ str(ram_loop2.PartNumber)
            print(str("内存插槽:"+ram_loop2.Tag))


        elif ram_sifang == 1:
            ram_loop1 = w.Win32_PhysicalMemory()[ram_sifang]
            ram_daxiao1 = "内存大小:" + str("%.2f"%(int(ram_loop1.Capacity)/1024/1024/1024))  + "GB" + "\n内存最大可用频率:" + str(ram_loop1.Speed) + "Hz"+ "\n内存当前工作频率:" + str(ram_loop1.ConfiguredClockSpeed) + "Hz"+ "\n内存厂商:"+ str(ram_loop1.Manufacturer)+ "\n内存编号:"+ str(ram_loop1.PartNumber)
            print(str("内存插槽:"+ ram_loop1.Tag))


        elif ram_sifang == 0:
            ram_loop0 = w.Win32_PhysicalMemory()[ram_sifang]
            ram_daxiao0 = "内存大小:" + str("%.2f"%(int(ram_loop0.Capacity)/1024/1024/1024))  + "GB" + "\n内存最大可用频率:" + str(ram_loop0.Speed) + "Hz"+ "\n内存当前工作频率:" + str(ram_loop0.ConfiguredClockSpeed) + "Hz"+ "\n内存厂商:"+ str(ram_loop0.Manufacturer)+ "\n内存编号:"+ str(ram_loop0.PartNumber)
            print("内存插槽:"+ str(ram_loop0.Tag))

    #获取硬盘类型数据
    cmd = 'powershell Get-PhysicalDisk'
    disk_leixin = subprocess.run(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = disk_leixin.stdout.decode("utf-8")
    error = disk_leixin.stderr.decode("utf-8")  
    disk_leixingshuju = re.sub(r"\s+", "", output) #处理掉返回结果中的空格，为下文获取硬盘类型做准备
    print(disk_leixingshuju) 

    #初始化硬盘状态
    disk_sifang = disk_shuju()
    disk_daxiao0 = "不存在"
    disk_daxiao1 = "不存在"
    disk_daxiao2 = "不存在"
    disk_daxiao3 = "不存在"
    disk_leixin_out0 = "不存在"
    disk_leixin_out1 = "不存在"
    disk_leixin_out2 = "不存在"
    disk_leixin_out3 = "不存在"
    while disk_sifang >=1:
        disk_sifang -= 1
        if disk_sifang == 3:
            disk_loop3 = w.Win32_DiskDrive()[disk_sifang]
            disk3_SerialNumber = re.sub(r"\s+", "", disk_loop3.SerialNumber)
            disk_daxiao3 = "硬盘大小:" + str("%.2f"%(int(disk_loop3.Size)/1024/1024/1024))  + "GB" + "\n品牌名称:" + str(disk_loop3.Model) + "\n硬盘序列号:" + str(disk3_SerialNumber)
            print(str("硬盘插槽:"+disk_loop3.PNPDeviceID))
            disk_pipei3 = re.compile(disk3_SerialNumber +'[A-Z][A-Z][A-Z]')
            disk_jieguo_out3 = disk_pipei3.search(disk_leixingshuju)
            if "SSD" in disk_jieguo_out3.group():
                disk_leixin_out3 = "固态硬盘"
            else:
                disk_leixin_out3 = "机械硬盘" 

        elif disk_sifang == 2:
            disk_loop2 = w.Win32_DiskDrive()[disk_sifang]
            disk2_SerialNumber = re.sub(r"\s+", "", disk_loop2.SerialNumber)
            disk_daxiao2 = "硬盘大小:" + str("%.2f"%(int(disk_loop2.Size)/1024/1024/1024))  + "GB" + "\n品牌名称:" + str(disk_loop2.Model) + "\n硬盘序列号:" + str(disk2_SerialNumber)
            print(str("硬盘插槽:"+disk_loop2.PNPDeviceID))
            disk_pipei2 = re.compile(disk2_SerialNumber +'[A-Z][A-Z][A-Z]')
            disk_jieguo_out2 = disk_pipei2.search(disk_leixingshuju)
            if "SSD" in disk_jieguo_out2.group():
                disk_leixin_out2 = "固态硬盘"
            else:
                disk_leixin_out2 = "机械硬盘" 

        elif disk_sifang == 1:
            disk_loop1 = w.Win32_DiskDrive()[disk_sifang]
            disk1_SerialNumber = re.sub(r"\s+", "", disk_loop1.SerialNumber)
            disk_daxiao1 = "硬盘大小:" + str("%.2f"%(int(disk_loop1.Size)/1024/1024/1024))  + "GB" + "\n品牌名称:" + str(disk_loop1.Model) + "\n硬盘序列号:" + str(disk1_SerialNumber)
            print(str("硬盘插槽:"+disk_loop1.PNPDeviceID))
            disk_pipei1 = re.compile(disk1_SerialNumber +'[A-Z][A-Z][A-Z]')
            disk_jieguo_out1 = disk_pipei1.search(disk_leixingshuju)
            if "SSD" in disk_jieguo_out1.group():
                disk_leixin_out1 = "固态硬盘"
            else:
                disk_leixin_out1 = "机械硬盘" 


        elif disk_sifang == 0:
            disk_loop0 = w.Win32_DiskDrive()[disk_sifang]
            disk0_SerialNumber = re.sub(r"\s+", "", disk_loop0.SerialNumber)
            disk_daxiao0 = "硬盘大小:" + str("%.2f"%(int(disk_loop0.Size)/1024/1024/1024))  + "GB" + "\n品牌名称:" + str(disk_loop0.Model) + "\n硬盘序列号:" + str(disk0_SerialNumber)
            print(str("硬盘插槽:"+disk_loop0.PNPDeviceID))
            disk_pipei0 = re.compile(disk0_SerialNumber +'[A-Z][A-Z][A-Z]')
            disk_jieguo_out0 = disk_pipei0.search(disk_leixingshuju)
            if "SSD" in disk_jieguo_out0.group():
                disk_leixin_out0 = "固态硬盘"
            else:
                disk_leixin_out0 = "机械硬盘" 

    
    gpu_sifang = gpu_shuju()
    gpu_daxiao0 = "不存在"
    gpu_daxiao1 = "不存在"
    while gpu_sifang >= 1:
        gpu_sifang -= 1
        if gpu_sifang == 1:
            gpu_loop1 = w.Win32_VideoController()[gpu_sifang]
            gpu_daxiao1 = "显卡厂商：" + gpu_loop1.AdapterCompatibility + "\n显卡型号:" + gpu_loop1.Description + "\n显存:" + str("%.2f"%(gpu_loop1.AdapterRAM/-1024 **3)) + "GB" + "\n当前分辨率:" +str(gpu_loop1.CurrentHorizontalResolution) + "x" +str(gpu_loop1.CurrentVerticalResolution) + "\t当前刷新率：" +str(gpu_loop1.CurrentRefreshRate)
            print(gpu_daxiao1)


        elif gpu_sifang == 0:
            gpu_loop0 = w.Win32_VideoController()[gpu_sifang]
            gpu_daxiao0 = "显卡厂商：" + gpu_loop0.AdapterCompatibility + "\n显卡型号:" + gpu_loop0.Description + "\n显存:" + str("%.2f"%(int(gpu_loop0.AdapterRAM)/-1024 **3)) + "GB" + "\n当前分辨率:" +str(gpu_loop0.CurrentHorizontalResolution) + "x" +str(gpu_loop0.CurrentVerticalResolution) + "\t当前刷新率：" +str(gpu_loop0.CurrentRefreshRate)
            print(gpu_daxiao0)

    #获取计算机名称和IP
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("计算机名称: %s" %hostname)
    print("IP地址: %s" %ip)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()