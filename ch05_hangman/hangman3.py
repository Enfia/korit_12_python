import random

word_list = ['maple', 'story', 'demon', 'avenger']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

display = []

for i in range(len(chosen_word)):
    display.append('_')

isAnswer = True
while isAnswer:
    guess = input("알파벳 하나를 추측해서 입력하세요. >>> ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if '_' in display :
        print(' '.join(display))
    else:
        print('정답입니다 !!')
        isAnswer = False