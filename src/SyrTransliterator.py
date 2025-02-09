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

from typing import Dict, List, Tuple
from SyrTools import SyrTools


class SyrTransliterator(SyrTools):
    """
    A class to transliterate Syriac text into IPA and Romanized forms and to
    reverse the process.

    It extends the SyrTools class with additional mappings and functions
    specific to transliteration.
    """

    def __init__(self) -> None:
        """
        Initialize the SyrTransliterator with IPA-to-Roman mappings,
        punctuation replacements, and various IPA vowel and consonant
        collections.
        """
        super().__init__()

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

        self.ipa_vowels: List[str] = (
            list(self.eastern_vowel_ipa_map.values())
            + list(self.western_vowel_ipa_map.values())
            + list(self.mater_lectionis_ipa_map.values())
        )

        self.ipa_bdol: Tuple[str, ...] = ("b", "d", "w", "l")
        self.ipa_mater_lectionis: List[str] = list(
            self.mater_lectionis_ipa_map.values()
        )

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
        return text.replace(self.COMBINING_DIAERESIS, "")

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
        Additional mappings for maternal lectionis, rukakheh/qushayeh,
        majleaneh, and consonants are then applied.

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

        for key in self.mater_lectionis_ipa_map:
            token_str = token_str.replace(
                key, self.mater_lectionis_ipa_map[key]
            )

        for key in self.rukakheh_qushayeh_ipa_map:
            token_str = token_str.replace(
                key, self.rukakheh_qushayeh_ipa_map[key]
            )

        for key in self.majleaneh_ipa_map:
            token_str = token_str.replace(key, self.majleaneh_ipa_map[key])

        for key in self.consonant_ipa_map:
            token_str = token_str.replace(key, self.consonant_ipa_map[key])

        for key in self.eastern_vowel_ipa_map:
            token_str = token_str.replace(key, self.eastern_vowel_ipa_map[key])

        return token_str

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
                bdolized_str += f"{tok[0]}'{tok[1:]}"
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
