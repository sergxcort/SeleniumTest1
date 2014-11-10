__author__ = 'Sergey'

import sys
import re
import os


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def minimum(list_of_values_for_min):
    """

    Function to return min values from list of given arguments
    """
    number_only = []

    [number_only.append(float(item)) for index, item in enumerate(list_of_values_for_min) if is_number(item)]

    number_only.sort()

    print number_only[0], number_only[1]


def count_args_passed(num):
    if len(num) == 2:
        return 2
    if len(num) > 2:
        return 0
    else:
        return -1


def repeated_elements(*lists):
    try:
        type(lists[1])
        list_2 = lists[1]
    except:
        ValueError
        list_2 = [1, 2, 3, 4, 5]

    repeated_elem = list(set(lists[0]) & set(list_2))

    return repeated_elem


def parse_options(*passed_options):
    """
    Parse options and make list of parsed options
    available to program
    """

    args = list(passed_options[0])
    options = {} # this should be variable to output data
    get_value = lambda a, x: a[a.index(x) + 1] # write lambda expression to get value of option
    is_option = lambda option: option[0:2] == "--" # Paste here 1 value (supposed option). True if it's true

    next_is_a_value = lambda list, current_option: not is_option(
        list[list.index(current_option) + 1]) #True if next option start with '--'

    if args:
        for option in args:

            if is_option(option) and not (option is args[-1]) and next_is_a_value(args, option):
                #second is if the last value will be alone option
                options[option] = get_value(args, option)

    return options


ISSUES_TYPE = ('BUG', 'ISSUE', 'ERROR')


def get_stat(text):


    BUG_count = ISSUE_count = ERROR_count = 0
    intrmd_text = text.split()

    for word in intrmd_text:

        if re.search(r"BUG", word):
            BUG_count += 1
        elif re.search(r"ISSUE", word):
            ISSUE_count +=1
        elif re.search(r"ERROR", word):
            ERROR_count +=1

    return BUG_count, ISSUE_count, ERROR_count

def get_warn_lines(text):


    warnSentence = []
    Sentence = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
    splitSentence = Sentence.findall(text)
    for i in splitSentence:
         if sum(get_stat(i)) >= 1:
            warnSentence.append(i)

    return warnSentence


def parse_text(**kwargs):
    """

    Parse text and get stat. Here we need to write code to read keyword passed to function and pass it to text variable
    """

    for value in kwargs.values():
       stat, warns = get_stat(value), get_warn_lines(value)

    return stat, warns



def main():
    text = """ ERROR - this is FUCK! Today we got ISSUE on produciton that crashed our server. ISSUE_FUCK What is going on there? How much time can we wait for this ERROR to be resolved? Finally, ISSUE-123 is resolved and we can go next with out business client. Phew!	Ok let's do following, if there is BUG on production then fire all stuff in Bangalore. Otherwise we will have huge lose. Will see how it will be!"""

    (stat, warns) = parse_text(analyze=text)


    print "\nStatistics on issues %r:\n" % str(ISSUES_TYPE)
    for k, v in enumerate(stat):
        print "\tFound %r occurred %r times" % (ISSUES_TYPE[k], stat[k])

    print "\nFound %r sentences:\n" % len(warns)

    for line in warns:
        print "\tFound issue here: %s" % line

if __name__ == "__main__":
    main()
