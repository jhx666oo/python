
def count_developers(lst):
    count=0
    for list1 in lst:
        if list1["continent"]=="Europe" and list1["language"]=="JavaScript":
            count+=1
    return count
    

