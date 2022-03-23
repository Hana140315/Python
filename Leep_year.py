def leap_year(year):
    if year% 4 !=0:
        return "Common Year"
    elif year%100!=0:
        return"Leap year"
    elif year %400!=0:
        return "Common Year"
    else:return True

print(leap_year(2000))

#2
def substring(str,sub_str):

    return str.count(sub_str)

print(substring("ishtbis","is"))
