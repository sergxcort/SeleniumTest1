__author__ = 'Sergey'
xt = """
timeout:
    whole: 1200
    element: 12000
browsers:
    major: firefox, chrome
    unstable: explorer
os: linux, windows
"""

#implement class Parser that will parse
#text to dictionary
#implement get_dict method that will return
#dictionary of converted values
class Parser:

    def __init__(self, text):
        self.text = text

    def parse(self, text):
        self.dictionary = {text}
        return self.dictionary

    def get_dict(self):
        return self.parse()


class Config(Parser):
    """

    Text here
    """

    def __init__(self, text):
        self.config = Parser(text).get_dict()

    def __str__(self):
        #do code to represent config

    #def __getitem__(self, key):
        #do code to get value from config
        #when call it like config['os']



if __name__ == "__main__":
    pass
    #config = Config(__doc__)
   # print config
   # print config['timeout']['whole']
   # print config['os']