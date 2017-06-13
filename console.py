#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
'''module: console
This module contains the entry point of command line iterpreter
Includes: help(builtin), EOF, quit, and custom prompt('hbnb')
'''


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    model_id = ""
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        '''if empty line entered pass
        '''
        pass

    def do_EOF(self, line):
        '''EOF command to exit the program
        '''
        return (True)

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return (True)

    def do_create(self, args):
        ''' creates a new instance of class BaseModel
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        arg_list = list(args.split())
        if arg_list[0] in self.classes:
            b_model = eval(arg_list[0])()
            b_model.save()
            self.model_id = b_model.id
            print('{0}'.format(b_model.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        ''' print string representation of instance based on
        class name and ID
        '''
        if self.model_id == "":
            print ("** instance id missing **")
            return
        if len(args) == 0:
            print("** class name missing **")
            return

        all_obj = storage.all()
        arg_list = list(args.split())

        key_name = arg_list[0] + "." + self.model_id

        if arg_list[0] in self.classes:
            if len(arg_list) > 1:
                if arg_list[1] == self.model_id and key_name in all_obj:
                    print(all_obj[arg_list[0] + "." + self.model_id])
                elif arg_list[1] == self.model_id and key_name not in all_obj:
                    print("** no instance found **")
                    return
            else:
                    print("** instance id missing **")
                    return
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        ''' deletes instance based on class name and id
        '''
        if self.model_id == "":
            print ("** instance id missing **")
            return

        if len(args) == 0:
            print("** class name missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())

        if arg_list[0] in self.classes and arg_list[1] == self.model_id:
            del(all_obj[arg_list[0] + "." + self.model_id])
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif arg_list[0] in self.classes and arg_list[1] != self.model_id:
            print("** instance id missing **")

    def do_all(self, args):
        ''' prints all string representation of instances created
        '''
        if self.model_id == "":
            print ("** instance id missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())
        results = []

        if len(args) == 0:
            for obj in all_obj:
                results += [str(all_obj[obj])]
            print(results)
            return

        if arg_list[0] in self.classes:
            for obj in all_obj:
                results += [str(all_obj[obj])]
            print(results)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        '''updates instance based on class name and id by
        adding attribute
        '''
        if self.model_id == "":
            print ("** instance id missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())

        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if len(arg_list) == 1 and arg_list[0] in self.classes:
            print("** instance id missing **")
            return
        if len(arg_list) == 2 and arg_list[
                0] in self.classes and arg_list[1] == self.model_id:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3 and arg_list[0] in self.classes and arg_list[
                1] == self.model_id and arg_list[2]:
            print("** value missing **")
            return
        if len(arg_list) > 4:
            arg_list = arg_list[:4]

        if arg_list[0] in self.classes:
            if arg_list[1] != self.model_id:
                print("** no instance found **")
                return
            if arg_list[1] == self.model_id and hasattr(
                    eval(arg_list[0]), arg_list[2]) is False:
                print("** attribute name missing **")
                return
            elif arg_list[1] == self.model_id and hasattr(
                    eval(arg_list[0]), arg_list[2]) is True:
                all_obj[arg_list[0] + "." + self.model_id].__dict__[
                    arg_list[2]] = arg_list[3].replace('\"', '')
                storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
