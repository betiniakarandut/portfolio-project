import pandas as pd
import numpy as np
from conversions import evaluate_scrhs
# from pseudocritical_properties import natural_gas_systems2
from pseudoreduced_properties import pseudo_reduced_wellhead_pressure, pseudo_reduced_temp
# from error_message import err_msg


df = pd.read_csv('../sukkarcornelintegral.csv')
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
    target_pseudoreduced_pressure = pseudo_reduced_wellhead_pressure()
    return truncate_to_one_dp(target_pseudoreduced_pressure)

# print_target_pseudoreduced_pressure()
    
def locate_cell_with_ppr():
    target_ppr = print_target_pseudoreduced_pressure()
    # print(target_ppr)
    find_ppr = df["pseudoreduced_pressures"].searchsorted(target_ppr)
    
    # if find_ppr < 0 or find_ppr >= len(df):
    #     return None
    # found_ppr = df['pseudoreduced_pressures'][find_ppr]
    return find_ppr

print('')
print('<-------------------------------------->')
print(f"PSEUDOREDUCED TEMP(Tpr) = {pseudo_reduced_temp()}")
print(f"PSEUDOREDUCED PRESSURE(Ppr) = {pseudo_reduced_wellhead_pressure()}")
print('<-------------------------------------->')
print('')


# locate cell value above and below ppr

cell_below_ppr = locate_cell_with_ppr() + 1
# print(cell_below_ppr)

def value_of_cell_above_ppr():
    cell_above_ppr = locate_cell_with_ppr() - 1
    return df['pseudoreduced_pressures'][cell_above_ppr]
# print("Cell value above ppr: ", value_of_cell_above_ppr())


def value_of_cell_below_ppr():
    cell_below_ppr = locate_cell_with_ppr() + 1
    return df['pseudoreduced_pressures'][cell_below_ppr]
# print("This cell above ppr: ", value_of_cell_below_ppr())

def interpolated_ppr():
    value_1 = value_of_cell_above_ppr() - pseudo_reduced_wellhead_pressure()
    value_2 = value_of_cell_above_ppr() - value_of_cell_below_ppr()
    res = value_1 / value_2
    return res
# print("The cal ppr is: ", interpolated_ppr())

# locate sukkar cornell integral in the csv file
def sciv_for_cell_above_ppr():
    # future optimization
#     tpr_to_column = {
#     1.5: 1,
#     1.6: 2,
#     1.7: 3
# }

# target_tpr_index = tpr_to_column[pseudo_reduced_temp()]
# target_value = df.iloc[target_ppr_index, target_tpr_index]
    try:
        target_ppr_index = locate_cell_with_ppr() - 1
        if not 1.5 <= pseudo_reduced_temp() <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            if pseudo_reduced_temp() == 1.5:
                target_tpr_index = 1
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            elif pseudo_reduced_temp() == 1.6:
                target_tpr_index = 2
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            elif pseudo_reduced_temp() == 1.7:
                target_tpr_index = 3
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            return target_value
    except Exception as e:
        print(f"Error: {e}")
# print("sciv above ppr: ", sciv_for_cell_above_ppr())


def sciv_for_cell_below_ppr():
    try:
        target_ppr_index = locate_cell_with_ppr() + 1
        if not 1.5 <= pseudo_reduced_temp() <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            if pseudo_reduced_temp() == 1.5:
                target_tpr_index = 1
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            elif pseudo_reduced_temp() == 1.6:
                target_tpr_index = 2
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            elif pseudo_reduced_temp() == 1.7:
                target_tpr_index = 3
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            return target_value
    except Exception as e:
        print(f"Error: {e}")
# print("sciv below ppr: ", sciv_for_cell_below_ppr())

def sciv_for_ppr_cell():
    try:
        target_ppr_index = locate_cell_with_ppr()
        if not 1.5 <= pseudo_reduced_temp() <= 1.7:
            raise ValueError("Tpr range must be between 1.5 and 1.7")
        else:
            if pseudo_reduced_temp() == 1.5:
                target_tpr_index = 1
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            elif pseudo_reduced_temp() == 1.6:
                target_tpr_index = 2
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            elif pseudo_reduced_temp() == 1.7:
                target_tpr_index = 3
                target_value = df.iloc[target_ppr_index, target_tpr_index]
            return target_value
    except Exception as e:
        print(f"Error: {e}")

