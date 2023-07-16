#!/usr/bin/env python3
""" Defines the HBNB console """
import cmd

class HBNBCommand(cmd.Cmd):
    'Class for the AirBnB console'
    prompt = '(hbnb)'

    def do_quit(self, arg):
        'Stop the console, close the window and exit'
        return True
    def do_EOF(self, line):
        'Handle the EOF signal to exit program'
        return True
    def emptyline(self):
        'Called when an empty line is entered'
        pass

if __name_ == '__main__':
    HBNBCommand().cmdloop()
