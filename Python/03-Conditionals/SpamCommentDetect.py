comment1 = "Click Here!"
comment2 = "Congratulations! You've won a free gift card!"
comment3 = "buy now!"
comment4 = "You Won!"

comment = input("Enter your comment: ")
if comment.lower() in [comment1.lower(), comment2.lower(), comment3.lower(), comment4.lower()]:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")