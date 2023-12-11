from flask import Blueprint, render_template, request
from app.physical_properties.conversions import evaluate_scrhs
from app.physical_properties.staticbhp import StaticBHP
from app.physical_properties.pseudoreduced_properties import pseudo_reduced_temp, pseudo_reduced_wellhead_pressure
from app.physical_properties.pseudocritical_properties import natural_gas_systems, natural_gas_systems2
from app.physical_properties.automate_integral_df import (
    pseudo_reduced_bhp,
    print_target_pseudoreduced_pressure,
    locate_cell_with_ppr,
    compute_denominator_sciv,
    compute_the_value_of_unknown_sciv,
    pivot_sciv,
    locate_and_get_cell_values,
)

physical_properties = Blueprint("physical_properties", __name__, template_folder="physical_properties")

@physical_properties.route("/")
def index():
    return render_template("index.html")

@physical_properties.route("/calculate_properties", methods=["POST"])
def calculate_properties():
    try:
        # Get input values from the form
        well_depth = float(request.form.get("well_depth"))
        temp_avg_sys = float(request.form.get("temp_avg_sys"))
        gas_specific_gravity = float(request.form.get("gas_specific_gravity"))
        static_wellhead_pressure = float(request.form.get("static_wellhead_pressure"))

        # Calculate pseudocritical properties
        tpc_natural_gas_systems = natural_gas_systems(gas_specific_gravity)
        ppc_natural_gas_systems = natural_gas_systems2(gas_specific_gravity)

        # Call functions from your modules with the input values
        scrhs = evaluate_scrhs(gas_specific_gravity, well_depth, temp_avg_sys)
        reduced_temp = pseudo_reduced_temp(temp_avg_sys, gas_specific_gravity)
        reduced_pressure = pseudo_reduced_wellhead_pressure(static_wellhead_pressure, gas_specific_gravity)

        sbhp = StaticBHP()

        # Get the result from the print_staticbhp method
        static_bhp_result = sbhp.print_staticbhp(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity)

        # Render the result page and pass the computed values
        return render_template(
            "result.html",
            scrhs=scrhs,
            reduced_temp=reduced_temp,
            reduced_pressure=reduced_pressure,
            static_bhp_result=static_bhp_result,
            tpc_natural_gas_systems=tpc_natural_gas_systems,
            ppc_natural_gas_systems=ppc_natural_gas_systems,
            static_wellhead_pressure=static_wellhead_pressure,
            locate_ppr=locate_cell_with_ppr(reduced_pressure),
            ppr_value=locate_and_get_cell_values(reduced_pressure)[0],
            check=print_target_pseudoreduced_pressure(reduced_pressure),
            deno_sciv=compute_denominator_sciv(reduced_temp, reduced_pressure),
            pseudo_reduced_bhp=pseudo_reduced_bhp(reduced_temp, reduced_pressure, scrhs),
            unknown_sciv=compute_the_value_of_unknown_sciv(reduced_temp, reduced_pressure),
            pivot_sci=pivot_sciv(reduced_temp, reduced_pressure, scrhs),
        )
    except Exception as e:
        return f'Error: {e}'
