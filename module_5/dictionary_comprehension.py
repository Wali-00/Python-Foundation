square = {x:x**2 for x in range(1,11)}
print(square)
square = {x:x**2 for x in range(1,11) if x%2==0}
print(square)

Co_ordinates =  [(10,20,30),(40,50,60),(70,80,90)]
locations = ["Dhaka","Dinajpur","Joypurhat"]
exact_locations = {co:lo for co,lo in zip(Co_ordinates,locations)}
print(exact_locations)