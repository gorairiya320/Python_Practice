# Define he menu
cafe_menu = {
    "Coffe":70,
    "Pasta":40,
    "Chicken pokora":10,
    "Tea":10,
    "Chawmin":70,
 }


#Greet
print("Welcome to RIYA's Cafe\nSelect menu:-")
print("Coffe: Rs70,\nPasta: Rs40,\nChicken pokora: Rs10,\nTea: Rs10,\nChawmin: Rs70\n\n")

total_Ammount=0

first_order=input("Enter the item which you want:-")
if first_order in cafe_menu:
    total_Ammount=total_Ammount+cafe_menu[first_order]
    print(f"Your item {first_order} is successfully added to your order!")
else:
    print(f"Ordered item {first_order} is not available\nPlease order something which are available!")

second_order=input("Anything else?(Yes/No):-")
if second_order=="Yes":
    scd_ord=input("Enter the second item:-")
    if scd_ord in cafe_menu:
        total_Ammount=total_Ammount+cafe_menu[scd_ord]
        print(f"Your item {scd_ord} also successfully added to your order!")
    else:
        print(f"Ordered item {scd_ord} is not available\nPlease order something which are available!")

print(f"Total ammount of item is  {total_Ammount}")
    
    