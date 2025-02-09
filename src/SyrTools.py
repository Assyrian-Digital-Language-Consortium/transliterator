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
from typing import Tuple, Dict


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

        self.rukakheh_qushayeh_ipa_map: Dict[str, str] = {
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

        self.majleaneh_ipa_map: Dict[str, str] = {
            "ܓ̰": "ʤ",
            "ܙ̰": "ʒ",
            "ܙ̃": "ʒ",
            "ܟ̰": "tʃ",
            "ܟ̃": "tʃ",
            "ܫ̃": "ʒ",
            "ܫ̰": "ʒ",
        }

        self.mater_lectionis_ipa_map: Dict[str, str] = {
            "ܘܼ": "u",
            "ܘܿ": "o",
            "ܝܼ": "i",
        }

        self.consonant_ipa_map: Dict[str, str] = {
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

        self.eastern_vowel_ipa_map: Dict[str, str] = {
            self.PTHAHA_DOTTED: "a",
            self.ZQAPHA_DOTTED: "ɑ",
            self.DOTTED_ZLAMA_HORIZONTAL: "ɪ",
            self.DOTTED_ZLAMA_ANGULAR: "e",
        }

        self.western_vowel_ipa_map: Dict[str, str] = {
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

        # Define NON_VOWEL_DIACRITICS as those diacritics that are not vowels.
        self.NON_VOWEL_DIACRITICS: Tuple[str, ...] = tuple(
            set(self.DIACRITICS) - set(self.VOWEL)
        )

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
            bool: True if at least one character in the text is a Syriac letter
                  or vowel; otherwise, False.
        """
        for c in text:
            if c in self.LETTER or c in self.VOWEL:
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
