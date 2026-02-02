import random

word_list = ['apple', 'banna', 'camel']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

# todo 1 : 비어있는 list인 display를 만들기
display = []


# todo 2 : chosen_word의 각 문자 개수마다 _를 추가하시오
guess = input("알파벳 하나를 추측해서 입력하세요. >>> ").lower()

for i in range(len(chosen_word)):
    display.append('_')
    if chosen_word[i] == guess:
        display[i] = guess

print(display)
