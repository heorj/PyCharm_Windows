
radius = int(input('Please enter the radius '))
area_circle= ((radius + radius) * (radius + radius)) * 3.14
side = int(input("Enter side of your sqaure "))
area_square = side * side

if area_circle > area_square:
    print('True')
else:print(False)