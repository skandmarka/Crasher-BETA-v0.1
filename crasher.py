import requests
import random
import time
import os

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""{Colors.RED}
    ╔══════════════════════════════════════╗
    ║        SKAND IP CHANGER v2          ║
    ╚══════════════════════════════════════╝
    {Colors.RESET}""")

class IPChanger:
    def __init__(self):
        self.proxy_list = []
        self.fetch_proxies()
    
    def get_current_ip(self):
        try:
            r = requests.get("http://ip-api.com/json/", timeout=5)
            data = r.json()
            return data
        except:
            return {"query": "Bilinmiyor", "country": "?", "city": "?", "isp": "?"}
    
    def fetch_proxies(self):
        print(f"{Colors.CYAN}[*] Proxy listesi cekiliyor...{Colors.RESET}")
        try:
            urls = [
                "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all",
                "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
            ]
            
            for url in urls:
                try:
                    r = requests.get(url, timeout=10)
                    proxies = r.text.strip().split('\n')
                    self.proxy_list.extend([p.strip() for p in proxies if ':' in p])
                except:
                    pass
            
            self.proxy_list = list(set(self.proxy_list))
            
            if len(self.proxy_list) < 10:
                self.proxy_list = [
                    "103.149.162.194:8080", "103.157.116.253:8080", "103.165.155.66:8080",
                    "104.131.182.82:3128", "107.178.9.186:8080", "111.92.164.246:80",
                    "113.53.60.101:8080", "116.12.250.234:8080", "118.99.80.123:8080",
                    "119.93.129.34:80", "124.121.127.178:8080", "134.209.29.120:8080",
                    "138.197.157.32:8080", "139.59.1.14:8080", "159.192.97.182:8080",
                    "167.172.109.12:80", "175.139.179.65:80", "177.54.204.38:3128",
                    "178.128.58.199:8080", "181.129.133.58:46721", "182.253.207.74:8080",
                    "185.199.228.195:80", "185.199.229.156:3128", "185.199.231.45:80",
                    "188.166.212.125:8080", "190.61.44.138:999", "190.64.18.162:80",
                    "192.111.129.146:4145", "192.111.137.35:4145", "194.163.179.67:3128",
                    "195.138.73.54:31135", "20.206.106.157:80", "202.169.253.106:8080",
                    "203.150.128.199:8080", "207.244.251.188:3128", "209.127.191.180:80",
                    "213.230.101.235:80", "216.137.184.251:80", "34.81.72.31:80",
                    "35.185.196.38:80", "45.77.56.122:8080", "46.4.41.22:3128",
                    "47.243.92.199:3128", "5.161.47.157:80", "51.15.242.202:3128",
                    "51.89.173.40:80", "64.227.44.67:8080", "66.29.154.105:3128",
                    "68.183.143.134:80", "72.10.164.178:1399", "74.208.177.198:80",
                    "8.219.97.248:80", "80.94.105.228:80", "82.223.227.100:8080",
                    "83.1.176.118:80", "85.214.224.23:3128", "87.248.114.11:8080",
                    "91.202.230.29:8080", "92.205.105.117:8080", "93.127.179.139:80",
                    "94.23.97.162:8118", "95.216.193.179:3128", "98.162.25.29:31679",
                ]
            
            print(f"{Colors.GREEN}[+] {len(self.proxy_list)} proxy hazir!{Colors.RESET}")
        except:
            print(f"{Colors.RED}[-] Proxy cekilemedi!{Colors.RESET}")
    
    def test_proxy(self, proxy):
        try:
            r = requests.get("http://ip-api.com/json/", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return None
    
    def change_ip_random(self):
        print(f"\n{Colors.CYAN}[*] Calisan proxy araniyor...{Colors.RESET}")
        
        random.shuffle(self.proxy_list)
        
        for proxy in self.proxy_list[:20]:
            print(f"{Colors.CYAN}    deneniyor: {proxy}{Colors.RESET}", end='\r')
            result = self.test_proxy(proxy)
            if result:
                print(f"\n{Colors.GREEN}[+] BASARILI! IP Degisti!{Colors.RESET}")
                print(f"{Colors.YELLOW}    Proxy: {proxy}")
                print(f"    Yeni IP: {result.get('query', '?')}")
                print(f"    Ulke: {result.get('country', '?')}")
                print(f"    Sehir: {result.get('city', '?')}")
                print(f"    ISP: {result.get('isp', '?')}{Colors.RESET}")
                return result
            time.sleep(0.3)
        
        print(f"\n{Colors.RED}[-] Calisan proxy bulunamadi!{Colors.RESET}")
        return None
    
    def change_ip_manual(self, proxy):
        print(f"\n{Colors.CYAN}[*] Proxy deneniyor: {proxy}{Colors.RESET}")
        
        result = self.test_proxy(proxy)
        if result:
            print(f"{Colors.GREEN}[+] BASARILI! IP Degisti!{Colors.RESET}")
            print(f"{Colors.YELLOW}    Yeni IP: {result.get('query', '?')}")
            print(f"    Ulke: {result.get('country', '?')}")
            print(f"    Sehir: {result.get('city', '?')}")
            print(f"    ISP: {result.get('isp', '?')}{Colors.RESET}")
            return result
        else:
            print(f"{Colors.RED}[-] Proxy calismadi!{Colors.RESET}")
            return None
    
    def auto_change(self):
        print(f"\n{Colors.CYAN}[*] Otomatik IP degistirme basladi...{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] 10 saniyede bir IP degisecek. Ctrl+C ile dur.{Colors.RESET}\n")
        
        count = 0
        while True:
            try:
                count += 1
                print(f"\n{Colors.CYAN}--- Degisim #{count} ---{Colors.RESET}")
                self.change_ip_random()
                print(f"\n{Colors.YELLOW}[*] 10 saniye bekleniyor...{Colors.RESET}")
                time.sleep(10)
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}[!] Durduruldu!{Colors.RESET}")
                break

def main():
    banner()
    
    changer = IPChanger()
    
    current = changer.get_current_ip()
    print(f"\n{Colors.YELLOW}[*] Gercek IP bilgilerin:{Colors.RESET}")
    print(f"{Colors.WHITE}    IP: {current.get('query', '?')}")
    print(f"    Ulke: {current.get('country', '?')}")
    print(f"    Sehir: {current.get('city', '?')}")
    print(f"    ISP: {current.get('isp', '?')}{Colors.RESET}\n")
    
    while True:
        print(f"\n{Colors.CYAN}[*] Ne yapalim?{Colors.RESET}")
        print(f"{Colors.WHITE}    1. Rastgele IP degistir")
        print(f"    2. Manuel proxy gir (IP:Port)")
        print(f"    3. Otomatik degistir (10sn aralik)")
        print(f"    4. IP bilgilerimi goster")
        print(f"    5. Cikis{Colors.RESET}")
        
        sec = input(f"{Colors.GREEN}[?] Secim: {Colors.RESET}").strip()
        
        if sec == "1":
            changer.change_ip_random()
        
        elif sec == "2":
            proxy = input(f"{Colors.GREEN}[?] Proxy gir (IP:Port): {Colors.RESET}").strip()
            if ':' in proxy:
                changer.change_ip_manual(proxy)
            else:
                print(f"{Colors.RED}[-] Format yanlis! IP:Port seklinde gir.{Colors.RESET}")
        
        elif sec == "3":
            changer.auto_change()
        
        elif sec == "4":
            current = changer.get_current_ip()
            print(f"\n{Colors.YELLOW}[*] Guncel IP bilgilerin:{Colors.RESET}")
            print(f"{Colors.WHITE}    IP: {current.get('query', '?')}")
            print(f"    Ulke: {current.get('country', '?')}")
            print(f"    Sehir: {current.get('city', '?')}")
            print(f"    ISP: {current.get('isp', '?')}{Colors.RESET}")
        
        elif sec == "5":
            print(f"{Colors.RED}[!] Cikis...{Colors.RESET}")
            break
        
        else:
            print(f"{Colors.RED}[-] Yanlis secim!{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}[*] Enter...{Colors.RESET}")
        clear()
        banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Cikis...{Colors.RESET}")
