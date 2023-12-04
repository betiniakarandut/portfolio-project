"""
Module to automate sukkar and cornell integral
for pseudo reduced pressure less than 2 or 
wellhead pressure less than 2000 psia
"""
import pandas as pd
import numpy as np
from conversions import evaluate_scrhs
from pseudoreduced_properties import pseudo_reduced_wellhead_pressure, pseudo_reduced_temp

df2 = pd.read_csv('../sukkarcornellintegral2.csv')


def truncate_to_one_dp(digit_to_truncate):
    """Truncates a real number to 1 decimal place
    
    Args
        digit_to_truncate(real number)
    
    Returns
        the truncated number
    """
    number_string = str(digit_to_truncate)
    decimal_index = number_string.find(".")
    if decimal_index != -1:
        truncated_number_string = number_string[:decimal_index + 2]
        return float(truncated_number_string)
    else:
        return digit_to_truncate


def print_target_pseudoreduced_pressure():
    """Truncates pseudoreduced pressure to 1 dp

    Returns:
        target_pseudoreduced_pressure
    """
    target_pseudoreduced_pressure = pseudo_reduced_wellhead_pressure()
    return truncate_to_one_dp(target_pseudoreduced_pressure)

    
def locate_cell_with_ppr():
    """Locates the cell containing ppr in the csv file

    Returns:
        find_ppr
    """
    target_ppr = print_target_pseudoreduced_pressure()
    find_ppr = df2["pseudoreduced_pressures"].searchsorted(target_ppr)
    return find_ppr


# Displays the pseudoreduced temp and pressure
print('')
print('<-------------------------------------->')
print(f"PSEUDOREDUCED TEMP(Tpr) = {pseudo_reduced_temp()}")
print(f"PSEUDOREDUCED PRESSURE(Ppr) = {pseudo_reduced_wellhead_pressure()}")
print('<-------------------------------------->')
print('')

# locates the cell index below ppr
cell_below_ppr = locate_cell_with_ppr() + 1


def value_of_cell_above_ppr():
    """Locates the value of the cell above ppr in the csv file

    Returns:
        value of the cell
    """
    cell_above_ppr = locate_cell_with_ppr() - 1
    return df2['pseudoreduced_pressures'][cell_above_ppr]


def value_of_cell_below_ppr():
    """Locates the value of the cell below ppr in the csv file

    Returns:
        value of the cell
    """
    cell_below_ppr = locate_cell_with_ppr() + 1
    return df2['pseudoreduced_pressures'][cell_below_ppr]


def interpolated_ppr():
    """Computes the LHS of the linear interpolation

    Returns:
        res[float]
    """
    value_1 = value_of_cell_above_ppr() - pseudo_reduced_wellhead_pressure()
    value_2 = value_of_cell_above_ppr() - value_of_cell_below_ppr()
    res = value_1 / value_2
    return res


# locate sukkar cornell integral in the csv file
def sciv_for_cell_above_ppr():
    """Locates the sciv cell above corresponding to ppr in the csv file

    Returns:
        target value[float]
    """

    try:
        target_ppr_index = locate_cell_with_ppr() - 1
        # checks if the Tpr is in range
        if not 1.5 <= pseudo_reduced_temp() <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            # checks if Tpr is 1.5
            if pseudo_reduced_temp() == 1.5:
                target_tpr_index = 1
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            # checks if Tpr is 1.6
            elif pseudo_reduced_temp() == 1.6:
                target_tpr_index = 2
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            # checks if Tpr is 1.7
            elif pseudo_reduced_temp() == 1.7:
                target_tpr_index = 3
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            return target_value
    except Exception as e:
        print(f"Error: {e}")


def sciv_for_cell_below_ppr():
    """Locates the sciv cell below corresponding to ppr in the csv file

    Returns:
        target value[float]
    """

    try:
        target_ppr_index = locate_cell_with_ppr() + 1
        if not 1.5 <= pseudo_reduced_temp() <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            # checks if Tpr is 1.5
            if pseudo_reduced_temp() == 1.5:
                target_tpr_index = 1
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            # checks if Tpr is 1.6
            elif pseudo_reduced_temp() == 1.6:
                target_tpr_index = 2
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            # checks if Tpr is 1.7
            elif pseudo_reduced_temp() == 1.7:
                target_tpr_index = 3
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            return target_value
    except Exception as e:
        print(f"Error: {e}")


