print(
    "66.Make two given strings anagrams removing any characters from any of the strings"
)


def char_count(s):
    count_map = {}
    for char in s:
        if char not in count_map:
            count_map[char] = 1
        else:
            count_map[char] += 1
    return count_map


def edit_distance(str1, str2):
    map1 = char_count(str1)
    map2 = char_count(str2)
    ctr = 0

    for key in map2.keys():
        if key not in map1:
            ctr += map2[key]
        else:
            ctr += max(0, map2[key] - map1[key])

    for key in map1.keys():
        if key not in map2:
            ctr += map1[key]
        else:
            ctr += max(0, map1[key] - map2[key])

    return ctr


str1 = input("Input string1: ")
str2 = input("Input string2: ")
print(edit_distance(str1, str2))
