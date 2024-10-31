'''

####################################################### Data Analysis #######################################################

I made an analysis of the maximum and minimum life expectancy in a country, as well as the average life expectancy. 
Also, I included a menu that allows users to choose between performing the analysis by year or by country.

'''

import textwrap
with open('life-expectancy.csv') as database:

    #functions to get the max and min life expectation

    def max_life_expectation(life_expectation, country, year, max_value, max_country, max_year):
        if life_expectation > max_value:
            max_value = life_expectation
            max_year = year
            max_country = country
        return max_country, max_year, max_value

    def min_life_expectation(life_expectation, country, year, min_value, min_country, min_year):
        if life_expectation < min_value:
            min_value = life_expectation
            min_year = year
            min_country = country
        return min_country, min_year, min_value 


    analysis_input = 'yes'

    while analysis_input.lower() == 'yes':
        menu = """
        What type of analysis do you want?
        1. By year
        2. By Country
        """

        menu = textwrap.dedent(menu)

        print(menu)
        menu_input = int(input())

        # Initialize variables for the current analysis
        life_expectation_max = -1
        life_expectation_max_year = 0
        life_expectation_max_country = ''
        
        life_expectation_min = 100
        life_expectation_min_year = 0
        life_expectation_min_country = ''
        
        overall_life_expectation_max = -1
        overall_life_expectation_max_year = 0
        overall_life_expectation_max_country = ''
        
        overall_life_expectation_min = 100
        overall_life_expectation_min_year = 0
        overall_life_expectation_min_country = ''
        
        average_sum = 0
        lines = 0

        if menu_input == 1:  # By year
            year_input = input('Enter the year of interest: ')
            database.seek(0)
            next(database)  # Skip header
            
            for line in database:
                line = line.strip().split(',')
                life_expectation = float(line[3])
                life_expectation_year = line[2]
                life_expectation_country = line[0]  

                overall_life_expectation_min_country, overall_life_expectation_min_year, overall_life_expectation_min = min_life_expectation(
                    life_expectation, life_expectation_country, life_expectation_year, overall_life_expectation_min, overall_life_expectation_min_country, overall_life_expectation_min_year
                )
                overall_life_expectation_max_country, overall_life_expectation_max_year, overall_life_expectation_max = max_life_expectation(
                    life_expectation, life_expectation_country, life_expectation_year, overall_life_expectation_max, overall_life_expectation_max_country, overall_life_expectation_max_year
                )            

                if life_expectation_year == year_input:
                    life_expectation_min_country, life_expectation_min_year, life_expectation_min = min_life_expectation(
                        life_expectation, life_expectation_country, life_expectation_year, life_expectation_min, life_expectation_min_country, life_expectation_min_year
                    )
                    life_expectation_max_country, life_expectation_max_year, life_expectation_max = max_life_expectation(
                        life_expectation, life_expectation_country, life_expectation_year, life_expectation_max, life_expectation_max_country, life_expectation_max_year
                    )
                        
                    average_sum += life_expectation
                    lines += 1
            
            # Calculate average only if lines > 0
            average = average_sum / lines if lines > 0 else 0
            
            output = f"""
            The overall max life expectancy is: {overall_life_expectation_max:.2f} from {overall_life_expectation_max_country} in {overall_life_expectation_max_year}
            The overall min life expectancy is: {overall_life_expectation_min:.2f} from {overall_life_expectation_min_country} in {overall_life_expectation_min_year}
            
            For the year {year_input}:
            The average life expectancy across all countries was {average:.2f}
            The max life expectancy was in {life_expectation_max_country} with {life_expectation_max:.2f}
            The min life expectancy was in {life_expectation_min_country} with {life_expectation_min:.2f}
            """
            output = textwrap.dedent(output)
            
            print(output)

        elif menu_input == 2:  # By country
            country_input = input('Enter the country of interest: ').lower()
            database.seek(0)
            next(database)  # Skip header
            
            for line in database:
                line = line.strip().split(',')
                life_expectation = float(line[3])
                life_expectation_year = line[2]
                life_expectation_country = line[0].lower()
           

                if life_expectation_country == country_input:
                    life_expectation_min_country, life_expectation_min_year, life_expectation_min = min_life_expectation(
                        life_expectation, life_expectation_country, life_expectation_year, life_expectation_min, life_expectation_min_country, life_expectation_min_year
                    )
                    life_expectation_max_country, life_expectation_max_year, life_expectation_max = max_life_expectation(
                        life_expectation, life_expectation_country, life_expectation_year, life_expectation_max, life_expectation_max_country, life_expectation_max_year
                    )
                    
                    average_sum += life_expectation
                    lines += 1

            # Calculate average only if lines > 0
            average = average_sum / lines if lines > 0 else 0
            
            output = f"""
           
            For the country {country_input.title()}:
            The average life expectancy was {average:.2f}
            The max life expectancy was in {life_expectation_max_year} with {life_expectation_max:.2f}
            The min life expectancy was in {life_expectation_min_year} with {life_expectation_min:.2f}
            """
            output = textwrap.dedent(output)

            print(output)

        analysis_input = input('Do you want to make another analysis? yes/no: ')

    if analysis_input.lower() == 'no':
        print('End...')
