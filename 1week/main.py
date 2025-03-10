print('Hello Mars') #파이썬 설치 테스트

try: #예외처리 
    file = open ('mission_computer_main.log', 'r') #로그파일을 read모드로 오픈한다.
    log = file.readlines()  # 모든 내용을 읽어 리스트에 저장한다.

    for i in log: 
        print(i.strip()) 
        '''한 줄씩 log에 입력된 내용을 출력한다. 
        strip는 공백을 제거해주는 함수로 readlines을 이용하면 \n이 포함되기 때문에 이를 제거해주기 위해 사용한다.'''

    print('###역순###')

    for j in reversed(log):  #log파일을 역순으로 출력한다.
        print(j.strip())

    file.close() #파일을 열었으면 닫아줘야함.

    error_log = open('error.log', 'w',encoding = 'utf-8') #문제가 되는 부분을 저장하기 위해 파일 생성을 한다.
    error_line = log[-3:-1] #log파일 확인시 마지막 첫, 두번째 줄이 문제가 되는 부분이었음으로 범위를 지정해준다.

    for k in error_line:  #error log 파일에 문제가 되는 부분을 써준다.
        error_log.write(k)

    error_log.close() #파일을 열었으면 닫아줘야함.


except FileNotFoundError: #파일을 처리할 때 발생할 수 있는 예외 처리.
    print('파일을 찾을 수 없습니다.')

