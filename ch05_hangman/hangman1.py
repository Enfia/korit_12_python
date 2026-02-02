import random

# todo - 1
word_list = ['apple','banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

# todo - 2
guess = input("알파벳 하나를 추측해서 입력하세요. >>> ").lower()

# 인덱스가 요구될때만 일반 for문
# 일반 for문은 for i in range()
# todo - 3
for i in chosen_word:
    if i == guess:
        print("정답")
    else:
        print("오답")
