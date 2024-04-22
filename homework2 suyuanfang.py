# PPHA 30537
# Spring 2024
# Homework 2

# YOUR NAME HERE Suyuan Fang
# YOUR GITHUB USER NAME HERE suyuan-fang

# Due date: Sunday April 21st before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the csv document included in
# your repo.  In nst-est2022-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, and other values represent smaller geographies. 
# REGION is the fips code for the US region. STATE is the fips code for the 
# US state.  The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2022/NST-EST2022-ALLDATA.pdf
# Note that each question will build on the modified dataframe from the
# question before.  Make sure the SettingWithCopyWarning is not raised.

# PART 1: Macro Data Exploration

# Question 1.1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.
import pandas as pd

file_path = '/Users/suyuanfang/Desktop/NST-EST2022-ALLDATA.csv'
data = pd.read_csv(file_path)
print(data.head())

# Question 1.2: Your data only includes fips codes for states (STATE).  Use 
# the us library to crosswalk fips codes to state abbreviations.  Drop the
# fips codes.
fips_to_state = {
    '01': 'AL', '02': 'AK', '04': 'AZ', '05': 'AR', '06': 'CA', 
    '08': 'CO', '09': 'CT', '10': 'DE', '11': 'DC', '12': 'FL', 
    '13': 'GA', '15': 'HI', '16': 'ID', '17': 'IL', '18': 'IN', 
    '19': 'IA', '20': 'KS', '21': 'KY', '22': 'LA', '23': 'ME', 
    '24': 'MD', '25': 'MA', '26': 'MI', '27': 'MN', '28': 'MS', 
    '29': 'MO', '30': 'MT', '31': 'NE', '32': 'NV', '33': 'NH', 
    '34': 'NJ', '35': 'NM', '36': 'NY', '37': 'NC', '38': 'ND', 
    '39': 'OH', '40': 'OK', '41': 'OR', '42': 'PA', '44': 'RI', 
    '45': 'SC', '46': 'SD', '47': 'TN', '48': 'TX', '49': 'UT', 
    '50': 'VT', '51': 'VA', '53': 'WA', '54': 'WV', '55': 'WI', 
    '56': 'WY'
}

def fips_to_abbreviation(fips_code):
    fips_code_str = str(fips_code).zfill(2)
    return fips_to_state.get(fips_code_str)

data['State_Abbreviation'] = data['STATE'].apply(fips_to_abbreviation)
data.drop('STATE', axis=1, inplace=True)
print(data.head())

# Question 1.3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.  Do not 
# create plots or use groupby; we will do that in future homeworks.  
# Show the relevant exploration output with print() statements.
# Display the shape of the DataFrame
print("Shape of the Data:", data.shape)

print("\nColumn Headers:", data.columns.tolist())

print("\nData Types:")
print(data.dtypes)

print("\nDescriptive Statistics:")
print(data.describe())

print("\nMissing Values in Each Column:")
print(data.isnull().sum())

print("\nNumber of Unique Values in Key Columns:")
print(data.nunique())

print("\nFirst Few Rows:")
print(data.head())

# Question 1.4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.
state_data = data[data['SUMLEV'] == 40]
columns_to_keep = ['State_Abbreviation', 'POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022']
state_population_data = state_data[columns_to_keep]
print(state_population_data.head())
print("Shape of the Subset:", state_population_data.shape)

# Question 1.5: Show only the 10 largest states by 2021 population estimates,
# in decending order.
largest_states_2021 = state_population_data.sort_values('POPESTIMATE2021', ascending=False)
top_10_largest_states = largest_states_2021.head(10)
print("10 Largest States by 2021 Population Estimates:")
print(top_10_largest_states)

# Question 1.6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?
state_population_data['POPCHANGE'] = state_population_data['POPESTIMATE2022'] - state_population_data['POPESTIMATE2020']
states_gained_population = (state_population_data['POPCHANGE'] > 0).sum()
states_lost_population = (state_population_data['POPCHANGE'] < 0).sum()
print(f"Number of states that gained population: {states_gained_population}")
print(f"Number of states that lost population: {states_lost_population}")

# Question 1.7: Show all the states that had an estimated change in either
# direction of smaller than 1000 people. 
small_popchange_states = state_population_data[abs(state_population_data['POPCHANGE']) < 1000]
print("States with Estimated Population Change Smaller than 1000 People:")
print(small_popchange_states[['State_Abbreviation', 'POPCHANGE']])

# Question 1.8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.
std_dev_pop_change = state_population_data['POPCHANGE'].std()
significant_popchange_states = state_population_data[
    abs(state_population_data['POPCHANGE']) > std_dev_pop_change
]
significant_popchange_states = significant_popchange_states.sort_values(
    by='POPCHANGE', 
    key=abs,  
    ascending=False
)

print("States with Population Growth or Loss Greater Than One Standard Deviation:")
print(significant_popchange_states[['State_Abbreviation', 'POPCHANGE']])

#PART 2: Data manipulation

