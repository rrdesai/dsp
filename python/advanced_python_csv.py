import pandas as pd

fac = pd.read_csv('faculty.csv')

out = open('emails.csv', 'w')

for i in fac[' email']:
    out.write(i + '\n')

