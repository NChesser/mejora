"""
Details surronding trials
"""

# Libraries
import os
import json

from datetime import datetime


class Trial:
    def __init__(self, trial, difficulty=5, completed=0, notes=[], created=datetime.today().strftime('%d-%m-%Y')):
        self.trial = trial
        self.difficulty = difficulty
        self.completed = completed
        self.notes = notes
        self.created = created

    def __str__(self):
        return self.trial

    def add_completed(self):
        print('Adding completed...')
        self.completed = self.completed + 1

    def add_note(self):
        # Handle input for new note
        note = input("Enter note...\n")
        while True:
            difficulty = input('Enter difficulty...\n')

            try:
                difficulty = int(difficulty)

                if difficulty >= 0 and difficulty <= 10:
                    break
            except:
                print('Invalid number entered!')

        note_dict = {
            "date": datetime.today().strftime('%d-%m-%Y'),
            "note": note,
            "difficulty": difficulty,
        }
        self.notes.append(note_dict)

        # If Note added then they have completed trial
        self.add_completed()

    def save(self, filename):
        # Load trials file first
        try:
            with open(filename) as file:
                trials = json.load(file)
        except:
            trials = []

        trials = list(filter(lambda t: t['trial'] != self.trial, trials))
        trials.append(self.__dict__)

        with open(filename, 'w+') as outfile:
            json.dump(trials, outfile, indent=4)


def add_new_trial(outfile, trial, difficulty):

    new_trial = Trial(trial, difficulty)
    new_trial.save(outfile)


def trials_setup(infile, outfile):
    with open(infile) as file:
        trials_list = [line.strip() for line in file.readlines()]

    trials_dict = {}

    for trial in trials_list:
        [key, value] = trial.split(', ')

        trials_dict[key] = value

    # Load trials file first
    try:
        with open(outfile) as file:
            trials = json.load(file)
    except:
        trials = []

    # Exclude already included trials
    for trial in trials:
        trialname = trial['trial']
        if trialname in trials_dict:
            del trials_dict[trialname]

    for trial, difficulty in trials_dict.items():
        print(f'Adding Trial... {trial}')
        add_new_trial(outfile, trial, difficulty)


def main():
    pass


if __name__ == "__main__":
    main()
