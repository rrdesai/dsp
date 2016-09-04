import pandas as pd

fac = pd.read_csv('faculty.csv')

degree_dict = {}
for i in fac[' degree']:
    degrees = i.replace('.','').split(' ')
    for j in degrees:
        if j != '' and j not in degree_dict.keys():
            degree_dict[j] = 1
        elif j != '':
            degree_dict[j]+=1
        else:
            continue

print degree_dict
title_dict = {}
for i in fac[' title']:
    loc = i.find('Professor')+10
    title = i[:loc]
    if title not in title_dict.keys():
        title_dict[title] = 1
    else:
        title_dict[title] += 1

print title_dict

email_list = []
for i in fac[' email']:
    email_list.append(i)

print email_list
domain_list = []
for i in email_list:
    domain = i.split('@')[1]
    if domain not in domain_list:
        domain_list.append(domain)
print domain_list
