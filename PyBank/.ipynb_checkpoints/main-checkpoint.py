import os
import csv
total_months=0
profit_revenue=0
change=0
net_change=[]
monthly_revenue=[]
csvpath = os.path.join('PyBank','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_months+=1
        profit_revenue+=int(row[1])
        monthly_revenue.append(int(row[1]))
        net_change= sum([profit_revenue])/len([profit_revenue])
    #average_net_change=(profit_losses)/(total_months)
    print(total_months)
    print(profit_revenue)
    #print(average_net_change)
    print(net_change)



