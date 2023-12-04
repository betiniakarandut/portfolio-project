from pseudocritical_properties import natural_gas_systems2
from pseudoreduced_properties import pseudo_reduced_wellhead_pressure
# from error_message import err_msg


class staticBHP:

    def staticbhp_for_ppr_gt_2(self):
        """Function to compute the
        Static Bottom Hole Pressure

        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """
        import automate_integral_df

        pws = automate_integral_df.pseudo_reduced_bhp() * natural_gas_systems2()
        return f"The static BHP is: {round(pws, 3)} psia"
    
    def staticbhp_for_ppr_lt_2(self):
        """Function to compute the
        Static Bottom Hole Pressure

        Return:
            pws(floats): The static BHP rounded to 3
            decimal places

        """
        import automate_integral_df2

        pws = automate_integral_df2.pseudo_reduced_bhp() * natural_gas_systems2()
        return f"The static BHP is: {round(pws, 3)} psia"

    def print_staticbhp(self):

        if pseudo_reduced_wellhead_pressure() < 2.0:
            return self.staticbhp_for_ppr_lt_2()
        else:
            return self.staticbhp_for_ppr_gt_2()


sbhp = staticBHP()
print('')
print(sbhp.print_staticbhp())
print('<-------------------------------------->')
