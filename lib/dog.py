#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def __init__(self, name="Unnamed", breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    #Instance method definition
    def sit(self):
        print("The dog is sitting.")
    pass
