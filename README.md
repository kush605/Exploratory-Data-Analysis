# 📊 Exploratory Data Analysis (EDA) on Crocodile Dataset

##  Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a comprehensive dataset of crocodile observations.  
The dataset contains information about various species of crocodiles, including their physical characteristics, geographic location, age, sex, habitat, and conservation status.  

The main goal of this project is to:
- Understand the dataset structure and characteristics  
- Identify patterns, correlations, and anomalies in the data  
- Generate visual insights using statistical plots and interactive charts  

---

## 🐊 Dataset Description
The dataset `crocodile_dataset.csv` includes the following features:

| Column Name | Description | Data Type | Example Values |
|-------------|-------------|-----------|----------------|
| Observation ID | Unique identifier for each observation | Integer | 1, 25, 102 |
| Common Name | Common name of the species observed | String | "Morelet's Crocodile", "American Alligator" |
| Scientific Name | Scientific/Latin name of the species | String | "Crocodylus moreletii", "Alligator mississippiensis" |
| Family | Biological family of the species | String | "Crocodylidae", "Alligatoridae" |
| Genus | Genus classification | String | "Crocodylus", "Alligator" |
| Observed Length (m) | Measured or estimated length in meters | Float | 1.9, 3.2, 5.1 |
| Observed Weight (kg) | Measured or estimated weight in kilograms | Float | 62, 250, 480 |
| Age Class | Age group classification | String (Categorical) | "Juvenile", "Subadult", "Adult" |
| Sex | Biological sex of the individual | String (Categorical) | "Male", "Female", "Unknown" |
| Date of Observation | Date of observation | Date (DD-MM-YYYY) | "31-03-2018", "12-07-2020" |
| Country/Region | Geographic location of observation | String | "Belize", "Florida, USA", "Australia" |
| Habitat Type | Type of ecosystem/environment | String | "Swamps", "Rivers", "Mangroves", "Lakes" |
| Conservation Status | IUCN Red List status | String (Categorical) | "Least Concern", "Vulnerable", "Endangered" |
| Observer Name | Name of the observer/researcher | String | "Allison Hill", "Dr. James Carter" |
| Notes | Additional comments or field notes | Text | "Observed basking near riverbank." |

---

## 🛠️ Tools & Libraries
- **Python** – Programming language  
- **Pandas** – Data handling, cleaning, and descriptive statistics  
- **Matplotlib** – Basic data visualizations  
- **Seaborn** – Statistical plots and correlation analysis  
- **Plotly Express** – Interactive visualizations  

---

## 📝 Work Done
The EDA workflow includes:

1. **Data Overview**
   - Load the dataset and inspect basic information  
   - Check for missing values and data types  
   - Generate summary statistics (mean, median, std, etc.)  

2. **Visualizations**
   - **Histograms & Boxplots** for numeric features (length, weight)  
   - **Correlation Matrix** to find relationships between numeric features  
   - **Pairplots** to explore feature interactions  
   - **Interactive Scatter Plots (Plotly)** for trend analysis  

3. **Feature-Level Inferences**
   - Identify patterns in length, weight, and age classes  
   - Analyze distribution of species across countries, habitats, and conservation status  
   - Observe any anomalies or outliers  

---

## 📊 Key Insights
- Patterns in size and weight distribution across different species  
- Relationship between habitat type and conservation status  
- Geographic distribution of observed species  
- Insights into population trends and potential conservation focus areas  


