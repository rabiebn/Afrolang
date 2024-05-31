#!/usr/bin/python3
"""
CLI For our Afrolang app
"""
from datetime import datetime
from afrolang.base_model import BaseModel
import cmd


class AfroCommand(cmd.Cmd):
    """Afro Console"""
    prompt = '(afro) '


    def do_EOF(self, arg):
        """Exit"""
        return True
    
    def do_quite(self, arg):
        """quits program"""
        return True
    
    def emptyline(self) -> bool:
        """Overwriting the empty line method""" 
        return False
    
    def do_create(self):
        """Creates a new instance of a class"""
        pass

    def do_show(self):
        """Display instances of a class"""
        pass

    def do_destroy(self):
        """Deletes an instance of a class"""
        pass
