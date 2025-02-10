import sys
import os
import pytest

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f'{script_dir}/../src/')

from SyrTools import SyrTools

s = SyrTools()

test_cases = {
    "ܐܲܒܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},

    # # Matis Lectionis
    "ܐܝܼܕܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܘܼܪܚܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܘܼܪ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܝܼܡܵܡܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܘܿܫܲܥܢܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    
    # # Yodh + Khwasa
    "ܣܲܪܓܝܼܣ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܓܝܼܘܵܪܓܝܼܣ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܥܝܼܪܵܩ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܝܼܪܵܢ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},

    # # BDOLs
    "ܒܫܸܡܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܠܘܼܚܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܘܲܪܕܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܟܬܵܒ݂ܵܐ ܕܝܘܼܐܝܼܠ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},

    # # Single letters
    "ܐܵ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܲ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܹ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܐܸ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},

    # ## Resh
    "ܣܘܼܖ̈ܵܝܹܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܣܘܼܪ̈ܵܝܹܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܣܘܼܪܵܝܹܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},

    # ## Sentences with lots of features
    "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܝܵܠܘܿܦܵܐ ܟܬ݂ܝܼܒ݂ ܠܹܗ ܡܹܐܡܲܪܬܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܘܟܠܹܐܠܹܗ ܥܲܠ ܣܹܠܵܐ ܕܝܵܡܵܐ. ܘܚܙܹܠܝܼ ܕܐ݇ܣܸܩܠܹܗ ܕܵܒܵܐ ܡ̣ܢ ܝܵܡܵܐ.": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܠܵܐ ܡܗܲܝܡܢܸܬ ܠܚܲܒܪ̈ܵܢܹܐ ܕܫܡܝܼܥ ܠܘܼܟ݂": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܠܵܐ ܟܹܐ ܝܵܕ݂ܥܹܢ ܚܲܒܪ̈ܵܢܹܐ ܕܗ̇ܝ ܙܡܵܪܬܵܐ": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܠܵܗ̇": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܒܲܛܵܪܝܼܬ݂ܵܐ ܗܸܫ ܡܠܵܝܵܐ ܝܠܗ̇": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܠܹܐ ܝܠܹܗ ܒܸܡܨܵܝܵܐ ܢܵܦܹܫ!": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
    "ܫܘܼܐܵܠܵܐ ܡܸܨܝܵܐ ܝܠܹܗ؟": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},

    "ܫܠܵܡܵܐ! Welcome!": {'containsSyr': True, 'isSyr': False, 'ratio': 0.5625},
    "Welcome!": {'containsSyr': False, 'isSyr': False, 'ratio': 0.0},
    "!!!!!!!": {'containsSyr': False, 'isSyr': False, 'ratio': 0.0},
    "!!!ܐ!!!": {'containsSyr': True, 'isSyr': True, 'ratio': 1.0},
}

@pytest.mark.parametrize("syriac_text,expected", list(test_cases.items()))
def test_isSyr(syriac_text, expected):
    """
    Tests that the isSyr() and constainsSyr() methods of SyrTools produce 
    the expected results.
    """

    # isSyr
    isSyrRes = s.isSyr(syriac_text)
    assert isSyrRes == expected['isSyr'], (
        f"\n[isSyr() Failed]\n"
        f"Text: {syriac_text}\n"
        f"Expected: {expected['isSyr']}\n"
        f"Got:      {isSyrRes}"
    )

    # constainsSyr
    constainsSyrRes = s.containsSyr(syriac_text)
    assert constainsSyrRes == expected['containsSyr'], (
        f"\n[containsSyr() Failed]\n"
        f"Text: {syriac_text}\n"
        f"Expected: {expected['containsSyr']}\n"
        f"Got:      {constainsSyrRes}"
    )

    # ratio
    ratio = s.ratio(syriac_text)
    assert ratio == expected['ratio'], (
        f"\n[containsSyr() Failed]\n"
        f"Text: {syriac_text}\n"
        f"Expected: {expected['ratio']}\n"
        f"Got:      {ratio}"
    )