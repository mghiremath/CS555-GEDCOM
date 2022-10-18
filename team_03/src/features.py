from datetime import datetime
from unittest import TestCase
import family

err_list = []


def story_validation():
    # To print Errors
    print(("ERRORS".center(80, ' ')))
    print("\nUser Story             Description:                             "
          "     Location")
    print(('-' * 80))

###########################################################################################

# US02 - Birth should occur before marriage of that individual
def birth_before_marriage(indi, fam):
    for i in range(len(fam)):
        for j in range(len(indi)):
            if fam[i][3]==indi[j][0] and fam[i][1]<indi[j][3]:
                validate_birth(indi[j], 'M')
            if fam[i][5]==indi[j][0] and fam[i][1]<indi[j][3]:
                validate_birth(indi[j],'F')
def validate_birth(individual, gender):
    error_type = "US02"
    if (gender=='M'):
        error_descrip = "Birth of Husband occurs after marriage"
    else: error_descrip = "Birth of Wife occurs after marriage"
    error_location = [individual[0]]
    report_error(error_type, error_descrip, error_location)
    return False




########################################################################
#US05 Marriage before Death
def us05(indi, fam):
    for i in range(len(fam)):
        for j in range(len(indi)):
            if  fam[i][3]==indi[j][0] and fam[i][1]>indi[j][6]:
                validate_death(indi[j])
            

def validate_death(individual):
    error_type = "US05"
    if (individual[2]=='M'):
        error_descrip = "Death of Husband occurs before marriage"
    else: error_descrip = "Death of Wife occurs before marriage"
    error_location = [individual[0]]
    report_error(error_type, error_descrip, error_location)
    return False

########################################################################
#US04 Marriage before divorce
def us04(fam:list[family]):

    # For each family check divorce before marriage
    return_flag = True
    error_type = "US04"
    for family in fam:
        if family.divorce == 'NA' or family.fam_marr== 'NA':
            continue
        if family.divorce > family.fam_marr:
            report_error(error_type,"Family divorce before marriage",str(family.uniqueId))
            return_flag=False
        else:
            report_error(error_type,"Family divorce after marriage",str(family.uniqueId))
            return_flag=False

    return return_flag

########################################################################
#US15
def  us15(fam):
    error_type = "US15"
    for i in fam:
        if len(i[-1])>15:
            report_error(error_type,"Family has 15 or more siblings",str(i[0]))
            return True
        
        


########################################################################
#US16

def US16(indi, fam):
    error_type = "US16"
    for family in fam:
        name_l=family[4].split()
        last_name=name_l[-1].replace('/','')
        for individual in indi:
            if individual[0] in family[-1]:
                if individual[2] =='M' :
                    if last_name not in individual[1].split():
                        report_error(error_type,"Lastname not the same as father ",individual[0])
                        return False
                    else: return True



# report Error to the console
def report_error(error_type, description, locations):

    if isinstance(locations, list):
        locations = ','.join(locations)

    estr = '{:14.14s}  {:50.50s}    {:10.10s}' \
        .format(error_type, description, locations)
    print(estr)

    err_list.extend(locations)

    err_list.extend(locations)
    
 
