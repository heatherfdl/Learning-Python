# need to import a specific module for plotting
import matplotlib.pyplot as plt

# importing it under the name "plt" rather then type the whole thing out

# if it doesnt work check to make sure the package you are using is installed under preferences


# Plotting graphs in python - basic

#x = [1, 3, 5, 10] # creating a list to plot on a graph (what we are plotting)
#plt.plot(x)
#plt.show() # to visualize plot you have created

# plotting x and y against each other - will come up as 2 figures - x and y lists must be same length
#y = [7, 12, 21, 22]
#plt.plot(x, y)
#plt.show()

# Creating a plot with proper formatting
# line 1 - points
x = [3, 9, 14]
y = [2, 7, 30]
# plotting x and y
plt.plot(x, y, c="Blue", linewidth=2, label="Line 1") # after x, y, define features you want in the plot (eg color, line width...)

#line 2 - points
x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2, y2, c="green", linewidth=0.5, label="Line 2", linestyle="dashed",
         marker='o', markerfacecolor="black", markersize=10)
#plt.show()
#should show up as a plot with 2 lines (with the point values defined above)

#label axes and give the plot a title
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Two Lines")

#limits of the axes
plt.xlim(0, 30)
plt.ylim(1, 10)

#show legend on the plot (as we defined above)
plt.legend()

#get python to show plot and DONE!!
plt.show()

# New plot - keep line 1 as is, change line 2



