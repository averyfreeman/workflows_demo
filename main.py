#!/usr/bin/env python3
import sys
from art import text2art

def main(text):
    return print(str(text2art(text, font="random")))

hello = "hello world"

if __name__ == "__main__":
    main(hello)