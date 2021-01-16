# Constant complexity example
# O(1) - the same time no matter how much input 
def sum(a, b, c):
    return a + b + c


print(sum(3,2,1))
# takes the same time as:
print(sum(1000,300,111))

# Linear complexity example
# O(n) - grows with the input 1:1
foodArray = ['pizza', 'burger', 'sushi', 'curry']

def findFoodInTheApp(arrayOfFood, desiredFood):
    for food in arrayOfFood:
        if food == desiredFood:
            return f'Here is your {food}'

print(findFoodInTheApp(foodArray, 'curry')) # O(n) 
