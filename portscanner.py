from termcolor import colored
from pyfiglet import figlet_format

print((colored(figlet_format("PORTSCANNER", font="future_1"), color="red")))
print((colored("-------------------- Coded by Dzaki Althalsyah -------------------- \n", color="blue")))
print((colored("Github: https://github.com/dzakialthalsyah/   ||   Instagram: https://instagram.com/dzakialthalsyah/ \n\n\n", color="cyan")))

# import module requests
import requests

# function untuk scanning port
def subscanner(scan_nama_domain, scan_nama_port):

    print("\n\n\n---------------- Hasil Scan ----------------")

    # looping untuk mendapatkan url
    for port in scan_nama_port:

        # membuat url dengan memasukkan subdomain satu persatu *bruteforce
        url = f"https://{scan_nama_domain}:{port}"

        # memakai syntax try untuk menghindari crash pada program
        try:
        # sending GET request ke url
            requests.get(url)
        # jika setelah mencoba subdomain satu persatu valid kemudian print url nya
            print(f"[+] {url}")

    # jika url nya invalid kemudian lewatkan
        except requests.ConnectionError:
            pass
# function Desc = scan_nama_port in port, port dan scan_nama_domain in url, url got request

# function utama
if __name__ == "__main__":

    # memasukkan nama domain
    nama_dom = input("Masukkan Domain: ")

    # membuka nama list file port nya
    with open("listport.ini","r") as file:

        # membaca file nya
        baca = file.read()

        # memakai garis pemisah/spilitlines() function untuk storing list yang string nya terbelah
        list_port = baca.splitlines()


# memanggil function untuk memanggil port
subscanner(nama_dom, list_port)

