#!/usr/bin/python3
import cmd
"""
This module contain the HBNB console
We use it to interact with the system
"""


class HBNBCommand(cmd.Cmd):
    '''
    Our command line
    '''
    def do_EOF(self, Line):
        ''' Terminate the program using Ctrl+D'''
        return True

    def do_quit(self, line):
        ''' Quit command to exit the program '''
        return True

    prompt = "(hbnb) "

    def emptyline(self):
        ''' Executed when no command is entered in the command line '''
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
