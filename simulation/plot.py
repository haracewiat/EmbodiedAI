import pygame
import sys
from itertools import count
from simulation import config
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation.agent import State
import numpy as np
import pandas as pd

import csv
import random
import time


class LivePlot():

    def __init__(self):
        plt.style.use('fivethirtyeight')

        x = []
        y = []
        index = count()
        self.running = True

        self.run()

    def run(self):
        if not bool(config.terminate_threads):
            ani = FuncAnimation(plt.gcf(), self.animate, interval=500)
            plt.tight_layout()
            plt.show()

    def animate(self, i):

        if not bool(config.terminate_threads):

            data = pd.read_csv('data.csv')

            data_points = []
            x = []

            # plt.plot(x, y1, label="Channel 1")
            # plt.plot(x, y2, label="Channel 1")

            for i, key in enumerate(data):
                if i == 0:
                    x = data[key]
                else:
                    variable = "y{0}".format(i)
                    variable = data[key]
                    data_points.append(variable)

            plt.cla()

            for i in range(0, len(data_points)):
                color_name = "N_{}".format(
                    data_points[i].name.replace('State.', ''))
                plt.stackplot(
                    x, data_points[i], color=config.COLORS[color_name])

            # Adjust the legend manually!
            plt.legend(labels=['Susceptible', 'Recovered', 'Infected'])

            plt.tight_layout()
        else:
            plt.close('all')


class Data():

    def __init__(self, data):
        self.field_names = ["x_value"]
        self.x_value = 0

        # Get the field names
        for key in data.keys():
            self.field_names.append(key)

    def initialize(self):
        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
            csv_writer.writeheader()

    def add_entry(self, data):
        with open('data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)

            data.update({'x_value': self.x_value})
            data.update(data)

            csv_writer.writerow(data)

            self.x_value += 1
