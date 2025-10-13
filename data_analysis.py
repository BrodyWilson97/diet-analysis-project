import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')

print("Starting data analysis...")

# Create sample data since we don't have the real CSV
data = {
    'Diet_type': ['Paleo', 'Paleo', 'Vegan', 'Keto', 'Mediterranean', 'Vegan', 'Keto'],
    'Recipe_name': ['Bone Broth', 'Pork Sides', 'Vegan Salad', 'Keto Burger', 'Med Salad', 'Vegan Soup', 'Keto Chicken'],
    'Cuisine_type': ['american', 'asian', 'american', 'mexican', 'mediterranean', 'french', 'american'],
    'Protein(g)': [5.22, 181.55, 10, 30, 15, 8, 25],
    'Carbs(g)': [1.29, 28.62, 20, 5, 30, 15, 3],
    'Fat(g)': [3.2, 146.14, 5, 20, 10, 2, 15],
    'Extraction_day': ['10/16/2022', '10/16/2022', '10/16/2022', '10/16/2022', '10/16/2022', '10/16/2022', '10/16/2022'],
    'Extraction_time': ['17:20:09', '17:20:09', '17:20:09', '17:20:09', '17:20:09', '17:20:09', '17:20:09']
}

df = pd.DataFrame(data)
print("Sample dataset created!")
print(df)

# Calculate averages
avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
print("\nAverage macros by diet type:")
print(avg_macros)

# Create simple visualization
plt.figure(figsize=(10, 6))
avg_macros.plot(kind='bar')
plt.title('Average Macronutrients by Diet Type')
plt.ylabel('Grams')
plt.tight_layout()
plt.savefig('output.png')
print("\nChart saved as 'output.png'")

print("\n✅ Analysis complete!")