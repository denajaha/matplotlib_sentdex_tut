import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 12, 14]

plt.plot(x, y, label='First line')  # write label if you want to put it later into a legend
plt.plot(x2, y2, label='second line')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting graph boiiiii\nCheck it out')
plt.legend()    # function for putting the legend on the screen
plt.show()