def compute_denominator_sciv():
    res = sciv_for_cell_above_ppr() - sciv_for_cell_below_ppr()
    return res
# print("diff btw sciv sbove and below: ", compute_denominator_sciv())

def compute_the_value_of_unknown_sciv():
    computed_sciv = sciv_for_cell_above_ppr() - (compute_denominator_sciv() * interpolated_ppr())
    return computed_sciv

# print("This is the sciv: ", compute_the_value_of_unknown_sciv())

def real_sciv():
    real_sciv = compute_the_value_of_unknown_sciv() - evaluate_scrhs()
    return real_sciv
# print("This is the sciv: ", compute_the_value_of_unknown_sciv())
# print("This is the value of evaluate_schrs(): ", evaluate_scrhs())
print('real sciv: ', real_sciv())

pseudoreduced_temps = df['pseudoreduced_temp1.5', 'pseudoreduced_temp1.6', 'pseudoreduced_temp1.7']
target_ppr = round(real_sciv(), 4)
for pseudoreduced_temp in pseudoreduced_temps:
    if target_ppr in pseudoreduced_temp.values:
        print(f"Target value {target_ppr} exists in the DataFrame")
        # Locate the cell using the index of the target value
        target_index = pseudoreduced_temp.searchsorted(target_ppr)
        cell_above_ppr = pseudoreduced_temp[target_index - 1]
        cell_below_ppr = pseudoreduced_temp[target_index + 1]
        print(f"Cell above: {cell_above_ppr}, Cell below: {cell_below_ppr}")
    else:
        upper_bound = pseudoreduced_temp.max()
        lower_bound = pseudoreduced_temp.min()

        if target_ppr > upper_bound:
            print(f"Target value {target_ppr} is greater than the maximum value in the DataFrame")
        elif target_ppr < lower_bound:
            print(f"Target value {target_ppr} is less than the minimum value in the DataFrame")
        else:
            lower_index = pseudoreduced_temp.searchsorted(target_ppr)

            difference = target_ppr - pseudoreduced_temp[lower_index]

            estimated_upper_value = pseudoreduced_temp[lower_index] + (difference * (pseudoreduced_pressures[lower_index + 1] - pseudoreduced_pressures[lower_index]))

            print(f"Estimated cell above: {estimated_upper_value}")
            print(f"Cell below: {pseudoreduced_temp[lower_index]}")


# # Extract the relevant columns
# pseudoreduced_pressures = df['pseudoreduced_pressures']
# sciv_values = df['sciv_values']

# # Find the index of the cell closest to the target sciv value
# closest_index = df['sciv_values'].searchsorted(target_sciv_value)

# # Extract the corresponding pseudoreduced pressure
# pivot_pressure = pseudoreduced_pressures[closest_index]

# # Locate the row and column indices for the pivot cell
# pivot_row_index = df.index[closest_index]
# pivot_column_index = df.columns.get_loc('sciv_values')

# # Locate the cell above and below the pivot cell in the pseudoreduced pressures column
# cell_above_ppr = pseudoreduced_pressures[pivot_row_index - 1]
# cell_below_ppr = pseudoreduced_pressures[pivot_row_index + 1]

# # Extract the corresponding sciv values for the cells above and below the pivot
# sciv_above = sciv_values[pivot_row_index - 1]
# sciv_below = sciv_values[pivot_row_index + 1]

# Print the results
# print(f"Target sciv value: {target_sciv_value}")
# print(f"Pivot pseudoreduced pressure: {pivot_pressure}")
# print(f"Cell above: {cell_above_ppr}")
# print(f"Cell below: {cell_below_ppr}")
# print(f"Sciv value above: {sciv_above}")
# print(f"Sciv value below: {sciv_below}")

# def locate_sciv_above_pivot():

    

# print(f"Found it to be equal with the ppr above: {locate_cell_with_ppr()}")
# isna_values = df['pseudoreduced_pressures'].isna()
# if any(isna_values):
#     print("The 'pseudoreduced_pressures' series contains None values.")
# else:
#     print('ppr found')
# print_target_pseudoreduced_pressure()

# target_pseudoreduced_pressure = pseudo_reduced_wellhead_pressure()
# # print(target_pseudoreduced_pressure)
# print(truncate_to_one_dp(target_pseudoreduced_pressure))
# # target_pseudoreduced_pressure = round(pseudo_reduced_wellhead_pressure(), 1)
# # print(target_pseudoreduced_pressure)