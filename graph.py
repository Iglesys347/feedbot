from os import name
import matplotlib.pyplot as plt
import json
import os

COLORS = ["r", "b", "g", "y", "m", "k"]

class NoteGraph:

    def __init__(self):
        with open('notes.json') as f:
            self._data = json.load(f)
        self._users = list(self._data.keys())

    def compute_mean(self):
        tmp_data = {}
        for usr in self._data:
            for nb_week in self._data[usr]:
                if nb_week in tmp_data.keys():
                    tmp_data[nb_week].append(self._data[usr][nb_week])
                else:
                    tmp_data[nb_week] = [self._data[usr][nb_week]]
        return [sum(tmp_data[elt]) / len(tmp_data[elt]) for elt in tmp_data], list(tmp_data.keys())

    def make_graph(self, file_name):
        for i, usr in enumerate(self._users):
            plt.plot(self._data[usr].keys(), self._data[usr].values(), '-o', c=COLORS[i])
        y_mean, x_mean = self.compute_mean()
        plt.plot(x_mean, y_mean, '-o', c=COLORS[-1], linewidth=7.0)
        plt.legend(self._users + ["Mean"])
        plt.xlabel("Week numbers")
        plt.ylabel("Satisfaction note")
        if os.path.isfile(file_name):
            os.remove(file_name)
        plt.savefig(file_name)
        plt.clf()

    def __del__(self):
        self._data.clear()
        self._users.clear()

if __name__ == "__main__":
    n = NoteGraph()
    n.make_graph("Graph.png")
