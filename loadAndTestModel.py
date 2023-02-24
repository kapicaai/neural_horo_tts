# V3
import os
import torch

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                   local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

example_text = 'Близнецы: Гороскоп советует вам заняться чем то интересным например изнасилованием мусорного бака. День идеален для посещения театра абсурда. Не забывайте следить за тэмпом вращения Земли. Не стесняйтесь орать: "Господа, это пиздец!!!"'
sample_rate = 48000
speaker='baya'

audio_paths = model.save_wav(text=example_text,
                             speaker=speaker,
                             sample_rate=sample_rate)