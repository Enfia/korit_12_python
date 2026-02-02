import random

word_list = ['maple', 'story', 'demon', 'avenger']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

stages = [r'''
0
''', '''
1
''', '''
2
''', '''
3
''','''
4
''', '''
5
''', '''
6
''']

display = []

for i in range(len(chosen_word)):
    display.append('_')

# todo 1
lives = 6

# todo 2
end_of_game = False
while not end_of_game:
    print(stages[lives])
    print(f'기회가 {lives} 번 남았습니다.')
    guess = input("알파벳 하나를 추측해서 입력하세요. >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print('틀렸습니다')


    print(' '.join(display))

    if lives == 0:
        print('죽었습니다')
        end_of_game = True

    if '_' not in display:
        print('정답입니다!')
        end_of_game = True