
cubed = [i**3 for i in range(1, 1001, 2)]

def summer (element):
    sum = 0
    while element != 0:
        sum += element % 10
        element //= 10
    return sum

sum_cubed = 0
for element_arr in cubed:
    if summer(element_arr) % 7 == 0:
        sum_cubed += element_arr
print(sum_cubed)

sum_cubed = 0
for element_arr in cubed:
    if summer(element_arr + 17) % 7 == 0:
        sum_cubed += element_arr + 17
print(sum_cubed)
