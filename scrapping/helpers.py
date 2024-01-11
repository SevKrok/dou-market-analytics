import os
from datetime import datetime, date

import pandas as pd

from config import PYTHON_TECHNOLOGIES

UA_MONTHS_TO_NUMS = {
    "січня": "1",
    "лютого": "2",
    "березня": "3",
    "квітня": "4",
    "травня": "5",
    "червня": "6",
    "липня": "7",
    "серпня": "8",
    "вересня": "9",
    "жовтня": "10",
    "листопада": "11",
    "грудня": "12",
}

SAME_TECHNOLOGIES = {
    "django rest framework": "drf",
    "machine learning": "ml",
    "javascript": "js",
}


def convert_month_name_to_month_num(ua_date: str) -> date:
    """
    Convert UA month name to month number and return it as a date object
    :param ua_date: "4 січня 2024"
    :return: 2024-01-04
    """

    date_segments = ua_date.split()
    date_segments[1] = UA_MONTHS_TO_NUMS[date_segments[1]]

    return datetime.strptime(" ".join(date_segments), "%d %m %Y").date()


def find_technologies(description: str) -> list:
    """
    Find technologies (PYTHON_TECHNOLOGIES) in description
    :param description:
    :return: technologies_in_description
    """
    technologies_in_description = []

    for tech in PYTHON_TECHNOLOGIES:
        if tech in description.lower():
            if tech in SAME_TECHNOLOGIES.keys():
                technologies_in_description.append(SAME_TECHNOLOGIES[tech])
            else:
                technologies_in_description.append(tech)

    return technologies_in_description
