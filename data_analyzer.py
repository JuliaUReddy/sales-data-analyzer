import csv

#Load Data Once
def loadSalesData():
    data = []
    with open("sales.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Amount"] = int(row["Amount"])
            data.append(row)
    return data

#Feature1: List All Sales
def listAllSales(data):
    total = 0

    for row in data:
        print(f"{row["Name"]} bought {row["Product"]} for ${row['Amount']}")

        total += row['Amount']
    print(f"\nTotal amount spent is: {total}")


#Feature2: Highest Spender
def highestSpender(data):
    totals = {}

    for row in data:
        if row["Name"] in totals:
            totals["Name"] += row['Amount']
        else:
            totals["Name"] = row['Amount']

    for name, total in totals.items():
        print(f"{name}: {total}")

    
    max_name = ""
    max_total = 0

    for name, total in totals.items():
        if total > max_total:
            max_total = total
            max_name = name

    print(f"\nThe top spender is: {max_name} with {max_total} ")

# Feature3: Sproduct Sales
def productSales(data):
    product_sales ={}


    for row in data:
        product = row["Name"]
        amount = int(row['Amount'])
        if product in product_sales:
            product_sales[product] += amount
        else:
            product_sales[product] = amount
    for product, total in product_sales.items():
        print(f"{product}: {total}")


# Main Menu
def main():
    data = loadSalesData()
    while True:
        choice = int(input("\n 1: List All Sales 2: Top Spender 3: Each Product Sale 4: Exit\n"))

        if choice == 1:
            listAllSales(data)
        elif choice == 2:
            highestSpender(data)
        elif choice == 3:
            productSales(data)
        elif choice == 4:
            break
        else:
            print("invalid choice")


# Run Program
main()


