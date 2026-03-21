#Tip calculator - 100-days-of-python
#Date created: 21 Mar 2026

print("Welcome to the Tip Calculator\n")

bill = float(input("\nHow much is the total bill? RM "))
tip_percent = int(input("\nHow many percent you want to tip? 10, 12, or 15? "))
person = int(input("\nHow many people to split? "))
tip = (tip_percent / 100) + 1
split_bill = round((bill * tip) / person, 2)

print(f"Amount each person need to pay is: RM {split_bill}")

#suggestion for further learning - add extra question if user want to cover the tip / split equally