N = int(input())
k = int(input())
people = list(range(1, N+1))
while len(people) != 1:
    index = k % len(people)
    del people[index]
    k = index + 2
print(people)