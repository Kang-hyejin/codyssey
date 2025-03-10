try:
    file = open('mission_computer_main.log', 'r', encoding = 'utf-8')
    log = file.read()
    file.close()
    print(log)

except FileNotFoundError:
    print('파일이 존재햐지 않습니다.')