# Question 2.1: Reshape the data from wide to long, using the wide_to_long function,
# making sure you reset the index to the default values if any of your data is located 
# in the index.  What happened to the POPCHANGE column, and why should it be dropped?
# Explain in a brief (1-2 line) comment.
data.reset_index(drop=True, inplace=True)
data['index'] = range(len(data))
if 'POPCHANGE' in data.columns:
    data.drop('POPCHANGE', axis=1, inplace=True)
df_long1 = pd.wide_to_long(data, stubnames='POPESTIMATE', i='index', j='Year', sep='')
print(df_long1)

# Question 2.2: Repeat the reshaping using the melt method.  Clean up the result so
# that it is the same as the result from 2.1 (without the POPCHANGE column).
df_reset = data.reset_index()
df_reset['index'] = range(len(df_reset))
df_reset.set_index('index', inplace=True)

id_vars = [col for col in df_reset.columns if col not in ['POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022']]
df_long2 = pd.melt(df_reset, id_vars=id_vars, value_vars=['POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022'], var_name='Year', value_name='Population')
df_long2['Year'] = df_long2['Year'].str.extract('(\d+)').astype(int)
print(df_long2)

# Question 2.3: Open the state-visits.xlsx file in Excel, and fill in the VISITED
# column with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the xlsx file as a dataframe in
# Python, and merge the VISITED column into your original wide-form population 
# dataframe, only keeping values that appear in both dataframes.  Are any 
# observations dropped from this?  Show code where you investigate your merge, 
# and display any observations that weren't in both dataframes.

df_visits = pd.read_excel('/Users/suyuanfang/Desktop/state-visits.xlsx')
data['STATE'] = data['STATE'].astype(str)
df_visits['STATE'] = df_visits['STATE'].astype(str)
df_merged = data.merge(df_visits[['STATE', 'VISITED']], on='STATE', how='outer', indicator=True)
print(df_merged.head())


# Question 2.4: The file policy_uncertainty.xlsx contains monthly measures of 
# economic policy uncertainty for each state, beginning in different years for
# each state but ending in 2022 for all states.  The EPU_National column esimates
# uncertainty from national sources, EPU_State from state, and EPU_Composite 
# from both (EPU-N, EPU-S, EPU-C).  Load it as a dataframe, then calculate 
# the mean EPU-C value for each state/year, leaving only columns for state, 
# year, and EPU_Composite, with each row being a unique state-year combination.
df_pol=pd.read_excel('/Users/suyuanfang/Desktop/policy_uncertainty.xlsx')
df_pol.head()
df_new=df_pol.groupby(['state','year'])['EPU_Composite'].mean().reset_index()
df_fin=df_new[['state','year','EPU_Composite']]
print(df_fin)

# Question 2.5) Reshape the EPU data into wide format so that each row is unique 
# by state, and the columns represent the EPU-C values for the years 2022, 
# 2021, and 2020. 
filtered_data = df_fin[df_fin['year'].isin([2020, 2021, 2022])]
wide_format = filtered_data.pivot(index='state', columns='year', values='EPU_Composite')
wide_format.columns = [f'EPU_C_{year}' for year in wide_format.columns]
wide_format.reset_index(inplace=True)
print(wide_format.head())

# Question 2.6) Finally, merge this data into your merged data from question 2.3, 
# making sure the merge does what you expect.
df_merged.set_index('state', inplace=True)
wide_format.reset_index(inplace=True)
df_merged_final=df_merged.merge(wide_format,on='state',how='outer')
print(df_merged_final)

# Question 2.7: Using groupby on the VISITED column in the dataframe resulting 
# from the previous question, answer the following questions and show how you  
# calculated them: a) what is the single smallest state by 2022 population  
# that you have visited, and not visited?  b) what are the three largest states  
# by 2022 population you have visited, and the three largest states by 2022 
# population you have not visited? c) do states you have visited or states you  
# have not visited have a higher average EPU-C value in 2022?
# Filter and find the smallest state by 2022 population for visited and not visited
smallest_visited = df_merged_final[df_merged_final['VISITED'] == 1].nsmallest(1, 'POPESTIMATE2022')
smallest_not_visited = df_merged_final[df_merged_final['VISITED'] == 0].nsmallest(1, 'POPESTIMATE2022')
largest_visited = df_merged_final[df_merged_final['VISITED'] == 1].nlargest(3, 'POPESTIMATE2022')
largest_not_visited = df_merged_final[df_merged_final['VISITED'] == 0].nlargest(3, 'POPESTIMATE2022')
average_epu_c_visited = df_merged_final[df_merged_final['VISITED'] == 1]['EPU_C_2022'].mean()
average_epu_c_not_visited = df_merged_final[df_merged_final['VISITED'] == 0]['EPU_C_2022'].mean()


# Question 2.8: Transforming data to have mean zero and unit standard deviation
# is often called "standardization", or a "zscore".  The basic formula to 
# apply to any given value is: (value - mean) / std
# Return to the long-form EPU data you created in step 2.4 and then, using groupby
# and a function you write, transform the data so that the values for EPU-C
# have mean zero and unit standard deviation for each state.  Add these values
# to a new column named EPU_C_zscore.
def zscore(x):
    return (x - x.mean()) / x.std()
df_fin['EPU_C_zscore'] = df_fin.groupby('state')['EPU_Composite'].transform(zscore)
print(df_fin.head())


