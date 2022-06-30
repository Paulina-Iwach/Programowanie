from scipy.integrate import odeint
import argparse
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction as frac

def getData():
    """
    Function gets data from user.
    :return: list with values of variables.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-Q', type=int)
    parser.add_argument("-w", type=frac)
    parser.add_argument("-A", type=float)
    parser.add_argument("-v", type=int)
    parser.add_argument("-theta", type=float)
    parser.add_argument("-time", type=float)

    args = parser.parse_args()
    return args


def solveOscylatorEquation(y, T, Q, w, A):
    """
    Function solves the equation of motion of a mathematical pendulum with damping
    and periodic forcing force.
    :return: Solution of equation.
    """
    theta, omega = y
    dtheta_dt = [omega, A * np.cos(w * T) - 1 / Q * omega - np.sin(theta)]
    return dtheta_dt

def draw(args):
    """
    Function draws plot of motion of a mathematical pendulum with damping and periodic forcing force.
    :param args: list with values of variables.
    """
    y0 = [args.theta, args.v]
    t = np.linspace(0, args.time, 1000)

    sol = odeint(solveOscylatorEquation, y0, t, args=(args.Q, args.w, args.A))
    plt.plot(t, sol[:, 0], 'b', label='theta(t)')
    plt.plot(t, sol[:, 1], 'r', label='omega(t)')
    plt.legend(loc="best")
    plt.xlabel("time")
    plt.grid()
    plt.show()

def start():
    args = getData()
    draw(args)

start()