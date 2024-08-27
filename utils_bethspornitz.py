'''  ITERATION 3

Module: Synapse Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this third iteration, I declare additional variables to show skills with different data types.
 '''
 
 #####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Boolean variable to indicate if the company has Spanish speaking Analysts
has_spanish_speaking_analysts = True

# Boolean variable to indicate if the company has female analysts
has_female_analysts = True

# Integer variable for the number of employees
number_employees: int = 150

# List of cities where we serve Clients
locations:  list = ['Tampa', 'Kansas City', 'New York']

# List of floats representing the number of years experience of the top five analysts
years_of_experience: list = [30, 28, 22, 18, 15]


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
