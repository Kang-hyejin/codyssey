log_list = []

try:

    # CSV 파일 읽기
    file = open('Mars_Base_Inventory_List.csv', 'r')
    csv_content = file.readlines()
    file.close()  # 파일 닫기

    header = csv_content[0].strip().split(',')
    log_list.append(header)  # 헤더도 log_list에 추가

    for i in csv_content[1:]:
        li = i.strip().split(',')
        log_list.append(li)

    # 데이터 부분만 분리
    data_list = log_list[1:]

    # 데이터 부분만 정렬 
    data_list.sort(key=lambda x: float(x[4]), reverse=True)

    # 정렬된 데이터를 헤더와 다시 합치기
    log_list = [header] + data_list

    print('전체 데이터')
    for j in log_list:
        print(j)

    # 0.7 이상 데이터 필터링
    filtered_data = [header]  # 새로운 파일에도 헤더 포함

    print('\n0.7 이상 데이터')  
    for j in data_list:
        if float(j[4]) >= 0.7:
            filtered_data.append(j)
            print(j)

    # 새로운 파일로 저장 
    with open('Mars_Base_Inventory_danger.csv', 'w') as new_file:
        for row in filtered_data:
            new_file.write(','.join(row) + '\n')

    # 이진파일 생성
    with open('Mars_Base_Inventory_List.bin', 'wb') as bin_file:
        for row in log_list:
            bin_file.write((','.join(row) + '\n').encode('utf-8'))

    # 이진파일 출력
    with open('Mars_Base_Inventory_List.bin', 'rb') as bin_file:
        loaded_data = bin_file.read().decode('utf-8').splitlines()

    for row in loaded_data:
        print(row.split(','))

except FileNotFoundError:
    print('파일이 존재하지 않습니다.')

'''
txt 파일은 사람이 읽을 수 있음
bin 파일은 기계가 읽을 수 있음

txt파일은 텍스트 편집기를 사용하여 쉽게 열고 편집이 가능해 이식성이 높지만
저장 효율성이 떨어진다

bin파일은 엔디안이나 보편적으로 지원되지 않는 특정 파일 형식과 같은 문제가 발생할 수 있어
이식성은 떨어지지만 효율적인 저장이 가능하다

'''