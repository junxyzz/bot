import os
from main import c as main


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
