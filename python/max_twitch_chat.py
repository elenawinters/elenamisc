import math

while True:  # 500 is too long. Web browser accepts it but it doesn't get sent to the chat server. i'll do more testing another time
	text = input('What do you want to max out?: ')
	print('')
	print(text * math.trunc((500) / len(text)), end='\n\n')
