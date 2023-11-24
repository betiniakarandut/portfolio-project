import pandas as pd
# from conversions import evaluate_scrhs
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


def value_of_cell_below_ppr():
    cell_below_ppr = locate_cell_with_ppr() + 1
    return df['pseudoreduced_pressures'][cell_below_ppr]


def interpolated_ppr():
    value_1 = value_of_cell_above_ppr() - pseudo_reduced_wellhead_pressure()
    value_2 = value_of_cell_above_ppr() - value_of_cell_below_ppr()
    return value_1 / value_2

# locate sukkar cornell integral in the csv file
def sciv_for_cell_above_ppr():
    target_ppr_index = locate_cell_with_ppr() - 1
    target_tpr_index = 2
    target_value = df.iloc[target_ppr_index, target_tpr_index]
    return target_value


def sciv_for_cell_below_ppr():
    target_ppr_index = locate_cell_with_ppr() + 1
    target_tpr_index = 2
    target_value = df.iloc[target_ppr_index, target_tpr_index]
    return target_value
print(sciv_for_cell_below_ppr())

def sciv_for_ppr_cell():
    target_ppr_index = locate_cell_with_ppr()
    target_tpr_index = 2
    target_value = df.iloc[target_ppr_index, target_tpr_index]
    return target_value

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