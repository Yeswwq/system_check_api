import sys
import json

from ui import *

#将结果汇总为json格式
sys_txt1 = {}
sys_txt1 ["id"] = "1"
sys_txt1 ["type"] = "system"
sys_txt1 ["name"] = system_jiagou.UserName
sys_txt1 ["system"] = system_shuju.Caption + "\t" + system_shuju.OSArchitecture
sys_txt1 ["install_time"] = system_data
sys_txt1 ["sys_ram"] = str("%.2fGB"%(int(system_shuju.TotalVisibleMemorySize)/1024**2))
sys_txt1 ["Manufacturer"] = system_jiagou.Manufacturer

cpu_txt1 = {}
cpu_txt1 ["id"] = "2"
cpu_txt1 ["type"] = "cpu"
cpu_txt1 ["name"] = cpu_name
cpu_txt1 ["specs"] = "核心数:" + str(cpu_NumberOfCores) + "\t线程数:"+ str(cpu_NumberOfLogicalProcessors) + "\t基准频率:" + str("%.2f"%(cpu_pinlv[2]/1000))+ "GHz"

gpu_txt0 = {}
gpu_txt0 ["id"] = "6"
gpu_txt0 ["type"] = "gpu0"
gpu_txt0 ["AdapterCompatibility"] = gpu_loop0.AdapterCompatibility
gpu_txt0 ["name"] = gpu_loop0.Description
gpu_txt0 ["gpu_ram"] = str("%.2fGB"%(int(gpu_loop0.AdapterRAM)/1024 **3))
gpu_txt0 ["gpu_resolution"] = str(gpu_loop0.CurrentHorizontalResolution) + "x" +str(gpu_loop0.CurrentVerticalResolution)
gpu_txt0 ["CurrentRefreshRate"] = str(gpu_loop0.CurrentRefreshRate)




#输出json
textarr = []
textarr.append(cpu_txt1)
textarr.append(gpu_txt0)

print(textarr)
jtext = json.dumps(textarr,ensure_ascii=False)
print(jtext)

#硬盘数据打印
diskshuju = 1
while diskshuju <= disk_shuju():
    print("共计" + str(disk_shuju()) + "块硬盘")
    print("第" + str(diskshuju) + "块硬盘参数如下：")
    print("容量：" + DISK(diskshuju).disk_size())
    print("型号：" + DISK(diskshuju).disk_model())
    print("类型：" + DISK(diskshuju).disk_type())
    print("编号：" + DISK(diskshuju).disk_SerialNumber())
    print("标志位：" + DISK(diskshuju).disk_id() + "\n")
    diskshuju += 1

#内存数据打印
ramshuju = 1
while ramshuju <= ram_shuju():
    print("共计" + str(ram_shuju()) + "条内存")
    print("第" + str(ramshuju) + "条内存参数如下：")
    print("容量：" + RAM(ramshuju).ram_size())
    print("当前频率：" + RAM(ramshuju).ram_speed())
    print("实际频率：" + RAM(ramshuju).ram_maxspeed())
    print("品牌：" + RAM(ramshuju).ram_vendor())
    print("编号：" + RAM(ramshuju).ram_PartNumber())
    print("标志位：" + RAM(ramshuju).ram_tag() + "\n")
    ramshuju += 1

#显卡数据打印
gpushuju = 1
while gpushuju <= gpu_shuju():
    print("共计" + str(gpu_shuju()) + "张显卡")
    print("第" + str(gpushuju) + "张显卡参数如下：")
    print("品牌：" + GPU(gpushuju).gpu_vendor())
    print("型号：" + GPU(gpushuju).gpu_name())
    print("显存：" + GPU(gpushuju).gpu_ram())
    print("显示信息：" + GPU(gpushuju).gpu_resolution())
    gpushuju += 1




if __name__ == '__main__':

    print(GPU(gpu_shuju()).gpu_name())
    print(DISK(disk_shuju()).disk_type())

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
