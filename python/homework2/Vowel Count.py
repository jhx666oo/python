def get_count(sentence):
    get_count="aeiou"
    count=0
    for char in sentence:
        if char.islower() and char in get_count:
            count+=1
    return count
    pass