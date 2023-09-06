from check_module import *

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

class RAM():
    def __init__(self,a):
        self.__a = a
        self.__a -= 1
        self.__ram = w.Win32_PhysicalMemory()[self.__a]

    def ram_vendor(self):
        ram_vendor = str(self.__ram.Manufacturer)
        return ram_vendor

    def ram_PartNumber(self):
        ram_PartNumber = str(self.__ram.PartNumber)
        return ram_PartNumber

    def ram_size(self):
        ram_size = str("%.2fGB"%(int(self.__ram.Capacity)/1024 **3))
        return ram_size

    def ram_speed(self):
        ram_speed = str(self.__ram.ConfiguredClockSpeed) + " Hz"
        return ram_speed

    def ram_maxspeed(self):
        ram_maxspeed = str(self.__ram.Speed) + " Hz"
        return ram_maxspeed

    def ram_tag(self):
        ram_tag = str(self.__ram.Tag)
        return ram_tag

