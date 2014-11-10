__author__ = 'Sergey'

import sys
import os
import re


def main():
    usage = ("\n"
             "\tYou should pass at least 1 argument to %s\n"
             "\tArguments are folders full path separated by space.\n"
             "\t"
            ) % sys.argv[0]

    argv = sys.argv[1:]
    output = []


    #if not arguments passed
    if not argv:
        print usage
        sys.exit(1)#do some code

    for option in argv:
        exist = "folder not exist"
        path_pattern = re.compile(r"[a-z]:\\")
        result = path_pattern.match(option)
        #do some code here to check string is path
        if result and os.path.exists(option):
            exist = "Folder exist. Yeaa!"
        elif result and not os.path.exists(option):
            exist = "This is not a folder motherfucker!"
        output.append([option, exist])

    for i, output in enumerate(output):
        print "%r. %s\t %s" % (i+1, output[0], output[1])

#Checking that value is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def summa():
    usage = ("\n"
             "\tYou should pass at least 1 argument to %s\n"
             "\tArguments are folders full path separated by space.\n"
             "\t"
            ) % sys.argv[0]

    argv = sys.argv[1:]
    print 'The list is the next: \n', argv
    argvmax = []

    if not argv:
        print usage
        sys.exit(1)

    [argvmax.append(float(args)) for indx, args in enumerate(argv) if is_number(args)]

    argvmax.sort()
    the_last_summa_here = argvmax[-1] + argvmax[-2]

    assert isinstance(the_last_summa_here, float)
    print 'Result summ of formatted input list is:', the_last_summa_here


if __name__ == '__main__':
    summa()
