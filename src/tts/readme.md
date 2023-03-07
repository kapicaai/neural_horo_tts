# prerequisites
Install python 3!
And install pip for it, in case it's not bundled for your OS

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
usage: tts.py [-h] -in <inputFile> -out <outputFile.wav> -v <voicename>

optional arguments:
  -h, --help            show this help message and exit

REQUIRED arguments:
  -in <inputFile>, --input <inputFile>
                        Text file to convert
  -out <outputFile.wav>, --output <outputFile.wav>
                        Output file name to write the sound to
  -v <voicename>, --voice <voicename>
                        name of the voice to be used

VoiceName
any of voices supported by Silero

```