# unpacking the list to a function


def health_calc(age, apples, ciger):
    ans = (100 - age) + (apples * 3.5) - (ciger * 2)
    print('you are', ans, 'healthy')

myList = [25, 2, 0]

# 1st
# healthCalc(myList[0], myList[1], myList[2])

# 2nd
health_calc(*myList)
