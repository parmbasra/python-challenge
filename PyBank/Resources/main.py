#Library allows to excess path objects across operating systems
import os

#Library allows to read and write to the csv files
import csv

#Library allow us to set currency symbol 
import locale

#Here we are setting which currency symbol should be shown
locale.setlocale(locale.LC_ALL,'')

#Building the path to the csv file and storing it into the object
csvpath = os.path.join("..","Resources","budget_data.csv")

#To store number of months present in Date (Column A) populated from month_list
total_months = 0

#To store the month list as per the Column A data 
month_list = []

#List to store the profit loss differences
change_in_pofit_loss_list = []

#List to store the Column B (Profit/Loss)
profit_loss_list = []

#To store the diffrence
total_change = 0

#To store the average of total rows divided by the change in the profit loss and round the result to two decimal places
average_change = 0

#To store the maximum of change in the profit loss
max_change_in_profits = 0

#To store the minimum of change in the profit loss
min_change_in_profits = 0

#To store the greatest increase in profits alongwith the month
greatest_increase_in_profits_month = ""

#To store the greatest decrease in profits alongwith the month
greatest_decrease_in_profits_month = ""

#Opening the csvfile for reading
with open(csvpath) as csvfile:

    #Returns a reader object which will iterate over lines in given csvfile
    csvreader = csv.reader(csvfile, delimiter=',')

    #To skip the headers stored in the csv file and stored them in the variable
    heading = next(csvreader, None) 
    
    #Fetching each row through the csvreader
    for csvrow in csvreader:
        
        #Append row by row Column A values from the CSV into the list
        month_list.append(csvrow[0])

        #calculated number of total months presented in the CSV file Column A
        total_months = len(month_list)

        #Append row by row Column B values from the CSV into the list
        profit_loss_list.append(int(csvrow[1]))

        #Here calulating the difference in the two values as there is no change in the profit loss for row[1] data value, so appending 0 as there is no value at index (-1) of profit_loss_list
        if(total_months - 2 < 0):
            change_in_pofit_loss_list.append(0)
        else:
            change_in_pofit_loss_list.append(profit_loss_list[total_months - 1] - profit_loss_list[total_months - 2])
    
    #Calculated and stored values 
    total_change = sum(change_in_pofit_loss_list)
    average_change = round(total_change/int(len(change_in_pofit_loss_list)-1), 2)
    max_change_in_profits = max(change_in_pofit_loss_list)
    greatest_increase_in_profits_month = month_list[change_in_pofit_loss_list.index(max_change_in_profits)]
    min_change_in_profits = min(change_in_pofit_loss_list)
    greatest_decrease_in_profits_month = month_list[change_in_pofit_loss_list.index(min_change_in_profits)]


#Created a list and assign all the values to print on the console and write into the file budget_data_analysis.txt
print_analysis = []


print_analysis.append("Financial Analysis")
print_analysis.append("--------------------------------------------")
print_analysis.append(f"Total Months: {total_months}")
print_analysis.append(f"Total: {locale.currency(sum(profit_loss_list))} ")
print_analysis.append(f"Average Change: {locale.currency(average_change)} ")
print_analysis.append(f"Greatest Increase in Profits: {greatest_increase_in_profits_month} ({locale.currency(max_change_in_profits)}) ")
print_analysis.append(f"Greatest Decrease in Profits: {greatest_decrease_in_profits_month} ({locale.currency(min_change_in_profits)}) ")

#To create Analysis folder/directory for the text file
analysis_path = os.path.join("..","Analysis")

#To create or overwrite file inside the Analysis folder/directory
budget_txt_path = os.path.join("..","Analysis","budget_data_analysis.txt")

#Try to execute this part of code and throw an exception at run-time "The file or directory does not exist"
try:
    #Checking whether the Analysis folder/directory exists 
    if not os.path.exists(analysis_path):
         #If not exist create the Analysis folder/directory first 
         
         os.makedirs(analysis_path)
         #Create or overwrite the file budget_data_analysis.txt
         with open(budget_txt_path, 'w') as budget_file:
            for to_print in print_analysis:
                #To write all the statements in the print_analysis list to the file budget_data_analysis.txt
                budget_file.write(to_print + '\n')
                #To print the output on the Terminal
                print(to_print)
    else:
        #If Analysis folder/directory exists then create or overwrite the file budget_data_analysis.txt
        with open(budget_txt_path, 'w') as budget_file:
            for to_print in print_analysis:
                #To write all the statements in the print_analysis list to the file budget_data_analysis.txt
                budget_file.write(to_print + '\n')
                #To print the output on the Terminal
                print(to_print)
        
except:
   print("The file or directory does not exist")

