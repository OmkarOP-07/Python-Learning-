print("70. Concatenate uncommon characters in strings.")


def concat_uncommon_chars(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    common_chars = set1 & set2

    uncommon_s1 = []
    for ch in s1:
        if ch not in common_chars:
            uncommon_s1.append(ch)

    uncommon_s2 = []
    for ch in s2:
        if ch not in common_chars:
            uncommon_s2.append(ch)

    result = uncommon_s1 + uncommon_s2
    return "".join(result)


s1 = "xyzawbfajfj"
s2 = "uabjfkagxyznakj"
print("Original Substrings:\n", s1 + "\n", s2)
print("\nAfter concatenating uncommon characters:")
print(concat_uncommon_chars(s1, s2))
