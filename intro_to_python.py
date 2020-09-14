# List
nba_teams = ["Lakers", "Nuggets", "Celtics"]
nba_teams.append("clippers")

# print with format
print(f"Length of nba teams: {len(nba_teams)}")

array_of_ones = [1] * 6

# declaring a list with range
one_through_ten = list(range(10))
print(one_through_ten)


random_number = [9,6,7,4,2,4]
random_number.sort()

# dictionary
dog = {
    "name": "Rocc",
    "location": "Long Beach City",
    "age": 9
}

print(dog)

# using f keyword for string interpolation
my_message = f"{dog["name"] lives in {dog['location']}"
print(memoryview)

def add_numbers(num1, num2):
    result = num1 + num2
    return result

def print_this():
    print("hello, my name is...")

def channee_prediction(team1, team 2):
    return "I predict the {} and {} in the Western Conforence"
    channee_prediction(name_teams[0], nba_teams[3])

def legal_age(age):
    if (age<21):
        return "Sorry your too young"
        elif(age == 21):
            return "You made it"
            else:
                return "You're free to pass"

                