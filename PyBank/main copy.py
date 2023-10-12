import os
import csv
total_months=0
profit_revenue=0
change=0
month_year=[]
monthly_revenue=[]
csvpath = os.path.join('PyBank','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_months+=1
        profit_revenue+=int(row[1])
        monthly_revenue.append(int(row[1]))
        month_year.append(row[0])
    revenue_change=[monthly_revenue[i+1]-monthly_revenue[i] for i in range(len(monthly_revenue)-1)]
#Making a variable to find average change caculation
print(total_months)
print(profit_revenue)
print(max(revenue_change))   
print(min(revenue_change))
print(round(sum(revenue_change)/(len(revenue_change)),2))

txt_file_path = os.path.join('PyBank','PyBankAnalysis.txt')
with open(txt_file_path, 'w') as f:
    f.write('Finacial Analysis\n')
    f.write(f'Total Months:{total_months}\n')
    f.write(f'Total:{profit_revenue}\n')
    f.write(f'Average Change:{(round(sum(revenue_change)/(len(revenue_change)),2))}\n')
    f.write(f'Greastest Increase in Profits:{max(revenue_change)}\n')
    f.write(f'Greastest Decrease in Profits:{min(revenue_change)}\n')
    f.close()