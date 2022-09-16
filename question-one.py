input = "5 dollar"


# for i in range(len(input)):
#     if input[i]== " " or input[i]>str(5):
#        new_list = list(input)
#        new_list.pop(1)
#        new_list.pop(0)
#        print(new_list)



#1(b)
x=3
y=5

#a. x == y
print(x==y) #False

#b
print(x > y-3) #true

#c
print(x<=y-2) #True


#d. x == y or x > 2
print(x == y or x > 2)#True

#e
print(x != 6 and y > 10) #False

#f
print(x > 0 and x < 100)# True


#1(c)
input1 = "I am a python dev"
# reversing words in the string
splitted_string = input1.split()[::-1]
string_characters = []
for i in splitted_string:
    # apending reversed words to the list
    string_characters.append(i)
# printing reverse words
print(" ".join(string_characters))




# 1(d)
def problem_one():
    capitals = {

        "Maryland": "Annapolis",
        "California": "Sacramento",
        "New York": "Albany",
        "Utah": "Salt Lake City",
        "Alabama": "Montgomery"

    }

    for state, city in capitals.items():
     print(f"The capital of {state} is {city}")

#calling the function
problem_one()     
