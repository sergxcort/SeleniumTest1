from __future__ import division
import math


def main():
    text = raw_input("Please type yor text: ")

    #example of count of big letters
    big_letters_amount = []
    numbers = []
    sentenses = []
    for char in text:
        if char >= "A" and char <= "Z":
           big_letters_amount.append(char)
        if char >= "0" and char <= "9":
           numbers.append(char)
        if char == '.':
           sentenses.append(char)
    print "amount of big letters in text is %s" % len(big_letters_amount)
    print "amount of numbers in in text is %s" % len(numbers)
    stringsplit = text.split()
    print "amount of words in text is %s" % len(stringsplit)
    print "amount of sentenses in text is %s" % len(sentenses)
    sentences = 0 #write code here
    words = 0 #write code here
    numbers = 0 #write code here
 
	#print "numbers: %s, words: %s, sentences: %s" % (numbers, words, sentences)
def currency():
    #Input of currency
    input_currency = raw_input("Please type yor text of future income: ")
    separate_input_currency = list(input_currency.split())
    dict_input_currency = {"input_currency_value" : separate_input_currency[0], "input_currency_is" : separate_input_currency[1]}

    if dict_input_currency.get("input_currency_is") == "USD":
       converted_currency = float(dict_input_currency.get("input_currency_value"))*1.22
       converted_currency_meaning = 'EUR'
    else:
       converted_currency = float(dict_input_currency.get("input_currency_value"))*0.88
       converted_currency_meaning = 'USD'

    converted_currency_number, converted_currency_digit = divmod(converted_currency, 1)
    converted_currency_digit = round(converted_currency_digit, 2)*100


    if converted_currency_digit != 0:
        print dict_input_currency.get("input_currency_value"), dict_input_currency.get("input_currency_is"), \
              "- equal to", str(int(converted_currency_number)), converted_currency_meaning, str(int(converted_currency_digit)) + " cents"
    else:
        print dict_input_currency.get("input_currency_value"), dict_input_currency.get("input_currency_is"), \
              "- equal to", str(int(converted_currency_number)), converted_currency_meaning



	#print "numbers: %s, words: %s, sentences: %s" % (numbers, words, sentences)

 
if __name__ == '__main__':
	currency()