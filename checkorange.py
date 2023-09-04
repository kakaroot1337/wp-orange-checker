# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##AwAwAw##
#### PS: CHANGE Your Threads pool on line 352 to make script more faster :)
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """                                                   
Mass Check WP INSTALL
P3TRUK - INFINITY CYBER TEAM
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



print_logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
	pass
	
try:
    ooo = list((ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count

##########################################################################################
def jamet1(url):
    try:
        Agent1 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        cek = requests.get(url, headers=Agent1, timeout=5)
        if 'WordPress Social Login' in cek.text.encode('utf-8'):
            print(ktngreen + '[Ok] Live kayanya(OJS VALID FILES)' + '(' + url + ')'+ CEND)
            open('Valid-Mini-Orange.txt', 'a').write(url+'\n')            
        else:
             print(ktnred + '[Not] Live' + '(' + url + ')' + CEND)
             open('mati.txt', 'a').write(url+'\n')
    except:
        pass
    pass

def Jenderal92(url):
	try:
		jamet1(url)
	except:
		pass
##########################################################################################
def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pr = pp.map(Jenderal92, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
    
