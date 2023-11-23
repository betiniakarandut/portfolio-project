""""Module to compute pseudo reduced properties"""
from conversions import temp_avg_in_rankine
from pseudocritical_properties import natural_gas_systems, natural_gas_systems2

# COMPUTING PSEUDOREDUCED PROPERTIES
# gas_type = input('type in a gas system:Natural gas system or gas condensate system? ')
# if (gas_type == 'Natural gas system'):
def pseudo_reduced_temp():
    """Function to compute reduced temperature

    Return
        floats: reduced temperature rounded to one
        decimal place
    """
    tpr_pseudo_reduced_temp = float(temp_avg_in_rankine()) / natural_gas_systems()
    return round(tpr_pseudo_reduced_temp, 1)


static_wellhead_pressure = float(input('what is the value of the wellhead pressure in psia '))


def pseudo_reduced_wellhead_pressure():
    """Function to compute reduced pressure
    at wellhead pressure

    Return:
        floats: reduced pressure at wellhead rounded
        to three decimal places
    """
    ppr1_wellhead = static_wellhead_pressure / natural_gas_systems2()
    return round(ppr1_wellhead, 3)


input('using the values of Tpr and Ppr displayed below. Goto sukkarcornel integral'
      'table and read the value of the CELL. Type "ok" to see Tr and Pr values- ')

# print('')
# print('<-------------------------------------->')
# print(f"PSEUDOREDUCED TEMP(Tpr) = {pseudo_reduced_temp()}")
# print(f"PSEUDOREDUCED PRESSURE(Ppr) = {pseudo_reduced_wellhead_pressure()}")
# print('<-------------------------------------->')
# print('')
