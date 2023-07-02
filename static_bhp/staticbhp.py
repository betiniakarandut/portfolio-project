import pandas as pd
from ErrorMessage import err_msg
from PseudoreducedProperties import *


df = pd.read_csv('sukkarcornelintegral.csv')
df2 = pd.read_csv('sukkarcornellintegral2.csv')


# Block for calculating static BHP for REDUCED PRESSURE GREATER THAN 2.0 or PRESSURE ABOVE 2000

decision = input('IS REDUCED PRESSURE GREATER THAN 2.0 or PRESSURE ABOVE 2000 psia? TYPE "yes" or "no" TO CONTINUE => ')

if decision.upper() == "YES":

    print('<------------------------------------------------------------------------------------>')
    print('SUKKAR_CORNELL INTEGRAL TABLE FOR PRESSURES ABOVE 2000 psia or Ppr = 2.0 and ABOVE '
        'constant B = 0')
    print('<------------------------------------------------------------------------------------>')


    def table_integral_head():
        """Function to display sukkar and cornell
        table of integral-head


        Return:
            dataframe: for the first fifty one rows
        """

        return df.head(51)


    #     Stores table_integral_head in the variable t1
    t1 = table_integral_head()


    def table_integral_tail():
        """Function to display sukkar and cornell
        table of integral-tail


        Return:
            dataframe: for the last forty nine rows

        """

        return df.tail(49)


    #     Stores table_integral_tail in the variable t2
    t2 = table_integral_tail()

    print('TABLE 1')
    print('<--------------------------------------------------------------------------------------------------->')
    print(t1)
    print('<--------------------------------------------------------------------------------------------------->')
    print('CONTINUE FROM TABLE 1')
    print('<--------------------------------------------------------------------------------------------------->')
    print(t2)
    print('<--------------------------------------------------------------------------------------------------->')

    #     First interpolation to compute the sukkar and cornell integral value

    ppr_above = float(input("what is the value of CELL ABOVE 'Ppr'? "))
    ppr_below = float(input("what is the value of CELL BELOW 'Ppr'? "))
    sciv_above = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL ABOVE Ppr'? "))
    sciv_below = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL BELOW Ppr'? "))

    a = ppr_above - pseudo_reduced_wellhead_pressure()
    a2 = ppr_above - ppr_below
    b = sciv_above - sciv_below


    def interpolated_integral_value():
        """Function to interpolate sukkar and cornell
        integral value


        Return:
            i_integral_value(floats): interpolated integral value

        """

        i_integral_value = sciv_above - ((a / a2) * b)

        return i_integral_value


    def real_integral_value():
        """Function to calculate real integral value


        Return:
            real_value(floats): Difference btw interpolated value and
            the sukkar and cornell integral-RHS

        """

        real_value = interpolated_integral_value() - evaluate_scrhs()
        return real_value


    print('')
    print('<-------------------------------------------------------->')
    print(f"sukkar and cornel integral value is:{real_integral_value()}")
    print('<-------------------------------------------------------->')
    print('')

    #     Second interpolation to compute reduced pressure at real integral value

    upper_value_integral = float(input('what is the integral value of CELL ABOVE '
                                    '"sukkar and cornel integral value"? '))
    lower_value_integral = float(input('what is the integral value of CELL BELOW '
                                    '"sukkar and cornel integral value"? '))
    ppr_of_upper_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of '
            'CELL ABOVE "sukkar and cornel integral value"? '))
    ppr_of_lower_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of '
            'CELL BELOW "sukkar and cornel integral value"? '))

    i = upper_value_integral - real_integral_value()

    i2 = upper_value_integral - lower_value_integral

    pr = ppr_of_upper_value_integral - ppr_of_lower_value_integral


    def pseudo_reduced_bhp():
        """Function to compute reduced
        bottom hole pressure


        Return:
            floats: pseudo_reduced BHP rounded to
            three decimal places

        """

        reduced_bhp = ppr_of_upper_value_integral - (i / i2) * pr

        return round(reduced_bhp, 3)


    def static_bhp():
        """Function to compute the
        Static Bottom Hole Pressure


        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """

        pws = pseudo_reduced_bhp() * natural_gas_systems2()

        return f"The static_bhp is:{round(pws, 3)} psia"


    print('')
    print('<-------------------------------------->')
    print(static_bhp())

