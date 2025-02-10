import sys
import os
import pytest

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
src_dir = f'{script_dir}/../src/'

sys.path.insert(1, src_dir)

from SyrTransliterator import SyrTransliterator

s = SyrTransliterator(dialect_map_filename=f'{src_dir}/dialects/koine.json',
                      ipa_mapping_filename=f'{src_dir}/ipa/intermediate.json')

test_cases = {
    "ܐܲܒܵܐ": {'ipa': 'ʔabɑʔ', 'natural_ipa': 'abɑ', 'romanized': 'aba'},

    # # Matis Lectionis
    "ܐܝܼܕܵܐ": {'ipa': 'ʔidɑʔ', 'natural_ipa': 'idɑ', 'romanized': 'ida'},
    "ܐܘܼܪܚܵܐ": {'ipa': 'ʔurḥɑʔ' , 'natural_ipa': 'urḥɑ', 'romanized': 'urkha'},
    "ܐܘܼܪ": {'ipa': 'ʔur' , 'natural_ipa': 'ur', 'romanized': 'ur'},
    "ܐܝܼܡܵܡܵܐ": {'ipa': 'ʔimɑmɑʔ' , 'natural_ipa': 'imɑmɑ', 'romanized': 'imama'},
    "ܐܘܿܫܲܥܢܵܐ": {'ipa': 'ʔoʃaʕnɑʔ' , 'natural_ipa': 'oʃaʕnɑ', 'romanized': 'oshaʿna'},
    
    # # Yodh + Khwasa
    "ܣܲܪܓܝܼܣ": {'ipa': 'sargis', 'natural_ipa': 'sargɪs', 'romanized': 'sargis'},
    "ܓܝܼܘܵܪܓܝܼܣ": {'ipa': 'giwɑrgis', 'natural_ipa': 'gɪwɑrgɪs', 'romanized': 'giwargis'},
    "ܥܝܼܪܵܩ": {'ipa': 'ʕirɑq' , 'natural_ipa': 'ʕɪrɑq', 'romanized': 'ʿiraq'},
    "ܐܝܼܪܵܢ": {'ipa': 'ʔirɑn' , 'natural_ipa': 'irɑn', 'romanized': 'iran'},

    # # BDOLs
    "ܒܫܸܡܵܐ": {'ipa': 'bʃɪmɑʔ' , 'natural_ipa': 'bʃɪmɑ', 'romanized': 'b\'shima'}, # BDOL
    "ܠܘܼܚܵܐ": {'ipa': 'luḥɑʔ' , 'natural_ipa': 'luḥɑ', 'romanized': 'lukha'}, # not BDOL
    "ܘܲܪܕܵܐ": {'ipa': 'wardɑʔ' , 'natural_ipa': 'wardɑ', 'romanized': 'warda'}, # not BDOL
    "ܟܬܵܒ݂ܵܐ ܕܝܘܼܐܝܼܠ": {'ipa': 'ktɑvɑʔ djuʔil' , 'natural_ipa': 'ktɑvɑʔ djuʔɪl', 'romanized': 'ktawa d\'yu\'il'}, # not BDOL

    # # Single letters
    "ܐܵ": {'ipa': 'ʔɑ', 'natural_ipa': 'ɑ', 'romanized': 'a'},
    "ܐܲ": {'ipa': 'ʔa', 'natural_ipa': 'a', 'romanized': 'a'},
    "ܐܹ": {'ipa': 'ʔe', 'natural_ipa': 'e', 'romanized': 'e'},
    "ܐܸ": {'ipa': 'ʔɪ', 'natural_ipa': 'ɪ', 'romanized': 'i'},

    # ## Resh
    "ܣܘܼܖ̈ܵܝܹܐ": {'ipa': 'surɑjeʔ', 'natural_ipa': 'surɑje', 'romanized': 'suraye', 'ipa2syr': 'ܣܘܼܪܵܝܹܐ'}, # with dot-less resh + siyameh
    "ܣܘܼܪ̈ܵܝܹܐ": {'ipa': 'surɑjeʔ', 'natural_ipa': 'surɑje', 'romanized': 'suraye', 'ipa2syr': 'ܣܘܼܪܵܝܹܐ'}, # with resh + siyameh
    "ܣܘܼܪܵܝܹܐ": {'ipa': 'surɑjeʔ', 'natural_ipa': 'surɑje', 'romanized': 'suraye', 'ipa2syr': 'ܣܘܼܪܵܝܹܐ'}, # no siyameh

    # ## Sentences with lots of features
    "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ": {'ipa': 'bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑʔ', 'natural_ipa': 'bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑ', 'romanized': 'b\'ṣapra ke kathwen igratha', 'ipa2syr': 'ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪܵܬ݂ܵܐ'},
    "ܝܵܠܘܿܦܵܐ ܟܬ݂ܝܼܒ݂ ܠܹܗ ܡܹܐܡܲܪܬܵܐ": {'ipa': 'jɑlopɑʔ kθiv leh meʔmartɑʔ', 'natural_ipa': 'jɑlopɑʔ kθɪv leh meʔmartɑ', 'romanized': 'yalopa kthiw leh me\'marta'},
    "ܘܟܠܹܐܠܹܗ ܥܲܠ ܣܹܠܵܐ ܕܝܵܡܵܐ. ܘܚܙܹܠܝܼ ܕܐ݇ܣܸܩܠܹܗ ܕܵܒܵܐ ܡ̣ܢ ܝܵܡܵܐ.": {'ipa': 'wkleʔleh ʕal selɑʔ djɑmɑʔ. wḥzeli d[ʔ]sɪqleh dɑbɑʔ mɪn jɑmɑʔ.', 'natural_ipa': 'wkleʔleh ʕal selɑʔ djɑmɑʔ. wḥzelɪ d[ʔ]sɪqleh dɑbɑʔ mɪn jɑmɑʔ.', 'romanized': 'o\'kle\'leh ʿal sela d\'yama. o\'khzeli d\'siqleh daba min yama.', 'ipa2syr': 'ܘܟܠܹܐܠܹܗ ܥܲܠ ܣܹܠܵܐ ܕܝܵܡܵܐ. ܘܚܙܹܠܝܼ ܕܐ݇ܣܸܩܠܹܗ ܕܵܒܵܐ ܡܸܢ ܝܵܡܵܐ.'},
    "ܠܵܐ ܡܗܲܝܡܢܸܬ ܠܚܲܒܪ̈ܵܢܹܐ ܕܫܡܝܼܥ ܠܘܼܟ݂": {'ipa': 'lɑʔ mhajmnɪt lḥabrɑneʔ dʃmiʕ lux', 'natural_ipa': 'lɑʔ mhajmnɪt lḥabrɑneʔ dʃmɪʕ lux', 'romanized': 'la mhaymnit l\'khabrane d\'shmiʿ lukh', 'ipa2syr': 'ܠܵܐ ܡܗܲܝܡܢܸܬ ܠܚܲܒܪܵܢܹܐ ܕܫܡܝܼܥ ܠܘܼܟ݂'},
    "ܠܵܐ ܟܹܐ ܝܵܕ݂ܥܹܢ ܚܲܒܪ̈ܵܢܹܐ ܕܗ̇ܝ ܙܡܵܪܬܵܐ": {'ipa': 'lɑʔ keʔ jɑðʕen ḥabrɑneʔ dʔɑjɑ zmɑrtɑʔ', 'natural_ipa': 'lɑʔ keʔ jɑðʕen ḥabrɑneʔ dʔɑjɑ zmɑrtɑ', 'romanized': 'la ke yadhʿen khabrane d\'aya zmarta', 'ipa2syr': 'ܠܵܐ ܟܹܐ ܝܵܕ݂ܥܹܢ ܚܲܒܪܵܢܹܐ ܕܐܵܝܵ ܙܡܵܪܬܵܐ'},
    "ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܠܵܗ̇": {'ipa': 'batˤɑriθɑʔ hɪʃ mlɑjɑʔ ilɑh', 'natural_ipa': 'batˤɑrɪθɑʔ hɪʃ mlɑjɑʔ ɪlɑh', 'romanized': 'baṭaritha hish mlaya ilah', 'ipa2syr': 'ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܼܠܵܗ'},
    "ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܠܗ̇": {'ipa': 'batˤɑriθɑʔ hɪʃ mlɑjɑʔ ilɑh', 'natural_ipa': 'batˤɑrɪθɑʔ hɪʃ mlɑjɑʔ ɪlɑh', 'romanized': 'baṭaritha hish mlaya ilah', 'ipa2syr': 'ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܼܠܵܗ'},
    "ܠܹܐ ܝܠܹܗ ܒܸܡܨܵܝܵܐ ܢܵܦܹܫ!": {'ipa': 'leʔ ileh bɪmsˤɑjɑʔ nɑpeʃ!', 'natural_ipa': 'leʔ ɪleh bɪmsˤɑjɑʔ nɑpeʃ!', 'romanized': 'le ileh bimṣaya napesh!', 'ipa2syr': 'ܠܹܐ ܝܼܠܹܗ ܒܸܡܨܵܝܵܐ ܢܵܦܹܫ!'},
    "ܫܘܼܐܵܠܵܐ ܡܸܨܝܵܐ ܝܠܹܗ؟": {'ipa': 'ʃuʔɑlɑʔ mɪsˤjɑʔ ileh?', 'natural_ipa': 'ʃuʔɑlɑʔ mɪsˤjɑʔ ɪleh?', 'romanized': 'shu\'ala miṣya ileh?', 'ipa2syr': 'ܫܘܼܐܵܠܵܐ ܡܸܨܝܵܐ ܝܼܠܹܗ؟'}
}