def sciv_for_ppr_cell():
    """Locates the sciv cell corresponding to ppr in the csv file

    Returns:
        target value[float]
    """

    try:
        target_ppr_index = locate_cell_with_ppr()
        if not 1.5 <= pseudo_reduced_temp() <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            # checks if Tpr is 1.5
            if pseudo_reduced_temp() == 1.5:
                target_tpr_index = 1
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            # checks if Tpr is 1.6
            elif pseudo_reduced_temp() == 1.6:
                target_tpr_index = 2
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            # checks if Tpr is 1.7
            elif pseudo_reduced_temp() == 1.7:
                target_tpr_index = 3
                target_value = df2.iloc[target_ppr_index, target_tpr_index]
            return target_value
    except Exception as e:
        print(f"Error: {e}")


def compute_denominator_sciv():
    """Computes denominator side for the second linear interpolation

    Returns:
        res[the result of the evaluation: float]
    """
    res = sciv_for_cell_above_ppr() - sciv_for_cell_below_ppr()
    return res


def compute_the_value_of_unknown_sciv():
    """
    Computes the unknown value of the sciv in the
    second linear interpolation

    Returns:
        computed_sciv[the result of the evaluation: float]
    """
    computed_sciv = sciv_for_cell_above_ppr() - (compute_denominator_sciv() * interpolated_ppr())
    return computed_sciv

print("This is the sciv: ", compute_the_value_of_unknown_sciv())

def pivot_sciv():
    """
    Determines the pivot sciv value

    Returns:
        pivot_sciv rounded to 4 dp[the result of the evaluation: float]
    """
    pivot_sciv = compute_the_value_of_unknown_sciv() - evaluate_scrhs()
    return round(pivot_sciv, 4)


print("This is the value of Sukkar&Cornell RHS: ", evaluate_scrhs())
print('real sciv: ', pivot_sciv())

# To locate the cell value closest to pivot sciv
if pseudo_reduced_temp() == 1.5:

    # checks for the column containing the Tpr
    abs_diffs = np.abs(df2['pseudoreduced_temp1.5'] - pivot_sciv())
    closest_index = abs_diffs.idxmin()
    closest_value = df2['pseudoreduced_temp1.5'][closest_index]

elif pseudo_reduced_temp() == 1.6:
    abs_diffs = np.abs(df2['pseudoreduced_temp1.6'] - pivot_sciv())
    closest_index = abs_diffs.idxmin()
    closest_value = df2['pseudoreduced_temp1.6'][closest_index]

elif pseudo_reduced_temp() == 1.7:
    abs_diffs = np.abs(df2['pseudoreduced_temp1.7'] - pivot_sciv())
    closest_index = abs_diffs.idxmin()
    closest_value = df2['pseudoreduced_temp1.7'][closest_index]
else:
    print('Index or required value is out of bound')

# Displays the closest value and index of the closest value in the csv
print(f'the closest value is {closest_value}')
print(f'the closest index is {closest_index}')
ppr = df2['pseudoreduced_pressures'][closest_index]
cell_value_1_level_below_ppr = df2['pseudoreduced_pressures'][closest_index - 1]
# print(f'this is ppr_1 {cell_value_1_level_below_ppr}')
print(f'ppr is: {ppr}')

# Dictionary to store Tpr and it associated column
tpr_to_column = {
    1.5: 1,
    1.6: 2,
    1.7: 3
}

# Gets the value of the intersect(the value of sciv above and below pivot sciv)
target_tpr_index = tpr_to_column[pseudo_reduced_temp()]
cell_value_above_pivot_sciv = df2.iloc[closest_index, target_tpr_index]
cell_value_below_pivot_sciv = df2.iloc[closest_index - 1, target_tpr_index]
# print(f'target_tpr_index is {target_tpr_index} and ppr_index is {closest_index} 
#       and sciv is {cell_value_above_pivot_sciv} & {cell_value_below_pivot_sciv}')


def pseudo_reduced_bhp():
    """Function to compute reduced
    bottom hole pressure

    Return:
        floats: pseudo-reduced BHP rounded to
        three decimal places
    """
    numerator = cell_value_above_pivot_sciv - pivot_sciv()
    denominator = cell_value_above_pivot_sciv - cell_value_below_pivot_sciv
    LHS = numerator / denominator
    RHS_denominator = ppr - cell_value_1_level_below_ppr
    reduced_bhp = ppr - (LHS * RHS_denominator)
    return round(reduced_bhp, 1)


print('<-------------------------------------->')