# Block for calculating static BHP for REDUCED PRESSURES FROM 1.0 to 5.0 or PRESSURES FROM 600 psia to 3200

elif decision.upper() == "NO":
    print('<-------------------------------------------------------------------------------------------------------->')
    print('SUKKAR_CORNELL_INTEGRAL TABLE FOR REDUCED PRESSURES FROM 1.0 to 5.0 or PRESSURES FROM 600 psia to 3200 '
        'constant B = 0')
    print('<-------------------------------------------------------------------------------------------------------->')


    def table_integral_head():
        """Function to display sukkar and cornell
        table of integral-head


        Return:
            dataframe: for the first forty five rows

        """

        return df2.head(45)


    #     Stores table_integral_head in the variable t1
    t1 = table_integral_head()

    print(t1)
    print('<------------------------------------------------------------------------------------------------------>')

    #     First interpolation to compute the sukkar and cornell integral value

    ppr_above = float(input("what is the value of CELL ABOVE 'Ppr'? "))
    ppr_below = float(input("what is the value of CELL BELOW 'Ppr'? "))
    sciv_above = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL ABOVE Ppr'? "))
    sciv_below = float(input("what is the sukkarcornel integral value corresponding to 'value of CELL BELOW Ppr'? "))

    a = ppr_above - pseudo_reduced_wellhead_pressure()
    a2 = ppr_above - ppr_below
    b = sciv_above - sciv_below


    def interpolated_integral_value():
        """Function to interpolate sukkar and cornell
        integral value


        Return:
        i_integral_value(floats): interpolated integral value

        """

        i_integral_value = sciv_above - ((a / a2) * b)

        return i_integral_value


    def real_integral_value():
        """Function to calculate real integral value


        Return:
            real_value(floats): Difference btw interpolated value and
            the sukkar and cornell integral-RHS

        """

        real_value = interpolated_integral_value() - evaluate_scrhs()

        return real_value


    print('')
    print('<-------------------------------------------------------->')
    print(f"sukkarcornel integral value is:{real_integral_value()}")
    print('<-------------------------------------------------------->')
    print('')

    #     Second interpolation to compute reduced pressure at real integral value
    upper_value_integral = float(input('what is the integral value of CELL ABOVE "sukkarcornel integral value"? '))
    lower_value_integral = float(input('what is the integral value of CELL BELOW "sukkarcornel integral value"? '))
    ppr_of_upper_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of CELL ABOVE "sukkarcornel integral value"? '))
    ppr_of_lower_value_integral = float(
        input('what is the value of Ppr corresponding to integral value of CELL BELOW "sukkarcornel integral value"? '))

    i = upper_value_integral - real_integral_value()

    i2 = upper_value_integral - lower_value_integral

    pr = ppr_of_upper_value_integral - ppr_of_lower_value_integral


    def pseudo_reduced_bhp():
        """Function to compute reduced
        bottom hole pressure


        Return:
            floats: pseudo-reduced BHP rounded to
            three decimal places

        """

        reduced_bhp = ppr_of_upper_value_integral - (i / i2) * pr

        return round(reduced_bhp, 3)


    def static_bhp():
        """Function to compute the
        Static Bottom Hole Pressure


        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """

        pws = pseudo_reduced_bhp() * natural_gas_systems2()

        return f"The static_BHP is:{round(pws, 3)} psia"


    print('')
    print('<-------------------------------------->')
    print(static_bhp())

else:
    err_msg()


class Static_BHP:
    
    def static(self):
        return static_bhp
