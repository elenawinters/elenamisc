import pyperclip
import math

while True:  # 500 is the max
	text = input('What do you want to max out?: ')
	full = text * math.trunc((500) / len(text))
	print(f'\nlen {len(full)}\n\n{full}\n')
	pyperclip.copy(full)
