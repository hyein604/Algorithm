while True:
    string_input = input()
    if string_input == 'end':
        break
    answer = 'acceptable.'
    string = list(string_input)
    moeum = ['a','e','i','o','u']
    jaeum = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    for letter in moeum:
        if letter in string:
            answer = 'acceptable.'
            break
        if letter == 'u' and letter not in string:
            answer = 'not acceptable.'


    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(len(string)-2):
        if string[i] in moeum and string[i+1] in moeum and string[i+2] in moeum:
            answer = 'not acceptable.'
            break
        if string[i] in jaeum and string[i+1] in jaeum and string[i+2] in jaeum:
            answer = 'not acceptable.'
            break

    # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            if string[i] == 'e' or string[i] == 'o':
                continue
            else:
                answer = 'not acceptable.'

    print(f'<{string_input}> is {answer}')