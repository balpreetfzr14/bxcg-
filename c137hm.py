import matplotlib.pyplot as plt
week = ['week 1','week 2','week 3','week 4']
money = [34,23,45,32]
plt.plot(week,money,color = 'green', marker = '*', markersize = 12,linewidth = 4,linestyle = 'dotted')
plt.title('money saved each week')
plt.ylabel('money saved')
plt.xlabel('week number')
plt.show()
plt.bar(week,money,color = 'green', )
plt.title('money saved each week')
plt.ylabel('money saved')
plt.xlabel('week number')
plt.show()

