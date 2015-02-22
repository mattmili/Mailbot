"""
TEMPPPPPP SHIT BRO
"""
import re
import pprint

email = 'Hey lets go to {{SEARCH the capital of China}}. Take a look at this {{SEARCH cheapest flights to china}}'

def find(string):
    temp=[]

    for i in string.split("{{"):
        for j in i.split("}}"):
            temp.append(j)

    for n,i in enumerate(temp):
        if str(i).startswith("SEARCH"):
            # do the search here
            temp[n] = 'hello'
    return temp

print ' '.join(find(email))

