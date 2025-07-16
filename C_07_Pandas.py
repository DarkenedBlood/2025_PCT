import pandas

# lists to hold ticket details
all_item_names = ["A", "B", "C", "D", "E"]
all_weights = [1000.56, 1527.63, 150, 65, 2000]
all_kg_weights = [1.00056, 1.52763, 0.15, 0.065, 2]
all_prices = [150, 2763, 1200, 1340, 5555]
all_price_per_kg = [149.91604701367237, 1808.684039983504, 8000.0, 20615.384615384613, 2777.5]
all_rounded_price_kg = [149.92, 1808.68, 8000.00, 20615.38, 2777.50]


price_comparison_dict = {
    'Name': all_item_names,
    'Weights': all_weights,
    'Weights (KG)': all_kg_weights,
    'Prices': all_prices,
    'Prices per KG': all_price_per_kg,
    'Prices per KG (2 dp)': all_rounded_price_kg
}

# create dataframe / table from dictionary
price_comparer_frame = pandas.DataFrame(price_comparison_dict)

print(price_comparer_frame)
