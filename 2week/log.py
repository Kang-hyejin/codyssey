log_list = []  # 로그 데이터 저장할 리스트 생성

try:  # 파일 예외처리
    file = open('mission_computer_main.log', 'r') # 'mission_computer_main.log' 파일을 읽기 모드로 오픈
    loglist = file.readlines() # 파일의 모든 줄을 읽음
    
    # ','로 구분해 리스트화 하기 위한 for문 헤더를 제외하고 리스트화 하기 위해 [1:] 적용
    for i in loglist[1:]:
        # 줄 끝에 생기는 공백 제거 후 쉼표를 기준으로 분리하여 리스트로 변환
        li = i.strip().split(',')
        # 변환된 리스트를 log_list에 추가
        log_list.append(li)
        
    # 로그 출력
    print(log_list)
    
    # 역순으로 출력하기 위해 sort적용 (reverse = False는 오름차순)
    log_list.sort(reverse=True)
    print('역순 출력')
    # 역순출력
    for j in log_list:
        print(j)
    
    # 리스트를 딕셔너리화 하기 위한 구문
    # x[0](타임스탬프)키: {x[1]이벤트(key):x[2]메세지(value)}밸류 형식으로 딕셔너리화 함
    dic = {x[0]: {"event":x[1],"message":x[2]} for x in log_list}
    print(dic)

    file_2 = open('mission_computer_main.json', 'w')  # 'mission_computer_main.json' 파일로 만들기 위한 구문

    json_dump = '{\n' #json 파일은 {로 시작
    for key, value in dic.items(): #딕셔너리의 키, 밸류 값 쓰기 위해 for문 사용
        json_dump += '    "' + key + '": {\n' #"key:{ }형식으로 쓰기"
        json_dump += '        "event": "' + value['event'] + '",\n' #"event":밸류에 로그값 쓰기 '+'는 문자열을 합치는 역할을 함함
        json_dump += '        "message": "' + value['message'] + '"\n' #"message":밸류에 로그값 쓰기(가독성을 위해 들여쓰기 해줌)
        json_dump += '    },\n'
    
    # 마지막 쉼표와 개행문자 제거 후 닫는 중괄호 추가
    json_dump = json_dump.strip(',\n') + '\n}'
    
    file_2.write(json_dump) #json 정규화 시켜준 것 file_2에 쓰기

    
    # 사용한 파일들 닫아줘야함
    file.close()
    file_2.close()
    
    # 보너스문제
    # 특정 문자열 입력받기
    search = input('특정 문자열(ex.Oxygen[대소문자 구분])을 입력하시오: ')
    found = False  # 올바른 결과값을 입력했는지 확인하기 위한 변수
    
    # dic.items()은 키,밸류를 반환하므로 key, value를 변수로 둬야함
    # 입력받은 값이 로그에 존재하는지 찾는 과정임
    for key, value in dic.items():
        info = value['message']  # 각 딕셔너리의 value에서 'message' 키의 밸류를 가져옴
        # 입력값이 info에 포함되어 있는지 확인
        if search in info:
            # 포함되어 있다면 출력
            found = True  # 찾았으니 True로 전환
            print(info)

    
    # 올바른 값이 아닌경우 출력
    if found == False:
        print('잘못된 입력 값 입니다.')

except FileNotFoundError:  # 파일을 찾지 못할 경우 발생하는 예외 처리
    print('파일을 찾을 수 없습니다.')
