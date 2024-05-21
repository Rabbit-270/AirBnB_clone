#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
"""
This module contain the HBNB console
We use it to interact with the system
"""


class HBNBCommand(cmd.Cmd):
    '''
    Our command line
    '''
    CLASSES = ['BaseModel']
    def do_EOF(self, Line):
        ''' Terminate the program using Ctrl+D'''
        print()
        exit()

    def do_quit(self, line):
        ''' Quit command to exit the program '''
        exit()
    
    prompt = "(hbnb)"

    def emptyline(self):
        ''' Executed when no command is entered in the command line '''
        pass

    def do_create(self, argv):
        '''
Create command that creates a new
BaseModel object, saves it
and returns the new object's id.
        '''
        if len(argv) == 0:
            print("** class name missing **")
        else:
            if argv != 'BaseModel':
                print("** class doesn't exist **")
            else:
                newObject = BaseModel()
                return newObject.id

    def do_show(self, argv):
        '''
Show command to print a string representation
of an instance based on its class name and id
provided
        '''
        if len(argv) == 0:
            print("** class name missing **")
        else:
            whitespaces = 0
            index = -1
            counter = 0
            while counter < len(argv):
                currChar = argv[counter]
                if currChar == " ":
                    whitespaces += 1
                    index = counter
                    break
                else:
                    counter += 1
        if counter == (len(argv) - 1):
            if argv != 'BaseModel':
                print("** class doesn't exist **")
        elif whitespaces != 0:
            retrievedClassName = argv[:index]
            retrievedId = argv[(index+1):]
            KEY = "{}.{}".format(retrievedClassName, retrievedId)
            '''
            retrieve all objects and search
            '''
            ALL_OBJS = storage.all()
            for key in ALL_OBJS.keys():
                if key == KEY:
                    foundObject = ALL_OBJS[key]
                    foundObjectInstance = BaseModel(**foundObject)
                    print(foundObjectInstance)
                else:
                    pass
            print("** no instance found **")
        elif whitespaces == 0:
            print("** instance id missing **")
    return
            

    
if __name__=="__main__":
    HBNBCommand().cmdloop()
