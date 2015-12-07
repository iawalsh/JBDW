# -*- coding: utf-8 -*-

import pandas as pd

fileName = '/Users/Isaac/Desktop/School/Last Semester/MIS 407/MIS407_Project1/NCES-DROPOUT_RACE.xls'
fileName2 = '/Users/Isaac/Desktop/School/Last Semester/MIS 407/MIS407_Project1/ECPI-MEDIAN_FAMILY_INCOME.xls'
fileName3 = '/Users/Isaac/Desktop/School/Last Semester/MIS 407/MIS407_Project1/NCES-HIGHSCHOOL_EMPLOY_TOTAL.xls'

df_drop = pd.read_excel(fileName)
df_income = pd.read_excel(fileName2)
df_employment = pd.read_excel(fileName3)

#dates to calc:
#   1990 - 1995
#   1995 - 2000
#   2000 - 2004
#   2004 - 2006
#   2006 - 2010
def calcSlope(x1, y1, x2, y2):
    slope = (y2 - y1)/(x2 - x1)
    return slope

# Calculating slopes for the Median Family Income Dataset
income_y1 = df_income.loc[df_income['Date'] == '1990-12-31']['Dollars'].values 
income_y2 = df_income.loc[df_income['Date'] == '1995-12-31']['Dollars'].values
income_x1 = 1990
income_x2 = 1995

income_slope1 = calcSlope(income_x1, income_y1, income_x2, income_y2)

income_y1 = df_income.loc[df_income['Date'] == '1995-12-31']['Dollars'].values 
income_y2 = df_income.loc[df_income['Date'] == '2000-12-31']['Dollars'].values
income_x1 = 1995
income_x2 = 2000

income_slope2 = calcSlope(income_x1, income_y1, income_x2, income_y2) 

income_y1 = df_income.loc[df_income['Date'] == '2000-12-31']['Dollars'].values 
income_y2 = df_income.loc[df_income['Date'] == '2004-12-31']['Dollars'].values
income_x1 = 2000
income_x2 = 2004

income_slope3 = calcSlope(income_x1, income_y1, income_x2, income_y2)

income_y1 = df_income.loc[df_income['Date'] == '2004-12-31']['Dollars'].values 
income_y2 = df_income.loc[df_income['Date'] == '2006-12-31']['Dollars'].values
income_x1 = 2004
income_x2 = 2006

income_slope4 = calcSlope(income_x1, income_y1, income_x2, income_y2)

income_y1 = df_income.loc[df_income['Date'] == '2006-12-31']['Dollars'].values 
income_y2 = df_income.loc[df_income['Date'] == '2010-12-31']['Dollars'].values
income_x1 = 2006
income_x2 = 2010

income_slope5 = calcSlope(income_x1, income_y1, income_x2, income_y2)

print("Income Slopes")
print(income_slope1)
print(income_slope2)
print(income_slope3)
print(income_slope4)
print(income_slope5)
    
# Calculating slopes for the High School Drop Rate Dataset
drop_y1 = df_drop.loc[df_drop['Date'] == '1990-12-31']['Total'].values 
drop_y2 = df_drop.loc[df_drop['Date'] == '1995-12-31']['Total'].values
drop_x1 = 1990
drop_x2 = 1995

drop_slope1 = calcSlope(drop_x1, drop_y1, drop_x2, drop_y2)

drop_y1 = df_drop.loc[df_drop['Date'] == '1995-12-31']['Total'].values 
drop_y2 = df_drop.loc[df_drop['Date'] == '2000-12-31']['Total'].values
drop_x1 = 1995
drop_x2 = 2000

drop_slope2 = calcSlope(drop_x1, drop_y1, drop_x2, drop_y2)

drop_y1 = df_drop.loc[df_drop['Date'] == '2000-12-31']['Total'].values 
drop_y2 = df_drop.loc[df_drop['Date'] == '2004-12-31']['Total'].values
drop_x1 = 2000
drop_x2 = 2004

drop_slope3 = calcSlope(drop_x1, drop_y1, drop_x2, drop_y2)

drop_y1 = df_drop.loc[df_drop['Date'] == '2004-12-31']['Total'].values 
drop_y2 = df_drop.loc[df_drop['Date'] == '2006-12-31']['Total'].values
drop_x1 = 2004
drop_x2 = 2006

drop_slope4 = calcSlope(drop_x1, drop_y1, drop_x2, drop_y2)

drop_y1 = df_drop.loc[df_drop['Date'] == '2006-12-31']['Total'].values 
drop_y2 = df_drop.loc[df_drop['Date'] == '2010-12-31']['Total'].values
drop_x1 = 2006
drop_x2 = 2010

drop_slope5 = calcSlope(drop_x1, drop_y1, drop_x2, drop_y2)

print("Dropout Rate Slopes")
print(drop_slope1)
print(drop_slope2)
print(drop_slope3)
print(drop_slope4)
print(drop_slope5)
    
# Calculating slopes for the High School Employment Dataset
employment_y1 = df_employment.loc[df_employment['Date'] == '1990-12-31']['Total Employed'].values 
employment_y2 = df_employment.loc[df_employment['Date'] == '1995-12-31']['Total Employed'].values
employment_x1 = 1990
employment_x2 = 1995

employment_slope1 = calcSlope(employment_x1, employment_y1, employment_x2, employment_y2)

employment_y1 = df_employment.loc[df_employment['Date'] == '1995-12-31']['Total Employed'].values 
employment_y2 = df_employment.loc[df_employment['Date'] == '2000-12-31']['Total Employed'].values
employment_x1 = 1995
employment_x2 = 2000

employment_slope2 = calcSlope(employment_x1, employment_y1, employment_x2, employment_y2)
    
employment_y1 = df_employment.loc[df_employment['Date'] == '2000-12-31']['Total Employed'].values 
employment_y2 = df_employment.loc[df_employment['Date'] == '2004-12-31']['Total Employed'].values
employment_x1 = 2000
employment_x2 = 2004

employment_slope3 = calcSlope(employment_x1, employment_y1, employment_x2, employment_y2)

employment_y1 = df_employment.loc[df_employment['Date'] == '2004-12-31']['Total Employed'].values 
employment_y2 = df_employment.loc[df_employment['Date'] == '2006-12-31']['Total Employed'].values
employment_x1 = 2004
employment_x2 = 2006

employment_slope4 = calcSlope(employment_x1, employment_y1, employment_x2, employment_y2)
    
employment_y1 = df_employment.loc[df_employment['Date'] == '2006-12-31']['Total Employed'].values 
employment_y2 = df_employment.loc[df_employment['Date'] == '2010-12-31']['Total Employed'].values
employment_x1 = 2006
employment_x2 = 2010

employment_slope5 = calcSlope(employment_x1, employment_y1, employment_x2, employment_y2)
    
print("High School Employment Slopes")
print(employment_slope1) 
print(employment_slope2) 
print(employment_slope3) 
print(employment_slope4) 
print(employment_slope5) 



    
'''
print("--- DROP RATE DATASET ---")
print("prints just total column")
print(df_drop['Total'])

print("prints just date column")
print(df_drop['Date'])


print("--- INCOME DATASET ---")
print("prints full dataset")
print(df_income)

print("prints just dollar column")
print(df_income['Dollars'])

print("prints just date column")
print(df_income['Date'])


print("--- HIGHSCHOOL EMPLOYMENT DATASET ---")
print("prints just Total Employed column")
print(df_employment['Total Employed'])

print("prints just date column")
print(df_employment['Date'])
'''