class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    # Печатаем все буквы алфавита
    def print(self):
        print(self.letters)

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        len(self.letters)


# Английский алфавит
class EngAlphabet(Alphabet):

    __letters_num = 26

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False


