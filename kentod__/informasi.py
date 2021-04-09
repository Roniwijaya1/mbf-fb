import requests as req,re,json,os
uid=None
username=None
class info:
	def __init__(self,kuki,url):
		self.kuki,self.url=kuki,url
	def myinfo(self):
		global uid,username
		try:
			kontol=req.get(f"{self.url}/profile.php?v=info",cookies=self.kuki).text
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("[!] Kesalahan Pada Koneksi")
		if "Facebook - Masuk atau Daftar" in kontol or "Masuk ke Facebook" in kontol or "Epsilon" in kontol:
			try:os.remove("lo_ngentod/cookie");os.remove("lo_ngentod/token");os.remove("lo_ngentod/my_info")
			except:os.system("rm -rf lo_ngentod/cookie && rm -rf lo_ngentod/token && rm -rf lo_ngentod/my_info")
			exit("[!] Cookies Kedaluwarsa, Harap Login Ulang")
		else:
			try:uid=re.findall("/(\d*)/allactivity",kontol)[0]
			except:pass
			nama=re.findall("\<title\>(.*?)<\/title\>",kontol)[0]
			try:username=re.findall('> . <a href="\/(.*?)\/friends',kontol)[0]
			except:pass
			open("lo_ngentod/my_info","w").write(json.dumps({"uid":uid,"nama":nama,"username":username}))