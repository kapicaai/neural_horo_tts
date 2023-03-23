# prerequisites
Install python 3!
And install pip for it, in case it's not bundled for your OS

Also download/install ffmpeg and make sure it's accessible as `ffmpeg` command.
That is required in case You want to use the -mp3 switch to automatically convert the output to mp3.

# initialize

``` py
# install packages
pip install -r requirements.txt

# run it for the first time to load the model
python loadAndTestModel.py
```
on windows use `py -m pip` instead of `pip`


# run
```
usage: tts.py [-h] -o <outputFile.wav> -v <voicename> [-i <inputFile>] [-mp3]

Convert text file(s) into audio files using Silero's Model!

options:
  -h, --help            show this help message and exit
  -i <inputFile>, --input <inputFile>
                        Text file to convert
  -mp3                  also convert the output into .mp3

REQUIRED arguments:
  -o <outputFile.wav>, --output <outputFile.wav>
                        Output file name to write the sound to, otherwise will
                        read stdin firstly
  -v <voicename>, --voice <voicename>
                        name of the voice to be used

Enjoy!

VoiceName
Any of voices supported by Silero.
At the time of writing that were:
  -  aidar
  -  baya
  -  kseniya
  -  xenia
  -  eugene
  -  random (Silero will generate a new voice)

```