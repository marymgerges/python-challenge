# Modules
import os
import csv

# Set path for file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Set initial variable for total number of months included in the data
total_number_months = 0

# Set initial variable for total profit/loss over the entire period
total_profit_or_loss = 0

# Set initial variable for the previous profit/loss
previous_profit_or_loss = 0

# Set initial variable for the change in profit/loss over the entire period
change_of_profit_or_loss = 0

# Set initial variable for total change in profit/loss over the entire period
total_change = 0

# Set initial variable for the counter for the total change in profit/loss over the entire period
total_change_counter = 0

# Set initial variable for the greatest increase in profits over the entire period
greatest_increase_profits = ["", 0]

# Set initial variable for the greatest decrease in profits over the entire period
greatest_decrease_profits = ["", 99999999]

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip row of headers
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Calculate total number of months in data
        total_number_months += 1

        # Calculate total profit/loss over entire period
        total_profit_or_loss += int(row[1])

        # Calculate change in profit/loss from previous to current row
        if row[0] != "Jan-10":
            change_of_profit_or_loss = int(row[1]) - previous_profit_or_loss
            total_change += change_of_profit_or_loss
            total_change_counter += 1

        previous_profit_or_loss = int(row[1])


        # Calculate greatest increase in profits (date and amount) over entire period
        if greatest_increase_profits[1] < change_of_profit_or_loss:
            greatest_increase_profits[0] = row[0]
            greatest_increase_profits[1] = change_of_profit_or_loss

        # Calculate greatest decrease in profits (date and amount) over entire period
        if greatest_decrease_profits[1] > change_of_profit_or_loss:
            greatest_decrease_profits[0] = row[0]
            greatest_decrease_profits[1] = change_of_profit_or_loss 

# Calculate average change in profit/loss over entire period and set value to two decimal places
average_change_profits_or_losses = round(total_change/total_change_counter, 2)


# Print analysis to console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_months}")
print(f"Total: ${total_profit_or_loss}")
print(f"Average Change: ${average_change_profits_or_losses}")
print(f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease_profits[0]} (${greatest_decrease_profits[1]})")

analysis = os.path.join("analysis/analysis_results.txt")

# Print analysis to text file
with open(analysis, "w") as csvfile:
    # csvwriter = csv.writer(csvfile)
    csvfile.write("Financial Analysis\n")
    csvfile.write("----------------------------\n")
    csvfile.write(f"Total Months: {total_number_months}\n")
    csvfile.write(f"Total: ${total_profit_or_loss}\n")
    csvfile.write(f"Average Change: ${average_change_profits_or_losses}\n")
    csvfile.write(f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})\n")
    csvfile.write(f"Greatest Decrease in Profits: {greatest_decrease_profits[0]} (${greatest_decrease_profits[1]})\n")