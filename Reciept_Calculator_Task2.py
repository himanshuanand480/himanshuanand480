while True:   
 def calculator(item_name,number_of_kg):
    print("====Items available in our shop====")
    list1=["Apple,Mango,Lichi,Guava"]
    print(list1)
    tax_rate=number_of_kg*0.07
    discount_rate=number_of_kg*0.15
    if item_name=="Apple":
        price=200*number_of_kg
    elif item_name=="Mango":
        price=150*number_of_kg
    elif item_name=="Lichi":
        price=180*number_of_kg
    else:
        price=0*number_of_kg
        tax_rate=0
        discount_rate=0
        print("items is not available in my shop")
        print("================sorry=====================")
    total=price-tax_rate-discount_rate
    print("Your total cost:",total)
    print("====Thank you visit Again====")
    print()
    print()
    print("===Enter new data===")
 print("====welcome====")
 number_of_kg=float(input("enter the quantity in kg"))
 item_name=input("enter the item name")
 calculator(item_name,number_of_kg)
    
