import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import continuous_plotter, discrete_plotter


def continuous_sine():
    frequency = 1
    amplitude = 1
    number_of_points = 10000
    time_initial = 0
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    x_t = amplitude * np.sin(2 * np.pi * frequency * time)

    continuous_plotter(
        time, x_t,
        'Continuous Sine wave Signal', 'Sin wave Signal',
        'Time [s]',  'Amplitude')


def discrete_sine():
    frequency = 1
    amplitude = 1
    fs = 20
    ts = 1 / fs
    samples = 100
    n = np.arange(samples)
    x_n = amplitude * np.sin(2 * np.pi * frequency * n * ts )

    discrete_plotter(
        n, x_n,
        'Discrete Sine wave Signal', 'Sin wave Signal',
        'Time [n = index of sample]',  'Amplitude')
