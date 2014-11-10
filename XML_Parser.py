__author__ = 'Sergey'
import os, re

class Read_replace_save:

    def __init__(self, file_name):
        self.file_name = file_name
        self.open = open(self.file_name, 'r+')

    def insert_new_data_and_save(self, data_to_insert):
        self.open.seek(0)
        self.open.truncate()
        self.open.write(data_to_insert)
        self.open.close()


class Phone_email_replace():
    def __init__(self, xml_object):
        self.xml_text = xml_object.read()

    def phone_change(self, phone_to_replace_on):
        self.xml_text = re.sub( r"(\d{3}-\d{2}-\d{2})", phone_to_replace_on, self.xml_text)
        return self.xml_text

    def email_change(self, email_to_replace_on):
        self.xml_text = re.sub(r"(\w+@\w+\.\w+)", email_to_replace_on, self.xml_text)
        return self.xml_text

    def remove_empty_nodes(self):
        pattern = r"(<\w+/>)"
        list = self.xml_text.split('\n')
        for item in list:
            if re.search(pattern, item):
               list.remove(item)
        self.xml_text = "\n".join(list)
        return self.xml_text

def main():

    xml_file = Read_replace_save('XML_file.xml')
    str = Phone_email_replace(xml_file.open)
    print os.getcwd() +"\n" + str.xml_text
    str.phone_change('548-54-99')
    str.email_change('test@gmail.com')
    print str.remove_empty_nodes()
    xml_file.insert_new_data_and_save(str.xml_text)

if __name__ == "__main__":
   main()