class COption:
    """Class for representing command line options"""
    def __init__(self, cname: str, type='short'):
        self.cname = cname
        self.type = type
