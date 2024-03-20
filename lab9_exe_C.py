"""
=======================================
Name: lab9_exe_C.py
Assignment: Lab 9, Exercise C
Author(s): Sarah Yip (UCID: 30174831), Stephenie Oboh (UCID: 30151629)
Submission: March 20, 2024
Description: Fetch data by Python.
=======================================
"""

import requests
import json

# Fetches product data from the specified URL.
def fetch_product_data(url):
    """
    - Args: url (str) -> The URL to fetch product data from.
    - Returns: list -> List of products retrieved from the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        # Extracts the list of products from the JSON response
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# Displays the names of all products.
def list_all_products(products):
    """
    - Args: products (list) -> List of products to display.
    - Output: List of product titles retrieved from the URL.
    """
    for product in products:
        print(product['title'])


# Searches for a product by name and prints its details.
def search_product(products, name):
    """
    - Args:
        products (list) -> List of products to search within.
        name (str) -> Name of the product to search for.
    - Output: Details of the matching product if found, otherwise prints "Product not found." message.
    """
    found = False
    for product in products:
        if product['title'].lower() == name.lower():
            # Prints the details of the matching product
            print(json.dumps(product, indent=4))
            found = True
            break
    if not found:
        # Prints a message if the desired product is not found
        print("Product not found.")


# Main function to interact with the user and run the application.
def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            # Prompt the user for options and handle user input
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n> ")

            if choice == '1':
                print("List of all products:")
                list_all_products(products)
                print('\n')
            elif choice == '2':
                product_name = input("Enter the product name: ")
                print("Product details:")
                search_product(products, product_name)
                print('\n')
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.\n")
    else:
        print("Failed to fetch product data.\n")

if __name__ == "__main__":
    main()



