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
        for arg in parsed_args:
            if arg.cname == 'q':
                PyConsole.core.terminal.Terminal.closing_window = True
        PyConsole.core.terminal.Terminal.quit = True
