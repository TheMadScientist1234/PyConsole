import PyConsole.core.command
import PyConsole.core.option
import PyConsole.core.terminal

import PyConsole.display.console

import os

class CommandLs(PyConsole.core.command.Command):
    """
    LS: List all files and folders in the current directory

    Options:
    -l, --long: detailed list mode
    """
    def __init__(self):
        self.cstr = 'ls'

    def execute(self, args: list, console: PyConsole.display.console.Console)->bool:
        parsed_args = self._parse_options(args)
        for dir in os.listdir(PyConsole.core.terminal.Terminal.cur_dir):
            console.cprint(dir)
