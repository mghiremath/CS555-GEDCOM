import datetime
from dataclasses import dataclass, field


@dataclass
class Family:
    """helps to act as family"""

    identifier: str = "N/A"
    married: datetime.date = datetime.datetime(1776, 7, 4).date()
    divorced: datetime.date = datetime.datetime(1776, 7, 4).date()
    is_divorced: bool = False
    husband_id: str = "N/A"
    husband_name: str = "N/A"
    wife_id: str = "N/A"
    wife_name: str = "N/A"
    children: list = field(default_factory=list)

    def get_is_divorced(self):
        """Helps to check is_divorced"""
        return "N/A" if self.is_divorced else self.divorced

    def get_children(self):
        """helps to get children"""
        if self.children == []:
            return "N/A"
        else:
            temp_str = "{"
            for child in self.children:
                temp_str = temp_str + child + ", "
            temp_str = temp_str[:-2]
            return temp_str + "}"
