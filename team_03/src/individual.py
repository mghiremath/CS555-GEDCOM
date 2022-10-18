from dataclasses import dataclass, field
import datetime


@dataclass
class Individual:
    """Helps to process individuals acts as an object"""

    children_family: list = field(default_factory=list)
    spouse_family: list = field(default_factory=list)
    identifier: str = "N/A"
    name: str = "N/A"
    gender: str = "N/A"
    birthday: datetime.date = datetime.datetime(1776, 7, 4).date()
    age: int = 0
    alive: bool = True
    death_day: datetime.date = datetime.datetime(1776, 7, 4).date()

    def process_age(self) -> None:
        """
        helps to process the age
        """

        death_day = datetime.date.today() if self.alive else self.death_day
        self.age = death_day.year - self.birthday.year

        if death_day.month < self.birthday.month:
            self.age -= 1
        elif death_day.month == self.birthday.month:
            if death_day.day < self.birthday.day:
                self.age -= 1

    def get_death_day(self) -> str | datetime.date:
        """helps to get death day"""
        return "N/A" if self.alive else str(self.death_day)

    def get_children_family(self) -> str:
        """helps to get children family"""
        if self.children_family == []:
            return "N/A"
        else:
            temp_str = "{"
            for child in self.children_family:
                temp_str = temp_str + child + ", "
            temp_str = temp_str[:-2]
            return temp_str + "}"

    def get_spouse_family(self) -> str:
        """helps to get spouse family"""
        if self.spouse_family == []:
            return "N/A"
        else:
            temp_str = "{"
            for spouse in self.spouse_family:
                temp_str = temp_str + spouse + ", "
            temp_str = temp_str[:-2]
            return temp_str + "}"
