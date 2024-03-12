import os
import csv

# Reading the Dataset
file_path = os.path.join("budget_data.csv")

# Define the variables to store results
months = []
profit_loss_changes = []

total_months = 0
net_total = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Calculating Total Number of Months and Net Total Amt
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # skip header
    for row in csvreader:
        total_months += 1

        profit_loss = int(row[1])
        net_total += profit_loss

        # Changes in profit and losses
        current_month_profit_loss = profit_loss
        if total_months > 1:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            profit_loss_changes.append(profit_loss_change)

            # Update greatest increase and decrease
            if profit_loss_change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = profit_loss_change
            if profit_loss_change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = profit_loss_change

        previous_month_profit_loss = current_month_profit_loss

# sum and avg of profit and losses
sum_profit_loss = sum(profit_loss_changes)
average_profit_loss = round(sum_profit_loss / (total_months - 1), 2)

# Displaying the Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# exports !!!!

output_file = "financial_analysis.txt"
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_profit_loss}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print(f"\nFinancial analysis has been exported to {output_file}.")