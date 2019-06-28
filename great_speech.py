from num2words import num2words
from transliterate import translit


print(translit('''
    Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a\
lifetime and I guess that this is mine. People have also told me to make these next few\
minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.\n
More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40.\
When I was 8...\n\n''',
    'ru'))

print('\t78\t', translit(num2words(78), 'ru'), '\n',
      '\t15\t', translit(num2words(15), 'ru'), '\n',
      '\t3\t',  translit(num2words(3),  'ru'), '\n',
      '\t40\t', translit(num2words(40), 'ru'), '\n',
      '\t8\t',  translit(num2words(8),  'ru'), '\n',
      )
