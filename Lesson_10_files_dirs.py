# -*- coding: utf-8 -*-
import os
import codecs

def find_files(dir):
    files = os.listdir(dir)
    give_abspath = lambda dir,filename: os.path.abspath(os.path.join(dir, filename))
    files_names = []
    for filename in files:
        file_path = give_abspath(dir, filename)
        if os.path.isdir(file_path):
            files_names += find_files(file_path)
        else:
            if filename == 'config.ini':
                files_names.append(give_abspath(dir, filename))
    return files_names

def main():

    os.chdir("D:/Media/Krupnaya.ryba.2003.DUAL.XviD.BDRip.-Allfilms")
    config_ini_path = find_files(os.getcwd())
    content_in_config_ini_file = codecs.open(config_ini_path[0], 'r')
    new_ini_path = config_ini_path[0][:-10]
    read_config_ini = content_in_config_ini_file.readlines()
    content_in_config_ini_file.close()
    os.remove(config_ini_path[0])
    os.chdir(new_ini_path)
    os.mkdir('Configs'); os.chdir(new_ini_path+'\Configs');
    content_in_config_ini_file = open('Config_ini_new.ini', 'w+')
    content_in_config_ini_file.writelines(line for line in read_config_ini)
    content_in_config_ini_file.close()


if __name__ == "__main__":
    main()
