import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../src/')

from SyrTransliterator import SyrTransliterator

s = SyrTransliterator()

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
    "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ": {'ipa': 'bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑʔ', 'natural_ipa': 'bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑ', 'romanized': 'b\'ṣapra ke kathwen igratha'},
    "ܝܵܠܘܿܦܵܐ ܟܬ݂ܝܼܒ݂ ܠܹܗ ܡܹܐܡܲܪܬܵܐ": {'ipa': 'jɑlopɑʔ kθiv leh meʔmartɑʔ', 'natural_ipa': 'jɑlopɑʔ kθɪv leh meʔmartɑ', 'romanized': 'yalopa kthiw leh me\'marta'},
    "ܘܟܠܹܐܠܹܗ ܥܲܠ ܣܹܠܵܐ ܕܝܵܡܵܐ. ܘܚܙܹܠܝܼ ܕܐ݇ܣܸܩܠܹܗ ܕܵܒܵܐ ܡ̣ܢ ܝܵܡܵܐ.": {'ipa': 'wkleʔleh ʕal selɑʔ djɑmɑʔ. wḥzeli d[ʔ]sɪqleh dɑbɑʔ mɪn jɑmɑʔ.', 'natural_ipa': 'wkleʔleh ʕal selɑʔ djɑmɑʔ. wḥzelɪ d[ʔ]sɪqleh dɑbɑʔ mɪn jɑmɑʔ.', 'romanized': 'w\'kle\'leh ʿal sela d\'yama. w\'khzeli d\'siqleh daba min yama.'},
    "ܠܵܐ ܡܗܲܝܡܢܸܬ ܠܚܲܒܪ̈ܵܢܹܐ ܕܫܡܝܼܥ ܠܘܼܟ݂": {'ipa': 'lɑʔ mhajmnɪt lḥabrɑneʔ dʃmiʕ lux', 'natural_ipa': 'lɑʔ mhajmnɪt lḥabrɑneʔ dʃmɪʕ lux', 'romanized': 'la mhaymnit l\'khabrane d\'shmiʿ lukh'},
    "ܠܵܐ ܟܹܐ ܝܵܕ݂ܥܹܢ ܚܲܒܪ̈ܵܢܹܐ ܕܗ̇ܝ ܙܡܵܪܬܵܐ": {'ipa': 'lɑʔ keʔ jɑðʕen ḥabrɑneʔ dʔɑjɑ zmɑrtɑʔ', 'natural_ipa': 'lɑʔ keʔ jɑðʕen ḥabrɑneʔ dʔɑjɑ zmɑrtɑ', 'romanized': 'la ke yadhʿen khabrane d\'aya zmarta'},
    "ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܠܵܗ̇": {'ipa': 'batˤɑriθɑʔ hɪʃ mlɑjɑʔ ilɑh', 'natural_ipa': 'batˤɑrɪθɑʔ hɪʃ mlɑjɑʔ ɪlɑh', 'romanized': 'baṭaritha hish mlaya ilah'},
    "ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܠܗ̇": {'ipa': 'batˤɑriθɑʔ hɪʃ mlɑjɑʔ ilɑh', 'natural_ipa': 'batˤɑrɪθɑʔ hɪʃ mlɑjɑʔ ɪlɑh', 'romanized': 'baṭaritha hish mlaya ilah'},
    "ܠܹܐ ܝܠܹܗ ܒܸܡܨܵܝܵܐ ܢܵܦܹܫ!": {'ipa': 'leʔ ileh bɪmsˤɑjɑʔ nɑpeʃ!', 'natural_ipa': 'leʔ ɪleh bɪmsˤɑjɑʔ nɑpeʃ!', 'romanized': 'le ileh bimṣaya napesh!'},
    "ܫܘܼܐܵܠܵܐ ܡܸܨܝܵܐ ܝܠܹܗ؟": {'ipa': 'ʃuʔɑlɑʔ mɪsˤjɑʔ ileh?', 'natural_ipa': 'ʃuʔɑlɑʔ mɪsˤjɑʔ ɪleh?', 'romanized': 'shu\'ala miṣya ileh?'}
}

ipa_error_count = 0
romanized_error_count = 0
natipa_error_count = 0

debug_print = True
test = 0

for case in test_cases.keys():
    test += 1
    if debug_print:
        print(f'-------- Test {test} --------')
        print(f'Test: {case}')

    transliteration = s.transliterate(case)
    
    if transliteration['ipa'] != test_cases[case]['ipa']:
        print(f"Test failed for ipa: {case}. Expected: {test_cases[case]['ipa']}, got: {transliteration['ipa']}")
        ipa_error_count += 1
    elif debug_print:
        print(f"IPA Result: {transliteration['ipa']}")

    if transliteration['natural_ipa'] != test_cases[case]['natural_ipa']:
        print(f"Test failed for natural IPA: {case}. Expected: {test_cases[case]['natural_ipa']}, got: {transliteration['natural_ipa']}")
        natipa_error_count += 1
    elif debug_print:
        print(f"Natural IPA Result: {transliteration['natural_ipa']}")

    revipa = s.reverse_transliterate(transliteration['ipa'])
    if revipa != case and ('ipa2syr' in test_cases[case].keys() and test_cases[case]['ipa2syr'] != revipa):
        if 'ipa2syr' in test_cases[case].keys():
            print(f'Reverse IPA Failed: got: {revipa}, expected: {test_cases[case]['ipa2syr']}')
        else:
            print(f'Reverse IPA Failed: got: {revipa}, expected: {case}')
    elif debug_print:
        print(f'Reverse IPA Result: {revipa}')

    if transliteration['romanized'] != test_cases[case]['romanized']:
        print(f"Test failed for romanized: {case}. Expected: {test_cases[case]['romanized']}, got: {transliteration['romanized']}")
        romanized_error_count += 1
    elif debug_print:
        print(f"Romanized: {transliteration['romanized']}")

if debug_print:
    print(f'-----------------------------')

print(f"IPA errors: {ipa_error_count}, romanized errors: {romanized_error_count}, natipa_error_count: {natipa_error_count}")
print(f'Error rate: {((ipa_error_count + romanized_error_count + natipa_error_count) / (3 * len(test_cases))) * 100}%')



# TODO:
# - put talqana over [X] in IPA->Syr