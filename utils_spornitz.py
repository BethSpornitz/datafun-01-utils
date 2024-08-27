''' ITERATION 4

Module: Synapse Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.
'''
#####################################
# Import Modules at the Top
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - `statistics`: This gives us tools to calculate things like averages.
# Use CTRL F and type statistics to see where it is used in the code. 

import statistics

#####################################
# Declare global variables
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# Float variable for the average client satisfaction score
average_client_satisfaction: float = 4.7

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Boolean variable to indicate if the company has Spanish speaking Analysts
has_spanish_speaking_analysts = True

# Boolean variable to indicate if the company has female analyts
has_female_analysts = True

# Integer variable for the number of employees
number_employees: int = 150

# List of floats representing the number of years experience of the top five analysts
years_of_experience: list = [30, 28, 22, 18, 15]

# float variable for the average years of experience
average_years_of_experience: float = 22.6

# List of cities where we serve Clients
locations:  list = ['Tampa', 'Kansas City', 'New York']

#####################################
# Calculate Basic Statistics 
#   Do this BEFORE we declare the byline 
#   So the values have been calculated 
#   and are ready for use in the byline.
#####################################

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_years_experience: float = min(years_of_experience)  
max_years_experience: float = max(years_of_experience)  
mean_years_experience: float = statistics.mean(years_of_experience)  
stdev_years_experience: float = statistics.stdev(years_of_experience)

#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
Synapse Analytics: Deeper Insights. Clearer Decisions.
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Has Spanish Speaking Analysts:    {has_spanish_speaking_analysts}
Has Female Analysts:    {has_female_analysts}
Number of Employees:    {number_employees}
Locations Served:    {locations}
Years of Experience of our top five analysts:    {years_of_experience}
Minimum Client Satisfaction Score:    {min_score}
Maximum Client Satisfaction Score:   {max_score}
Average Client Satisfaction Score:    {mean_score}
Standard Deviation of Client Satisfaction Scores:    {stdev_score}
Minimum Years of Experience:    {min_years_experience} 
Maximum Years of Experience:    {max_years_experience}
Average Years of Experience:    {mean_years_experience} 
Standard Deviation of Years of Experience:    {stdev_years_experience}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
