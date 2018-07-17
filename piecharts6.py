#! python
import matplotlib.pyplot as plt
plt.style.use('dark_background')

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'k']

plt.pie(slices, 
        labels=activities, 
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

#plt.xlabel('x')
#plt.ylabel('y')

plt.title('Interesting Graph\nCheck it out')
#plt.legend()

plt.show()

