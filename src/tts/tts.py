import os
import sys

import argparse

argparser = argparse.ArgumentParser(
    prog = 'Silero TTS cli'
    description = "Convert text file(s) into audio files using Silero's Model!"
    epilog = 'Enjoy!'
)

argparser.add_argument('inputs',
                       metavar='<inputFile>+', type=str, nargs='+',
                       help='List of text file paths to convert')

