def xo(s):
#  "DAVIT".lower() ----> 'davit'
#  "DAVIT".count()
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    else:
        return False