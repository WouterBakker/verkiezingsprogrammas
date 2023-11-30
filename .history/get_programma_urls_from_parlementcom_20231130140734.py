# Get pdfs from 2017 & 2021

import requests
import pickle
import sys, os


class Verkiezingsprogramma:
    def __init__(self, party, year, url, raw_text):
        self.party = party
        self.year = year
        self.url = url
        self.raw_text = raw_text
        