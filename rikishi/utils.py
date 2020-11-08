import random, math

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

def get_syllabic_anagrams(string, requested_anagrams=3):
  syllables = get_syllables(string)
  max_anagrams = math.factorial(len(syllables))
  if requested_anagrams < max_anagrams:
    max_anagrams = requested_anagrams;
  
  anagrams = []
  while len(anagrams) < max_anagrams:
    random.shuffle(syllables)
    anagram = ''.join(syllables).capitalize()
    if anagram not in anagrams:
      anagrams.append(''.join(syllables).capitalize())
  
  if string in anagrams:
    anagrams.remove(string)
  
  return anagrams
