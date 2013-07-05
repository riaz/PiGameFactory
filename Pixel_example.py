def game_render(cmd):
    background = [1,1,2,1,1,2,1]
    screen = [0]*7
    for i in range(len(screen)):
        screen[i] = background[i]
    screen[playerPos] = 8
    print(cmd+str(screen))

playerPos = 3
run = True


while run:
    print('-----------Maneuver--------')
    print('1. Move Left [Cmd: MLFT]')
    print('2. Move Right[Cmd: MRHT]')
    print('3. Hop Left  [Cmd: HLFT]')
    print('4. Hop Right [Cmd: HRHT]')
    print('5. Exit Game [Cmd: EXIT]')
    print('---------------------------')

    game_render('OPT>>')

    option = int(input("OPT>>Enter your choice:"))    

    if option == 1:
        playerPos = playerPos - 1
        game_render('MLFT>>')
    elif option == 2:
        playerPos = playerPos + 1
        game_render('MRHT>>')
    elif option == 3:
        jmp = int(input('HLFT>>Enter where to Hop Left:'))

        if jmp < playerPos:
            playerPos = jmp
            game_render('HLFT>>')
        else:
            print('HLFT>>Cannot Hop Left:')
    elif option == 4:
        jmp = int(input('HLRT>>Enter where to Hop Right:'))

        if jmp > playerPos:
            playerPos = jmp
            game_render('MHRT>>')
        else:
            print('HLRT>>Cannot Hop Right:')
    elif option == 5:
        print('EXIT>>You chose to exit.')
        run = False
    else:
        print('OPT>>You Entered an Invalid Option.')
       
       
        






