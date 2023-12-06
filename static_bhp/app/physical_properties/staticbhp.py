from .pseudocritical_properties import natural_gas_systems2
from .pseudoreduced_properties import pseudo_reduced_wellhead_pressure
from .automate_integral_df import pseudo_reduced_bhp
from .automate_integral_df2 import pseudo_reduced_bhp2
# from error_message import err_msg


class staticBHP:

    def staticbhp_for_ppr_gt_2(self):
        """Function to compute the
        Static Bottom Hole Pressure

        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """

        pws = pseudo_reduced_bhp() * natural_gas_systems2()
        return f"The static BHP is: {round(pws, 3)} psia"
    
    def staticbhp_for_ppr_lt_2(self):
        """Function to compute the
        Static Bottom Hole Pressure

        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """

        pws = pseudo_reduced_bhp2() * natural_gas_systems2()
        return f"The static BHP is: {round(pws, 3)} psia"

    def print_staticbhp(self):

        try:
            if pseudo_reduced_wellhead_pressure() >= 2.0:
                return self.staticbhp_for_ppr_gt_2()
            elif pseudo_reduced_wellhead_pressure() < 2.0:
                return self.staticbhp_for_ppr_lt_2()
        except Exception as e:
            print(f'Error: No index found. {e}')


# sbhp = staticBHP()
# print('')
# print(sbhp.print_staticbhp())
# print('<-------------------------------------->')
