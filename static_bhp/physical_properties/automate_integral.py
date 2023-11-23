# import pandas as pd
# from conversions import evaluate_scrhs
# from pseudocritical_properties import natural_gas_systems2
from pseudoreduced_properties import pseudo_reduced_wellhead_pressure
# from error_message import err_msg


# df = pd.read_csv('../sukkarcornelintegral.csv')
# df2 = pd.read_csv('../sukkarcornellintegral2.csv')

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
    print(truncate_to_one_dp(target_pseudoreduced_pressure))
    
print_target_pseudoreduced_pressure()

# target_pseudoreduced_pressure = pseudo_reduced_wellhead_pressure()
# # print(target_pseudoreduced_pressure)
# print(truncate_to_one_dp(target_pseudoreduced_pressure))
# # target_pseudoreduced_pressure = round(pseudo_reduced_wellhead_pressure(), 1)
# # print(target_pseudoreduced_pressure)