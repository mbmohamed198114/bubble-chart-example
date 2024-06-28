import matplotlib.pyplot as plt

# Data for the bubble chart
regions = [
    'Africa', 'Southeast Asia', 'Eastern Mediterranean', 'Western Pacific', 
    'Europe', 'Americas', 'Sweden'
]
global_burden_disease = [25, 30, 10, 15, 9, 8, 0.3]
global_workforce = [3, 5, 8, 25, 37, 40, 1]
bubble_sizes = [200, 300, 150, 200, 250, 300, 150]  # Sizes for visualization

# Plotting the bubble chart
plt.figure(figsize=(14, 8))
plt.scatter(global_workforce, global_burden_disease, s=bubble_sizes, alpha=0.5)

# Annotating the points
for i, region in enumerate(regions):
    plt.annotate(region, (global_workforce[i], global_burden_disease[i]), fontsize=12)

# Adding custom annotations and lines
plt.axline((0, 0), slope=1, color='r', linestyle='--')
plt.annotate('3% vs. 25%', (2, 23), color='red', fontsize=12)
plt.annotate('37% vs. 9%', (36, 7), color='green', fontsize=12)
plt.annotate('Difference 33-fold!', (15, 25), color='purple', fontsize=12, rotation=30)

# Labels and title
plt.xlabel('% of global workforce', fontsize=14)
plt.ylabel('% of global burden of disease', fontsize=14)
plt.title('Global Workforce vs. Global Burden of Disease', fontsize=16)

plt.grid(True)
plt.show()
