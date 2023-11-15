def find_senior(lst): 
    mage = max(a['age'] for a in lst)
    return [a for a in lst if a['age']==mage]