@pytest.mark.parametrize("syriac_text,expected", list(test_cases.items()))
def test_syriac_transliteration(syriac_text, expected):
    """
    Tests that the transliterate() and reverse_transliterate() methods
    of SyrTransliterator produce the expected results.
    """
    # 1. Transliterate forward
    transliteration = s.transliterate(syriac_text)

    # 2. Check IPA
    assert transliteration['ipa'] == expected['ipa'], (
        f"\n[IPA Mismatch]\n"
        f"Text: {syriac_text}\n"
        f"Expected IPA: {expected['ipa']}\n"
        f"Got IPA:      {transliteration['ipa']}"
    )

    # 3. Check Natural IPA
    assert transliteration['natural_ipa'] == expected['natural_ipa'], (
        f"\n[Natural IPA Mismatch]\n"
        f"Text: {syriac_text}\n"
        f"Expected Natural IPA: {expected['natural_ipa']}\n"
        f"Got:                  {transliteration['natural_ipa']}"
    )

    # 4. Check Romanized
    assert transliteration['romanized'] == expected['romanized'], (
        f"\n[Romanized Mismatch]\n"
        f"Text: {syriac_text}\n"
        f"Expected: {expected['romanized']}\n"
        f"Got:       {transliteration['romanized']}"
    )

    # 5. Reverse transliterate if IPA2Syr is specified, or default to original text
    reverse_expected = expected.get('ipa2syr', syriac_text)
    revipa = s.reverse_transliterate(transliteration['ipa'])
    assert revipa == reverse_expected, (
        f"\n[Reverse IPA Mismatch]\n"
        f"Text: {syriac_text}\n"
        f"Expected Reverse: {reverse_expected}\n"
        f"Got:              {revipa}"
    )