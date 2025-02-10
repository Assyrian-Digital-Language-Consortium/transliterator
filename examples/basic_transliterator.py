import sys
import os

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
src_dir = f'{script_dir}/../src/'

sys.path.insert(1, src_dir)

from SyrTransliterator import SyrTransliterator

# Instantiate the transliterator (using default mappings)
transliterator = SyrTransliterator()

text = "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ"
result = transliterator.transliterate(text)

print("IPA:", result["ipa"])
print("Natural IPA:", result["natural_ipa"])
print("Romanized:", result["romanized"])