import time
while True:
	Localtime = time.localtime()
	result = time.strftime("%I:%M:%S%p", Localtime)
	print(result)
	time.sleep(1)
