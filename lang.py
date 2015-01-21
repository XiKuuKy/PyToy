# Unimportant
__author__ = 'Simon'
# Imports
from subprocess import call
from IPython.terminal.embed import InteractiveShellEmbed
from colorama import Fore, init
# PyToy's language class
class PyToy:
    # Initialize the OOP
    def __init__ (self,path=None,version='1.0',name="Untitled"):
        """
        Initiation. path for a easy variable. version is the app's version. name for the name of the project
        Example:
            toy = lang.PyToy(path="/",version="0.1",name="PyToy")
        """
        # class declarations
        self.version=version
        self.name=name
        self.tab = "\t"
        self.nl="\n"
        self.ws = " "
        # Init colorama
        init()
        # Check if path exists
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
        # call the cmd from the function
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
        #Use the builtin color command
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
        # Check if the color is green
        if c == 'green':
            # If so print with that color
            print(Fore.GREEN + s)
        # Check if the color is red
        if c == 'red':
            # If so print with the color red
            print(Fore.RED)
        # Check if the color is blue
        if c == 'blue':
            # If so print with the color blue
            print(Fore.BLUE + s)
        # Check if the color is purple
        if c == 'purple':
            # If so print with the color purple
            print(Fore.PURPLE + s)
    def ipy(self):
        """
        ipy():
            start an IPython shell
        Example:
            toy.ipy()
        :return:
        """
        # Assign the interactive shell to ipshell
        self.ipshell = InteractiveShellEmbed()
        # start the interactive shell
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
        # Uncollected input that isn't going to be recorded
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
        # print but make the end of it blank
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
        # print but the end is a space
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
        # print with the end being a tab
        print(s,end="\t")
    def newline(self):
        """
        newline():
            prints a newline.
        Example:
            newline()
        :return:
        """
        # print a newline
        print("\n")
