from dataclasses import dataclass
from dataclasses import field
	

class Translation():
	    def __init__(self, english_value, russian_value):
	        self.english_value = english_value
	        self.russian_values = [russian_value]
	
@dataclass
class TranslationItem:
	    english_value:str
	    russian_value:str
	
class Translator():
	    
	    def __init__(self):
	        self.translations_list = []
	

	    def add_translation(self, translation):
	        for translation_item in self.translations_list:
	            if translation_item.english_value == translation.english_value:
	                translation_item.russian_values.append(translation.russian_value)
	                return
	
	        self.translations_list.append(Translation(translation.english_value, translation.russian_value))
	
	    def print_translations_of_english_word(self, english_word):
	        print(f"English word: {english_word}")
	        for translation_item in self.translations_list:
	            if(translation_item.english_value == english_word):
	                translation_str = ""
	                for russian_value in translation_item.russian_values:
	                    translation_str += russian_value + " "
	
	                print(f"Translations: {translation_str}")
	                return
test_list = [TranslationItem("company", "компанія") , TranslationItem("company", "фірма"), TranslationItem("vary","відрізнятися"), TranslationItem("vary","змінюватися"),TranslationItem("staff", "персонал"), TranslationItem("staff", "штат")  ]
translator = Translator()
	

for test_item in test_list:
	    translator.add_translation(test_item)
print("введіть слово для перекладу:")
a = input()
translator.print_translations_of_english_word(a)


	




	
