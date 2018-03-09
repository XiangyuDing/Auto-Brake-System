import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def ABStest():
    # Input initial variables: distance and velocity
    init_s = float(input("Current distance is(m):"))
    init_v = float(input("Current velocity is(m/s):"))
    init_b = 0

    # Initial condition classifying
    if init_s > 50 and 0 < init_v <= 30:
        print("Normal driving.")
    elif 0 < init_s <= 50 and 0 < init_v <= 30:
        print("Automatic Brake System is launching.")
        feedback(init_s, init_v)
    elif init_v > 30:
        print("Driving over the speed limit!")
    else:
        print("Error input, please try again.")


def feedback(distance, speed):
    # Entire processing simulation
    # weight = 1
    t = 0.5
    count = 0
    while speed > 0:
        brake = FLctrl(distance, speed)
        speed = speed - brake * t
        if speed < 0:
            speed = 0
        distance = distance - (2 * speed + brake * t) / 2
        if distance <= 0:
            print('Crash!')
            break
        print('speed is: {0:.2f} m/s, distance is: {1:.2f} m, brake force is: {2:.2f} kN'
              .format(speed, distance, brake))
        count += 1
    T = t * count
    print('Total time is {0:1f}'.format(T))


def FLctrl(current_distance, current_speed):
    # Define input and output variables
    distance = ctrl.Antecedent(np.arange(0, 50, 1), 'distance')
    velocity = ctrl.Antecedent(np.arange(0, 30, 1), 'velocity')
    brake = ctrl.Consequent(np.arange(0, 30, 1), 'brake')

    # Distance membership function
    distance['near'] = fuzz.trimf(distance.universe, [0, 0, 25])
    distance['medium'] = fuzz.trimf(distance.universe, [0, 25, 50])
    distance['far'] = fuzz.trimf(distance.universe, [25, 50, 50])

    # Velocity membership function
    velocity['low'] = fuzz.trimf(velocity.universe, [0, 0, 15])
    velocity['medium'] = fuzz.trimf(velocity.universe, [0, 15, 30])
    velocity['high'] = fuzz.trimf(velocity.universe, [15, 30, 30])

    # Brake force membership function
    brake['low'] = fuzz.trimf(brake.universe, [0, 0, 15])
    brake['medium'] = fuzz.trimf(brake.universe, [0, 15, 30])
    brake['high'] = fuzz.trimf(brake.universe, [15, 30, 45])
    brake['full'] = fuzz.trimf(brake.universe,[30, 45, 45])

    # Inference Engine
    rule1 = ctrl.Rule(antecedent=(distance['medium'] & velocity['low']) |
                                                 (distance['far'] & velocity['medium']),
                             consequent=brake['low'])
    rule2 = ctrl.Rule(antecedent=(distance['near'] & velocity['low']) |
                                                 (distance['medium'] & velocity['medium']) |
                                                 (distance['far'] & velocity['high']),
                             consequent=brake['medium'])
    rule3 = ctrl.Rule(antecedent=(distance['medium'] & velocity['high']) |
                                                 (distance['near'] & velocity['medium']),
                             consequent=brake['high'])
    rule4 = ctrl.Rule(antecedent=(distance['near'] & velocity['high']),
                             consequent=brake['full'])

    # Controller simulation
    ABS_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    ABS = ctrl.ControlSystemSimulation(ABS_ctrl)

    # Automatic brake processing
    ABS.input['distance'] = current_distance
    ABS.input['velocity'] = current_speed
    ABS.compute()
    # brake.view(sim = ABS)
    return ABS.output['brake']


def linear_regression(res_s, res_v):
    pass

def polycurvefit(res_s, res_v):
    pass

if __name__ == "__main__":
    ABStest()
