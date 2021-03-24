print("importando modulos")
import os,psutil,platform,sys,requests,json,socket,nmap3,wget,zipfile
from bs4 import BeautifulSoup 
from base64 import b64decode
from random import choice
os.system("clear")
def banner():
	formats = [
	"gay",
	"crop"
	]
	fonts = [
	"pagga",
	"smblock",
	"smbraille",
	"smmono12",
	"smmono9",
	"emboss",
	"emboss2",
	"mini"]
	banners = "toilet -f "
	a = os.popen(f"toilet -f {choice(fonts)} -F {choice(formats)} flyead tools|lolcat")
	print(a.read())
def my_infoRmation():
	uname = platform.uname()
	print(
		f"""\n\n
|-----------------------------
| - System: {uname.system}    
| - Node Name: {uname.node}	  
| - Release: {uname.release}  
| - Version: {uname.version}  
| - Machine: {uname.machine}  
|-----------------------------
""")
def get_code_for_tryhackme():
	print("\nINVITE CODE OF HTB ---------- ")
	url = "https://www.hackthebox.eu/api/invite/generate"
	headers = {'Content-type': 'application/json; charset=utf-8', 'Accept': 'text/json', 'user-agent' : 'anything!'}
	payload = {'key': 'value'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	print(f"""
status code : {r.status_code}
code : {json.loads(r.text)['data']['code']}
decrypted : {b64decode(json.loads(r.text)['data']['code']).decode('utf-8')}
---------------------------------------""")
def view_web(web):
	web = web
	try:
		nmap = nmap3.Nmap()
		ports = nmap.scan_top_ports(web)
		asd = json.dumps(ports, indent=3)
		ai = json.loads(asd)[socket.gethostbyname(web)]['ports']
		a = 0
		print(f"HOST : {socket.gethostbyname(web)}")
		for i in ai:
			print(f"""
\n---- informacion recogida numero {a} ----------------
protocolo : {ai[a]['protocol']}
puerto : {ai[a]['portid']}
estado : {ai[a]['state']}
razon : {ai[a]['reason']}

nombre del servicio : {ai[a]['service']['name']}""")
			a+=1
		opt = input("\ndesea volver repetir el proceso? [Y][N] > ")
		if opt.lower() == "y":
			os.system("clear")
			web = input("ingrese la web > ")
			view_web(web)
		elif opt.lower() == "n":
			opt = input("\ndesea volver al menu? [Y][N] > ")
			if opt == "y":
				os.system("clear")
				menu()
			else:
				print("gracias por haber usado mi script")
				sys.exit()
		while opt.lower() not in ["y","n"]:
			os.system("clear")
			print("opcion no valida")
			opt = input("\ndesea volver repetir el proceso? [Y][N] > ")
			if opt.lower() == "y":
				os.system("clear")
				web = input("ingrese la web > ")
				view_web(web)
			elif opt.lower() == "n":
				opt = input("\ndesea volver al menu? [Y][N] > ")
				if opt == "y":
					os.system("clear")
					menu()
				else:
					os.system("clear")
					print("gracias por haber usado mi script")
					sys.exit()
	except:
		os.system("clear")
		print("< ERROR > DEBE INGRSESAR UNA WEB VALIDA")
		opt = input("\ndesea volver repetir el proceso? [Y][N] > ")
		if opt.lower() == "y":
			os.system("clear")
			web = input("ingrese la web > ")
			view_web(web)
		elif opt.lower() == "n":
			opt = input("\ndesea volver al menu? [Y][N] > ")
			if opt == "y":
				os.system("clear")
				menu()
			else:
				print("gracias por haber usado mi script")
				sys.exit()
		while opt.lower() not in ["y","n"]:
			os.system("clear")
			print("opcion no valida")
			opt = input("\ndesea volver repetir el proceso? [Y][N] > ")
			if opt.lower() == "y":
				os.system("clear")
				web = input("ingrese la web > ")
				view_web(web)
			elif opt.lower() == "n":
				opt = input("\ndesea volver al menu? [Y][N] > ")
				if opt == "y":
					os.system("clear")
					menu()
				else:
					os.system("clear")
					print("gracias por haber usado mi script")
					sys.exit()
def making_phishing():
	uname = platform.uname()
	if "zphisher" in os.listdir():
		pass
	else: 
		print("[*] instalando zphisher ...")
		os.system("git clone https://github.com/htr-tech/zphisher > /dev/null 2>&1")
		print("[----> listo")
		print("[*] instalando paquetes necesarios ...")
		if uname.node == "kali":
			os.system("sudo apt-get install curl php unzip wget")
		else:
			os.popen("apt install curl php unzip wget -y")
		print("[*] instalacion de paquetes completada ...")
	opt = input("[--] desea iniciar el programa? [Y][N] > ")
	if opt.lower() == "n":
		opt = input("[--] desea ir al menu? [Y][N] > ")
		if opt.lower() == "n":
			print("gracias por usar el programa")
			sys.exit()
		else:
			os.system("clear")
			menu()
	elif opt.lower() == "y":
		os.system("cd zphisher;./zphisher.sh")
		opt = input("\n[--] desea ir al menu? [Y][N] > ")
		if opt.lower() == "n":
			print("gracias por usar el programa")
		else:
			os.system("clear")
			menu()
def mask_link():
	try:
		req = requests.session()
		print("-----------------------------------------")
		webx = input("[*] ingrese su web > ")
		print("-----------------------------------------")
		params = {
		"url":f"{webx}",
		}
		url = req.post("https://shorte.st/shortener/shorten",data=params)
		web = json.loads(url.text)['shortenedUrl']
		print(f"[1] url enmascarado > {web}")
		print("--------------------------------------------")
		web_re = input("ingrese la web que quiere remplazar > ")
		print("--------------------------------------------")
		print(f"[2] url enmascarado > {web_re}@{webx}")
		url_2 = req.get(f"https://vurl.com/api.php?url={webx}")
		print(f"[3] url enmascarado > {url_2.text}")
	except:
		print("[X] error > ingrese una web valida ( sin http o https)")
def menu_v():
	opt = input("desea volver al menu? [Y][N] > ")
	if opt.lower() == "y":
		os.system("clear")
		menu()
	else:
		os.system("clear")
		print("gracias por usar mi script :D")
		sys.exit()
def menu():
	banner()
	def option_p():
		print("""
OPTIONS ---------------------
1) GET A HACK THE BOX INVITE CODE
2) VIEW YOUR INFORMATION
3) GET A INFORMATION OF A WEB
4) MAKE FALSE LINK FOR PHISHING
5) PUT MASK IN YOUR LINK
---------------------------END""")
	option_p()
	option = input("\ninput your option > ")
	if option =="1":
		get_code_for_tryhackme()
		menu_v()
	elif option =="2":
		my_infoRmation()
		menu_v()
	elif option =="3":
		os.system("clear")
		web = input("input your web > ")
		view_web(web)
	elif option == "4":
		making_phishing()
	elif option == "5":
		mask_link()
		menu_v()
	while option not in ['1','2','3',"4","5"]:
		os.system("clear")
		banner()
		option_p()
		print("\n« ERROR » OPCION NO RECONOCIDA\n")
		option = input("por favor ingrese una opcion valida > ")
		if option =="1":
			get_code_for_tryhackme()
			menu_v()
		elif option =="2":
			my_infoRmation()
			menu_v()
		elif option =="3":
			os.system("clear")
			web = input("input your web > ")
			view_web(web)
		elif option == "4":
			making_phishing()
		elif option == "5":
			mask_link()
			menu_v()
def main():
	os.system("clear")
	menu()
if __name__ == '__main__':
	try:
		main()
	except:
		os.system("clear")
		print("Gracias por usar mi script :D")
		sys.exit()