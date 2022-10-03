from datetime import date
from datetime import datetime
from models import tagLine, individual, family
def gedFileParser(file):
    indi = []
    fam = []
    gedcomLst = []

    lines = [line.rstrip('\n\r') for line in open(file)]

    for line in lines:
        curr_gedcom_line = tagLine(line)
        gedcomLst.append(curr_gedcom_line)

    # traverse  tags
    for i, gedcomline in enumerate(gedcomLst):
        if gedcomline.num_tag == 'INDI':

            date_type = None
            indiObject = individual(gedcomline.reference)

            for l in gedcomLst[i + 1:]:
                if l.num_level == 0:
                    break
                if l.num_tag == "NAME":
                    indiObject.indi_name = l.arguments
                if l.num_tag == "SEX":
                    indiObject.indi_sex = l.arguments[0]
                if l.num_tag == "BIRT":
                    date_type = "BIRT"
                if l.num_tag == "DEAT":
                    date_type = "DEAT"
                if l.num_tag == "FAMC":
                    indiObject.fam_id_of_indi_child.append(l.arguments[0])
                if l.num_tag == "FAMS":
                    indiObject.fam_id_of_indi_parent.append(l.arguments[0])

                # check if date is birth or date
                if l.num_tag == 'DATE':
                    if date_type == 'BIRT':
                        indiObject.indi_birth = date(
                            int(l.arguments[2]),
                            datetime.strptime(l.arguments[1], '%b').month,
                            int(l.arguments[0])
                        )
                        date_type = None
                    elif date_type == 'DEAT':
                        indiObject.indi_death = date(
                            int(l.arguments[2]),
                            datetime.strptime(l.arguments[1], '%b').month,
                            int(l.arguments[0])
                        )
                        indiObject.indi_alive = False
                        date_type = None

            # add object into the individual list
            indi.append(indiObject)

        # For family list
        if gedcomline.num_tag == 'FAM':

            date_type = None

            # create blank object
            familyObject = family(gedcomline.reference)

            # ste values until next level 0
            for l in gedcomLst[i + 1:]:
                if l.num_level == 0:
                    break
                if l.num_tag == "MARR":
                    date_type = "MARR"
                if l.num_tag == "DIV":
                    date_type = "DIV"
                if l.num_tag == "HUSB":
                    familyObject.husband = l.arguments[0]
                    for persons in indi:
                        if persons.uniqueId == l.arguments[0]:
                            familyObject.husbandName = persons.indi_name
                if l.num_tag == "WIFE":
                    familyObject.wife = l.arguments[0]
                    for persons in indi:
                        if persons.uniqueId == l.arguments[0]:
                            familyObject.wifeName = persons.indi_name
                if l.num_tag == "CHIL":
                    familyObject.children.append(l.arguments[0])

                # check if marriage date or divorce date
                if l.num_tag == "DATE":
                    if date_type == "MARR":

                        familyObject.fam_marr = date(
                            int(l.arguments[2]),
                            datetime.strptime(l.arguments[1], '%b').month,
                            int(l.arguments[0]))
                        date_type = None

                    elif date_type == "DIV":

                        familyObject.divorce = date(
                            int(l.arguments[2]),
                            datetime.strptime(l.arguments[1], '%b').month,
                            int(l.arguments[0]))
                        date_type = None
            # append object into the family list
            fam.append(familyObject)

    return indi, fam