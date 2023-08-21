# SysInfoSaver

Bu Python betiği, bir bilgisayarın çeşitli bilgilerini toplar ve bu bilgileri bir Excel dosyasına kaydeder. Aşağıda kodun ne yaptığına dair bir açıklama bulunmaktadır.

## Kullanım

1. Bilgisayarınızda Python yüklü olduğundan emin olun.
2. Gerekli Python kütüphanelerini yüklemek için terminalde aşağıdaki komutu çalıştırın:

  ```bash
  pip install -r requirements.txt
  ```
3. Kod, bilgisayarınızdaki çeşitli bilgileri toplar ve bu bilgileri bir Excel dosyasına kaydeder.

## Fonksiyonlar

- `get_computer_name()`: Bilgisayar adını döndürür.
- `get_windows_version()`: Windows sürümünü döndürür.
- `get_domain_status()`: Bilgisayarın etki alanına bağlı olup olmadığını belirler.
- `get_ram_info()`: RAM bilgilerini gigabayt cinsinden döndürür.
- `get_cpu_info()`: İşlemci bilgilerini döndürür.
- `get_disk_info()`: Disk bilgilerini döndürür.
- `get_ip_address()`: Bilgisayarın IPv4 adresini döndürür.
- `get_mac_address()`: Ethernet arabirimine ait MAC adresini döndürür.
- `get_bios_number()`: BIOS serisi numarasını döndürür.
- `get_monitor_info()`: Bağlı olan monitörlerin bilgilerini döndürür.
- `save_to_excel(data)`: Verileri Excel dosyasına kaydeder.

## Çalıştırma

1. Terminal veya komut istemcisini açın ve proje klasörüne gidin.
2. Kodu çalıştırmak için aşağıdaki komutu girin:

  ```bash
  python app.py
  ```

3. Kod çalıştırıldığında, toplanan bilgiler bir Excel dosyasına kaydedilir.

**Not:** Bu kod, belirli bir bilgisayarın çeşitli sistem bilgilerini toplamak ve bu bilgileri düzenli bir şekilde bir Excel dosyasına kaydetmek için kullanılabilir. Daha fazla bilgi veya özel gereksinimler için kodu düzenlemekten çekinmeyin.

## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.
