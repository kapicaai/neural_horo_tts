import os
import sys

import argparse

argparser = argparse.ArgumentParser(
    prog = 'tts.py',
    description = "Convert text file(s) into audio files using Silero's Model!",
    epilog = 'Enjoy!'
)

requiredArgs = argparser.add_argument_group('REQUIRED arguments')

requiredArgs.add_argument('-in', '--input',
                        metavar='<inputFile>', type=str,
                        help='Text file to convert',
                        required=True)

requiredArgs.add_argument('-out', '--output',
                        metavar='<outputFile.wav>', type=str,
                        help='Output file name to write the sound to',
                        required=True)
                        
requiredArgs.add_argument('-v', '--voice',
                        metavar='<voicename>', type=str,
                        help='name of the voice to be used',
                        required=True)

args = argparser.parse_args()

