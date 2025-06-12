name = input("Please enter your name: ")
mobile = int(input("Please enter your mobile number: "))
letter = f"""\
Dear Friend,

I hope this letter finds you well. I wanted to reach out and let you know how much I appreciate your friendship and support.
Looking forward to catching up soon.

Best regards,
{name}
Mobile: {mobile}
"""
print(letter)