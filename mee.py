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
sys.stdout.write('\x1b]2;PANDA-X 7.0 VERSION\x07')
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
