import numpy as np
import math
import matplotlib.pyplot as plt

def get_float_input(var, prompt):
    while (isinstance(var, float) == False):
        var = input(f'{prompt}')
        try:
            var = float(parsed(var))
        except ValueError:
            var = None
    return var

def parsed(s):
    if ('pi' in s):
        if (s[0] == 'p'):
            s = s.replace('pi', str(math.pi))
            return eval(s)
        else:
            s = s.replace('pi', ('*' + str(math.pi)))
            return eval(s)
    return s

def plot_angle(t):
    label = f'{round(t, 3)} rad'
    
    angles = np.linspace(0, 2 * math.pi, 1000)
    
    x = np.cos(angles)
    y = np.sin(angles)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.plot(x, y, color='b')
    plt.gca().set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Unit circle')
    plt.grid(True)
    
    ax.quiver(0, 0, math.cos(t), math.sin(t), scale_units='xy', scale=1, color='r')
    plt.text(math.cos(t) * 1.05, math.sin(t) * 1.05, label, fontsize=10)
    plt.show()

angle = None
mode = None
func = None
result = None

deg_inputs = ['d', 'deg', 'degrees']
rad_inputs = ['r', 'rad', 'radians']

instructions = {
    1: ['sine', 'result = math.sin(angle)'],
    2: ['cosine','result = math.cos(angle)'],
    3: ['tangent', 'result = math.tan(angle)'],
    4: ['cotangent', 'result = 1 / math.tan(angle)'],
    5: ['secant', 'result = 1 / math.cos(angle)'],
    6: ['cosecant', 'result = 1 / math.sin(angle)'],
}

print('You are using a simple trigonometric function calculator in Python.\n')

print('Type "d" or "deg" for degrees')
print('Type "r" or "rad" for radians\n')

while (mode not in deg_inputs + rad_inputs):
    mode = input('Select angle mode: ').lower()
    
print('')
print('Press 1 for sine')
print('Press 2 for cosine')
print('Press 3 for tangent')
print('Press 4 for cotangent')
print('Press 5 for secant')
print('Press 6 for cosecant')

print('')
while (func not in (list(range(1, 10)))):
    func = input('Enter your function: ')
    try:
        func = int(func)
    except ValueError:
        func = None
    
angle = get_float_input(angle, 'Enter your angle: ')

if (mode in deg_inputs):
    angle *= (math.pi / 180)
    
angle %= (2 * math.pi)

exec(instructions[func][1])
print('\n--------------------------------------------------------------')
print(f'The {instructions[func][0]} of {round(angle, 3)} radians ({round(angle * (180 / math.pi))} degrees) is {round(result, 3)}.')
print('--------------------------------------------------------------')

print('\nPlotting angle on the unit circle...')
plot_angle(angle)
