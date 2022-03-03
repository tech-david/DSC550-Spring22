# Thompson Sampling for Slot Machines

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000  # Amount of bets
d = len(conversionRates)  # Machines

# Creating the dataset
X = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1

# Making arrays to count our losses and wins
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

# Taking our best slot machine through beta distribution and updating its losses and wins
for i in range(N):
    selected = 0
    maxRandom = 0
    for j in range(d):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j
    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

# Showing which slot machine is considered the best
nSelected = nPosReward + nNegReward
for i in range(d):
    # Obtaining B distribution
    print('Machine number ' + str(i + 1) + ' was selected ' + str(nSelected[i]) + ' times')
print('Conclusion: Best machine is machine number ' + str(np.argmax(nSelected) + 1))

# Bar plot parameters
bin_bounds = np.linspace(0, 5, 6)
r_width = 0.7
width = bin_bounds[1] - bin_bounds[0]

# Plotting how many times each slot machine got chosen
bars_selected = plt.bar(bin_bounds[:-1] + width / 2, height=nSelected, width=width * r_width, align='edge')
plt.title('Times Selected')
plt.xlabel('Machine')
plt.yscale('linear')
plt.ylabel('# of Events')
for rect in bars_selected:
    x, y = rect.get_xy()
    w = rect.get_width()
    h = rect.get_height()
    plt.text(x + w / 2, h, f'{h}\n', ha='center', va='center')
plt.show()

# Plotting how many times each slot machine got a positive reward
bars_pos = plt.bar(bin_bounds[:-1] + width / 2, height=nPosReward, width=width * r_width, align='edge')
plt.title('+1 Reward')
plt.xlabel('Machine')
plt.yscale('linear')
plt.ylabel('# of Events')
for rect in bars_pos:
    x, y = rect.get_xy()
    w = rect.get_width()
    h = rect.get_height()
    plt.text(x + w / 2, h, f'{h}\n', ha='center', va='center')
plt.show()

# Plotting how many times each slot machine got a negative reward
bars_neg = plt.bar(bin_bounds[:-1] + width / 2, height=nNegReward, width=width * r_width, align='edge')
plt.title('-1 Reward')
plt.xlabel('Machine')
plt.yscale('linear')
plt.ylabel('# of Events')
for rect in bars_neg:
    x, y = rect.get_xy()
    w = rect.get_width()
    h = rect.get_height()
    plt.text(x + w / 2, h, f'{h}\n', ha='center', va='center')
plt.show()
