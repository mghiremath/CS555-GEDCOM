import argparse
import os
import sys

from gedFileParser import gedFileParser
from prettytable import PrettyTable
from test_features import story_validation

#authors of the project
__author__ = "Maheshwarswami Hiremath"
__email__ = "mhiremat@stevens.edu"

#default file path

FILENAME = 'Sprint_1/gedcom_files/testFile_incorrectData.ged'

x = PrettyTable()
y = PrettyTable()

# main function for taking the file path
def main():
    # Allow for arguments to be passed for filename
    arg_parser = argparse.ArgumentParser()
    action = arg_parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME,
                        help="Specify a specific file to run GEDCOM parser on. \
                        Default is " + FILENAME)

    arguments = arg_parser.parse_args()
    path = arguments.file
    if os.path.exists(path):
        print("Path accepted")
        indi, fam = gedFileParser(path)
    else:
        print("[!!] File \"%s\" does not exist.\nExiting..." % path)
        exit(-1)

    # Check for user stories
    story_validation(indi, fam)

    #printing values
    printSummary(indi, fam)

# function for printing the list of individuals and families to
def printSummary(individual, families):
    print("\n")
    # for printing Individuals
    x.field_names = ["id","Name","Birthday","Sex","Death Date","Alive","Child","Spouse"]
    for line in individual:
        attrs = vars(line)
        x.add_row(attrs.values())

    print(x)

#    print(', '.join("%s: %s" % item for item in attrs.items()))

    print('----------------------------------------------------------------------------------------------------------------------------------------')
    # For printing Families
    y.field_names = ["Fid","Marriage","Husband","Husband Name","Wife","Wife Name","Children","Divorce"]
    for line in families:
        attrs = vars(line)
        y.add_row(attrs.values())
#        print (', '.join("%s: %s" % item for item in attrs.items()))
    print(y)

if __name__ == '__main__':
    sys.stdout = open("Sprint_1/output.txt","w")
    main()
    sys.__stdout__.close()