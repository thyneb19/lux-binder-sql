import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://testuser:testpass@localhost:5432/testdb")

data = pd.read_csv('https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/college.csv')
data.to_sql(name='college', con=engine, if_exists = 'replace', index=False)

data = pd.read_csv('https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/car.csv')
data.to_sql(name='car', con=engine, if_exists = 'replace', index=False)

employee = pd.read_csv("https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/employee.csv")
employee_demo = employee[['EmployeeNumber', 'Age', 'Education', 'EducationField', 'Gender', 'MaritalStatus', ]]
employee_work_details = employee[['BusinessTravel', 'DailyRate', 'Department','EmployeeNumber', 'HourlyRate','JobInvolvement', 'JobLevel', 'JobRole', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'StandardHours', 'StockOptionLevel','TotalWorkingYears', 'TrainingTimesLastYear','YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion','YearsWithCurrManager']]
employee_satisfaction = employee[['EmployeeNumber', 'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']]

employee_demo = employee_demo.rename(columns={'EmployeeNumber':'demo_employeenumber'})
employee_work_details = employee_work_details.rename(columns={'EmployeeNumber':'work_employeenumber'})
employee_satisfaction = employee_satisfaction.rename(columns={'EmployeeNumber':'satisfaction_employeenumber'})

employee_demo.to_sql(name="employee_demographics", con=engine, if_exists="replace", index=False)
employee_work_details.to_sql(name="employee_work_details", con=engine, if_exists="replace", index=False)
employee_satisfaction.to_sql(name="employee_satisfaction", con=engine, if_exists="replace", index=False)