menu={
  "pasta":40,
  "pizza":60,
  "salad":30,
  "burger":60,
  "cofee":25,
  "tea":10
} 
print("welcome to PYTHON RESTAURANT ")
print(" pasta = 40 \n pizza = 60 \n salad = 30 \n burger = 60 \n cofee = 25 \n tea = 10 \n")
l={}
order_total=0
while(True):
  item_1=input("Enter the name of the item you want to order : ")
  q=int(input("enter the quantity you require : "))
  if item_1 in menu:
      order_total+=menu[item_1]*q
      l[item_1]=l.get(item_1,0)+q
      print(f"your item {item_1} has been added to your oder")
  else:
      print(f"ordered item {item_1} not available in the menu") 
  x=input("do you want to order something else (y/n) ")
  if x=="n":
     break
print(" your order is succesfully placed ")
print("here is the list of your order and the total bill ")
for k,v in l.items():
   print(f"{k} ---- {v}")
print("your total bill is == ",order_total)
