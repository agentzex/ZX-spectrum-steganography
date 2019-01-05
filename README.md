# ZX-spectrum-steganography

The idea behind this repo is to hide steganography messages via sound.
This tool relies on the z88dk compiler for the ZX Spectrum (https://github.com/z88dk/z88dk), currently working on windows but should be easy to port to other OS.

1. You should first download  the latest win32 build from - http://nightly.z88dk.org/ and extract all the files to the "z88dk" directory under this repo.
2. Then run:\
  create_secret.py -i "path_to_txt_file"\
  where "path_to_txt_file" is the local path to the .txt file where your secret message is saved\
  For demo, run:\
  create_secret.py -i test.txt
3. an "out.tap" and "out.wav" files will be created in the same directory. The "out.tap" file is ZX spectrum file that you can run on a ZX spectrum emulator.
The "out.wav" file is the sound file you can play on some media in order to pass your hidden message
4. In order to revert the .wav file back to  .tap file in order to run on an emulator, you can use "Wav2Tap_Converter" from https://github.com/SilverGreen93/ZXwav2tap/tree/master/Release
5. I used ZEsarUX emulator to run .tap files on windows - http://www.emutopia.com/index.php/emulators/item/364-sinclair-zx-spectrum/1278-zesarux
