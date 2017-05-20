import numpy as np
import sys
import os
import re


def parse_title(raw):
    nosqbrackets = re.sub(r'\[.+?\]', '', raw.lower())
    rmvideo = re.sub(r'\(o.+? video\)', '', nosqbrackets)

    return rmvideo.strip()

def to_input(s):
    return s.replace("-", "__").replace("(","___").replace(")","____").replace(" ", "_")

if __name__ == "__main__":
    #playlists_path = sys.argv[1]
    #output_file = sys.argv[2]

    print (to_input(parse_title('[HD] Hallo - Test (Original Mix) (Official Video)')))
    print (to_input(parse_title('[HD] Hallo - Test (Someone Remix) (Official Video)')))
    print (to_input(parse_title('[HD] Hallo - Test (Someone Edit) (Official Video)')))
