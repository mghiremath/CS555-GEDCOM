"""This function returns the Current Date"""
import datetime

def print_list(input_list):
    print("\n")
    for i in input_list:
        print(i)

def getCurrentDate():
    current_date = str(datetime.date.today())
    return current_date

def create_individuals_list():
    op_list = [0 for i in range(7)]
    op_list[5] = []
    return op_list

def create_families_list():
    op_list = [0 for i in range(6)]
    op_list[5] = []
    return op_list

def getLastName(str):
    place_holder=''
    for i in str:
        if(i != '/'):
            place_holder += i
    return place_holder

def convertDateFormat(date):
    place_holder = date.split()
    if(place_holder[1] == 'JAN'): place_holder[1] = '01';
    if(place_holder[1] == 'FEB'): place_holder[1] = '02';
    if(place_holder[1] == 'MAR'): place_holder[1] = '03';
    if(place_holder[1] == 'APR'): place_holder[1] = '04';
    if(place_holder[1] == 'MAY'): place_holder[1] = '05';
    if(place_holder[1] == 'JUN'): place_holder[1] = '06';
    if(place_holder[1] == 'JUL'): place_holder[1] = '07';
    if(place_holder[1] == 'AUG'): place_holder[1] = '08';
    if(place_holder[1] == 'SEP'): place_holder[1] = '09';
    if(place_holder[1] == 'OCT'): place_holder[1] = '10';
    if(place_holder[1] == 'NOV'): place_holder[1] = '11';
    if(place_holder[1] == 'DEC'): place_holder[1] = '12';
    if(place_holder[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        place_holder[2] = '0' + place_holder[2]
    return (place_holder[0] + '-' + place_holder[1] + '-' + place_holder[2])


def parser(file_path):
    file =  open(file_path, 'r')
    individual_flag = 0
    family_flag = 0
    list_indi = []
    list_fam = []
    indi = create_individuals_list()
    fam = create_families_list()
    for line in file:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(individual_flag == 1):
                    list_indi.append(indi)
                    indi = create_individuals_list()
                    individual_flag = 0
                if(family_flag == 1):
                    list_fam.append(fam)
                    fam = create_families_list()
                    family_flag = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        individual_flag = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        family_flag = 1
                        fam[0] = (str[1])

            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    indi[1] = str[2] + " " + getLastName(str[3])
                if(str[1] == 'SEX'):
                    indi[2] = str[2]
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
                if(str[1] == 'FAMS'):
                    indi[5].append(str[2])
                if(str[1] == 'FAMC'):
                    indi[6] = str[2]
                if(str[1] == 'HUSB'):
                    fam[1] = str[2]
                if(str[1] == 'WIFE'):
                    fam[2] = str[2]
                if(str[1] == 'CHIL'):
                    fam[5].append(str[2])
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        indi[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indi[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        fam[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        fam[4] = convertDateFormat(date)
    return list_indi, list_fam
                
def DatesBeforeCurrentDate(list_indi, list_fam):
    curr_date = getCurrentDate()
    for i in list_indi:
        if(i[3] > curr_date):
            return False
        if(i[4] != 0):
            if(i[4] > curr_date):
                return False
    for i in list_fam:
        if(i[3] > curr_date):
            return False
        if(i[4] != 0):
            if(str(i[4]) > curr_date):
                return False
    return True
def getBirthDateByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            return i[3]
def BirthBeforeMarriage(list_indi, list_fam):
    for i in list_fam:
        marriage_date = i[3]
        if(getBirthDateByID(list_indi, i[1]) > marriage_date):
            return False
        if(getBirthDateByID(list_indi, i[2]) > marriage_date):
            return False
    return True
    
    
if __name__ == "__main__":
    list_indi, list_fam = parser("Team3-gedcom-testFile.ged")
    list_indi.sort()
    list_fam.sort()
    print_list(list_indi)
    print_list(list_fam)
    if(DatesBeforeCurrentDate(list_indi, list_fam)):
        print("\nAll the Dates are before the Current Date.")
    else:
        print("\nOne or more Dates are not before the Current Date.")
    if(BirthBeforeMarriage(list_indi, list_fam)):
        print("\nAll the Birth Dates are before the respective Marriage Dates")
    else:
        print("\nOne or more Birth Dates are not before their respective Marriage Date.")
   
