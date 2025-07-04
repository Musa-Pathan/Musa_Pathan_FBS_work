#3. Convert distant given in feet and inches into meter and centimeter.
feet=int(input("enter the distance in feet:"))
inches=int(input("enter the distance in inches:"))
total_meter=(feet*0.3048)+(inches*0.0254)
meter=int(total_meter)

centimeter=(total_meter-meter)*100
print("meter is :",total_meter,"centimeter is:",centimeter)