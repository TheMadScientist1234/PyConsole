import PyConsole.core.command
import PyConsole.core.commands.command_ls

import PyConsole.display.console

import getpass
from socket import gethostname

class Terminal:
    """Class for managing all terminal operations"""
    # Terminal flags
    quit = False

    cur_dir = ''

    def __init__(self):
        # Create the console object
        self.console = PyConsole.display.console.Console(120, 50)

        # Current directory
        Terminal.cur_dir = 'C:\\Users\\' + getpass.getuser()

        # Commands
        self.commands = {
            'ls': PyConsole.core.commands.command_ls.CommandLs()
        }

        # Clear the Console
        self.console.clear()

        # Start the terminal loop
        self.update()

        # self.console.cprint(getpass.getuser() + ': ', color=PyConsole.display.console.ConsoleColor.BRIGHT_GREEN, newline=False)
        # cinput = self.console.get_input('')
        # if cinput:
        #     if cinput[0] == 'ls':
        #         command.execute(cinput[1:], self.console)

    def update(self):
        """Recursive function for managing the current terminal operation"""
        self.console.cprint(getpass.getuser() + '@' + gethostname() + '#' + Terminal.cur_dir + '$ ', color=PyConsole.display.console.ConsoleColor.BRIGHT_GREEN, newline=False)
        cinput = self.console.get_input('')
        if cinput:
            self.commands[cinput[0]].execute(cinput[1:], self.console)

        if not Terminal.quit:
            self.update()
