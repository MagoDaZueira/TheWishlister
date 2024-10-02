month_map = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def name_prepare(name: str) -> str:
    final_name = name.replace(" ", "-").replace(".", "-")
    final_name = final_name.replace(":", "").replace("'", "").replace("(", "").replace(")", "")
    final_name = final_name.lower()
    return final_name


def date_prepare(date):
    if (date != 'TBD'):
        month_str, day_str, year_str = date.replace(",", "").split()

        month_num = month_map[month_str]

        date_dict = {"Year": int(year_str), "Month": month_num, "Day": int(day_str)}
        return date_dict
    else: 
        return 'TBD'
