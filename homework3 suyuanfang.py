# PPHA 30537
# Spring 2024
# Homework 3

# YOUR NAME HERE Suyuan Fang

# YOUR CANVAS NAME HERE Suyuan Fang
# YOUR GITHUB USER NAME HERE suyuan-fang

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.

# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

plt.scatter(x, y1, color='blue', label='y1')
plt.plot(x, y2, color='red', label='y2')
plt.title('HW3 Q1.1')
plt.xlabel('Date')
plt.ylabel('Values')

plt.legend()
plt.show()
# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.
x = range(10, 19)
y_blue = range(10, 19)  
y_red = range(18, 9, -1)  

plt.plot(x, y_blue, label='Blue', color='blue')  
plt.plot(x, y_red, label='Red', color='red')  
plt.title('X marks the spot')
plt.legend()
plt.show()

# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.
df = pd.read_csv('/Users/suyuanfang/Downloads/mpg.csv')
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

axes[0].scatter(df['displacement'], df['mpg'])
axes[0].set_title('MPG vs. Displacement')
axes[0].set_xlabel('Displacement')
axes[0].set_ylabel('Miles Per Gallon')

axes[1].scatter(df['horsepower'], df['mpg'])
axes[1].set_title('MPG vs. Horsepower')
axes[1].set_xlabel('Horsepower')
axes[1].set_ylabel('Miles Per Gallon')

axes[2].scatter(df['weight'], df['mpg'])
axes[2].set_title('MPG vs. Weight')
axes[2].set_xlabel('Weight')
axes[2].set_ylabel('Miles Per Gallon')

plt.tight_layout()
plt.show()

# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.
plt.scatter(df['cylinders'], df['mpg'])
plt.title('MPG vs. Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Miles Per Gallon')
plt.show()
### The scatter plot is not ideal for categorical data like 'cylinders' as it does not distinctly separate the groups, making it hard to discern patterns or distributions.

sns.boxplot(x='cylinders', y='mpg', data=df)
plt.title('MPG by Number of Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Miles Per Gallon')
plt.show()

# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

ax[0, 0].scatter(df['displacement'], df['mpg'])
ax[0, 0].set_xlabel('Displacement (cu inches)')

ax[0, 1].scatter(df['horsepower'], df['mpg'])
ax[0, 1].set_xlabel('Horsepower')
ax[0, 1].set_yticklabels([])  

ax[1, 0].scatter(df['weight'], df['mpg'])
ax[1, 0].set_xlabel('Weight (lbs)')

ax[1, 1].scatter(df['acceleration'], df['mpg'])
ax[1, 1].set_xlabel('Acceleration')
ax[1, 1].set_yticklabels([])  

fig.suptitle('Changes in MPG')
fig.supylabel('mpg')  

plt.tight_layout(rect=[0, 0, 1, 0.95])  

plt.savefig('/Users/suyuanfang/Documents/GitHub/datasci-harris-suyuan-fang/q1_5_plot.png')
plt.show()

# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.
average_mpg = df.groupby('origin')['mpg'].mean()

average_mpg.plot(kind='bar', color='skyblue')
plt.title('Average MPG by Car Origin')
plt.xlabel('Origin')
plt.ylabel('Average MPG')
plt.xticks(rotation=0)  
plt.show()
print(average_mpg)
#europe27.891429 japan30.450633 usa20.083534, Carsfrom the USA are the least fuel efficient, on average.

# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.
sns.scatterplot(data=df, x='displacement', y='mpg', hue='origin', palette='deep', s=60)
plt.title('MPG vs. Displacement by Country of Origin')
plt.xlabel('Displacement (cu inches)')
plt.ylabel('Miles Per Gallon')
plt.legend(title='Origin')
plt.show()
#The scatter plot illustrates that cars from the USA typically have larger engine displacements and lower mpg compared to cars from Japan and Europe, reinforcing the result from question 1.6 that American cars are the least fuel efficient on average.

# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).
#    2.1: Merge both dataframes together
# Load the unemployment data from CSV
import pandas as pd
import us

unemp_df = pd.read_csv('/Users/suyuanfang/Downloads/unemp.csv')
policy_df = pd.read_excel('/Users/suyuanfang/Downloads/policy_uncertainty.xlsx')
print("Unemployment Data Columns:", unemp_df.columns)
print("Policy Uncertainty Data Columns:", policy_df.columns)

