import random

def get_syllables(string):
  syllables = []
  active_substring = ""
  
  for char in string:
    active_substring += char.lower()
    if char.lower() in "aeiouōū":
      syllables.append(active_substring)
      active_substring = ""
  
  if active_substring:
    syllables.append(active_substring)
  
  return syllables

def get_syllabic_anagrams(string, number_of_anagrams=3):
  anagrams = []
  syllables = get_syllables(string)
  
  while len(anagrams) < number_of_anagrams:
    random.shuffle(syllables)
    anagrams.append(''.join(syllables).capitalize())
  
  return anagrams
