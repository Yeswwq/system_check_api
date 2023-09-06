from check_module import *

class System():
    def __init__(self,a):
        self.__a = a
        self.__a -= 1
        self.__cpu = w.Win32_Processor()[self.__a]
        self.__board = w.Win32_BaseBoard()[self.__a]
        self.__bios = w.Win32_BIOS()[self.__a]
        self.__sys = w.Win32_OperatingSystem()[self.__a]

    def cpu_name(self):
        cpu_name = self.__cpu.Name
        return cpu_name

    def cpu_cores(self):
        cpu_cores = str(self.__cpu.NumberOfCores) +"核心"+str(self.__cpu.NumberOfLogicalProcessors)+"线程"
        return cpu_cores

    def cpu_panufacturer(self):
        cpu_Manufacturer = self.__cpu.Manufacturer
        return cpu_Manufacturer

    def cpu_processorId(self):
        cpu_processorId = self.__cpu.ProcessorId
        return cpu_processorId

    def cpu_PartNumber(self):
        cpu_PartNumber = self.__cpu.PartNumber
        return cpu_PartNumber

    def cpu_SystemName(self):
        cpu_SystemName = self.__cpu.SystemName
        return cpu_SystemName

    def board_Manufacturer(self):
        board_Manufacturer = self.__board.Manufacturer
        return board_Manufacturer

    def board_Product(self):
        board_Product = self.__board.Product
        return board_Product

    def board_SerialNumber(self):
        board_SerialNumber = self.__board.SerialNumber
        return board_SerialNumber

    def bios_Manufacturer(self):
        bios_Manufacturer = self.__bios.Manufacturer
        return bios_Manufacturer

    def bios_time(self):
        bios_time = datetime.strptime(self.__bios.ReleaseDate.split('.')[0], "%Y%m%d%H%M%S")
        return bios_time

    def bios_version(self):
        bios_version = str(self.__bios.SMBIOSBIOSVersion)
        return bios_version

    def bios_CurrentLanguage(self):
        bios_CurrentLanguage = str(self.__bios.CurrentLanguage) + " " + str(self.__bios.OSArchitecture)
        return bios_CurrentLanguage

    def sys_Caption(self):
        sys_Caption = str(self.__sys.Caption)
        return sys_Caption

    def sys_CSName(self):
        sys_CSName = str(self.__sys.CSName)
        return sys_CSName

    def sys_InstallDate(self):
        sys_InstallDate = datetime.strptime(self.__sys.InstallDate.split('.')[0], "%Y%m%d%H%M%S")
        return sys_InstallDate

    def sys_ram(self):
        sys_ram = str("%.2fGB"%(int(self.__sys.TotalVisibleMemorySize)/1024**2))
        return sys_ram

    def sys_SerialNumber(self):
        sys_SerialNumber = str(self.__sys.SerialNumber)
        return sys_SerialNumber