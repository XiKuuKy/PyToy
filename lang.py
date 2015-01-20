__author__ = 'Simon'

from subprocess import call
from IPython.terminal.embed import InteractiveShellEmbed
from colorama import Fore, init

class PyToy:
    def __init__ (self,path=None):
        init()
        if path != None:
            self.opPath = path
    def exe(self,cmd):
        call(cmd,shell=True)
    def set_shell_color(self,color):
        call("color "+color,shell=True)
    def printc(self,s,c):
        if c == 'green':
            print(Fore.GREEN + s)
        if c == 'red':
            print(Fore.RED)
        if c == 'blue':
            print(Fore.BLUE + s)
        if c == 'purple':
            print(Fore.PURPLE + s)
    def startIPython(self):
        self.ipshell = InteractiveShellEmbed()
        self.ipshell()
    def stdin(self):
        input('...')
    def printf(self,s):
        print(s,end="")
    def prints(self,s):
        print(s,end=" ")
    def printt(self,s):
        print(s,end="\t")
    def newline(self):
        print("\n")