import os
hi = '\x1b[1;91m' 
def kontol():
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
		print("")
		os.system("git pull")
		print(f'{hi}─'*30)
		print(f"{hi}Waiting For Update.!")
		print(f"{hi}Thanks To Jun Pakaya:v")
		print(f'{hi}─'*30)
		os.system("xdg-open https://m.facebook.com/jun.WA08988884579");exit()
#if __name__=='__main__':
	#print("")
	#print("")
	#kontol()