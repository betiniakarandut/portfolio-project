"""Module for conversion.py"""

well_depth = float(input('What is the well depth? '))

# Temperature Conversion From Fahrenheit To Rankine

temp_avg_sys = float(input('what is the average temp in fahrenheit? '))


def temp_avg_in_rankine():
    """Function to calculate temperature in degrees rankine

    Return:
        floats: Temperature in degrees rankine

    """
    value = f"{460 + temp_avg_sys}"
    return value


# Evaluating sukkar and cornell integral right hand side(scrhs)

gas_specific_gravity = float(input('what is the gas specific gravity? '))


def evaluate_scrhs():
    """Function to evaluate the sukkar and cornell
    integral right hand side


    Return:
        floats: sukkar and cornell integral-RHS
    """
    scrhs = (0.01875 * float(gas_specific_gravity * well_depth)) / float(temp_avg_in_rankine())
    return round(scrhs, 4)