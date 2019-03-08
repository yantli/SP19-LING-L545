import sys
import matplotlib.pyplot as plt

labels = {0:'rus', 1:'chi', 2:'fin',3:'por',4:'jpn',5:'swe',6:'arm',7:'rum',8:'nno',9:'kor'}
x = [0.20, 0.03, 0.30, 0.09, 1.0, 0.06, 0.57, 0.15, 0.05, 1]  # proportion of OV
y = [0.80, 0.97, 0.70, 0.91, 0.0, 0.94, 0.43, 0.85, 0.95, 0]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)

plt.show()
