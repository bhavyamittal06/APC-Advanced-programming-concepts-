# texttools/cleaning.py
def clean(txt):
    return txt.replace(",","").replace(".","")

# texttools/tokenization.py
def tokenize(txt):
    return txt.split()

# texttools/frequency.py
def frequency(txt):
    d={}
    for w in txt.split():
        d[w]=d.get(w,0)+1
    return d