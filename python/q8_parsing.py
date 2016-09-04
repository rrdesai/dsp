# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# this assumes that smallest means that we're looking for the lowest positive difference
import pandas

df = pandas.read_csv('football.csv')
df_new = pandas.concat([df, df['Goals'] - df['Goals Allowed']], axis = 1)
low = 99999
for i in df_new[0]:
    if i > 0:
        if i < low:
            low = i

print df_new[df_new[0] == low]['Team'].to_string().split(' ')[-1]
