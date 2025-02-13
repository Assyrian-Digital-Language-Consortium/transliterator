#!/usr/bin/env python3
# coding=utf-8

import sys
import os

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
src_dir = f'{script_dir}/../src/'

sys.path.insert(1, src_dir)

from SyrTransliterator import SyrTransliterator

# Instantiate the transliterator (using default mappings)
iranian_koine_file = f'{src_dir}/dialects/iranian_koine.json'
transliterator = SyrTransliterator(dialect_map_filename=iranian_koine_file)

text = "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ"
result = transliterator.transliterate(text)

print("Syriac:", text)
print("IPA:", result["ipa"])
print("Natural IPA:", result["natural_ipa"])
print("Romanized:", result["romanized"])
