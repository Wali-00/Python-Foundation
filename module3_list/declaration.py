# declare
float_numbers = [1.2,5.2,6.3,9.3,5.5]
print(float_numbers)
print(type(float_numbers)) # list
print(type(float_numbers[0])) # float

string = ['Wali', 'Israt', 'Onik', 'Tanvir']
print(string)
print(type(string)) #list
print(type(string[0])) #string

mix = ['Wali', 23, 5.4]
print(type(mix)) #list
print(type(mix[0])) #string
print(type(mix[1])) #int
print(type(mix[2])) #float

#2d list
nested_list = [[10,20,30],[40,50,60],[70,80,90]]
print(type(nested_list))
print(type(nested_list[0]))
print(type(nested_list[0][1]))