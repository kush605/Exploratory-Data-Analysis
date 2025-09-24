
# Task 2: Exploratory Data Analysis
# Objective: Understand data using statistics and visualizations
# Tools: Pandas, Matplotlib, Seaborn, Plotly
# ===================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# =============================
# Load Dataset
# =============================
# Change 'data.csv' to your dataset file name
df = pd.read_csv("crocodile_dataset.csv")

# =============================
# 1. Summary Statistics
# =============================
print("\n===== BASIC INFO =====")
print(df.info())

print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe(include="all"))

print("\n===== NULL VALUES =====")
print(df.isnull().sum())

# =============================
# 2. Histograms and Boxplots
# =============================
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    plt.figure(figsize=(12, 5))
    
    # Histogram
    plt.subplot(1, 2, 1)
    sns.histplot(df[col].dropna(), kde=True, bins=30)
    plt.title(f"Histogram of {col}")
    
    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    
    plt.tight_layout()
    plt.show()

# =============================
# 3. Pairplot / Correlation Matrix
# =============================
if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

    # Seaborn pairplot
    sns.pairplot(df[numeric_cols])
    plt.show()

# =============================
# 4. Identify Patterns & Trends (Plotly Interactive Example)
# =============================
if len(numeric_cols) >= 2:
    fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1], color=df[numeric_cols[0]])
    fig.update_layout(title=f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
    fig.show()

# =============================
# 5. Inferences
# =============================
print("\n===== FEATURE-LEVEL INFERENCES =====")
for col in numeric_cols:
    print(f"{col}: Mean={df[col].mean():.2f}, Median={df[col].median():.2f}, Std={df[col].std():.2f}")
