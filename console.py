#!/usr/bin/python3
"""This module supplies a console that interracts with the airbnb system"""

from models.base_model import BaseModel
from models import storage
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    defines a class that inherits from cmd with its attributes and methods
    """

    prompt = "(hbnb) "
    Classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    do_quit = do_EOF

    def emptyline(self):
        pass

    def do_create(self, line=None):
        """ Create new instance of BaseModel"""

        if not line:
            print(f"** class name missing **")
        elif line in self.Classes:
            obj = self.Classes[line]()
            obj.save()
            print(obj.id)
        else:
            print(f"** class doesn't exist **")

    def do_show(self, line=None):
        """Prints the string representation of an instance """
        """based on the class name and id"""

        if line:
            if " " in line:
                classname, id = line.split()
                if classname not in self.Classes:
                    print(f"** class doesn't exist **")
                else:
                    key = classname + "." + id
                    all_instance = storage.all()

                    if key in all_instance.keys():
                        obj = all_instance[key]
                        print(obj)
                    else:
                        print(f"** no instance found **")
            else:
                print(f"** instance id missing **")
        else:
            print(f"** class name missing **")

    def do_destroy(self, line=None):
        """Deletes an instance based on the class name and id"""
        if line:
            if " " in line:
                classname, id = line.split()
                key = classname + "." + id
                all_instance = storage.all()
                if classname not in self.Classes:
                    print(f"** class doesn't exist **")
                elif key not in all_instance.keys():
                    print(f"** no instance found **")
                else:
                    all_instance.pop(key)
                    storage.save()
            else:
                print(f"** instance id missing **")
        else:
            print(f"** class name missing **")

    def do_all(self, line=None):
        """Prints all string representation of all
        instances based or not on the class name"""
        all_instance = storage.all()
        if line:
            if line in self.Classes:
                for key, value in all_instance.items():
                    name, id = key.split(".")
                    if line == name:
                        print(value)
            else:
                print(f"** class doesn't exist **")
        else:
            for key, value in all_instance.items():
                print(value)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        space_count = 0
        if line:
            for i in line:
                if i == " ":
                    space_count += 1
            if space_count == 0:
                print(f"** instance id missing **")
            elif space_count == 1:
                print(f"** attribute name missing **")
            elif space_count == 2:
                print(f"** value missing **")
            elif space_count == 3:
                all_instance = storage.all()
                classname, id, attr_name, attr_value = line.split()
                classname = classname.strip('\'"')
                id = id.strip('\'"')
                attr_name = attr_name.strip('\'"')
                attr_value = attr_value.strip('\'"')

                key = classname + "." + id

                if key in all_instance.keys():
                    instance = all_instance[key]
                    setattr(instance, attr_name, attr_value)
                    instance.save()

    def default(self, line):
        """Handles commands that are not in do"""
        if ".all()" in line:
            command = line.split(".")
            self.do_all(command[0])
        elif ".count()" in line:
            count = 0
            all_instance = storage.all()
            for k, v in all_instance.items():
                if line.split(".")[0] in k:
                    count += 1
            print(count)
        elif ".show(" in line or ".destroy(" in line:
            class_name, rest = line.split(".")
            if "'" in rest:
                split_char = "'"
            else:
                split_char = '"'
            rest = rest.split(split_char)
            if len(rest) >= 3:
                obj_id = rest[1]
                if ".show(" in line:
                    self.do_show(class_name + " " + obj_id)
                elif ".destroy(":
                    self.do_destroy(class_name + " " + obj_id)
            else:
                self.do_show(class_name)
        elif ".update(" in line:
            class_name, rest = line.split(".")
            separator = rest.count(", ")
            rest = rest.split(", ")

            if separator == 0:
                if '("' in rest[0]:
                    obj_id = rest[0].split('(')
                    self.do_update(class_name + " " + obj_id[1])
                else:
                    self.do_update(class_name)
            elif separator == 1:
                obj_id = rest[0].split('(')
                self.do_update(class_name + " " + obj_id[1] + " " + rest[1])
            elif separator == 2:
                obj_id = rest[0].split('(')
                attr_value = rest[2].split(")")
                self.do_update(f'{class_name} {obj_id[1]} ' +
                               f'{rest[1]} {attr_value[0]}')

        else:
            print(f"*** Unknown command: {line} ***")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
