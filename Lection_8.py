"""
os: linux, windows
timeout:
    whole: 1200
    element: 12000
    element1: none
browsers:
    major: firefox, chrome
    unstable: explorer
"""
class Parser:
    """
    Pasrse string to dictionary
    """ 
    def __init__(self, text):
        self._text = text.strip()
        self._text_to_dict()
 
    def _text_to_dict(self):
        self._parsed_dict = {}
        temporary_dict = {}
        store_key = None
        for line in self._text.splitlines():
            key, value = line.split(":")
            if not key.startswith('    ') and value:
                self._parsed_dict[key] = value.split(',')
            elif not key.startswith('    ') and not value:
                self._parsed_dict[key] = temporary_dict
                temporary_dict = {}
            elif key.startswith('    ') and value:
                self._parsed_dict[key] = value.split(',')
                temporary_dict[key] = value.split()

        return self._parsed_dict
 
    def get_dict(self):
        return self._parsed_dict

class Config(Parser):
    def __init__(self, text):
        self.config = Parser(text).get_dict()
 
    def __str__(self):
        return str(self.config)
 
    def __getitem__(self, key):
        return self.config[key]
 
if __name__ == '__main__':
    config = Config(__doc__)
    print config
