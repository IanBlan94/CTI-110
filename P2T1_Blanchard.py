import matplotlib.pyplot as plt
data = []
print("How many pokeman have you caught in the past three days?")
print ("day 1:", end="")
day1 = int(input())

print ("day 2:", end="")
day2 = int(input())

print ("day 3:", end="")
day3 = int(input())

# put the data in a list

data = [day1, day2, day3]
# TODO: Graph the real data


fig, ax = plt.subplots()
ax.plot([1, 2, 3], data)
plt.title("Pokemans Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()




