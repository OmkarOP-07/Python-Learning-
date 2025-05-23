print("69. Find longest common substring.")


from difflib import SequenceMatcher


def longest_common_substring(s1, s2):
    seq_match = SequenceMatcher(None, s1, s2)
    match = seq_match.find_longest_match(0, len(s1), 0, len(s2))
    if match.size != 0:
        return s1[match.a : match.a + match.size]
    else:
        return "Longest common sub-string not present"


s1 = "xyzhfhfhfhfdefgh"
s2 = "xswerabchfhfhfhfdwd"
print("Original Substrings:\n", s1 + "\n", s2)
print("\nCommon longest sub_string:")
print(longest_common_substring(s1, s2))
