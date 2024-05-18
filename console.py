#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Simple command line for the
    HBNB project.
    """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """exit the Command line"""
        exit()

    def do_EOF(self, line):
        """exits the Command line"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
