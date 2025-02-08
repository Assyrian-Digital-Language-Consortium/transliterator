"""
' @file SyrTools.py
'
' @author The Assyrian Digital Language Consortium  
' @date 1 Feb 2025
'
' @brief Tools for handling Syriac text
'
' @description: This file contains the Syr class which is used 
'               to as a base clase utility for working with Syriac 
'               text.
'
' @license MIT License
' @copyright Assyrian Digital Language Consortium  
"""


class SyrTools:
    def __init__(self):
        # --------------------------------------------------------------------------
        # 1) Punctuation and Special Marks
        # --------------------------------------------------------------------------
        self.END_OF_PARAGRAPH = "\u0700"  # ܀
        self.SUPRALINEAR_FULL_STOP = "\u0701"  # ܁
        self.SUBLINEAR_FULL_STOP = "\u0702"  # ܂
        self.SUPRALINEAR_COLON = "\u0703"  # ܃
        self.SUBLINEAR_COLON = "\u0704"  # ܄
        self.HORIZONTAL_COLON = "\u0705"  # ܅
        self.COLON_SKEWED_LEFT = "\u0706"  # ܆
        self.COLON_SKEWED_RIGHT = "\u0707"  # ܇
        self.SUPRALINEAR_COLON_SKEWED_LEFT = "\u0708"  # ܈
        self.SUBLINEAR_COLON_SKEWED_RIGHT = "\u0709"  # ܉
        self.CONTRACTION = "\u070A"  # ܊
        self.HARKLEAN_OBELUS = "\u070B"  # ܋
        self.HARKLEAN_METOBELUS = "\u070C"  # ܌
        self.HARKLEAN_ASTERISCUS = "\u070D"  # ܍
        self.ABBREVIATION_MARK = "\u070F"  # ܏
        self.BARREKH = "\u074A"  # ݊
        self.MUSIC = "\u0749"  # ݉

        # --------------------------------------------------------------------------
        # 2) Letters
        # --------------------------------------------------------------------------
        self.LETTER_ALAPH = "\u0710"  # ܐ
        self.LETTER_SUPERSCRIPT_ALAPH = "\u0711"  # ܑ
        self.LETTER_BETH = "\u0712"  # ܒ
        self.LETTER_GAMAL = "\u0713"  # ܓ
        self.LETTER_GAMAL_GARSHUNI = "\u0714"  # ܔ
        self.LETTER_DALATH = "\u0715"  # ܕ
        self.LETTER_DOTLESS_DALATH_RISH = "\u0716"  # ܖ
        self.LETTER_HE = "\u0717"  # ܗ
        self.LETTER_WAW = "\u0718"  # ܘ
        self.LETTER_ZAIN = "\u0719"  # ܙ
        self.LETTER_HETH = "\u071A"  # ܚ
        self.LETTER_TETH = "\u071B"  # ܛ
        self.LETTER_TETH_GARSHUNI = "\u071C"  # ܜ
        self.LETTER_YUDH = "\u071D"  # ܝ
        self.LETTER_YUDH_HE = "\u071E"  # ܞ
        self.LETTER_KAPH = "\u071F"  # ܟ
        self.LETTER_LAMADH = "\u0720"  # ܠ
        self.LETTER_MIM = "\u0721"  # ܡ
        self.LETTER_NUN = "\u0722"  # ܢ
        self.LETTER_SEMKATH = "\u0723"  # ܣ
        self.LETTER_FINAL_SEMKATH = "\u0724"  # ܤ
        self.LETTER_E = "\u0725"  # ܥ (ʿAyn - Unicode name is "Letter E")
        self.LETTER_PE = "\u0726"  # ܦ
        self.LETTER_REVERSED_PE = "\u0727"  # ܧ
        self.LETTER_SADHE = "\u0728"  # ܨ
        self.LETTER_QAPH = "\u0729"  # ܩ
        self.LETTER_RISH = "\u072A"  # ܪ
        self.LETTER_SHIN = "\u072B"  # ܫ
        self.LETTER_TAW = "\u072C"  # ܬ

        # --------------------------------------------------------------------------
        # 3) Garshuni (Persian and Sogdian) Letters
        # --------------------------------------------------------------------------
        self.LETTER_PERSIAN_BHETH = "\u072D"  # ܭ
        self.LETTER_PERSIAN_GHAMAL = "\u072E"  # ܮ
        self.LETTER_PERSIAN_DHALATH = "\u072F"  # ܯ
        self.LETTER_SOGDIAN_ZHAIN = "\u074D"  # ݍ
        self.LETTER_SOGDIAN_KHAPH = "\u074E"  # ݎ
        self.LETTER_SOGDIAN_FE = "\u074F"  # ݏ

        # --------------------------------------------------------------------------
        # 4) Vowel Marks (Zlameh, Ptakheh, Rwasa, Esasa, Hbasa, Zqapa, Rwakha)
        # --------------------------------------------------------------------------

        self.PTHAHA_DOTTED = "\u0732"  # ܲ
        self.ZQAPHA_DOTTED = "\u0735"  # ܵ
        self.DOTTED_ZLAMA_HORIZONTAL = "\u0738"  # ܸ
        self.DOTTED_ZLAMA_ANGULAR = "\u0739"  # ܹ

        self.HBASA_ESASA_DOTTED = "\u073C"  # ܼ
        self.RWAHA = "\u073F"  # ܿ

        self.PTHAHA_ABOVE = "\u0730"  # ܰ
        self.PTHAHA_BELOW = "\u0731"  # ܱ
        self.ZQAPHA_ABOVE = "\u0733"  # ܳ
        self.ZQAPHA_BELOW = "\u0734"  # ܴ
        self.RBASA_ABOVE = "\u0736"  # ܶ
        self.RBASA_BELOW = "\u0737"  # ܷ
        self.HBASA_ABOVE = "\u073A"  # ܺ
        self.HBASA_BELOW = "\u073B"  # ܻ
        self.ESASA_ABOVE = "\u073D"  # ܽ
        self.ESASA_BELOW = "\u073E"  # ܾ

        # --------------------------------------------------------------------------
        # 5) Other Diacritical/Grammatical Marks
        # --------------------------------------------------------------------------
        self.QUSHSHAYA = "\u0741"  # ݁
        self.RUKKAKHA = "\u0742"  # ݂
        self.TWO_VERTICAL_DOTS_ABOVE = "\u0743"  # ݃
        self.TWO_VERTICAL_DOTS_BELOW = "\u0744"  # ݄
        self.THREE_DOTS_ABOVE = "\u0745"  # ݅
        self.THREE_DOTS_BELOW = "\u0746"  # ݆
        self.OBLIQUE_LINE_ABOVE = "\u0747"  # ݇
        self.OBLIQUE_LINE_BELOW = "\u0748"  # ݈
        # (self.BARREKH and self.MUSIC are defined above under punctuation)

        # --------------------------------------------------------------------------
        # 6) Generic Combining Diacritical Marks (non-Syriac block)
        # --------------------------------------------------------------------------
        self.COMBINING_TILDE_BELOW = "\u0330"  #  ̰ (U+0330)
        self.COMBINING_TILDE_ABOVE = "\u0303"  #  ̃ (U+0303)
        self.COMBINING_MACRON_BELOW = "\u0331"  #  ̱ (U+0331)
        self.COMBINING_MACRON = "\u0304"  #  ̄ (U+0304)
        self.COMBINING_BREVE_BELOW = "\u032E"  #  ̮ (U+032E)
        self.COMBINING_DIAERESIS = "\u0308"  #  ̈ (U+0308)
        self.COMBINING_DIAERESIS_BELOW = "\u0324"  #  ̈ (U+0324)
        self.COMBINING_DOT_BELOW = "\u0323"  #  ̣ (U+0323)
        self.COMBINING_DOT_ABOVE = "\u0307"  #  ̇ (U+0307)

        # --------------------------------------------------------------------------
        # 7) Decorative Characters (non-Syriac block)
        # --------------------------------------------------------------------------
        self.KASHIDA = "\u0640"  # ـ (U+0640)

        # --------------------------------------------------------------------------
        # 8) Useful sets for easy reference
        # --------------------------------------------------------------------------
        self.LETTER = (
            self.LETTER_ALAPH,
            self.LETTER_SUPERSCRIPT_ALAPH,
            self.LETTER_BETH,
            self.LETTER_GAMAL,
            self.LETTER_GAMAL_GARSHUNI,
            self.LETTER_DALATH,
            self.LETTER_DOTLESS_DALATH_RISH,
            self.LETTER_HE,
            self.LETTER_WAW,
            self.LETTER_ZAIN,
            self.LETTER_HETH,
            self.LETTER_TETH,
            self.LETTER_TETH_GARSHUNI,
            self.LETTER_YUDH,
            self.LETTER_YUDH_HE,
            self.LETTER_KAPH,
            self.LETTER_LAMADH,
            self.LETTER_MIM,
            self.LETTER_NUN,
            self.LETTER_SEMKATH,
            self.LETTER_FINAL_SEMKATH,
            self.LETTER_E,
            self.LETTER_PE,
            self.LETTER_REVERSED_PE,
            self.LETTER_SADHE,
            self.LETTER_QAPH,
            self.LETTER_RISH,
            self.LETTER_SHIN,
            self.LETTER_TAW,
        )

        self.VOWEL = (
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.PTHAHA_DOTTED,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.ZQAPHA_DOTTED,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.HBASA_ESASA_DOTTED,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
            self.RWAHA,
        )

        self.EASTERN_VOWELS = (
            self.PTHAHA_DOTTED,
            self.ZQAPHA_DOTTED,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
        )

        self.WESTERN_VOWELS = (
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
        )

        self.NON_MATIS_VOWEL = (
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.PTHAHA_DOTTED,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.ZQAPHA_DOTTED,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
        )

        self.MATIS_VOWEL = (
            self.HBASA_ESASA_DOTTED,
            self.RWAHA,
        )

        self.MAJLEANEH = (
            self.COMBINING_TILDE_BELOW,
            self.COMBINING_TILDE_ABOVE,
        )

        self.RUKAKHEH = (
            self.COMBINING_BREVE_BELOW,
            self.RUKKAKHA,
        )

        self.QUSHAYEH = (self.QUSHSHAYA,)

        self.BDOL_LETTERS = (
            self.LETTER_BETH,
            self.LETTER_DALATH,
            self.LETTER_WAW,
            self.LETTER_LAMADH,
        )

        self.TALQANEH = (
            self.COMBINING_MACRON_BELOW,
            self.COMBINING_MACRON,
            self.OBLIQUE_LINE_ABOVE,
            self.OBLIQUE_LINE_BELOW,
        )

        self.PUNCTUATION = (
            self.END_OF_PARAGRAPH,
            self.SUPRALINEAR_FULL_STOP,
            self.SUBLINEAR_FULL_STOP,
            self.SUPRALINEAR_COLON,
            self.SUBLINEAR_COLON,
            self.HORIZONTAL_COLON,
            self.COLON_SKEWED_LEFT,
            self.COLON_SKEWED_RIGHT,
            self.SUPRALINEAR_COLON_SKEWED_LEFT,
            self.SUBLINEAR_COLON_SKEWED_RIGHT,
            self.CONTRACTION,
            self.HARKLEAN_OBELUS,
            self.HARKLEAN_METOBELUS,
            self.HARKLEAN_ASTERISCUS,
            self.BARREKH,
            ".",
            ",",
            "!",
            "?",
            ";",
            ":",
            "،",
            "؛",
            "؟",
        )

        self.QANUNEH = (
            self.COMBINING_DOT_BELOW,
            self.COMBINING_DOT_ABOVE,
        )

        self.SIYAMEH = (
            self.COMBINING_DIAERESIS,
            self.COMBINING_DIAERESIS_BELOW,
        )

        self.GARSHUNI = (
            self.LETTER_PERSIAN_BHETH,
            self.LETTER_PERSIAN_GHAMAL,
            self.LETTER_PERSIAN_DHALATH,
            self.LETTER_SOGDIAN_ZHAIN,
            self.LETTER_SOGDIAN_KHAPH,
            self.LETTER_SOGDIAN_FE,
        )

        self.DIACRITICS = (
            self.QUSHSHAYA,
            self.RUKKAKHA,
            self.COMBINING_TILDE_BELOW,
            self.COMBINING_TILDE_ABOVE,
            self.COMBINING_MACRON_BELOW,
            self.COMBINING_MACRON,
            self.COMBINING_BREVE_BELOW,
            self.COMBINING_DIAERESIS,
            self.COMBINING_DOT_BELOW,
            self.COMBINING_DOT_ABOVE,
            self.OBLIQUE_LINE_ABOVE,
            self.OBLIQUE_LINE_BELOW,
            self.PTHAHA_DOTTED,
            self.ZQAPHA_DOTTED,
            self.HBASA_ESASA_DOTTED,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
            self.RWAHA,
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
        )

        self.DECORATIVE = (self.KASHIDA,)

        self.rukakheh_qushayeh_ipa_map = {
            "ܒ݂": "v",
            "ܓ݂": "ɣ",
            "ܕ݂": "ð",
            "ܟ݂": "x",
            "ܦ݂": "f",
            "ܦ̮": "f",
            "ܬ݂": "θ",
            "ܒ݁": "ܒ",
            "ܓ݁": "g",
            "ܕ݁": "d",
            "ܟ݁": "k",
            "ܦ݁": "p",
            "ܬ݁": "t",
        }

        self.majleaneh_ipa_map = {
            "ܓ̰": "ʤ",
            "ܙ̰": "ʒ",
            "ܙ̃": "ʒ",
            "ܟ̰": "tʃ",
            "ܟ̃": "tʃ",
            "ܫ̃": "ʒ",
            "ܫ̰": "ʒ",
        }

        self.mater_lectionis_ipa_map = {
            "ܘܼ": "u",
            "ܘܿ": "o",
            "ܝܼ": "i",
        }

        self.consonant_ipa_map = {
            "ܐ": "ʔ",
            self.LETTER_SUPERSCRIPT_ALAPH: "ʔ",
            "ܒ": "b",
            "ܓ": "g",
            "ܔ": "ʤ",
            "ܕ": "d",
            "ܗ": "h",
            "ܘ": "w",
            "ܙ": "z",
            "ܚ": "ḥ",
            "ܛ": "tˤ",
            "ܝ": "j",
            "ܟ": "k",
            "ܠ": "l",
            "ܡ": "m",
            "ܢ": "n",
            "ܣ": "s",
            self.LETTER_FINAL_SEMKATH: "s",
            "ܥ": "ʕ",
            "ܦ": "p",
            "ܨ": "sˤ",
            "ܩ": "q",
            "ܪ": "r",
            "ܖ̈": "r",
            "ܫ": "ʃ",
            "ܬ": "t",
        }

        self.eastern_vowel_ipa_map = {
            self.PTHAHA_DOTTED: "a",
            self.ZQAPHA_DOTTED: "ɑ",
            self.DOTTED_ZLAMA_HORIZONTAL: "ɪ",
            self.DOTTED_ZLAMA_ANGULAR: "e",
        }

        self.western_vowel_ipa_map = {
            self.PTHAHA_ABOVE: "a",
            self.PTHAHA_BELOW: "a",
            self.ZQAPHA_ABOVE: "o",
            self.ZQAPHA_BELOW: "o",
            self.RBASA_ABOVE: "e",
            self.RBASA_BELOW: "e",
            self.HBASA_ABOVE: "ɪ",
            self.HBASA_BELOW: "ɪ",
            self.ESASA_ABOVE: "u",
            self.ESASA_BELOW: "u",
        }

    """
    This function removes all diacritics from the given text.
    """

    def remove_diacritics(self, text):
        return "".join([c for c in text if c in self.LETTER])

    """
    This function returns true if the given text contains any Syriac characters.
    """

    def isSyr(self, text):
        for c in text:
            if c in self.LETTER:
                return True
        return False

    """
    This function returns true if Eastern Assyrian is detected.
    """

    def eastern(self, text):
        if not self.isSyr(text):
            return False
        for c in text:
            if c in self.EASTERN_VOWELS:
                return True
        return False

    def western(self, text):
        if not self.isSyr(text):
            return False

        for c in text:
            if c in self.WESTERN_VOWELS:
                return True
        return False

    """
    This function returns true if the given text contains any Syriac vowels.
    """

    def contains_vowels(self, text):
        for c in text:
            if c in self.VOWEL:
                return True
        return False

    """
    This function returns true if the given text contains any Garshuni characters.
    """

    def contains_garshuni(self, text):
        for c in text:
            if c in self.GARSHUNI:
                return True
        return False

    """
    This function returns true if the given text contains any non-vowel diacritics.
    """

    def contains_non_vowel_diacritics(self, text):
        for c in text:
            if c in self.NON_VOWEL_DIACRITICS:
                return True
        return False
