import json


class Notes:

    def __init__(self) -> None:
        with open('notes.json') as f:
            self._data = json.load(f)

    def save_data(self):
        with open('notes.json', 'w') as json_file:
            json.dump(self._data, json_file)

    def add_note(self, name, date, note):
        #if self._data[name][date] is None:
        self._data[name] = {date: note}
        self.save_data()
        #else:
        #   raise Exception("There is already a note for this date and name.")



if __name__ == "__main__":
    n = Notes()
    n.add_note("patrice", '10', 10)
    print(n._data)