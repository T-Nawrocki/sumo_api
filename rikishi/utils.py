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
