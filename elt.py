import pandas as pd
import socket
import datetime

# Print student information
print("Student Name: Your Name")
print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
print(f"Machine Name: {socket.gethostname()}\n")

# Load the CSV files
customers = pd.read_csv('customer.csv')
orders = pd.read_csv('orders.csv')

# Merge the data
merged_data = pd.merge(orders, customers, on='customer_id')

# Calculate total sales
merged_data['total_sales'] = merged_data['quantity'] * merged_data['price']

# Add status column based on order date
merged_data['order_date'] = pd.to_datetime(merged_data['order_date'])
merged_data['status'] = merged_data['order_date'].apply(
    lambda x: 'new' if x >= datetime.datetime(2024, 10, 1) else 'old'
)

# Filter for sales > $4500
filtered_data = merged_data[merged_data['total_sales'] > 4500]

# Select relevant columns
result = filtered_data[['customer_id', 'name', 'product', 'quantity', 
                       'price', 'total_sales', 'order_date', 'status']]

# Print the original CSV data
print("=== Customers CSV ===")
print(customers)
print("\n=== Orders CSV ===")
print(orders)

# Print the final aggregated table
print("\n=== Aggregated Table (Sales > $4500) ===")
print(result)