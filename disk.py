from check_module import *
import subprocess

#获取硬盘类型数据
disk_leixingshuju = "不存在"
cmd = 'powershell Get-PhysicalDisk'
disk_leixin = subprocess.run(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = disk_leixin.stdout.decode("utf-8")
error = disk_leixin.stderr.decode("utf-8")
#处理掉返回结果中的空格，为下文获取硬盘类型做准备
disk_leixingshuju = re.sub(r"\s+", "", output)
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

class DISK():

    def __init__(self,a):
        self.__a = a
        self.__a -= 1

    def disk_model(self):
        disk_model = str(w.Win32_DiskDrive()[self.__a].Model)
        return disk_model
    
    def disk_SerialNumber(self):
        disk_SerialNumber = re.sub(r"\s+", "", w.Win32_DiskDrive()[self.__a].SerialNumber)
        return disk_SerialNumber

    def disk_type(self):
        disk_type = re.compile(self.disk_SerialNumber() +'[A-Z][A-Z][A-Z]')
        disk_type = disk_type.search(disk_leixingshuju)
        if "SSD" in disk_type.group():
            disk_type = "固态硬盘"
        else:
            disk_type = "机械硬盘" 
        return disk_type

    def disk_size(self):
        disk_size = str("%.2f"%(int(w.Win32_DiskDrive()[self.__a].Size)/1024 ** 3))
        return disk_size

