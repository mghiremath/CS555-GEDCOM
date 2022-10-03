supported_tags = [
    "INDI",
    "NAME",
    "SEX",
    "BIRT",
    "DEAT",
    "FAMC",
    "FAMS",
    "FAM",
    "MARR",
    "HUSB",
    "WIFE",
    "CHIL",
    "DIV",
    "DATE",
    "HEAD",
    "TRLR",
    "NOTE",
]

class individual(object):

    def __init__(self, uid):
        self.uniqueId = uid  
        self.indi_name = None 
        self.indi_birth = None 
        self.indi_sex = None 
        self.indi_death = None 
        self.indi_alive = True 
        self.fam_id_of_indi_child = [] 
        self.fam_id_of_indi_parent = [] 


class family(object):

    def __init__(self, uid):
        self.uniqueId = uid
        self.fam_marr = None  
        self.husband = None 
        self.husbandName = None 
        self.wife = None 
        self.wifeName = None
        self.children = [] 
        self.divorce = None 




class tagLine (object):
    def __init__(self, line):
        self.num_level = None
        self.num_tag = None
        self.arguments = None
        self.reference = None

        list_of_line = line.split(' ',)
        
        self.level = int(list_of_line[0])

        
        if self.level > 0:
            self.num_tag = list_of_line[1]
            self.arguments = list_of_line[2:]

        if self.level == 0:
            if list_of_line[1] in supported_tags:
                self.num_tag = list_of_line[1]
                self.arguments = None
            else:
                self.num_tag = list_of_line[2]
                self.reference = list_of_line[1]

