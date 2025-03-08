import csv
import random
from faker import Faker
from google.cloud import storage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


fake = Faker()

# Fetch GCP project ID and bucket name from environment variables
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")

# Constants
NUM_CUSTOMERS = 1000000  # 1 million customers
NUM_PRODUCTS = 100000    # 100 thousand products
NUM_ORDERS = 5000000     # 5 million orders

# Set up GCP storage client (assuming the service account key is set in the environment)
storage_client = storage.Client.from_service_account_json('keys/first-key.json')  # Replace with the path to your key file

# Generate Customers Data
def generate_customers():
    customers = []
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        customers.append([
            customer_id,
            fake.first_name(),
            fake.last_name(),
            fake.email(),
            fake.phone_number(),
            fake.address().replace("\n", ", "),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.country()
        ])
    return customers

# Generate Products Data
def generate_products():
    products = []
    for product_id in range(1, NUM_PRODUCTS + 1):
        products.append([
            product_id,
            fake.bs(),  # Fake product name
            fake.word(),  # Fake category
            round(random.uniform(10.0, 1000.0), 2),  # Random price
            random.randint(1, 1000)  # Random stock quantity
        ])
    return products

# Generate Orders Data
def generate_orders():
    orders = []
    for order_id in range(1, NUM_ORDERS + 1):
        customer_id = random.randint(1, NUM_CUSTOMERS)  # Randomly select a customer
        product_ids = [random.randint(1, NUM_PRODUCTS) for _ in range(random.randint(1, 5))]  # Random products per order
        total_amount = sum([random.uniform(10.0, 1000.0) for _ in product_ids])  # Random total amount
        
        orders.append([
            order_id,
            customer_id,
            fake.date_this_decade(),
            fake.address().replace("\n", ", "),
            round(total_amount, 2),
            random.choice(['Credit Card', 'PayPal', 'Bank Transfer']),
            random.choice(['Shipped', 'Pending', 'Delivered']),
            ','.join(map(str, product_ids))  # List of product IDs
        ])
    return orders

# Save CSV to GCP Bucket
def save_to_gcs(filename, data, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(filename)  # The file path in the GCP bucket
    with blob.open("w") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"{filename} has been uploaded to GCP bucket.")

# Generate the data and save to GCP
customers_data = generate_customers()
products_data = generate_products()
orders_data = generate_orders()

# Save the generated data to GCP
save_to_gcs('customers.csv', customers_data, BUCKET_NAME)
save_to_gcs('products.csv', products_data, BUCKET_NAME)
save_to_gcs('orders.csv', orders_data, BUCKET_NAME)

print("Data generation and upload to GCP completed.")
