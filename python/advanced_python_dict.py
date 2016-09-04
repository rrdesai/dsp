import pandas as pd

fac = pd.read_csv('faculty.csv')
faculty_dict = {}
professor_dict = {}
for index, row in fac.iterrows():
    name = row[0].split(' ')[-1]
    fname = row[0].split(' ')[0]
    degree = row[1]
    loc = row[2].find('Professor')+10
    title = row[2][:loc]
    email = row[3]
    if name not in faculty_dict.keys():
        faculty_dict[name] = [[degree, title, email]]
    else:
        faculty_dict[name].append([degree,title,email])

    if (fname, name) not in professor_dict.keys():
        professor_dict[(fname, name)] = [degree, title, email]
    else: continue

def last_sort(dicts):
    keys_list = dicts.keys()
    keys_list = sorted(keys_list, key = lambda x: x[1])
    return_dict = {}
    for i in keys_list[0:3]:
        return_dict[i] = dicts[i]
    print return_dict

def first_three(dicts):
    keys_list = dicts.keys()
    return_dict = {}
    for i in keys_list[0:3]:
        return_dict[i] = dicts[i]
    print return_dict

first_three(faculty_dict)
first_three(professor_dict)
last_sort(professor_dict)

