from question_model import Quistions
from data import question_data
from quiz_brain import Quizbrain
from colorama import Fore
import os

quistionbank=[]
for i in question_data:
	qtext=i['text']
	qans=i['answer']
	quistionsd=Quistions(qtext,qans)
	quistionbank.append(quistionsd)
lpd=Quizbrain(quistionbank)
i=1
while i > 0:
	print()
	print(f"{Fore.BLUE}QUIZ\n{'_'*4}{Fore.RESET}")
	print()
	lpd.still_h()
	if lpd.whr:
		os.system('clear')
		break
	else:
		lpd.nextq()
		pass
print()
print(f'{Fore.BLUE}RESULT\n{"_"*6}{Fore.RESET}')
print()
print(f'you scored {lpd.score}/12')
print()
print('pgm over')