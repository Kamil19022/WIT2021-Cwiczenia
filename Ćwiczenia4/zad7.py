def count_chars(latter):
    dict={}
    for x in latter:
        keys= dict.keys()
        if x in keys:
            dict[x]+=1
        else:
            dict[x]=1
    return print(dict)


print(count_chars('PpPP'))
