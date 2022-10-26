from colorama import Fore,Style
from os import system

print('This python program will allow you to convert english to morse code and vise versa .')
print()
start=input('can we start ? : (y/n) ')
print()
if start.lower()=='y':
	system('clear')
	morsedict={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----','/':'-..-.','@':'.--.-.','!':'-.-.--','&':'.-...','(':'-.--.',')':'-.--.-','=':'-...-',',':'--..--','\'':'.----.','"':'.-..-.',':':'---...'}
	while True:
		choice=input('Enter your choice\na.)convert english to morse code\nb.)convert morse code to english\n(a/b) : ')
		if choice.lower()=='a':
			converted=''
			print()
			inpt=input('enter what you want to convert ? : ')
			for i in inpt:
				if i.lower() in morsedict:
					converted+=morsedict[i.lower()]+' '
				else:
					print()
					print(f'{Fore.RED}error : there is no morse code for \'{i}\'{Style.RESET_ALL}')
					break
			else:
				print()
				print(f'morse code for your input is : {Fore.BLUE}{converted}{Style.RESET_ALL}')
				print()
		elif choice.lower()=='b':
			converted=''
			print()
			inpt=input('enter the morse code that you want to convert : ')
			for i in (inpt.split(' ')):
				key_list = list(morsedict.keys())
				val_list = list(morsedict.values())
				if i in val_list:
					converted+=key_list[val_list.index(i)]
				else:
					print()
					print(f'{Fore.RED}error : there is no english alphabet for \'{i}\'{Style.RESET_ALL}')
					break
			else:
				print()
				print(f'english for your input is : {Fore.BLUE}{converted}{Style.RESET_ALL}')
				print()

		else:
			print()
			print(f'{Fore.RED}error : your choice is not in options .{Style.RESET_ALL}')
		print()
		rech=input('do you want to start over ? : (y/n) ')
		print()
		if rech.lower()=='y':
			system('clear')
			pass
		elif rech.lower()=='n':
			print()
			print('ok')
			break
		else:
			print(f'{Fore.RED}error : your choice is not in options .{Style.RESET_ALL}')
			break
elif start.lower() == 'n':
	print('ok .')
else:
	print(f'{Fore.RED}error : your choice is not in options .{Style.RESET_ALL}')
print()
print('program over.')