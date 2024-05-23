#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
"""
This module contain the HBNB console
We use it to interact with the system
"""


class HBNBCommand(cmd.Cmd):
    '''
    Our command line
    '''
    CLASSES = ['BaseModel', 'User']

    def do_EOF(self, Line):
        ''' Terminate the program using Ctrl+D'''
        return "(hbnb)"

    def do_quit(self, line):
        ''' Quit command to exit the program '''
        return "(hbnb)"

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
            if argv not in self.CLASSES:
                print("** class doesn't exist **")
            else:
                if argv == 'BaseModel':
                        newObject = BaseModel()
                        storage.new(newObject)
                        storage.save()
                        print(newObject.id)
                elif argv == 'User':
                        newObject = User()
                        storage.new(newObject)
                        storage.save()
                        print(newObject.id)

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
                if argv not in  self.CLASSES:
                    print("** class doesn't exist **")
            elif whitespaces != 0:
                retrievedClassName = argv[:index]
                retrievedId = argv[(index+1):]
                KEY = "{}.{}".format(retrievedClassName, retrievedId)
                '''
                retrieve all objects and search
                '''
                if retrievedClassName not in self.CLASSES:
                    print("** class doesn't exist **")
                else:
                    ALL_OBJS = storage.all()
                    found = False
                    for key in ALL_OBJS.keys():
                        if key == KEY:
                            found = True
                            foundObject = ALL_OBJS[key]
                            print(foundObject)
                            break
                        else:
                            pass
                    if found is False:
                        print("** no instance found **")
            elif whitespaces == 0:
                print("** instance id missing **")

    def do_destroy(self, argv):
        '''
    Deletes an instance based on the id and class name given
        '''
        ObjectFound = False
        if len(argv) == 0:
            print("** class name missing **")
        else:
            whitespaces = 0
            index = -1
            counter = 0
            while counter < len(argv):
                currChar = argv[counter]
                if currChar != " ":
                    counter += 1
                else:
                    index = counter
                    whitespaces += 1
                    break
            if whitespaces == 0:
                print("** instance id missing **")
            else:
                '''
                both id and class name are provided
                '''
                classNameFromCmm = argv[:index]
                idFromCmm = argv[(index + 1):]
                if classNameFromCmm not in self.CLASSES:
                    print("** class doesn't exist **")
                else:
                    KeyGenerated = "{}.{}".format(classNameFromCmm, idFromCmm)
                    OBJECTS = storage.all()
                    for key in OBJECTS.keys():
                        if key == KeyGenerated:
                            ObjectFound = True
                            del OBJECTS[KeyGenerated]
                            break
                    if ObjectFound is not True:
                        print("** no instance found **")
                    else:
                        for KEY in OBJECTS.keys():
                            storage.new(OBJECTS[KEY])
                        storage.save()

    def do_all(self, argv):
        '''
        Prints all string represenetations of an object
        '''
        if len(argv) != 0 and argv not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            classFromCommand = None
            if len(argv) == 0:
                classFromCommand = 'BaseModel'
            else:
                classFromCommand = argv
            OBJECTS_ALL = storage.all()
            OBJECTS = []
            for obj in OBJECTS_ALL:
                OBJECTS.append(obj)
            counter = 0
            print("[", end="")
            classObjects = []
            for key in OBJECTS_ALL.keys():
                if key.find(classFromCommand) != -1:
                    classObjects.append(OBJECTS_ALL[key])
            for i in range(len(classObjects)):
                 currIddObject = classObjects[i]
                 print('"', end="")
                 print(currIddObject, end="")
                 if (i + 1) == len(classObjects):
                     '''counter is on the last element'''
                     print('"', end="")
                 else:
                    '''counter is not the last element'''
                    print('"', end=',')
            print("]")

    def do_update(self, argv):
        '''
        Updates an object with a given class name and id.
        Updates/adds the given attribute using the commandline
        '''
        if len(argv) == 0:
            print("** class name missing **")
        else:
            WHITESPACE_INDICES = []
            startIndex = 0
            counter = 0
            for i in range(len(argv)):
                j = argv.find(" ", startIndex)
                if j != -1:
                    WHITESPACE_INDICES.append(j)
                    startIndex = j + 1
                    counter += 1
            if counter == 3:
                className = argv[:(WHITESPACE_INDICES[0])]
                ID = argv[(WHITESPACE_INDICES[0] + 1):(WHITESPACE_INDICES[1])]
                st = (WHITESPACE_INDICES[1] + 1)
                end = (WHITESPACE_INDICES[2])
                ATTRIBUTE = argv[st:end]
                VALUE = argv[(WHITESPACE_INDICES[2] + 2):(len(argv) - 1)]
                if className not in self.CLASSES:
                    print("** class doesn't exist **")
                else:
                    KEY = "{}.{}".format(className, ID)
                    ALL_OBJS = storage.all()
                    found = False
                    foundObject = None
                    for key in ALL_OBJS.keys():
                        if key == KEY:
                            found = True
                            foundObject = ALL_OBJS[key]
                            dictionary = foundObject.to_dict()
                            dictionary[ATTRIBUTE] = VALUE
                            if className == 'User':
                                    foundObject_re = User(**dictionary)
                            elif className == 'BaseModel':
                                    foundObject_re = BaseModel(**dictionary)
                            storage.new(foundObject_re)
                            storage.save()
                    if found is not True:
                        print("** no instance found **")
            elif counter == 2:
                className = argv[:(WHITESPACE_INDICES[0])]
                ID = argv[(WHITESPACE_INDICES[0] + 1):(WHITESPACE_INDICES[1])]
                ATTRIBUTE = argv[(WHITESPACE_INDICES[1] + 1):]
                if className not in self.CLASSES:
                    print("** class doesn't exist **")
                else:
                    KEY = "{}.{}".format(className, ID)
                    ALL_OBJS = storage.all()
                    found = False
                    foundObject = None
                    for key in ALL_OBJS.keys():
                        if key == KEY:
                            found = True
                            foundObject = ALL_OBJS[key]
                            print("** value missing **")
                    if found is not True:
                        print("** instance not found **")
            elif counter == 1:
                className = argv[:(WHITESPACE_INDICES[0])]
                ID = argv[(WHITESPACE_INDICES[0] + 1):]
                if className not in self.CLASSES:
                    print("** class doesn't exist **")
                else:
                    KEY = "{}.{}".format(className, ID)
                    ALL_OBJS = storage.all()
                    found = False
                    for key in ALL_OBJS.keys():
                        if key == KEY:
                            found = True
                            print("** attribute name missing **")
                    if found is not True:
                        print("** instance not found **")
            elif counter == 0:
                className = argv
                if className in self.CLASSES:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
