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

import unicodedata
from typing import Dict, List, Tuple

class SyrTools:
    """
    A class providing various utilities and mappings for
    processing Syriac text.
    """

    def __init__(self) -> None:
        """
        Initialize the SyrTools class with constants for Syriac punctuation,
        letters, vowels, diacritics, and various mappings.
        """
        self.SYR_BLOCK_START: int = 0x0700
        self.SYR_BLOCK_END: int = 0x074F

        # ---------------------------------------------------------------------
        # 1) Punctuation and Special Marks
        # ---------------------------------------------------------------------
        self.END_OF_PARAGRAPH: str = "\u0700"  # ܀
        self.SUPRALINEAR_FULL_STOP: str = "\u0701"  # ܁
        self.SUBLINEAR_FULL_STOP: str = "\u0702"  # ܂
        self.SUPRALINEAR_COLON: str = "\u0703"  # ܃
        self.SUBLINEAR_COLON: str = "\u0704"  # ܄
        self.HORIZONTAL_COLON: str = "\u0705"  # ܅
        self.COLON_SKEWED_LEFT: str = "\u0706"  # ܆
        self.COLON_SKEWED_RIGHT: str = "\u0707"  # ܇
        self.SUPRALINEAR_COLON_SKEWED_LEFT: str = "\u0708"  # ܈
        self.SUBLINEAR_COLON_SKEWED_RIGHT: str = "\u0709"  # ܉
        self.CONTRACTION: str = "\u070a"  # ܊
        self.HARKLEAN_OBELUS: str = "\u070b"  # ܋
        self.HARKLEAN_METOBELUS: str = "\u070c"  # ܌
        self.HARKLEAN_ASTERISCUS: str = "\u070d"  # ܍
        self.ABBREVIATION_MARK: str = "\u070f"  # ܏
        self.BARREKH: str = "\u074a"  # ݊
        self.MUSIC: str = "\u0749"  # ݉

        # ---------------------------------------------------------------------
        # 2) Letters
        # ---------------------------------------------------------------------
        self.LETTER_ALAPH: str = "\u0710"  # ܐ
        self.LETTER_SUPERSCRIPT_ALAPH: str = "\u0711"  # ܑ
        self.LETTER_BETH: str = "\u0712"  # ܒ
        self.LETTER_GAMAL: str = "\u0713"  # ܓ
        self.LETTER_GAMAL_GARSHUNI: str = "\u0714"  # ܔ
        self.LETTER_DALATH: str = "\u0715"  # ܕ
        self.LETTER_DOTLESS_DALATH_RISH: str = "\u0716"  # ܖ
        self.LETTER_HE: str = "\u0717"  # ܗ
        self.LETTER_WAW: str = "\u0718"  # ܘ
        self.LETTER_ZAIN: str = "\u0719"  # ܙ
        self.LETTER_HETH: str = "\u071a"  # ܚ
        self.LETTER_TETH: str = "\u071b"  # ܛ
        self.LETTER_TETH_GARSHUNI: str = "\u071c"  # ܜ
        self.LETTER_YUDH: str = "\u071d"  # ܝ
        self.LETTER_YUDH_HE: str = "\u071e"  # ܞ
        self.LETTER_KAPH: str = "\u071f"  # ܟ
        self.LETTER_LAMADH: str = "\u0720"  # ܠ
        self.LETTER_MIM: str = "\u0721"  # ܡ
        self.LETTER_NUN: str = "\u0722"  # ܢ
        self.LETTER_SEMKATH: str = "\u0723"  # ܣ
        self.LETTER_FINAL_SEMKATH: str = "\u0724"  # ܤ
        self.LETTER_E: str = "\u0725"  # ܥ (ʿAyn - Unicode name is "Letter E")
        self.LETTER_PE: str = "\u0726"  # ܦ
        self.LETTER_REVERSED_PE: str = "\u0727"  # ܧ
        self.LETTER_SADHE: str = "\u0728"  # ܨ
        self.LETTER_QAPH: str = "\u0729"  # ܩ
        self.LETTER_RISH: str = "\u072a"  # ܪ
        self.LETTER_SHIN: str = "\u072b"  # ܫ
        self.LETTER_TAW: str = "\u072c"  # ܬ

        # ---------------------------------------------------------------------
        # 3) Garshuni (Persian and Sogdian) Letters
        # ---------------------------------------------------------------------
        self.LETTER_PERSIAN_BHETH: str = "\u072d"  # ܭ
        self.LETTER_PERSIAN_GHAMAL: str = "\u072e"  # ܮ
        self.LETTER_PERSIAN_DHALATH: str = "\u072f"  # ܯ
        self.LETTER_SOGDIAN_ZHAIN: str = "\u074d"  # ݍ
        self.LETTER_SOGDIAN_KHAPH: str = "\u074e"  # ݎ
        self.LETTER_SOGDIAN_FE: str = "\u074f"  # ݏ

        # ---------------------------------------------------------------------
        # 4) Vowel Marks (Zlameh, Ptakheh, Rwasa, Esasa, Hbasa, Zqapa, Rwakha)
        # ---------------------------------------------------------------------
        self.PTHAHA_DOTTED: str = "\u0732"  # ܲ
        self.ZQAPHA_DOTTED: str = "\u0735"  # ܵ
        self.DOTTED_ZLAMA_HORIZONTAL: str = "\u0738"  # ܸ
        self.DOTTED_ZLAMA_ANGULAR: str = "\u0739"  # ܹ

        self.HBASA_ESASA_DOTTED: str = "\u073c"  # ܼ
        self.RWAHA: str = "\u073f"  # ܿ

        self.PTHAHA_ABOVE: str = "\u0730"  # ܰ
        self.PTHAHA_BELOW: str = "\u0731"  # ܱ
        self.ZQAPHA_ABOVE: str = "\u0733"  # ܳ
        self.ZQAPHA_BELOW: str = "\u0734"  # ܴ
        self.RBASA_ABOVE: str = "\u0736"  # ܶ
        self.RBASA_BELOW: str = "\u0737"  # ܷ
        self.HBASA_ABOVE: str = "\u073a"  # ܺ
        self.HBASA_BELOW: str = "\u073b"  # ܻ
        self.ESASA_ABOVE: str = "\u073d"  # ܽ
        self.ESASA_BELOW: str = "\u073e"  # ܾ

        # ---------------------------------------------------------------------
        # 5) Other Diacritical/Grammatical Marks
        # ---------------------------------------------------------------------
        self.QUSHSHAYA: str = "\u0741"  # ݁
        self.RUKKAKHA: str = "\u0742"  # ݂
        self.TWO_VERTICAL_DOTS_ABOVE: str = "\u0743"  # ݃
        self.TWO_VERTICAL_DOTS_BELOW: str = "\u0744"  # ݄
        self.THREE_DOTS_ABOVE: str = "\u0745"  # ݅
        self.THREE_DOTS_BELOW: str = "\u0746"  # ݆
        self.OBLIQUE_LINE_ABOVE: str = "\u0747"  # ݇
        self.OBLIQUE_LINE_BELOW: str = "\u0748"  # ݈
        # (BARREKH and MUSIC are defined above under punctuation)

        # ---------------------------------------------------------------------
        # 6) Generic Combining Diacritical Marks (non-Syriac block)
        # ---------------------------------------------------------------------
        self.COMBINING_TILDE_BELOW: str = "\u0330"  # (U+0330)  ̰
        self.COMBINING_TILDE_ABOVE: str = "\u0303"  # (U+0303)  ̃
        self.COMBINING_MACRON_BELOW: str = "\u0331"  # (U+0331) ̱
        self.COMBINING_MACRON: str = "\u0304"  # (U+0304) ̄
        self.COMBINING_BREVE_BELOW: str = "\u032e"  # (U+032E)  ̮
        self.COMBINING_DIAERESIS: str = "\u0308"  # (U+0308) ̈
        self.COMBINING_DIAERESIS_BELOW: str = "\u0324"  # (U+0324)  ̈
        self.COMBINING_DOT_BELOW: str = "\u0323"  # (U+0323)  ̣
        self.COMBINING_DOT_ABOVE: str = "\u0307"  # (U+0307) ̇

        # ---------------------------------------------------------------------
        # 7) Decorative Characters (non-Syriac block)
        # ---------------------------------------------------------------------
        self.KASHIDA: str = "\u0640"  # ـ (U+0640)

        # ---------------------------------------------------------------------
        # 8) Useful sets for easy reference
        # ---------------------------------------------------------------------
        self.LETTER: Tuple[str, ...] = (
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

        self.VOWEL: Tuple[str, ...] = (
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

        self.EASTERN_VOWELS: Tuple[str, ...] = (
            self.PTHAHA_DOTTED,
            self.ZQAPHA_DOTTED,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
        )

        self.WESTERN_VOWELS: Tuple[str, ...] = (
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

        self.NON_MATIS_VOWEL: Tuple[str, ...] = (
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

        self.MATIS_VOWEL: Tuple[str, ...] = (
            self.HBASA_ESASA_DOTTED,
            self.RWAHA,
        )

        self.MAJLEANEH: Tuple[str, ...] = (
            self.COMBINING_TILDE_BELOW,
            self.COMBINING_TILDE_ABOVE,
        )

        self.RUKAKHEH: Tuple[str, ...] = (
            self.COMBINING_BREVE_BELOW,
            self.RUKKAKHA,
        )

        self.QUSHAYEH: Tuple[str, ...] = (self.QUSHSHAYA,)

        self.BDOL_LETTERS: Tuple[str, ...] = (
            self.LETTER_BETH,
            self.LETTER_DALATH,
            self.LETTER_WAW,
            self.LETTER_LAMADH,
        )

        self.TALQANEH: Tuple[str, ...] = (
            self.COMBINING_MACRON_BELOW,
            self.COMBINING_MACRON,
            self.OBLIQUE_LINE_ABOVE,
            self.OBLIQUE_LINE_BELOW,
        )

        self.PUNCTUATION: Tuple[str, ...] = (
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
            self.HARKLEAN_OBELUS,
            self.HARKLEAN_METOBELUS,
            self.HARKLEAN_ASTERISCUS,
            self.BARREKH,
            ".",
            "!",
            ";",
            ":",
            "،",
            "؛",
            "؟",
        )

        self.QANUNEH: Tuple[str, ...] = (
            self.COMBINING_DOT_BELOW,
            self.COMBINING_DOT_ABOVE,
        )

        self.SIYAMEH: Tuple[str, ...] = (
            self.COMBINING_DIAERESIS,
            self.COMBINING_DIAERESIS_BELOW,
        )

        self.GARSHUNI: Tuple[str, ...] = (
            self.LETTER_PERSIAN_BHETH,
            self.LETTER_PERSIAN_GHAMAL,
            self.LETTER_PERSIAN_DHALATH,
            self.LETTER_SOGDIAN_ZHAIN,
            self.LETTER_SOGDIAN_KHAPH,
            self.LETTER_SOGDIAN_FE,
        )

        self.DIACRITICS: Tuple[str, ...] = (
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

        self.DECORATIVE: Tuple[str, ...] = (self.KASHIDA,)

        self.VALID_NON_CODEPOINT_SYR_CHAR: Tuple[str, ...] = (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "٠",
            "١",
            "٢",
            "٣",
            "٤",
            "٥",
            "٦",
            "٧",
            "٨",
            "٩",
            ".",
            "!",
            ";",
            ":",
            "،",
            "؛",
            "؟",
            " ",
            self.KASHIDA,
            self.COMBINING_TILDE_BELOW,
            self.COMBINING_TILDE_ABOVE,
            self.COMBINING_MACRON_BELOW,
            self.COMBINING_MACRON,
            self.COMBINING_BREVE_BELOW,
            self.COMBINING_DIAERESIS,
            self.COMBINING_DIAERESIS_BELOW,
            self.COMBINING_DOT_BELOW,
            self.COMBINING_DOT_ABOVE,
        )

        # Define NON_VOWEL_DIACRITICS as those diacritics that are not vowels.
        self.NON_VOWEL_DIACRITICS: Tuple[str, ...] = tuple(
            set(self.DIACRITICS) - set(self.VOWEL)
        )

        # ---------------------------------------------------------------------
        # Grammatical Rules
        # ---------------------------------------------------------------------

        # Possessive particle
        self.POSSESSIVE_PARTICLE: Tuple[str, ...] = (
            self.LETTER_DALATH + self.LETTER_YUDH, # ܕܝ
        )

        # Possessive suffixes 
        self.PRONOMINAL_SUFFIXES: Tuple[str, ...] = (
            # -----------------------------------------------------------------
            # Singular 
            # -----------------------------------------------------------------

            # 1st person 
            self.LETTER_YUDH, # ܝ݂ (singular masculine and feminine)

            # 2nd person
            self.LETTER_KAPH, # ܟ݂ (singular masculine)
            self.LETTER_WAW + self.LETTER_KAPH, # ܘܟ݂ (singular masculine)
            self.LETTER_KAPH + self.LETTER_YUDH, # ܟ݂ܝ (singular feminine)

            # 3rd person
            self.LETTER_HE, # ܗ (singular masculine)
            self.LETTER_HE + self.COMBINING_DOT_ABOVE, # ܗ̇ (singular feminine)

            # -----------------------------------------------------------------
            # Plural
            # -----------------------------------------------------------------

            # 1st person
            self.LETTER_NUN, # ܢ (plural)

            # 2nd person
            self.LETTER_KAPH + self.LETTER_WAW + self.LETTER_NUN, # ܟ݂ܘܢ (plural masculine)
            self.LETTER_KAPH + self.RUKKAKHA + self.LETTER_YUDH + self.LETTER_NUN, # ܟ݂ܝܢ (plural feminine)
            self.LETTER_WAW + self.LETTER_KAPH + self.LETTER_WAW + self.LETTER_NUN, # ܘܟ݂ܘܢ (plural)

            # 3rd person
            self.LETTER_WAW + self.LETTER_HE + self.LETTER_YUDH, # ܘܗܝ (plural masculine)
            self.LETTER_WAW + self.LETTER_HE, # ܘܗ̇ (plural feminine)
            self.LETTER_HE + self.LETTER_WAW + self.LETTER_NUN, # ܗܘܢ (plural masculine)
            self.LETTER_HE + self.LETTER_YUDH + self.LETTER_NUN, # ܗܝܢ (plural feminine)
            self.LETTER_YUDH, # ܝ (plural)        
        )

        # Possessive particle suffixes
        self.POSSESSIVE_PARTICLE_SUFFIXES = tuple(
            # ܕܝ +‌ ܘܟ݂ = ܕܝܘܟ݂
            str(self.POSSESSIVE_PARTICLE) + str(suffix) 
            for suffix in self.PRONOMINAL_SUFFIXES
        )

        # ---------------------------------------------------------------------
        #  Personal pronouns and to be verbs
        #      - Ordered on a 1:1 basis with one another
        # ---------------------------------------------------------------------

        # Personal pronouns (masculine)
        self.PERSONAL_PRONOUNS_MASCULINE: Tuple[str, ...] = (
            self.LETTER_ALAPH + self.LETTER_NUN + self.LETTER_ALAPH, # ܐܢܐ
            self.LETTER_ALAPH + self.LETTER_NUN + self.LETTER_TAW, # ܐܢܬ
            self.LETTER_HE + self.LETTER_WAW, # ܗ݁ܘ
        )

        # Personal pronouns (feminine)
        self.PERSONAL_PRONOUNS_FEMININE: Tuple[str, ...] = (
            self.LETTER_ALAPH + self.LETTER_NUN + self.LETTER_ALAPH, # ܐܢܐ
            self.LETTER_ALAPH + self.LETTER_NUN + self.LETTER_TAW + self.LETTER_YUDH, # ܐܢܬܝ
            self.LETTER_HE + self.LETTER_YUDH, # ܗ݁ܝ
        )

        # Personal pronouns (plural)
        self.PERSONAL_PRONOUNS_PLURAL: Tuple[str, ...] = (
            self.LETTER_ALAPH + self.LETTER_HETH + self.LETTER_NUN + self.LETTER_NUN, # ܐܚܢܢ
            self.LETTER_ALAPH + self.LETTER_HETH + self.LETTER_TAW + self.LETTER_WAW + self.LETTER_NUN, # ܐܚܬܘܢ
            self.LETTER_ALAPH + self.LETTER_NUN + self.LETTER_YUDH, # ܐܢܝ݂            
        )

        # Demonstrative pronouns
        self.DEMONSTRATIVE_PRONOUNS: Tuple[str, ...] = (
            self.LETTER_ALAPH + self.LETTER_HE + self.LETTER_ALAPH, # ܐܗܐ
            self.LETTER_ALAPH + self.LETTER_NUN + self.LETTER_ALAPH, # ܐܢܐ
            self.LETTER_HE + self.LETTER_NUN + self.LETTER_ALAPH, # ܗܢܐ
            self.LETTER_HE + self.LETTER_DALATH + self.LETTER_ALAPH, # ܗܕܐ
            self.LETTER_HE + self.LETTER_WAW, # ܗܘ
            self.LETTER_HE + self.LETTER_YUDH, # ܗܝ
            self.LETTER_HE + self.LETTER_LAMADH + self.LETTER_YUDH + self.LETTER_NUN, # ܗܠܝܢ
            self.LETTER_HE + self.LETTER_NUN + self.LETTER_WAW + self.LETTER_NUN, # ܗܢܘܢ
            self.LETTER_HE + self.LETTER_NUN + self.LETTER_YUDH + self.LETTER_NUN, # ܗܢܝܢ
        )

        self.INTERROGATIVE_PRONOUNS: Tuple[str, ...] = (
            # Who?
            self.LETTER_MIM + self.LETTER_NUN, # ܡܢ
            self.LETTER_MIM + self.LETTER_NUN + self.LETTER_YUDH, # ܡܢܝ

            # What?
            self.LETTER_MIM + self.LETTER_WAW + self.LETTER_DALATH + self.LETTER_YUDH, # ܡܘܕܝ
            self.LETTER_MIM + self.LETTER_NUN + self.LETTER_ALAPH, # ܡܢܐ
            self.LETTER_MIM + self.LETTER_ALAPH, # ܡܐ

            # Which?
            self.LETTER_ALAPH + self.LETTER_YUDH + self.LETTER_NUN + self.LETTER_ALAPH, # ܐܝܢܐ (masculine)
            self.LETTER_ALAPH + self.LETTER_YUDH + self.LETTER_DALATH + self.LETTER_ALAPH, # ܐܝܕܐ (feminine)
            self.LETTER_ALAPH + self.LETTER_YUDH + self.LETTER_LAMADH + self.LETTER_ALAPH, # ܐܝܠܝܢ (plural)

            # Where?
            # FIXME: What about derived terms such as ܡܝܟܐ،‌ܠܝܟܐ، ܡܐܝܟܐ، ܟܝܠܗ?
            self.LETTER_ALAPH + self.LETTER_YUDH + self.LETTER_KAPH + self.LETTER_ALAPH, # ܐܝܟܐ            

            # When?
            self.LETTER_ALAPH + self.LETTER_YUDH + self.LETTER_MIM + self.LETTER_NUN, # ܐܝܡܢ

            # Why?
            self.LETTER_QAPH + self.LETTER_MIM + self.LETTER_WAW + self.LETTER_DALATH + self.LETTER_YUDH, # ܩܡܘܕܝ

            # How much?
            self.LETTER_KAPH + self.LETTER_MIM + self.LETTER_ALAPH, # ܟܡܐ
        )
 
        # To be verb (masculine)
        self.VERB_TO_BE_MASCULINE: Tuple[str, ...] = (
            self.LETTER_YUDH + self.LETTER_WAW + self.LETTER_NUN, # ܝ݂ܘܢ
            self.LETTER_YUDH + self.LETTER_WAW + self.LETTER_TAW, # ܝ݂ܘܬ
            self.LETTER_YUDH + self.LETTER_LAMADH + self.LETTER_HE, # ܝ݂ܠܗ 
        )

        # To be verb (feminine)
        self.VERB_TO_BE_FEMININE: Tuple[str, ...] = (              
            self.LETTER_YUDH + self.LETTER_WAW + self.LETTER_NUN, # ܝ݂ܘܢ
            self.LETTER_YUDH + self.LETTER_WAW + self.LETTER_TAW + self.LETTER_YUDH, # ܝ݂ܘܬܝ
            self.LETTER_YUDH + self.LETTER_LAMADH + self.LETTER_HE, # ܝ݂ܠܗ̇ 
        )

        # To be verb (plural)
        self.VERB_TO_BE_PLURAL: Tuple[str, ...] = (
            self.LETTER_YUDH + self.LETTER_WAW + self.LETTER_HETH, # ܝܘܚ
            self.LETTER_YUDH + self.LETTER_TAW + self.LETTER_WAW + self.LETTER_NUN, # ܝܬܘܢ
            self.LETTER_YUDH + self.LETTER_NUN + self.LETTER_ALAPH, # ܝܢܐ 
        )

        # Compound noun prefixes (common)
        self.COMPOUND_NOUN_PREFIXES: Tuple[str, ...] = (
            self.LETTER_BETH + self.LETTER_DALATH, # ܒܕ
            self.LETTER_BETH + self.LETTER_TAW + self.LETTER_RISH, # ܒܬܪ
            self.LETTER_BETH + self.LETTER_YUDH + self.LETTER_TAW, # ܒܝܬ
            self.LETTER_MIM + self.LETTER_RISH + self.LETTER_ALAPH, # ܡܪܐ
        )

        # Feminine noun suffixes
        self.FEMININE_NOUN_SUFFIXES: Tuple[str, ...] = (
            self.LETTER_TAW + self.LETTER_ALAPH, # ܬܐ
            self.LETTER_WAW + self.LETTER_TAW + self.LETTER_ALAPH, # ܘܬܐ
        )

        # Adjective suffixes
        self.ADJECTIVE_SUFFIXES: Tuple[str, ...] = (
            self.LETTER_NUN + self.LETTER_ALAPH, # ܢܐ
            self.LETTER_NUN + self.LETTER_YUDH + self.LETTER_ALAPH, # ܢܝـܐ
            self.LETTER_YUDH + self.LETTER_ALAPH, # ܝܐ
        )

        # Prepositions
        self.PREPOSITIONS: Tuple[str, ...] = (
            # ܒܬܪ is also repeated in COMPOUND_NOUN_PREFIXES
            self.LETTER_BETH + self.LETTER_TAW + self.LETTER_RISH, # ܒܬܪ
            self.LETTER_GAMAL + self.LETTER_WAW, # ܓܘ
            self.LETTER_HE + self.LETTER_LAMADH, # ܗܠ
            self.LETTER_MIM + self.LETTER_NUN, # ܡܢ
            self.LETTER_E + self.LETTER_LAMADH, # ܥܠ
            self.LETTER_E + self.LETTER_MIM, #  ܥܡ
            self.LETTER_QAPH + self.LETTER_ALAPH, # ܩܐ
            self.LETTER_QAPH + self.LETTER_DALATH + self.LETTER_MIM, # ܩܕܡ
            self.LETTER_TAW + self.LETTER_HETH + self.LETTER_WAW + self.LETTER_TAW, # ܬܚܘܬ

            # These prepositions with pronominal suffixes can be used without the particle ܕ,
            # while the last ܐ and vowel point of the penultimate letter are omitted
            #
            # FIXME: How do we check for this using mechanistic rules? Possibly a regular
            # expression?
            # ܡܢ ܕܦܢܐ ܕ، ܚܕܪܘܢܐ ܕ، ܒܪܩܘܒܟ ܕ            
        )

        # Preposition an be joined with pronominal suffixes
        self.PREPOSITIONS_WITH_PRONOMINAL_SUFFIXES = tuple(
            str(self.PREPOSITIONS) + str(suffix)            
            for suffix in self.PRONOMINAL_SUFFIXES       
        )

         # Define prefixes
        self.PREFIXES: Tuple[str, ...] = (
            self.BDOL_LETTERS,
            self.COMPOUND_NOUN_PREFIXES,
        )

        # Define suffixes
        self.SUFFIXES: Tuple[str, ...] = (            
            self.PRONOMINAL_SUFFIXES,
            self.POSSESSIVE_PARTICLE_SUFFIXES,            
            self.FEMININE_NOUN_SUFFIXES,
            self.ADJECTIVE_SUFFIXES,
            self.LETTER_ALAPH,            
        )

        # Define the verb 'to be'
        self.VERB_TO_BE: Tuple[str, ...] = (
            self.VERB_TO_BE_FEMININE,
            self.VERB_TO_BE_MASCULINE,
            self.VERB_TO_BE_PLURAL,
        )

        # Define personal pronouns
        self.PERSONAL_PRONOUNS: Tuple[str, ...] = (
            self.PERSONAL_PRONOUNS_FEMININE,
            self.PERSONAL_PRONOUNS_MASCULINE,
            self.PERSONAL_PRONOUNS_PLURAL,
        )
    
        # The letters ܐ ܘ ܝ  are considered weak letters (ܐܵܬܘܵܬܸ̈ܐ ܟܪ̈ܝ݂ܗܸܐ) because, in some positions, 
        # they are substituted, not pronounced, or are dropped completely.
        #
        # Roots of verbs without weak letters are called ܫܲܠܡܸ̈ܐ
        self.ROOT_WEAK_LETTERS: Tuple[str, ...] = (
            self.LETTER_ALAPH,
            self.LETTER_YUDH,
            self.LETTER_WAW,
        )

    def normalize(self, text: str) -> str:
        """
        Normalize the word by removing diacritics

        Parameters:
            text (str): The word to normalize.

        Returns:
            str: The normalized representation of the word.
        """
        # Remove decoratives
        text = "".join([c for c in text if c not in self.DECORATIVE])
        # Remove diacritics
        text = "".join([c for c in text if c not in self.DIACRITICS])
        # Remove diaresis/siyameh
        text = "".join([c for c in text if c not in self.SIYAMEH])
        return text

    def remove_bdol_prefixes(self, text: str) -> str:
        """
        Check to see if the word contains BDOL and if it does remove the prefix
        and return the word without the BDOL        

        Parameters:
            text (str): The word that will need to be checked. 

        Returns:
            str: The word without the BDOL.
        """
        # 1. Is the first character of the word a BDOL letter?
        for c in text[:1]:
            if c in self.BDOL_LETTERS:
                # 2. Is the rest of the word after the BDOL at least a tri-constant root?
                if len(text[2:]) > 3:
                    # 3. Return the word without the BDOL
                    text = text[:1]
        return text

    def ratio(self, text: str) -> float:
        """
        Returns the ratio of Syriac characters to non-Syriac characters in the
        text.

        Parameters:
            text (str): The text to calculate the ratio from.

        Returns:
            float: The ratio of Syriac in the text as a whole;
            otherwise, 0.
        """
        totalCharCnt = 0
        syrCharCnt = 0

        if not self.containsSyr(text):
            return 0

        for char in text:
            totalCharCnt += 1
            try:
                if (
                    "SYRIAC" in unicodedata.name(char)
                    or char in self.VALID_NON_CODEPOINT_SYR_CHAR
                ):
                    syrCharCnt += 1
            except ValueError:
                # Some characters don't have a Unicode name.
                continue

        if totalCharCnt == 0:
            return 0

        return syrCharCnt / totalCharCnt

    def isSyr(self, text: str) -> bool:
        """
        Check if the entire text is valid Syriac text based on Unicode names
        and allowed characters.

        This function ensures every character in the text either has a Unicode
        name containing "SYRIAC" or is among the valid non-codepoint Syriac
        characters. It then verifies that the text contains at least one Syriac
        character.

        Parameters:
            text (str): The text to validate.

        Returns:
            bool: True if the text is considered valid Syriac;
            otherwise, False.
        """
        for char in text:
            try:
                if (
                    "SYRIAC" not in unicodedata.name(char)
                    and char not in self.VALID_NON_CODEPOINT_SYR_CHAR
                ):
                    return False
            except ValueError:
                # Some characters don't have a Unicode name.
                continue
        return self.containsSyr(text)

    def containsSyr(self, text: str) -> bool:
        """
        Determine if the given text contains any Syriac characters.

        Parameters:
            text (str): The text to examine.

        Returns:
            bool: True if at least one character in the text is a letter;
            otherwise, False.
        """
        for c in text:
            if c in self.LETTER:
                return True
        return False

    def eastern(self, text: str) -> bool:
        """
        Determine if the given Syriac text contains any Eastern Assyrian
        vowels.

        Parameters:
            text (str): The Syriac text to check.

        Returns:
            bool: True if an Eastern vowel is detected and the text is valid
            Syriac; otherwise, False.
        """
        if not self.isSyr(text):
            return False
        for c in text:
            if c in self.EASTERN_VOWELS:
                return True
        return False

    def western(self, text: str) -> bool:
        """
        Determine if the given Syriac text contains any Western Assyrian
        vowels.

        Parameters:
            text (str): The Syriac text to check.

        Returns:
            bool: True if a Western vowel is detected and the text is valid
            Syriac; otherwise, False.
        """
        if not self.isSyr(text):
            return False
        for c in text:
            if c in self.WESTERN_VOWELS:
                return True
        return False

    def contains_vowels(self, text: str) -> bool:
        """
        Check if the given text contains any Syriac vowel characters.

        Parameters:
            text (str): The text to check.

        Returns:
            bool: True if any vowel character is present; otherwise, False.
        """
        for c in text:
            if c in self.VOWEL:
                return True
        return False

    def contains_garshuni(self, text: str) -> bool:
        """
        Check if the given text contains any Garshuni characters.

        Parameters:
            text (str): The text to check.

        Returns:
            bool: True if any Garshuni character is found; otherwise, False.
        """
        for c in text:
            if c in self.GARSHUNI:
                return True
        return False

    def contains_non_vowel_diacritics(self, text: str) -> bool:
        """
        Check if the given text contains any non-vowel diacritical marks.

        Parameters:
            text (str): The text to check.

        Returns:
            bool: True if any diacritic from the NON_VOWEL_DIACRITICS set is
            present; otherwise, False.
        """
        for c in text:
            if c in self.NON_VOWEL_DIACRITICS:
                return True
        return False

    def remove_decorative_chars(self, text: str) -> str:
        """
        Remove all decorative characters from the given text.

        Parameters:
            text (str): The input Syriac text.

        Returns:
            str: The text with decorative characters removed.
        """
        return "".join([c for c in text if c not in self.DECORATIVE])

    def remove_siyame(self, text: str) -> str:
        """
        Remove the combining diaeresis (used in siyame) from the text.

        Parameters:
            text (str): The input text.

        Returns:
            str: The text with the combining diaeresis removed.
        """
        for marking in self.SIYAMEH:
            return text.replace(marking, "")

    def get_subtoken_of_type(
        self, token: str, set_type: Tuple[str, ...]
    ) -> str:
        """
        Extract characters from 'token' that belong to the given set.

        Parameters:
            token (str): The token to search.
            set_type (Tuple[str, ...]): A tuple of characters defining the
            desired set.

        Returns:
            str: A substring containing only characters from set_type.
        """
        s: str = ""
        for t in token:
            if t in set_type:
                s += t
        return s

    def tokenize_cluster(self, cluster: str) -> str:
        """
        Tokenize a cluster of Syriac characters into an ordered token string.

        The token is constructed by extracting parts in a specific order:
        letters, siyame, qushayeh, rukakheh, majleaneh, vowels, and qanuneh.

        Parameters:
            cluster (str): A cluster of Syriac characters.

        Returns:
            str: The tokenized representation of the cluster.
        """
        token_str: str = (
            self.get_subtoken_of_type(cluster, self.LETTER)
            + self.get_subtoken_of_type(cluster, self.SIYAMEH)
            + self.get_subtoken_of_type(cluster, self.QUSHAYEH)
            + self.get_subtoken_of_type(cluster, self.RUKAKHEH)
            + self.get_subtoken_of_type(cluster, self.MAJLEANEH)
            + self.get_subtoken_of_type(cluster, self.VOWEL)
            + self.get_subtoken_of_type(cluster, self.QANUNEH)
        )

        if len(self.get_subtoken_of_type(cluster, self.TALQANEH)) > 0:
            token_str = f"[{token_str}]"

        return token_str

    def tokenize_word(self, word: str) -> str:
        """
        Tokenize a Syriac word into clusters based on consonants, diacritics,
        and vocalizations.

        Parameters:
            word (str): A Syriac word.

        Returns:
            str: The tokenized version of the word.
        """
        ret_tokens: str = ""
        cluster: List[str] = [word[0]]
        for c in word[1:]:
            if c not in self.LETTER:
                cluster.append(c)
            else:
                ret_tokens += self.tokenize_cluster("".join(cluster))
                cluster = [c]
        ret_tokens += self.tokenize_cluster("".join(cluster))
        return ret_tokens

    def split_syriac_text(self, text: str) -> List[str]:
        """
        Split Syriac text into a list of words and punctuation tokens.

        Parameters:
            text (str): The input Syriac text.

        Returns:
            List[str]: A list where each element is a word or a punctuation
            mark.
        """
        result: List[str] = []
        word: str = ""
        for char in text:
            if char in self.PUNCTUATION or char.isspace():
                if word:
                    result.append(word)
                    word = ""
                result.append(char)
            else:
                word += char
        if word:        
            result.append(word)        
        return result

    def handle_abbreviations_and_contractions(self, text: str) -> str:
        """
        Replace known abbreviations and contractions in the text with their
        full forms.

        Parameters:
            text (str): The input Syriac text.

        Returns:
            str: The text with abbreviations and contractions handled.
        """
        eastern_replacements: List[List[str]] = [
            ["܏ܩܛ", "ܩܲܕ݇ܡ ܛܲܗܪܵܐ"],
            ["܏ܒܛ", "ܒܲܬ݇ܪ ܛܲܗܪܵܐ"],
            ["ܩܫ܊", "ܩܵܫܝܼܫܵܐ"],
        ]

        if self.eastern(text):
            for old, new in eastern_replacements:
                text = text.replace(old, new)

        text = text.replace(self.ABBREVIATION_MARK, "")
        text = text.replace(self.CONTRACTION, "")
        return text

    def replace_punctuation(self, mark: str) -> str:
        """
        Replace punctuation in a token based on defined punctuation and special
        punctuation mappings.

        Parameters:
            mark (str): The token or punctuation mark.

        Returns:
            str: The token with punctuation replaced.
        """
        for key in self.punctuation_replacements:
            mark = mark.replace(key, self.punctuation_replacements[key])
        for key in self.special_punctuation_replacements:
            mark = mark.replace(
                key, self.special_punctuation_replacements[key]
            )
        return mark

    def apply_special_cases(self, word: str) -> str:
        """
        Apply special phonetic replacements to handle specific edge cases in
        the word.

        Parameters:
            word (str): The input word.

        Returns:
            str: The word after special phonetic replacements.
        """
        special_phonetic_replacements: List[List[str]] = [
            ["ܗ̇ܘ", "ܐܵܘܵ"],
            ["ܗ̇ܝ", "ܐܵܝܵ"],
            ["ܝܠܵܗ̇", "ܝܼܠܵܗ"],
            ["ܝܠܗ̇", "ܝܼܠܵܗ"],
            ["ܝܠܗ", "ܝܼܠܹܗ"],
            ["ܝܠܹܗ", "ܝܼܠܹܗ"],
            ["ܗ̇", "ܗ"],
            ["ܡ̇ܢ", "ܡܵܢ"],
            ["ܡ̣ܢ", "ܡܸܢ"],
            ["ܢܲܦ̮ܫ", "ܢܲܘܫ"],
            ["ܟܠ", "ܟܘܼܠ"],
            ["ܟܠܢ", "ܟܘܼܠܵܢ"],
        ]

        for old, new in special_phonetic_replacements:
            index: int = word.find(old)
            if old in word:
                if len(old) == len(word):
                    word = word.replace(old, new)
                elif len(word) >= index + len(old):
                    if (
                        len(word) > index + len(old)
                        and word[index + len(old)] in self.VOWEL
                    ):
                        pass
                    else:
                        word = word.replace(old, new)
        return word

    def invert_dict(self, d: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Invert a dictionary so that keys become values and values become keys.
        If multiple keys map to the same value, they are grouped into a list.

        Parameters:
            d (Dict[str, str]): The dictionary to invert.

        Returns:
            Dict[str, List[str]]: The inverted dictionary.
        """
        inverted: Dict[str, List[str]] = {}
        for key, value in d.items():
            if value in inverted:
                inverted[value].append(key)
            else:
                inverted[value] = [key]
        return inverted
