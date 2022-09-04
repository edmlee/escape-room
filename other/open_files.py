# Required files: "responses.txt", "secret_layout.txt", "escape_layout.txt"

import os
import random

def open_responses():
    file_name = "responses.txt"
    if os.path.exists(file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        random.shuffle(lines)
        count = 0

        for line in lines:
            line = line.rstrip("\n")
            print(f"{count}) {line}")
            count += 1
        file.close()
    else:
        print("> Missing file required to start the game")
        print(f"> Please import {file_name} into the same directory")
        quit()


def open_secret():
    file_name = "secret_layout.txt"
    if os.path.exists(file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            line = line.rstrip("\n")
            print(line)
        file.close()
    else:
        print("> Missing file required to start the game")
        print(f"> Please import {file_name} into the same directory")
        quit()

def open_escape():
    file_name = "escape_layout.txt"
    if os.path.exists(file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            line = line.rstrip("\n")
            print(line)
        file.close()
    else:
        print("> Missing file required to start the game")
        print(f"> Please import {file_name} into the same directory")
        quit()

# Main
open_responses()
open_secret()
open_escape()
