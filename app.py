import platform
import openpyxl
import psutil
import wmi
import socket
import cpuinfo
from openpyxl import Workbook

# Bilgisayar adını alma işlevi
def get_computer_name():
    return platform.node()

# Windows sürümünü alma işlevi
def get_windows_version():
    return platform.platform()

# Etki alanı durumunu kontrol eden işlev
def get_domain_status():
    return platform.node().endswith('.')

# RAM bilgilerini alma işlevi
def get_ram_info():
    svmem = wmi.WMI().Win32_ComputerSystem()[0]
    total_physical_memory = int(svmem.TotalPhysicalMemory)  # Integer'a dönüştürme
    total_physical_memory_gb = total_physical_memory / (1024 ** 3)  # GB'ye dönüştürme
    return f"{total_physical_memory_gb:.2f} GB"

# İşlemci bilgilerini alma işlevi
def get_cpu_info(ip_address=None):
    cpu_info = cpuinfo.get_cpu_info()
    return f"{cpu_info['brand_raw']} {cpu_info['hz_actual']}"

# Disk bilgilerini alma işlevi
def get_disk_info():
    partitions = wmi.WMI().Win32_DiskDrive()
    disk_info = ""
    for partition in partitions:
        disk_info += f"{partition.Caption} - Boyut: {partition.Size}\n"
    return disk_info

# IP adresini alma işlevi
def get_ip_address():
    interfaces = psutil.net_if_addrs()
    if "Ethernet" in interfaces:
        eth_interface = interfaces["Ethernet"]
        for entry in eth_interface:
            if entry.family == socket.AF_INET:  # IPv4 adresi olup olmadığını kontrol etme
                return entry.address
    return "N/A"  # Eğer IPv4 adresi bulunamazsa

# MAC adresini alma işlevi
def get_mac_address():
    # Ağ arayüzü adını ihtiyaca göre değiştirin
    return psutil.net_if_addrs()["Ethernet"][0].address

# BIOS numarasını alma işlevi
def get_bios_number():
    return wmi.WMI().Win32_BIOS()[0].SerialNumber

# Monitör bilgilerini alma işlevi
def get_monitor_info():
    monitors = wmi.WMI().Win32_DesktopMonitor()
    monitor_info = ""
    for monitor in monitors:
        monitor_info += f"{monitor.Name}\n"
    return monitor_info

# Verileri Excel'e kaydetme işlevi
def save_to_excel(data):
    workbook = Workbook()
    sheet = workbook.active

    headers = ["Bilgisayar Adı", "Windows Sürümü", "Domain Durumu", "RAM Bilgileri", "İşlemci Bilgileri", 
               "Disk Bilgileri", "IP Adresi", "MAC Adresi", "BIOS Numarası", "Monitör Bilgileri"]
    sheet.append(headers)

    for row in data:
        sheet.append(row)

    workbook.save("bilgisayar_bilgileri.xlsx")

def main():
    computer_name = get_computer_name()
    windows_version = get_windows_version()
    domain_status = "Bağlı" if get_domain_status() else "Bağlı Değil"
    ram_info = get_ram_info()
    cpu_info = get_cpu_info()
    disk_info = get_disk_info()
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    bios_number = get_bios_number()
    monitor_info = get_monitor_info()

    data = [
        [computer_name, windows_version, domain_status, ram_info, cpu_info, disk_info, ip_address, 
         mac_address, bios_number, monitor_info]
    ]

    save_to_excel(data)

if __name__ == "__main__":
    main()
