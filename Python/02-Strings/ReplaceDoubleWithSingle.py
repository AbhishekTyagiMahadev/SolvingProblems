text = "This  is  a  string  with  double  spaces."
print("Original text:", text)
if "  " in text:
    print("Double spaces detected!")
updated_text = text.replace("  ", " ")
print("Updated text:", updated_text)
