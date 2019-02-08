import PyConsole.core.command
import PyConsole.core.commands.command_ls
import PyConsole.core.commands.command_exit

import PyConsole.display.console

import getpass
from socket import gethostname
import os
from win32com.client import GetObject

class Terminal:
    """Class for managing all terminal operations"""
    # Terminal flags
    quit = False
    closing_window = False

    cur_dir = ''

    def __init__(self):
        # Create the console object
        self.console = PyConsole.display.console.Console(120, 50)

        # Current directory
        Terminal.cur_dir = 'C:\\Users\\' + getpass.getuser()

        # Commands
        self.commands = {
            'ls': PyConsole.core.commands.command_ls.CommandLs(),
            'exit': PyConsole.core.commands.command_exit.CommandExit()
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
            if cinput[0] in self.commands:
                self.commands[cinput[0]].execute(cinput[1:], self.console)
            else:
                os.system(' '.join(cinput))

        if not Terminal.quit:
            self.update()
        if Terminal.closing_window:
            WMI = GetObject('winmgmts:')
            processes = WMI.InstancesOf('Win32_Process')
            for p in WMI.ExecQuery('select * from Win32_Process where Name="cmd.exe"'):
                os.system('taskkill /pid ' + str(p.Properties_('ProcessId').Value))
