
name_1 = "chirag"
name_2 = "charg"


def match_name(name_1, name_2):
    for index, char in enumerate(name_2):
        if name_1[index] == char:
            print(char)
        else:
            name_2 = name_2[:index] + name_1[index] + name_2[index:]

    return name_2


ans = match_name(name_1, name_2)
print(ans)
