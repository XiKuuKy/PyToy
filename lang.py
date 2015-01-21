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
        """
        set_shell_color(color):
            set the color of the entire shell
        example:
            toy.set_shell_color('red')
        :param color:
        :return:
        """
        call("color "+color,shell=True)
    def printc(self,s,c):
        """
        printc:
            colored print()
        Example:
            toy.printc("Hello, World!",'green')
        :param s:
        :param c:
        :return:
        """
        if c == 'green':
            print(Fore.GREEN + s)
        if c == 'red':
            print(Fore.RED)
        if c == 'blue':
            print(Fore.BLUE + s)
        if c == 'purple':
            print(Fore.PURPLE + s)
    def ipy(self):
        """
        ipy():
            start an IPython shell
        Example:
            toy.ipy()
        :return:
        """
        self.ipshell = InteractiveShellEmbed()
        self.ipshell()
    def stdin(self):
        """
        stdin():
            waits for input
        Example:
            print('Hello')
            toy.stdin()
        :return:
        """
        input('...')
    def printf(self,s):
        """
        printf(string):
            print with no new line
        Example:
            toy.printf("Hi")
        :param s:
        :return:
        """
        print(s,end="")
    def prints(self,s):
        """
        prints(string):
            prints a whitespace after the string
        Example:
            toy.prints("There will be a space after this")
        :param s:
        :return:
        """
        print(s,end=" ")
    def printt(self,s):
        """
        printt(string):
            print with a ending tab.
        Example:
            toy.printt("Look out incoming tab!")
        :param s:
        :return:
        """
        print(s,end="\t")
    def newline(self):
        """
        newline():
            prints a newline.
        Example:
            newline()
        :return:
        """
        print("\n")
