#!/usr/bin/python3
""" console.py. contains the  entry point of the command
interpreter
"""
import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from shlex import split


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ Holberton Command interpretor
        using cmd module
    """

    prompt = "(hbnb) "
    # get all subclasses of BaseModel
    subclasses = BaseModel.__subclasses__()
    # output>>>
    __classes = [str(sub.__name__) for sub in subclasses]
    # append "BaseModel" to classes
    # output>>> classes = ["User", "State", City",
    # "Place", "Amenity", "Review"]
    __classes.append("BaseModel")
    # we can also use this instead
    # __classes = {
    #     "BaseModel",
    #     "User",
    #     "State",
    #     "City",
    #     "Place",
    #     "Amenity",
    #     "Review"
    # }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """ default action """
        # arg2 = "do_something(arg1, arg2)"
        # match = re.search(r"\((.*?)\)", arg2)
        # new_arg = [arg2[:match.span()[0]], match.group()[1:-1]]
        # print(new_arg)
        commands = {"all": self.do_all,
                    "count": self.do_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update
                    }
        match = re.search(r"\.", arg)
        if match:
            new_arg = [arg[:match.span()[0]], arg[match.span()[1]:]]
            # print(new_arg) test print
            match = re.search(r"\((.*?)\)", new_arg[1])
            if match:
                sub_arg = [new_arg[1][:match.span()[0]], match.group()[1:-1]]
                # print(sub_arg)    #   test print
                if sub_arg[0] in commands:
                    to_be_passed = "{} {}".format(new_arg[0], sub_arg[1])
                    #  print(to_be_passed)  # test print
                    return commands[sub_arg[0]](to_be_passed)
        else:
            print("Unknown syntax: {}".format(arg))
            return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """ 1- Creates a new instance of BaseModel,
            2 - saves it (to the JSON file)
            3 - and prints the id.
        """
        new_arg = parse(arg)
        # we can us print(HBNBCommand.__classes) to see
        # content of the __classes we just created
        if len(new_arg) == 0:
            print("** class name missing **")
        # ----- We can also use this
        # try:
        #     bm1 = eval(new_arg[0])()
        #     storage.save()
        #     # print(bm1.__class__.__name__)
        #     print(bm1.id)
        # except NameError:
        #     print("** class doesn't exist **")
        # -------------------------------------

        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            bm1 = eval(new_arg[0])()
            print(bm1.id)
            # or in short
            # print(eval(new_arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of
            an instance based on the class name and id
        """
        # print(storage.all())
        new_arg = parse(arg)
        # If the class name is missing, print ** class name missing **
        if len(new_arg) == 0:
            print("** class name missing **")
        # If the cls name doesn’t exist, print ** class doesn't exist
        # __** (ex: $ show MyModel)
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        # If the id is missing, print ** instance id missing **
        # __(ex: $ show BaseModel)
        elif len(new_arg) == 1:
            print("** instance id missing **")
        # If the inst of the cls name doesn’t exist for the id,
        # __print ** no instance found **
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            # print(FileStorage.__objects["{}.{}".format
            # (new_arg[0], new_arg[1])])
            # we can use the above or the bellow
            print(storage.all()["{}.{}".format(new_arg[0], new_arg[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file)
        """
        new_arg = parse(arg)
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            all_obj = storage.all()
            key = "{}.{}".format(new_arg[0], new_arg[1])
            del all_obj[key]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all
            instances based or not on the class name
        """
        new_arg = parse(arg)
        if len(new_arg) > 0 and new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            output_objs = []
            for obj in all_objs:
                if len(new_arg) == 0:
                    output_objs.append(all_objs[obj].__str__())
                elif all_objs[obj].__class__.__name__ == new_arg[0]:
                    output_objs.append(all_objs[obj].__str__())
            print(output_objs)

    def do_count(self, arg):
        """ count number of class instances """
        new_arg = parse(arg)
        count = 0
        all_objs = storage.all()
        for key in all_objs:
            if all_objs[key].__class__.__name__ == new_arg[0]:
                count += 1
        print(count)

    def do_update(self, arg):
        """ Updates an instance based on the class
            name and id by adding or updating attribute
            (save the change into the JSON file)
            update <class name> <id> <attribute name> "<attribute value>"
        """
        new_arg = parse(arg)
        all_objs = storage.all()
        #   print(storage.all())    # test print
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        # elif all(all_objs[new_arg[1]] != obj for obj in all_objs.values()):
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in all_objs.keys():
            print("** no instance found **")
        elif len(new_arg) == 2:
            print("** attribute name missing **")
        elif len(new_arg) == 3:
            print("** value missing **")
        elif len(new_arg) == 4:
            # <class name> <id> <attribute name> "<attribute value>
            # all_objs = storage.all()
            # obj_key = all_objs["{}.{}".format(new_arg[0], new_arg[1])]

            # if new_arg[2] in obj_key.to_dict():
            #     obj_type = type(obj_key.to_dict()[new_arg[2]])
            #     obj_key.to_dict()[new_arg[2]] = obj_type(new_arg[3])
            # else:
            #     obj_key.to_dict()[new_arg[2]] = new_arg[3]

            # Temporary Code
            obj = all_objs["{}.{}".format(new_arg[0], new_arg[1])]
            if new_arg[2] in obj.to_dict().keys():
                valtype = type(obj.to_dict()[new_arg[2]])
                obj.__dict__[new_arg[2]] = valtype(new_arg[3])
            else:
                obj.__dict__[new_arg[2]] = new_arg[3]
        elif type(eval(new_arg[2])) == dict:
            obj = all_objs["{}.{}".format(new_arg[0], new_arg[1])]
            for k, v in eval(new_arg[2]).items():
                if (k in obj.to_dict().keys() and
                   type(obj.to_dict()[k]) in {str, int, float}):
                    valtype = type(obj.to_dict()[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v

        #     obj = all_objs["{}.{}".format(new_arg[0], new_arg[1])]
        #     if new_arg[2] in obj.__class__.__dict__.keys():
        #         valtype = type(obj.__class__.__dict__[new_arg[2]])
        #         obj.__dict__[new_arg[2]] = valtype(new_arg[3])
        #     else:
        #         obj.__dict__[new_arg[2]] = new_arg[3]
        # elif type(eval(new_arg[2])) == dict:
        #     obj = all_objs["{}.{}".format(new_arg[0], new_arg[1])]
        #     for k, v in eval(new_arg[2]).items():
        #         if (k in obj.__class__.__dict__.keys() and
        #         type(obj.__class__.__dict__[k]) in {str, int, float}):
        #             valtype = type(obj.__class__.__dict__[k])
        #             obj.__dict__[k] = valtype(v)
        #         else:
        #             obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
