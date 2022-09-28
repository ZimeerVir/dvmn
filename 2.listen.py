from transliterate import translit
from num2words import num2words


text = "Ladies and gentlemen, " \
       "I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. " \
       "\nPeople have also told me to make these next few minutes escruciatingly embarrassing and to take " \
       "vengeance of my enemies.\nNeither will happen.\n\nMore than 3 years ago I moved to Novo-Novsk, " \
       "but worked on new Magnetic Storage for last 40. When I was 8...\n"

print(translit(text, 'ru'))
print(f"78 - {translit(num2words(78, 'en'), 'ru')}")
print(f"15 - {translit(num2words(15, 'en'), 'ru')}")
print(f"3 - {translit(num2words(3, 'en'), 'ru')}")
print(f"40 - {translit(num2words(40, 'en'), 'ru')}")
print(f"8 - {translit(num2words(8, 'en'), 'ru')}")