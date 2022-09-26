# -*- coding: utf-8 -*-
"""Created on Mon Sep 19 12:16:08 2022@author: Maheshwar Hiremath"""

import sys
supportedTags=['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT',
                'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE',
                'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
file_name = 'Mahesh G H- 20015431.ged'
def GEDCOM_parser(file_name):
    file = open(file_name,'r')
    list_of_lines = file.readlines()
    sys.stdout = open ("gedcom_proj02_outputLogs.txt", 'w')
    print("Output console logs of GEDCOM project 02: Authored by Maheshwarswami G Hiremath ; CWID-20015431")
    for line in list_of_lines:  
        line = line.replace('\n', '')
        print('--> {0}'.format(line))
        if 'INDI' in line or ('FAM' in line and 'FAMS' not in line and 'FAMC' not in line):
            index_of_tag = 2
        else:
            index_of_tag = 1
        
        list_of_args = line.split(" ")
        tag_name = list_of_args[index_of_tag]
        supported_tag_line = 'Y' if tag_name in supportedTags else 'N'
        level=list_of_args[0]
        list_of_args.pop(index_of_tag)
        list_of_args.pop(0)
        print('<-- {0}|{1}|{2}|{3}'.format(level,
                tag_name, supported_tag_line, ' '.join(list_of_args)))
    file.close()
    sys.stdout.close()
GEDCOM_parser(file_name)