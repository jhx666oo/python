def shorten_number(suffixes,base):
    def func(n):
        try: n = int(float(n))
        except: return str(n)
        i = 0; m = len(suffixes)-1
        while base<n and i<m: n = n//base; i += 1 
        return str(n)+suffixes[i]
    return func