import PyConsole.core.command
import PyConsole.core.option

import PyConsole.display.console

class CommandLs(PyConsole.core.command.Command):
    """
    LS: List all files and folders in the current directory

    Options:
    -l, --long: detailed list mode
    """
    def __init__(self):
        self.cstr = 'ls'

    def execute(self, args: list, console: PyConsole.display.console.Console)->bool:
        console.cprint('Doing thing...')
        parsed_args = self._parse_options(args)
        for option in parsed_args:
            if option.cname == 'l':
                console.cprint('Long list')
