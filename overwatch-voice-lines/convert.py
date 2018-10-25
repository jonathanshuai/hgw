import os
import soundfile as sf
from contextlib import suppress
from tqdm import tqdm

ogg_dir = "./ogg"
wav_dir = "./wav"

for ogg_prefix, dirs, files in tqdm(os.walk(ogg_dir)):
    for ogg_name in files:
        if ogg_name.endswith('ogg'):
            
            wav_prefix = os.path.join(wav_dir, ogg_prefix.split('/')[-1])

            wav_name = (ogg_name[:-3] + 'wav').replace(' ', '_')

            with suppress(FileExistsError):
                os.makedirs(wav_prefix)
            
            data, samplerate = sf.read(os.path.join(ogg_prefix, ogg_name))
            sf.write(os.path.join(wav_prefix, wav_name), data, samplerate)