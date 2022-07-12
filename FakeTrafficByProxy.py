from bs4 import BeautifulSoup
import requests
import re
from itertools import cycle
import pyfiglet
from pyfiglet import fonts
from termcolor import colored
from colorama import init
import argparse
import time
from random import randint

init()
G  = '\033[32m' 
O  = '\033[33m' 
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

blogurl = []
list_proxy = []

def banner():
    print (colored(pyfiglet.figlet_format("Fake Traffic By Proxy", font="standard"), "red"))
    print (G+BOLD+"By Rishabh Sharma [Follow: https://lazyhacker22.blogspot.com/]\n"+END)



def collect_HREF_From_URL(url):
    regex_collect_HREF_From_URL = r"("+url+".*)"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    
    for data in soup.find_all("a"):
        get_href = (str(data.get('href')))
        matches = re.finditer(regex_collect_HREF_From_URL, get_href, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            href_url = (match.group(1))
            if href_url not in blogurl:
                blogurl.append(href_url)
    #print(blogurl)
    findfreeproxy(url)
        

def findfreeproxy(url):
    proxyforfilter_file = open("proxyforfilter.txt","a")
    urlproxy= ("https://free-proxy-list.net/")
    regex_findfreeproxy = r"(<tr><td>)(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)(</td><td>)(\d*)(</td><td>\S*<td class=\"hm\">[a-zA-Z\s]*</td><td>[a-zA-Z\s]*</td><td class=\"hm\">[a-z]*</td><td class=\"hx\">)([a-z]*)"
    html_content = requests.get(urlproxy).text
    soup = BeautifulSoup(html_content, "lxml")
    for data in soup.find_all("tr"):
        filter1 = ("Inner Text: {}".format(data))
        matches = re.finditer(regex_findfreeproxy, filter1, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            if (match.group(6)=="no"):
                ip_port = ("http://"+match.group(2)+":"+match.group(4))
            elif(match.group(6)=="yes"):
                ip_port = ("https://"+match.group(2)+":"+match.group(4))
            
            #print (ip_port)
            list_proxy.append(ip_port)
            proxyforfilter_file.write(ip_port)
            proxyforfilter_file.write("\n")
    proxyforfilter_file.close()
    #print(list_proxy)
    fake_Traffic(url)

def fake_Traffic(url):
    url4 = (url.split('/')[2])
    proxy_cycle = cycle(list_proxy)
    proxy = next(proxy_cycle)
    x = (len(list_proxy))
    bu = (len(blogurl))
    z = 0
    #print(url4)
    headers = {
                "Host": url4,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Te": "trailers",
                }

    try:
        for i in range(1, x):
            proxy = next(proxy_cycle)
            proxies = {
                "http": proxy,
                }
            for burl in range(z,bu):
                url1 = blogurl[z]
                r = requests.get(url=url1, headers=headers, verify=True, proxies=proxies)
                print(G+"[+]"+END+(proxy.split('/')[2]+" ")+Y+f'Status Code: {r.status_code}'+END+" "+O+url1+END)
                if (r.status_code != 200):
                    break
                randomtime = (randint(50,65))
                #print ("Sleep for "+str(randomtime)+" sec...")
                time.sleep(randomtime)
                if(randomtime>=64):
                    break
                if(z>=bu-1):
                    print(G+"Fetching new proxies..."+END)
                    findfreeproxy(url)
                #print (r.text)
                z = z+1
                #print("z:"+str(z))
    except:
        print ("\nerror...")

def main():
    banner()
    parser = argparse.ArgumentParser(description='Fake Traffic By Proxy')
    parser.add_argument('url', help='URL to send fake traffic on')
    args = parser.parse_args()
    url = args.url
    print(url)
    collect_HREF_From_URL(url)   
    
if __name__ =='__main__':
        main()
