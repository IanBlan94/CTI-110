import matplotlib.pyplot as plt

'''print("How many pokeman have you caught in the past three days?")
print ("day 1:", end="")
day1 = int(input())

print ("day 2:", end="")
day2 = int(input())

print ("day 3:", end="")
day3 = int(input())

# put the data in a list

data = [day1, day2, day3]
# TODO: Graph the real data

total = sum(data)
print("The total pokemon caught was " , total)
max = max(data)
print("The maximum amount of pokemon caught between the three days is ", max)
min = min(data)
print("The minimum amount of pokemon caught between the three days is ", min)
average = total / data'''


data = []

num_days = int(input("How many days did you go out? "))

for day in range(num_days):
  print("Day", day, ":", end="")
  today = int(input())
  data.append(today)

total = sum(data)
print("The total amount of pokemans caught was ", total)
max = max(data)
print("The max amount of pokemans caught on any day was ", max)
min = min(data)
print("The minimum amount of pokemans caught on any day was ", min)

average = total / num_days 
print("The average of all days is ", average) 

fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokemans Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()



