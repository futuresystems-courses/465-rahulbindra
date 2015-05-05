from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_supercool.command_supercool import command_supercool


class cm_shell_supercool:

    def activate_cm_shell_supercool(self):
        self.register_command_topic('mycommands', 'supercool')

    @command
    def do_supercool(self, args, arguments):
     """
     Usage:
          supercool NAME

          Checks if the named file exists in root folder else giver error

          Arguments:

            NAME      Name of the file to create

          Options:

             -v       verbose mode

     """
     if arguments["NAME"] is None:
     	Console.error("Please specify a file name")
     else:
	file = arguments["NAME"]
        Console.info("Trying to create {0}".format(file))
        status = command_supercool.status(file)
       	if status:
		Console.error("A file with same name already exists in root!")
        else:
       	        Console.info(file + " can be created in the root folder.")

if __name__ == '__main__':
	command = cm_shell_supercool()
