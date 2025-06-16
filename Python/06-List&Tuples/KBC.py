print("***Welcome to KBC***\n***You Will Get 1Cr. for every correct answer and nothing for wrong answer***\n\n")

result = 0

questions = [
    ['Capital of India?', ["1:Delhi", "2:Meerut", "3:Mumbai", "4:New York"], 1],
    ['Who wins T20WC 2024?', ["1:India", "2:South Africa", "3:Australia", "4:England"], 1],
    ['Who wins WTC 2023-2025?', ["1:India", "2:Australia", "3:South Africa", "4:New Zeeland"], 3],
    ['Who is known as the Father of the Nation in India?', ["1:Jawaharlal Nehru", "2:Mahatma Gandhi", "3:Sardar Patel", "4:Subhas Chandra Bose"], 2],
    ['Which planet is known as the Red Planet?', ["1:Earth", "2:Venus", "3:Mars", "4:Jupiter"], 3],
    ['What is the largest mammal in the world?', ["1:Elephant", "2:Blue Whale", "3:Giraffe", "4:Hippopotamus"], 2],
    ['Who wrote the national anthem of India?', ["1:Rabindranath Tagore", "2:Bankim Chandra Chatterjee", "3:Sarojini Naidu", "4:Subramania Bharati"], 1],
    ['Which is the smallest prime number?', ["1:0", "2:1", "3:2", "4:3"], 3],
    ['Which river is the longest in the world?', ["1:Amazon", "2:Nile", "3:Ganga", "4:Yangtze"], 2],
    ['Who invented the telephone?', ["1:Alexander Graham Bell", "2:Thomas Edison", "3:Nikola Tesla", "4:Isaac Newton"], 1],
    ['Which is the largest continent?', ["1:Africa", "2:Asia", "3:Europe", "4:Australia"], 2],
    ['What is the chemical symbol for gold?', ["1:Au", "2:Ag", "3:Gd", "4:Go"], 1],
    ['Who was the first President of India?', ["1:Dr. Rajendra Prasad", "2:Dr. S. Radhakrishnan", "3:Jawaharlal Nehru", "4:Indira Gandhi"], 1]
]

for round in questions:
    for ques in round[0:2]:
        print(ques)
    try:
        ans = int(input("Enter your answer (option number):"))
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        break
    if(ans == round[2]):
        result += 1
        print(f"You Won {result}Cr.!\n")
    else:
        print(f"You Lose! The correct answer was: {round[1][round[2]-1]}\n")
        break
print(f"You won total {result}Cr.")