unemp_df['DATE'] = pd.to_datetime(unemp_df['DATE'])
policy_df['DATE'] = pd.to_datetime(policy_df.assign(day=1)[['year', 'month', 'day']])
unemp_df.rename(columns={'STATE': 'state'}, inplace=True)
policy_df['state'] = policy_df['state'].apply(lambda x: us.states.lookup(x).abbr if us.states.lookup(x) else x)

print("Unemployment Data:")
print(unemp_df[['DATE', 'state', 'unemp_rate']].head())
print("Policy Uncertainty Data:")
print(policy_df[['DATE', 'state', 'EPU_Composite']].head())

merged_df = pd.merge(unemp_df, policy_df, on=['DATE', 'state'], how='inner')
print(merged_df.head())

#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
merged_df.sort_values(by=['state', 'DATE'], inplace=True)
print(merged_df[merged_df['EPU_Composite'] <= 0][['DATE', 'state', 'EPU_Composite']])
merged_df['EPU_Composite'] = merged_df['EPU_Composite'].apply(lambda x: x if x > 0 else 0.01)
merged_df['log_EPU_Composite'] = np.log(merged_df['EPU_Composite'])
merged_df['LFD_EPU_Composite'] = merged_df.groupby('state')['log_EPU_Composite'].diff()
print(merged_df[['DATE', 'state', 'EPU_Composite', 'log_EPU_Composite', 'LFD_EPU_Composite']].head())

#    2.3: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.
# Example: Check if there are any NaN values in the key columns
states = ['AL', 'AK', 'CA', 'NY', 'TX']
fig, axs = plt.subplots(len(states), 1, figsize=(10, 20), sharex=True)

for i, state in enumerate(states):
    state_data = merged_df[merged_df['state'] == state]
    
    ax = axs[i]
    ax.plot(state_data['DATE'], state_data['unemp_rate'], color='blue', label='Unemployment Rate')
    ax.set_title(state)
    ax.set_ylabel('Unemployment Rate (%)')
    ax.legend(loc='upper left')
    
    ax2 = ax.twinx()
    ax2.plot(state_data['DATE'], state_data['LFD_EPU_Composite'], color='red', label='LFD EPU-C')
    ax2.set_ylabel('LFD of EPU-C')
    ax2.legend(loc='upper right')

fig.suptitle('Unemployment Rate and LFD of EPU-C over Time by State')
fig.tight_layout(rect=[0, 0, 1, 0.95])  
plt.show()

#    2.4: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.
import statsmodels.api as sm
import statsmodels.formula.api as smf
analysis_df = merged_df.dropna(subset=['LFD_EPU_Composite'])
formula = 'unemp_rate ~ LFD_EPU_Composite + C(state)'
model = smf.ols(formula, data=analysis_df).fit()


#    2.5: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.
print(model.summary())
#                           OLS Regression Results                            
#==============================================================================
#Dep. Variable:             unemp_rate   R-squared:                       0.171
#Model:                            OLS   Adj. R-squared:                  0.147
#Method:                 Least Squares   F-statistic:                     7.010
#Date:                Sun, 05 May 2024   Prob (F-statistic):           1.32e-41
#Time:                        17:22:30   Log-Likelihood:                -4226.6
#No. Observations:                1750   AIC:                             8555.
#Df Residuals:                    1699   BIC:                             8834.
#Df Model:                          50                                         
#Covariance Type:            nonrobust                                         
#==============================================================================
###R-squared: 0.171 - This value indicates that approximately 17.1% of the variability in the unemployment rate is explained by the model. While not very high, it's not uncommon for economic data where many other unmodeled factors could affect the outcome.
###Adjusted R-squared: 0.147 - Adjusted for the number of predictors in the model, this value is slightly lower, indicating that some of the predictors might not be significantly contributing to the explanation of the variance in the unemployment rate.
###F-statistic and its Prob: The F-statistic is 7.010 with a very small p-value (1.32e-41), suggesting that the model is statistically significant, meaning that the LFD of EPU-C and/or the state fixed effects do have a statistically significant effect on the unemployment rate.
###AIC and BIC: These are measures of the model fit that penalize for the number of predictors. The values are relatively high, suggesting that while the model is informative, there might be room for simplification or adjustment.
