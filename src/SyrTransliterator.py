"""
' @file SyrTransliterator.py
'
' @author The Assyrian Digital Language Consortium
' @date 1 Feb 2025
'
' @brief Syriac transliteration and phonetic approximation
'
' @description: This file contains the Syr class which is used
'               to as a base clase utility for working with Syriac
'               text.
'
' @license MIT License
' @copyright Assyrian Digital Language Consortium
"""

import json
from typing import Dict, List, Tuple
from SyrTools import SyrTools


class SyrTransliterator(SyrTools):
    """
    A class to transliterate Syriac text into IPA and Romanized forms and to
    reverse the process.

    It extends the SyrTools class with additional mappings and functions
    specific to transliteration.
    """

    def __init__(
        self, dialect_map_filename: str = "", ipa_mapping_filename: str = ""
    ) -> None:
        """
        Initialize the SyrTransliterator with IPA-to-Roman mappings,
        punctuation replacements, and various IPA vowel and consonant
        collections.
        """
        super().__init__()

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

        self.prepositional_b = "o"

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

        self.ipa_to_roman_map: Dict[str, str] = {
            # Rukakheh & Qushayeh
            "v": "w",
            "ɣ": "gh",
            "ð": "dh",
            "x": "kh",
            "f": "f",
            "θ": "th",
            "g": "g",
            "d": "d",
            "k": "k",
            "p": "p",
            "t": "t",
            # Majleaneh
            "ʤ": "j",
            "ʒ": "zh",
            "tʃ": "ch",
            # Mater Lectionis
            "u": "u",
            "o": "o",
            "i": "i",
            # Consonants
            "ʔ": "'",
            "b": "b",
            "g": "g",
            "d": "d",
            "h": "h",
            "w": "w",
            "z": "z",
            "ḥ": "kh",
            "tˤ": "ṭ",
            "j": "y",
            "l": "l",
            "m": "m",
            "n": "n",
            "s": "s",
            "ʕ": "ʿ",
            "p": "p",
            "sˤ": "ṣ",
            "q": "q",
            "r": "r",
            "ʃ": "sh",
            # Eastern Vowels
            "a": "a",
            "ɑ": "a",
            "ɪ": "i",
            "e": "e",
            # Western Vowels
            "o": "o",
            "u": "u",
        }

        self.special_punctuation_replacements: Dict[str, str] = {
            self.END_OF_PARAGRAPH: ".",
            self.SUPRALINEAR_FULL_STOP: ".",
            self.SUBLINEAR_FULL_STOP: ".",
            self.SUPRALINEAR_COLON: ",",
            self.SUBLINEAR_COLON: ",",
            self.HORIZONTAL_COLON: ",",
            self.COLON_SKEWED_LEFT: ",",
            self.COLON_SKEWED_RIGHT: ",",
            self.SUPRALINEAR_COLON_SKEWED_LEFT: ",",
            self.SUBLINEAR_COLON_SKEWED_RIGHT: ",",
            self.HARKLEAN_OBELUS: "",
            self.HARKLEAN_METOBELUS: "",
            self.HARKLEAN_ASTERISCUS: "",
            self.BARREKH: "",
        }

        self.punctuation_replacements: Dict[str, str] = {
            "؟": "?",
            "،": ",",
            "؛": ";",
        }

        if ipa_mapping_filename != "":
            with open(ipa_mapping_filename, "r", encoding="utf-8") as f:
                mappings = json.load(f)
                consonants = mappings["consonants"]
                bgdfkt = mappings["bgdfkt"]
                majleaneh = mappings["majleaneh"]
                mater_lectionis = mappings["mater_lectionis"]
                eastern_vowels = mappings["eastern_vowels"]
                western_vowels = mappings["western_vowels"]

                for key in self.consonant_ipa_map.keys():
                    self.consonant_ipa_map[key] = consonants[key]
                for key in self.rukakheh_qushayeh_ipa_map.keys():
                    self.rukakheh_qushayeh_ipa_map[key] = bgdfkt[key]
                for key in self.majleaneh_ipa_map.keys():
                    self.majleaneh_ipa_map[key] = majleaneh[key]
                for key in self.mater_lectionis_ipa_map.keys():
                    self.mater_lectionis_ipa_map[key] = mater_lectionis[key]

                self.eastern_vowel_ipa_map[self.PTHAHA_DOTTED] = (
                    eastern_vowels["ptakha"]
                )
                self.eastern_vowel_ipa_map[self.ZQAPHA_DOTTED] = (
                    eastern_vowels["zqappa"]
                )
                self.eastern_vowel_ipa_map[self.DOTTED_ZLAMA_HORIZONTAL] = (
                    eastern_vowels["zlama_kirya"]
                )
                self.eastern_vowel_ipa_map[self.DOTTED_ZLAMA_ANGULAR] = (
                    eastern_vowels["zlama_yarikha"]
                )

                self.western_vowel_ipa_map[self.PTHAHA_ABOVE] = western_vowels[
                    "pthaha_above"
                ]
                self.western_vowel_ipa_map[self.PTHAHA_BELOW] = western_vowels[
                    "pthaha_below"
                ]
                self.western_vowel_ipa_map[self.ZQAPHA_ABOVE] = western_vowels[
                    "zqapha_above"
                ]
                self.western_vowel_ipa_map[self.ZQAPHA_BELOW] = western_vowels[
                    "zqapha_below"
                ]
                self.western_vowel_ipa_map[self.RBASA_ABOVE] = western_vowels[
                    "rbasa_above"
                ]
                self.western_vowel_ipa_map[self.RBASA_BELOW] = western_vowels[
                    "rbasa_below"
                ]
                self.western_vowel_ipa_map[self.HBASA_ABOVE] = western_vowels[
                    "hbasa_above"
                ]
                self.western_vowel_ipa_map[self.HBASA_BELOW] = western_vowels[
                    "hbasa_below"
                ]
                self.western_vowel_ipa_map[self.ESASA_ABOVE] = western_vowels[
                    "esasa_above"
                ]
                self.western_vowel_ipa_map[self.ESASA_BELOW] = western_vowels[
                    "esasa_below"
                ]

        if dialect_map_filename != "":
            with open(dialect_map_filename, "r", encoding="utf-8") as f:
                mappings = json.load(f)
                romanization = mappings["romanization"]
                self.prepositional_b = mappings["prepositional_b"]
                for key in self.ipa_to_roman_map.keys():
                    self.ipa_to_roman_map[key] = romanization[key]

        self.ipa_vowels: List[str] = (
            list(self.eastern_vowel_ipa_map.values())
            + list(self.western_vowel_ipa_map.values())
            + list(self.mater_lectionis_ipa_map.values())
        )

        self.ipa_bdol: Tuple[str, str] = (
            self.consonant_ipa_map["ܒ"],
            self.consonant_ipa_map["ܕ"],
            self.consonant_ipa_map["ܘ"],
            self.consonant_ipa_map["ܠ"],
        )
        self.ipa_mater_lectionis: List[str] = list(
            self.mater_lectionis_ipa_map.values()
        )

    def transliterate(self, text: str) -> Dict[str, str]:
        """
        Transliterate Syriac text into IPA and Romanized forms.

        The process includes:
          - Encoding Syriac to IPA.
          - Removing specific diacritical marks.
          - Naturalizing the IPA for pronunciation.
          - Converting IPA to Romanized phonemes.

        Parameters:
            text (str): The input Syriac text.

        Returns:
            Dict[str, str]: A dictionary with keys "ipa", "natural_ipa", and
            "romanized".
        """
        lossless_ipa_text: str = self.encode_ipa(text)
        lossless_ipa_text = self.remove_siyame(lossless_ipa_text)

        phonetic_ipa_text: str = self.naturalize_ipa(lossless_ipa_text)

        return {
            "ipa": lossless_ipa_text,
            "natural_ipa": phonetic_ipa_text,
            "romanized": self.ipa_to_roman(phonetic_ipa_text),
        }

    def naturalize_ipa(self, ipa: str) -> str:
        """
        Convert an IPA transcription to a naturalized pronunciation by applying
        phonetic rules.

        Rules applied include:
          - Removing an initial glottal stop if it precedes a vowel.
          - Removing a final glottal stop if it follows a short vowel.
          - Converting 'i' to 'ɪ' when it is between two unvocalized
            consonants.

        Parameters:
            ipa (str): The IPA transcription.

        Returns:
            str: The naturalized IPA transcription.
        """
        vowels: List[str] = list(self.eastern_vowel_ipa_map.values()) + list(
            self.mater_lectionis_ipa_map.values()
        )
        ipa_chars: List[str] = list(
            ipa
        )  # Convert to list for easy modification

        # Remove initial glottal stop if followed by a vowel
        glottal_stop_ipa: str = self.consonant_ipa_map["ܐ"]
        if (
            ipa_chars
            and ipa_chars[0] == glottal_stop_ipa
            and len(ipa_chars) > 1
            and ipa_chars[1] in vowels
        ):
            ipa_chars.pop(0)

        # Remove final glottal stop if preceded by a short vowel
        short_vowels = {
            self.eastern_vowel_ipa_map[self.PTHAHA_DOTTED],
            self.eastern_vowel_ipa_map[self.ZQAPHA_DOTTED],
            self.eastern_vowel_ipa_map[self.DOTTED_ZLAMA_HORIZONTAL],
            self.eastern_vowel_ipa_map[self.DOTTED_ZLAMA_ANGULAR],
        }
        if (
            len(ipa_chars) > 1
            and ipa_chars[-1] == glottal_stop_ipa
            and ipa_chars[-2] in short_vowels
        ):
            ipa_chars.pop()

        # Convert 'i' to 'ɪ' if sandwiched between two unvocalized consonants
        for j in range(1, len(ipa_chars) - 1):
            if (
                ipa_chars[j] == self.mater_lectionis_ipa_map["ܝܼ"]
                and ipa_chars[j - 1] not in vowels
                and ipa_chars[j + 1] not in vowels
            ):
                ipa_chars[j] = self.eastern_vowel_ipa_map[
                    self.DOTTED_ZLAMA_HORIZONTAL
                ]

        return "".join(ipa_chars)

    def split_ipa_text(self, text: str) -> List[str]:
        """
        Split IPA text into tokens, separating words from punctuation.

        Parameters:
            text (str): The IPA text.

        Returns:
            List[str]: A list of IPA tokens.
        """
        result: List[str] = []
        word: str = ""
        punctuations: List[str] = [
            ",",
            ":",
            ";",
            "!",
            ".",
            "-",
            "<",
            ">",
            "?",
            "'",
            '"',
        ]
        for char in text:
            if char in punctuations or char.isspace():
                if word:
                    result.append(word)
                    word = ""
                result.append(char)
            else:
                word += char
        if word:
            result.append(word)
        return result

    def apply_ipa_map(self, word: str) -> str:
        """
        IPA mappings for maternal lectionis, rukakheh/qushayeh,
        majleaneh, and consonants are then applied.

        Parameters:
            word (str): The input word.

        Returns:
            str: The word after special IPA replacements.

        """
        for key in self.mater_lectionis_ipa_map:
            word = word.replace(key, self.mater_lectionis_ipa_map[key])

        for key in self.rukakheh_qushayeh_ipa_map:
            word = word.replace(key, self.rukakheh_qushayeh_ipa_map[key])

        for key in self.majleaneh_ipa_map:
            word = word.replace(key, self.majleaneh_ipa_map[key])

        for key in self.consonant_ipa_map:
            word = word.replace(key, self.consonant_ipa_map[key])

        for key in self.eastern_vowel_ipa_map:
            word = word.replace(key, self.eastern_vowel_ipa_map[key])

        return word

    def encode_ipa(self, text: str) -> str:
        """
        Encode Syriac text into an IPA transcription.

        The process includes splitting the text into words, handling
        decorations, abbreviations, special cases, tokenizing, and replacing
        punctuation.

        Parameters:
            text (str): The input Syriac text.

        Returns:
            str: The IPA transcription.
        """
        words: List[str] = self.split_syriac_text(text)
        ipastr: str = ""
        for word in words:
            if word not in self.PUNCTUATION and not word.isspace():
                word = self.remove_decorative_chars(word)
                word = self.handle_abbreviations_and_contractions(word)
                word = self.apply_special_cases(word)
                word = self.tokenize_word(word)
                word = self.apply_ipa_map(word)
            word = self.replace_punctuation(word)
            ipastr += word
        return ipastr

    def apply_bdol_prefixes(self, text: str) -> str:
        """
        Apply bdol prefixes to IPA tokens. If a token starts with a bdol
        consonant and is not followed by a vowel, an apostrophe is inserted
        after the consonant.

        Parameters:
            text (str): The IPA text.

        Returns:
            str: The IPA text with bdol prefixes applied.
        """
        split_ipa: List[str] = self.split_ipa_text(text)
        bdolized_str: str = ""
        for tok in split_ipa:
            if (
                len(tok) > 1
                and tok[0] in self.ipa_bdol
                and tok[1] not in self.ipa_vowels
            ):
                bdol = tok[0]
                if tok[0] == self.consonant_ipa_map["ܘ"]:
                    bdol = self.prepositional_b
                bdolized_str += f"{bdol}'{tok[1:]}"
            else:
                bdolized_str += tok
        return bdolized_str

    def handle_glottals(self, text: str) -> str:
        """
        Adjust IPA tokens by handling glottal stops. This function removes
        glottal stops at the beginning or end of tokens if present.

        Parameters:
            text (str): The IPA text.

        Returns:
            str: The IPA text with glottal adjustments.
        """
        split_ipa: List[str] = self.split_ipa_text(text)
        filtered_str: str = ""
        for tok in split_ipa:
            if (
                tok[0] == self.consonant_ipa_map["ܐ"]
                or tok[0] == self.consonant_ipa_map["ܑ"]
            ):
                filtered_str += tok[1:]
            elif (
                tok[-1] == self.consonant_ipa_map["ܐ"]
                or tok[-1] == self.consonant_ipa_map["ܑ"]
            ):
                filtered_str += tok[:-1]
            elif (
                tok[0] == self.consonant_ipa_map["ܐ"]
                or tok[0] == self.consonant_ipa_map["ܑ"]
            ) and (
                tok[-1] == self.consonant_ipa_map["ܐ"]
                or tok[-1] == self.consonant_ipa_map["ܑ"]
            ):
                filtered_str += tok[1:-1]
            else:
                filtered_str += tok
        return filtered_str

    def remove_bracketed_content(self, ipa_text: str) -> str:
        """
        Remove content enclosed in square brackets (including the brackets)
        from IPA text.

        Parameters:
            ipa_text (str): The IPA transcription.

        Returns:
            str: The IPA text with bracketed content removed.
        """
        result: List[str] = []
        inside_brackets: bool = False
        for char in ipa_text:
            if char == "[":
                inside_brackets = True
            elif char == "]":
                inside_brackets = False
            elif not inside_brackets:
                result.append(char)
        return "".join(result)

    def ipa_to_roman(self, ipa_text: str) -> str:
        """
        Convert an IPA transcription into its Romanized form.

        The process includes:
          - Removing bracketed content.
          - Applying bdol prefixes.
          - Handling glottal stop adjustments.
          - Mapping IPA segments to their Romanized equivalents.

        Parameters:
            ipa_text (str): The IPA transcription.

        Returns:
            str: The Romanized transcription.
        """
        ipa_text = self.remove_bracketed_content(ipa_text)
        ipa_text = self.apply_bdol_prefixes(ipa_text)
        ipa_text = self.handle_glottals(ipa_text)

        result: List[str] = []
        i: int = 0
        while i < len(ipa_text):
            found: bool = False
            for length in [3, 2, 1]:
                if i + length <= len(ipa_text):
                    segment: str = ipa_text[i : i + length]
                    if segment in self.ipa_to_roman_map:
                        result.append(self.ipa_to_roman_map[segment])
                        i += length
                        found = True
                        break
            if not found:
                result.append(ipa_text[i])
                i += 1
        return "".join(result)

    def reverse_transliterate(
        self, ipa_text: str, eastern: bool = True
    ) -> str:
        """
        Reverse the transliteration by converting an IPA transcription back to
        Syriac script.

        This function first inverts the IPA-to-Syriac mappings (using either
        Eastern or Western vowel rules) and then scans the IPA text for
        multi-character segments to reconstruct the Syriac text.

        Parameters:
            ipa_text (str): The IPA transcription.
            eastern (bool, optional): Whether to use Eastern vowel mappings.
            Defaults to True.

        Returns:
            str: The reconstructed Syriac text.
        """
        if not ipa_text:
            return ""

        ipa_to_syriac_map: Dict[str, List[str]] = {}
        if eastern:
            for original_map in [
                self.rukakheh_qushayeh_ipa_map,
                self.majleaneh_ipa_map,
                self.mater_lectionis_ipa_map,
                self.consonant_ipa_map,
                self.eastern_vowel_ipa_map,
                self.punctuation_replacements,
            ]:
                ipa_to_syriac_map.update(self.invert_dict(original_map))
        else:
            for original_map in [
                self.rukakheh_qushayeh_ipa_map,
                self.majleaneh_ipa_map,
                self.mater_lectionis_ipa_map,
                self.consonant_ipa_map,
                self.western_vowel_ipa_map,
                self.punctuation_replacements,
            ]:
                ipa_to_syriac_map.update(self.invert_dict(original_map))

        result: List[str] = []
        i: int = 0
        while i < len(ipa_text):
            found: bool = False
            for length in [3, 2, 1]:
                if i + length <= len(ipa_text):
                    segment: str = ipa_text[i : i + length]
                    if segment in ipa_to_syriac_map:
                        result.append(ipa_to_syriac_map[segment][0])
                        i += length
                        found = True
                        break
            if not found:
                result.append(ipa_text[i])
                i += 1

        syr_text: str = "".join(result)

        # Process bracketed content: remove brackets and add an oblique line
        # above if necessary.
        final_result: List[str] = []
        inside_brackets: bool = False
        for char in syr_text:
            if char == "[":
                inside_brackets = True
            elif char == "]":
                if inside_brackets:
                    final_result.append(self.OBLIQUE_LINE_ABOVE)
                inside_brackets = False
            else:
                final_result.append(char)
        return "".join(final_result)
