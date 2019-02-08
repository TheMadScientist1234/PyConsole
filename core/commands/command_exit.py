import PyConsole.core.command
import PyConsole.core.option
import PyConsole.core.terminal

import PyConsole.display.console

class CommandExit(PyConsole.core.command.Command):
    """
    EXIT: exit out of PyConsole

    Options:
    -q: quit out of the command prompt also
    """
    def __init__(self):
        self.cstr = ''

    def execute(self, args: list, console: PyConsole.display.console.Console):
        parsed_args = self._parse_options(args)
        quiting = False
        for arg in parsed_args:
            if arg.cname == 'q':
                quiting = True
        PyConsole.core.terminal.Terminal.quit = True
        if quiting:
            import os
            os.system('exit')
