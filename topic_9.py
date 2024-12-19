def preLetterCase(s, letter):
  index = s.lower().find(letter.lower())
  if index != -1:
    before_letter = s[:index]
    after_letter = s[index:]
    return before_letter.lower() + after_letter.upper()
  else:
    return s


print(preLetterCase("CAtCHA", "a"))
print(preLetterCase("Preteen", "e"))
print(preLetterCase("You've got this", "m"))
print(preLetterCase("Keep trying", "k"))
