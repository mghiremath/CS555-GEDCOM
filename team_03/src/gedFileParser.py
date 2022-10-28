import datetime
from individual import Individual
from family import Family

individuals = {}
families = {}

supported_tags: list = [
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


def parse_date(date: str) -> datetime.date:
    """Helps to parse date"""

    month_dict = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12,
    }
    date = date.split()
    return datetime.datetime(int(date[2]), month_dict[date[1]], int(date[0])).date()


def is_supported_tag(tag: str) -> bool:
    """check weather in"""
    return tag in supported_tags


def process_family(rows) -> Family:
    """read"""
    family = Family()

    # by default will not process marriage and divorce assuming level will be 0
    process_marriage = False
    process_divorce = False

    for row in rows:

        # Reads each row and sets the corresponding field in the family object
        if row[1] == "FAM":
            family.identifier = row[2].strip()
        elif row[1] == "HUSB":
            family.husband_id = row[2].strip()
        elif row[1] == "WIFE":
            family.wife_id = row[2].strip()
        elif row[1] == "CHIL":
            family.children.append(row[2].strip())
        elif row[1] == "DIV":
            # Begin reading in the divorce date
            process_divorce = True
            family.is_divorced = True
        elif row[1] == "MARR":
            # Begin reading in the marriage date
            process_marriage = True
        elif int(row[0]) == 2 and row[1] == "DATE":
            if process_marriage:
                family.married = parse_date(row[2].strip())
            elif process_divorce:
                family.is_divorced = True
                family.divorced = parse_date(row[2].strip())

    return family


def process_individual(rows: list) -> Individual:
    """Helps to read individual"""

    # create a new individual.
    individual = Individual()

    # by default will not process birth and death assuming level will be 0
    process_birth = False
    process_death = False

    for row in rows:
        
        if int(row[0]) == 1:
            process_birth = False
            process_death = False

        if row[1] == "INDI":
            individual.identifier = row[2].strip()
        elif row[1] == "BIRT":
            process_birth = True
        elif int(row[0]) == 2 and row[1] == "DATE":
            if process_birth:
                individual.birthday = parse_date(row[2].strip())
            elif process_death:
                individual.death_day = parse_date(row[2].strip())
        elif row[1] == "FAMS":
            individual.spouse_family.append(row[2].strip())
        elif row[1] == "FAMC":
            individual.children_family.append(row[2].strip())
        elif row[1] == "NAME":
            individual.name = row[2].strip()
        elif row[1] == "SEX":
            individual.gender = row[2].strip()
        elif row[1] == "DEAT":
            if "Y" == row[2].strip():
                process_death = True
                individual.alive = False
            else:
                individual.alive = True

    # process age
    individual.process_age()

    return individual


def parser_file(file_path: str):
    """"""

    is_individual = False
    is_family = False

    lines_list = []

    # default  tags and args to str
  
    tag = ""
    level = 0

    with open(file_path, "r") as lines:

        for line in lines:

            list_of_words = line.split()
            level = int(list_of_words.pop(0))

            if len(list_of_words) == 1:
                tag = list_of_words[0]
                args = ""
            else:
                tag = (
                    list_of_words.pop(1)
                    if list_of_words[1] == "INDI" or list_of_words[1] == "FAM"
                    else list_of_words.pop(0)
                )
                args=""
                for word in list_of_words:
                    args = args + word + " "

            if level == 0:
                if is_individual:
                    new_individual = process_individual(lines_list)
                    individuals[new_individual.identifier] = new_individual
                if is_family:
                    new_family = process_family(lines_list)
                    families[new_family.identifier] = new_family
                if tag == "INDI":
                    is_individual = True
                    is_family = False
                    lines_list = []
                elif tag == "FAM":
                    is_individual = False
                    is_family = True
                    lines_list = []
                else:
                    is_individual = False
                    is_family = False

            if tag in supported_tags:
                lines_list.append([level, tag, args])

            for family in families.keys():
                families[family].husband_name = individuals[families[family].husband_id].name
                families[family].wife_name = individuals[families[family].wife_id].name
        individual_list = []
        family_list = []
        individual_list = []
        for individual in sorted(individuals.keys()):
            ind = individuals[individual]
            individual_list.append(
                [
                    ind.identifier,
                    ind.name,
                    ind.gender,
                    ind.birthday,
                    ind.age,
                    ind.alive,
                    ind.death_day,
                    ind.get_children_family() ,
                    ind.get_spouse_family(),
                ]
            )
        for family in sorted(families.keys()):
            fam = families[family]
            family_list.append(
                [
                    fam.identifier,
                    fam.married,
                    fam.get_is_divorced(),
                    fam.husband_id,
                    fam.husband_name,
                    fam.wife_id,
                    fam.wife_name,
                    fam.get_children(),
                ]
            )

        return individual_list ,family_list   

