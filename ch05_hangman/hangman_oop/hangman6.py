import random
import hangman_arts
import hangman_word_list

chosen_word = random.choice(hangman_word_list.word_list).lower()
print(f'테스트 단어 : {chosen_word}')
print(hangman_arts.logo)

display = []

for i in range(len(chosen_word)):
    display.append('_')

lives = 6

end_of_game = False
while not end_of_game:
    print(hangman_arts.stages[lives])
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