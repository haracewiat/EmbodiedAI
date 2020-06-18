from simulation import config
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from experiments.covid import parameters as p
from simulation.agent import State
import pandas as pd
import csv


class LivePlot():

    def __init__(self, queue):
        plt.style.use('fivethirtyeight')

        # Get initial information
        self.data = pd.read_csv('data.csv')
        self.labels = []
        colors_array = []

        # Basic Reproduction Number
        self.r_value = 0
        self.queue = queue

        for i, key in enumerate(self.data):
            if i != 0:
                # Create labels
                self.labels.append(key.replace(
                    'State.', '').lower().capitalize())

                # Create colors
                colors_array.append(
                    config.COLORS["N_{}".format(key.replace('State.', ''))])

        self.colors = tuple(colors_array)

        self.running = True
        self.run()

    def run(self):
        animation = FuncAnimation(
            plt.gcf(), self.animate, interval=p.INTERVAL)
        plt.tight_layout()
        plt.show()

    def animate(self, i):

        data = pd.read_csv('data.csv')

        data_points = []
        x = []

        for i, key in enumerate(data):
            if i == 0:
                x = data[key]
            else:
                data_points.append(data[key])

        plt.cla()

        plt.stackplot(x, data_points, labels=self.labels,
                      colors=self.colors)

        plt.legend(loc='upper left')

        if not self.queue.empty():
            self.r_value = self.queue.get()

        plt.title("Basic Reproduction Number: " +
                  str(self.r_value + 0.0), fontdict=None, loc='center', fontsize=15)


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

    def add_entry(self, original_data):

        # Update data
        data = original_data.copy()
        data.update({'x_value': self.x_value})
        data.update(data)

        # Uncomment to change values to percentage
        # for key in data:
        #     if key != "x_value":
        #         data[key] = (data[key] / p.N_AGENTS)

        with open('data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
            csv_writer.writerow(data)

        self.x_value += 1
