import os
import sys
import argparse

argparser = argparse.ArgumentParser(
    prog = 'tts.py',
    description = "Convert text file(s) into audio files using Silero's Model!",
    epilog = 'Enjoy!'
)

requiredArgs = argparser.add_argument_group('REQUIRED arguments')

requiredArgs.add_argument('-o', '--output',
                        metavar='<outputFile.wav>', type=str,
                        help='Output file name to write the sound to, otherwise will read stdin firstly',
                        required=True)
requiredArgs.add_argument('-v', '--voice',
                        metavar='<voicename>', type=str,
                        help='name of the voice to be used',
                        required=True)


argparser.add_argument('-i', '--input',
                        metavar='<inputFile>', type=str,
                        help='Text file to convert',
                        required=False)

argparser.add_argument('-mp3',
                        action='store_true',
                        help='also convert the output into .mp3',
                        required=False)


args = argparser.parse_args()

if ('.wav' not in args.output):
    args.output = args.output +".wav"
    print(f"the output file name will be {args.output}")

scriptDir = os.path.dirname(os.path.abspath(__file__))
modelFileName = "model.pt"
modelFilePath = f"{scriptDir}/{modelFileName}"

if not os.path.isfile(modelFilePath):
    print('No model found, please read the readme first, there must be ' + modelFilePath)
    exit()


# returns the loaded model
def loadModel():
    device = torch.device('cpu')
    os.chdir(scriptDir)
    model = torch.package.PackageImporter(modelFileName).load_pickle("tts_models", "model")
    model.to(device)
    return model

def generate(model, textContent, outputFileName, speaker):
    sample_rate = 48000
    audio_paths = model.save_wav(text=textContent,
                             speaker=speaker,
                             sample_rate=sample_rate,
                             audio_path=outputFileName)

def getTextFromFile(filename):
    file = open(filename, mode='r', encoding='utf8')
    textFromFile = file.read()
    file.close()
    return textFromFile

def getTextFromStdin():
    textFromStdin = sys.stdin.read()
    return textFromStdin

def convertToMp3UsingFfmpeg(input, output):
    import subprocess
    mp3convert_command = ["ffmpeg", "-y", "-i", input, "-f", "mp3", output]
    process = subprocess.Popen(mp3convert_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    if (process.returncode != 0):
        print('ERROR while converting! Outputting the output from converting attempt:')
        print(out)
        print(err)
        return False
    else:
        return True

textToConvert = ""
if(args.input != None):
    print('reading text file...')
    textToConvert = getTextFromFile(args.input)
    print('got the text.\n')
else:
    textToConvert = getTextFromStdin()

print('importing TORCH...')
import torch
print('imported TORCH!\n')

print('loading model...')
model = loadModel()
print('done loading model.\n')

print('generating...')
generate(model, textToConvert, args.output, args.voice)
print('done generating.')

if (args.mp3):
    print('converting to mp3...')
    successConverting = convertToMp3UsingFfmpeg(args.output, args.output.replace('wav', 'mp3'))
    if (successConverting):
        print('done converting.')
    else:
        print('could not convert! See errors above.')

print('Thank You!')
