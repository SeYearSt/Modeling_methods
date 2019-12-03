import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature_min = 20
temperature_max = 120
temperature_diff_min = -5
temperature_diff_max = 5
power_min = 0
power_max = 100

# inputs = [[1, 4], [1, -4], [1, 2], [1, 1], [10, -4], [10, -2], [10, 1],[10, 4],
#           [20, -4], [20, -3], [20,-2], [20,-1],[20,1], [20,3], [20,4],
#           [30, -4], [30, -3], [30, 1], [30, 3]]

inputs = [[20, -4], [20, 4], [70, 0], [70, -4], [70, 4], [60, 0], [60, -4], [60, 4], [120, -4], [120, 4]]
# define scope
temperature = ctrl.Antecedent(np.arange(temperature_min, temperature_max, 1), 'temperature')
temperature_diff = ctrl.Antecedent(np.arange(temperature_diff_min, temperature_diff_max, 1), 'temperature_diff')
power = ctrl.Consequent(np.arange(power_min, power_max, 1), 'power')

# define membership functions
temperature['low'] = fuzz.trimf(temperature.universe, [20, 20, 60])
temperature['optimal'] = fuzz.trimf(temperature.universe, [50, 60, 80])
temperature['high'] = fuzz.trimf(temperature.universe, [70, 120, 120])

temperature_diff['decrease'] = fuzz.trimf(temperature_diff.universe, [-5, -5, -3])
temperature_diff['stable'] = fuzz.trimf(temperature_diff.universe, [-3, 0, 3])
temperature_diff['increase'] = fuzz.trimf(temperature_diff.universe, [1, 5, 5])

power['off'] = fuzz.trimf(power.universe, [0, 0, 50])
power['stand_by'] = fuzz.trapmf(power.universe, [40, 50, 60, 70])
power['on'] = fuzz.trimf(power.universe, [60, 90, 100])

# view of membership functions
temperature.view()
temperature_diff.view()
power.view()

# define rules for controller
rule1 = ctrl.Rule(temperature['low'], power['on'])
rule2 = ctrl.Rule(temperature['optimal'] & temperature_diff['decrease'], power['on'])
rule3 = ctrl.Rule(temperature['optimal'] & temperature_diff['increase'], power['off'])
rule4 = ctrl.Rule(temperature['optimal'] & temperature_diff['stable'], power['stand_by'])
rule5 = ctrl.Rule(temperature['high'], power['off'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])

boiler = ctrl.ControlSystemSimulation(tipping_ctrl)

template = 'Input: temperature: {}, temperature difference: {}\n' \
           'Output: power of boiler: {}\n'

for input in inputs:
 boiler.input['temperature'] = input[0]
 boiler.input['temperature_diff'] = input[1]
 boiler.compute()
 output_power = boiler.output['power']
 print(template.format(input[0], input[1], output_power))


# power.view(sim=boiler)
