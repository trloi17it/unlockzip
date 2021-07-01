import zipfile,time,sys

start_time =time.time()

def extract():
	filename = zipfile.ZipFile(r'your url file zip') #C:/Users/.....
	for num in range(1,99999,1):
		try:
			pwd =str(num)
			filename.extractall(path='.',pwd=pwd.encode('utf-8'))
			print ("PassWord: ",pwd)
			end_time =time.time()
			print ("Then %" %(end_time-start_time))
			sys.exit(0)
		except Exception as e:
			pass
if __name__ == "__main__":
	extract()