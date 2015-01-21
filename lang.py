__author__ = 'Simon'

from subprocess import call
from IPython.terminal.embed import InteractiveShellEmbed
from colorama import Fore, init

class PyToy:
    def __init__ (self,path=None,version='1.0',name="Untitled"):
        """
        Initiation. path for a easy variable. version is the app's version. name for the name of the project
        Example:
            toy = lang.PyToy(path="/",version="0.1",name="PyToy")
        """
        self.version=version
        self.name=name
        self.tab = "\t"
        self.nl="\n"
        self.ws = " "
        init()
        if path != None:
            self.opPath = path
    def exe(self,cmd):
        """
        For executing commands from the command line. cmd is the command.
        Example:
            toy.exe("ECHO Hi!")
        :param cmd:
        :return:
        """
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
    def ipy(self):
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
