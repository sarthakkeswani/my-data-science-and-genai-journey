print("Hello Data Science + GenAI!")
name = "Sarthak"
age = 22
height = 5.8
is_learning = True

#Data Types
print(name, age, height, is_learning)
print(type(name), type(age), type(height), type(is_learning))

#Lists
numbers = [10,20,30,40,50]
print(numbers)

numbers.append(60)
numbers.remove(30)
print(numbers[0],numbers[-1])
print(numbers[1:4])

#Dictionaries

student = {
    "name":"Sarthak",
    "age":22,
    "skills": ["Python", "Git", "GenAI"]
}
print(student["name"])
print(student["skills"][1])
student["city"] = "Delhi"
print(student)