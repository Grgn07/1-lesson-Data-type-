
# def polindrom(num: list)-> bool:
#     if num == num[::-1]:
#           return True
#     return False
# print(polindrom([1, 2, 5, 5, 2, 1]))



def replace_with(txt:str):
    text = ""
    for s in txt.split()[::-1]:
        if s == "":
            text += (" ")
        else:
            text += s
    return text
print(replace_with("ночь улица фонарь аптека"))


