def common_character_count(str1: str, str2: str):
    str1_set = set(str1)
    result = 0
    for letter in str1_set:
        str1_count = str1.count(letter)
        str2_count = str2.count(letter)
        result += min([str1_count, str2_count])
    return result
