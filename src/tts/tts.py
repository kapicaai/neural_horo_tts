import os
import argparse

argparser = argparse.ArgumentParser(
    prog = 'tts.py',
    description = "Convert text file(s) into audio files using Silero's Model!",
    epilog = 'Enjoy!'
)

requiredArgs = argparser.add_argument_group('REQUIRED arguments')

requiredArgs.add_argument('-i', '--input',
                        metavar='<inputFile>', type=str,
                        help='Text file to convert',
                        required=True)

requiredArgs.add_argument('-o', '--output',
                        metavar='<outputFile.wav>', type=str,
                        help='Output file name to write the sound to',
                        required=True)
                        
requiredArgs.add_argument('-v', '--voice',
                        metavar='<voicename>', type=str,
                        help='name of the voice to be used',
                        required=True)

args = argparser.parse_args()


print('importing TORCH...')
import torch
print('imported TORCH!\n')

model_file = 'model.pt'
if not os.path.isfile(model_file):
    print('No model found, please read the readme first, there must be ' + model_file)
    exit()


# returns the loaded model
def loadModel():
    device = torch.device('cpu')
    modelFilePath = 'model.pt'
    model = torch.package.PackageImporter(modelFilePath).load_pickle("tts_models", "model")
    model.to(device)
    return model

def generate(model, textContent, outputFileName, speaker):
    sample_rate = 48000
    audio_paths = model.save_wav(text=textContent,
                             speaker=speaker,
                             sample_rate=sample_rate,
                             audio_path=outputFileName)


print('reading text file...')
# Open a file: file
file = open(args.input, mode='r', encoding='utf8')
# read all lines at once
textToConvert = file.read()
# close the file
file.close()
print('got the text.\n')

print('loading model...')
model = loadModel()
print('model loaded.\n')

print('generating...')
generate(model, textToConvert, args.output, args.voice)
print('done generating.')
print('Thank You!')