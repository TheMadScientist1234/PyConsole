import PyConsole.core.option

import PyConsole.display.console

class Command:
    """Superclass for all commands that can be called in the terminal"""
    def __init__(self):
        # Command string
        self.cstr = ''

    def _parse_options(self, args: list)->list:
        """Parse options out of a list of arguments"""
        options = []
        for i in args:
            if i[0] == '-':
                type = 'long' if i[1] == '-' else 'short'
                options.append(PyConsole.core.option.COption(i[1:] if type == 'short' else i[2:], type=type))
        return options

    def execute(self, args: list, console: PyConsole.display.console.Console)->bool:
        """Called when the console is to execute this command"""
        pass
