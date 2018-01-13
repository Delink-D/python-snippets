# unpacking the list to a function


def health_calc(age, apples, cigar):
    ans = (100 - age) + (apples * 3.5) - (cigar * 2)
    print('you are', ans, 'healthy')

age_input = input('How old are you? ')
apples_input = input('How many apples per day? ')
cigar_input = input('How cigarettes ? ')

myList = [int(age_input), int(apples_input), int(cigar_input)]

# 1st
# healthCalc(myList[0], myList[1], myList[2])

# 2nd
health_calc(*myList)
