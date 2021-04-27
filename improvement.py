# Runner file for improvement tracker

# Improvement Tracker will help organise and schedule ways to improve my social skills and also be grateful for what I already have.

# Libraries
import os
import re
import json
import random
import requests

from datetime import datetime

# My Libraries
from mejora.trials import trials_setup

# Constants
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
MY_PATH = 'data\\nick_chesser\\'


def clean_advice(filename):
    with open(filename, encoding="utf-8") as file:
        advice = [line.strip('').replace('•', '')
                  for line in file.readlines() if re.search('•', line)]

    with open(filename, 'w+') as file:
        for index, line in enumerate(advice):
            file.write(f'{index + 1}.{line}')


def print_inspirational_quote():
    # Get Quote
    quotes = requests.get('https://type.fit/api/quotes')
    json_quotes = json.loads(quotes.text)

    # Pick Random Quote to Display
    quote = random.choice(json_quotes)
    print(f"{quote['text']} \n- {quote['author']} \n")


def print_advice(filename):
    with open(filename) as file:
        advice = random.choice([line.strip() for line in file.readlines()])

    print(f'{advice} \n')


def record_gratitude(filename):
    gratitude_list = []

    while True:
        grateful_for = input('Name something your grateful for...\n')

        if not grateful_for:
            break
        else:
            gratitude_list.append(grateful_for)

    with open(filename, 'a+') as file:
        today = datetime.today().strftime('%d-%m-%Y')

        for item in gratitude_list:
            file.write(f'{today}: {item}\n')


def main():
    # print_inspirational_quote()
    # print_advice(f'{MY_PATH}advice_99.txt')
    # print_advice(f'{MY_PATH}advice_68.txt')

    # record_gratitude(f'{MY_PATH}gratitude.txt')

    print("Running Improvement Script...")
    trials_setup(infile=f'{MY_PATH}trials_list.txt',
                 outfile=f'{MY_PATH}social_trials.json')


if __name__ == "__main__":
    main()
