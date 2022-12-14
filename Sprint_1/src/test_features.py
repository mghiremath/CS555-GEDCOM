from datetime import datetime
from unittest import TestCase
from models import family

err_list = []


def story_validation(indi, fam):
    # To print Errors
    print(("ERRORS".center(80, ' ')))
    print("\nUser Story             Description:                             "
          "     Location")
    print(('-' * 80))

    # Sprint 1
    birth_before_marriage(indi, fam)
    us05(indi, fam)

###########################################################################################

# US02 - Birth should occur before marriage of that individual
def birth_before_marriage(indi, fam):
    # For each individual check if birth occurs before marriage
    return_flag = True
    error_type = "US02"
    for family in fam:
        if family.fam_marr:
            # Search through indi to get husband and wife
            husband = None
            wife = None

            for indiv in indi:
                if indiv.uniqueId == family.husband:
                    husband = indiv
                if indiv.uniqueId == family.wife:
                    wife = indiv

            if wife.indi_birth and wife.indi_birth > family.fam_marr:
                # Found a case spouse marries before birth
                error_descrip = "Birth of wife occurs after marriage"
                error_location = [wife.uniqueId]
                report_error(error_type, error_descrip, error_location)
                return_flag = False

            if husband.indi_birth and husband.indi_birth > family.fam_marr:
                error_descrip = "Birth of husband occurs after marraige"
                error_location = [husband.uniqueId]
                report_error(error_type, error_descrip, error_location)
                return_flag = False

    return return_flag



########################################################################
#US05 Marriage before Death
def us05(indi, fam):

    # For each individual check if marriage occurs before death
    return_flag = True
    error_type = "US05"
    for family in fam:
        if family.fam_marr:
            # Search through indi to get husband and wife
            husband = None
            wife = None

            for indiv in indi:
                if indiv.uniqueId == family.husband:
                    husband = indiv
                if indiv.uniqueId == family.wife:
                    wife = indiv

            if wife.indi_alive == False:
                if family.fam_marr < wife.indi_death:
                    # Found a case spouse marries before birth
                    error_descrip = "Death of Wife occurs before marriage"
                    error_location = [wife.uniqueId]
                    report_error(error_type, error_descrip, error_location)
                    return_flag = False

            if husband.indi_alive == False:
                if husband.indi_death < family.fam_marr:
                    error_descrip = "Death of Husband occurs before marriage"
                    error_location = [husband.uniqueId]
                    report_error(error_type, error_descrip, error_location)
                    return_flag = False

    return return_flag

########################################################################
#US04 Marriage before divorce
def us04(indi, fam:list[family]):

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
        if len(i.children)>=0:
            report_error(error_type,"",str(i.uniqueId))
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
    
 
