import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../src/')

from Syr import Syr

s = Syr()

test_cases = {
    "ܐܲܒܵܐ": {'latin': 'abā', 'phonetic': 'aba'},

    # Matis Lectionis
    "ܐܝܼܕܵܐ": {'latin': 'īdā' , 'phonetic': 'eeda'},
    "ܐܘܼܪܚܵܐ": {'latin': 'ūrḥā' , 'phonetic': 'urkha'},
    "ܐܘܼܪ": {'latin': 'ūr' , 'phonetic': 'ur'},
    "ܐܝܼܡܵܡܵܐ": {'latin': 'īmāmā' , 'phonetic': 'eemama'},
    "ܐܘܿܫܲܥܢܵܐ": {'latin': 'ošaʿnā' , 'phonetic': 'osha`na'},
    
    # Yodh + Khwasa
    "ܣܲܪܓܝܼܣ": {'latin': 'sargis' , 'phonetic': 'sargis'},
    "ܥܝܼܪܵܩ": {'latin': 'ʿīrāq' , 'phonetic': '`eeraq'},
    "ܐܝܼܪܵܢ": {'latin': 'īrān' , 'phonetic': 'eeran'},

    # BDOLs
    "ܒܫܸܡܵܐ": {'latin': 'b\'šimā' , 'phonetic': 'b\'shima'}, # BDOL
    "ܠܘܼܚܵܐ": {'latin': 'lūḥā' , 'phonetic': 'lukha'}, # not BDOL
    "ܘܲܪܕܵܐ": {'latin': 'wardā' , 'phonetic': 'warda'}, # not BDOL
    "ܟܬܵܒ݂ܵܐ ܕܝܘܼܐܝܼܠ": {'latin': 'ktāḇā d\'yūʾil' , 'phonetic': 'ktawa d\'yu\'il'}, # not BDOL

    # Single letters
    "ܐܵ": {'latin': 'ā', 'phonetic': 'a'},
    "ܐܲ": {'latin': 'a', 'phonetic': 'a'},
    "ܐܹ": {'latin': 'ē', 'phonetic': 'eh'},
    "ܐܸ": {'latin': 'i', 'phonetic': 'i'},

    ## Resh
    "ܣܘܼܖ̈ܵܝܹܐ": {'latin': 'sūrāyē', 'phonetic': 'surayeh'}, # with dot-less resh + siyameh
    "ܣܘܼܪ̈ܵܝܹܐ": {'latin': 'sūrāyē', 'phonetic': 'surayeh'}, # with resh + siyameh
    "ܣܘܼܪܵܝܹܐ": {'latin': 'sūrāyē', 'phonetic': 'surayeh'}, # no siyameh

    ## Sentences with lots of features
    "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ": {'latin': 'b\'ṣaprā kē kāṯḇēn igrāṯā', 'phonetic': 'b\'ṣapra keh kathwehn igratha'},
    "ܝܵܠܘܿܦܵܐ ܟܬ݂ܝܼܒ݂ ܠܹܗ ܡܹܐܡܲܪܬܵܐ": {'latin': 'yālopā kṯiḇ lēh mēʾmartā', 'phonetic': 'yalopa kthiw leh meh\'marta'},
    "ܘܟܠܹܐܠܹܗ ܥܲܠ ܣܹܠܵܐ ܕܝܵܡܵܐ. ܘܚܙܹܠܝܼ ܕܐ݇ܣܸܩܠܹܗ ܕܵܒܵܐ ܡ̣ܢ ܝܵܡܵܐ.": {'latin': 'w\'klēʾlēh ʿal sēlā d\'yāmā. w\'ḥzēli d\'siqlēh dābā min yāmā.', 'phonetic': 'w\'kleh\'leh `al sehla d\'yama. w\'khzehli d\'siqleh daba min yama.'},
}

latin_error_count = 0
phonetic_error_count = 0

for case in test_cases.keys():
    transliteration = s.transliterate(case)

    # print(f"Transliteration for {case}: {transliteration}")
    
    if transliteration['latin'] != test_cases[case]['latin']:
        print(f"Test failed for latin: {case}. Expected: {test_cases[case]['latin']}, got: {transliteration['latin']}")
        latin_error_count += 1
    
    if transliteration['phonetic'] != test_cases[case]['phonetic']:
        print(f"Test failed for phonetic: {case}. Expected: {test_cases[case]['phonetic']}, got: {transliteration['phonetic']}")
        phonetic_error_count += 1

print(f"Latin errors: {latin_error_count}, Phonetic errors: {phonetic_error_count}")
print(f'Error rate: {((latin_error_count + phonetic_error_count) / (2 * len(test_cases))) * 100}%')