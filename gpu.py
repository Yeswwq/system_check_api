from check_module import *

gpu_sifang = gpu_shuju()
gpu_daxiao0 = "不存在"
gpu_daxiao1 = "不存在"
gpu_loop0 = "不存在"
gpu_loop1 = "不存在"
while gpu_sifang >= 1:
    gpu_sifang -= 1
    if gpu_sifang == 1:
        gpu_loop1 = w.Win32_VideoController()[gpu_sifang]
        gpu_daxiao1 = "显卡厂商：" + gpu_loop1.AdapterCompatibility + "\n显卡型号:" + gpu_loop1.Description + "\n显存:" + str("%.2fGB"%(int(gpu_loop1.AdapterRAM)/1024 **3)) + "\n当前分辨率:" +str(gpu_loop1.CurrentHorizontalResolution) + "x" +str(gpu_loop1.CurrentVerticalResolution) + "\t当前刷新率：" +str(gpu_loop1.CurrentRefreshRate)
        print(gpu_daxiao1)


    elif gpu_sifang == 0:
        gpu_loop0 = w.Win32_VideoController()[gpu_sifang]
        gpu_daxiao0 = "显卡厂商：" + gpu_loop0.AdapterCompatibility + "\n显卡型号:" + gpu_loop0.Description + "\n显存:" + str("%.2fGB"%(int(gpu_loop0.AdapterRAM)/1024 **3)) + "\n当前分辨率:" +str(gpu_loop0.CurrentHorizontalResolution) + "x" +str(gpu_loop0.CurrentVerticalResolution) + "\t当前刷新率：" +str(gpu_loop0.CurrentRefreshRate)
        print(gpu_daxiao0)

class GPU():

    #初始化
    def __init__(self,a): 
        self.__a = a
        self.__a -= 1
        self.__gpu = w.Win32_VideoController()[self.__a]

    def gpu_vendor(self):
        gpu_vendor = self.__gpu.AdapterCompatibility
        return gpu_vendor

    def gpu_name(self):
        gpu_name = self.__gpu.Description
        return gpu_name

    def gpu_ram(self):
        gpu_ram = str("%.2fGB"%(int(self.__gpu.AdapterRAM)/1024 **3))
        return gpu_ram

    def gpu_resolution(self):
        gpu_resolution ="分辨率：" + str(self.__gpu.CurrentHorizontalResolution) + "x" +str(self.__gpu.CurrentVerticalResolution) + " 当前刷新率：" +str(self.__gpu.CurrentRefreshRate)
        return gpu_resolution




