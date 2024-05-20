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
        '''
        Parse end-of-file-marker in the hbnb commnd line
        and return True to terminate the program
        '''
        return True

    def do_quit(self, line):
        '''
exit the program
        '''
        return True

    prompt = "(hbnb) "

    def emptyline(self):
        '''
Executed when no command is entered in the command line
        '''
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
