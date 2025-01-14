
import matplotlib.pyplot as plt

# Drawing a line from (1, 2) to (6, 8)
plt.plot([1, 6], [2, 8], label='Solid Line')

# Drawing a dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
plt.plot([1, 2, 6, 8], [3, 8, 1, 10], linestyle=':', label='Dotted Line')

# Adding labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Diagram')
plt.legend()

# Show the plot
plt.show()
