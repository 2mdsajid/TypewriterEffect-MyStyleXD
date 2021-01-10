import time, os

def type(text):
	list = []
	for char in text:
		list.append(char)
		time.sleep(0.1)
		os.system( 'clear' )
		print(*list,sep="")
	
text = input("> ")
type(text)