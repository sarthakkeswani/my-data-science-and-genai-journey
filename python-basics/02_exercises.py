# 1 Create a list of 5 numbers → print their sum.
num = [1,2,3,4,5]
sum=0
for i in range(0,len(num)):
    sum+=num[i]
print(sum)

# 2 Dictionary

movie = {
    "name": "Dhurandar",
    "year": 2025,
    "rating": 8.7,
    "actors": ["Ranveer Singh", "Sanjay Dutt", "R Mahadewan"]
}

#3
for i in movie["actors"]:
    print(i)

#4 function odd or even

def OddEven(x):
    if x%2==0:
        print(x, "is Even")
    else:
        print(x,"is odd")

OddEven(10)