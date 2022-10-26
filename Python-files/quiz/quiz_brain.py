from colorama import Fore
import os
from time import sleep
class Quizbrain:
	def __init__(self,qlist):
		self.qno=0
		self.qlist=qlist
		self.whr=None
		self.score=0
	def nextq(self):
		cq=self.qlist[self.qno]
		s=input(f'{self.qno+1}.) {cq.text} (true/false) : ')
		self.qno+=1
		self.gns=s
		if cq.answer==(s).lower():
			print()
			print(f'{Fore.GREEN}you got it right !{Fore.RESET}')
			self.score+=1
		else:
			print()
			print(f'{Fore.RED}wrong answer !{Fore.RESET}')
		sleep(0.7)
		os.system('clear')
	def still_h(self):
		if self.qno==len(self.qlist):
			self.whr=True
		else:
			self.whr=False
	
		