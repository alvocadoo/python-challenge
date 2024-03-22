import csv

# Define file path
file_path = "PyBank/Resources/budget_data.csv"

# Initialize Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        
        # Extract profit/loss and date
        profit_loss = int(row[1])
        date = row[0]
        
        # Calculate net total amount of profit/losses
        net_total += profit_loss
        
        # Calculate the change in profit/losses
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)
        
        # Set the current profit/loss as the previous for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/losses
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase in profits (date and amount)
greatest_increase_amount = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase_amount)
greatest_increase_month = months[greatest_increase_index]

# Find the greatest decrease in profits (date and amount)
greatest_decrease_amount = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease_amount)
greatest_decrease_month = months[greatest_decrease_index]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")