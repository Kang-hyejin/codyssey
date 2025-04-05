# 전역변수 정의
material = ''  #재질
diameter = 0  #지름
thickness = 0  #두께
area = 0  #면적
weight = 0  #무게

# 함수정의
def sphere_area(diameter, material='유리', thickness=1):
    global area, weight  # 전역 변수 사용 선언

    # 밀도 설정
    density_dict = {'유리': 2.4, '알루미늄': 2.7, '탄소강': 7.85}

    # 잘못된 재질 입력 처리
    if material not in density_dict:
        print('잘못된 재질을 입력하셨습니다. 유리, 알루미늄, 탄소강 중에서 선택하세요.')
        return

    # 잘못된 지름 입력 처리
    try:
        diameter = float(diameter)
        if diameter <= 0:
            print('지름은 0보다 커야 합니다.')
            return
    except ValueError:
        print('지름은 숫자로 입력해야 합니다.')
        return

    # 잘못된 두께 입력 처리
    try:
        thickness = float(thickness)
        if thickness <= 0:
            print('두께는 0보다 커야 합니다.')
            return
    except ValueError:
        print('두께는 숫자로 입력해야 합니다.')
        return

    radius = diameter / 2
    pi = 3.141592653589793

    # 면적 계산
    area = 3 * pi * (radius**2)
    area = round(area, 3)

    # 부피 계산
    volume = area * thickness
    volume = round(volume, 3)

    # 무게 계산
    weight = volume * density_dict[material] * 0.38 / 1000
    weight = round(weight, 3)

    # 전역 변수 저장
    globals()['material'] = material
    globals()['diameter'] = diameter
    globals()['thickness'] = thickness

    # 결과 출력
    print(
        '재질 ==>',material,', 지름 ==>',diameter,', 두께 ==>', \
        thickness,', 면적 ==>',area,', 무게 ==>',weight,'kg',
    )


while True:
    # 사용자 입력 받기
    material_input = input('재질을 입력하세요 (유리, 알루미늄, 탄소강): ')
    diameter_input = input('지름을 입력하세요 (단위: cm): ')
    thickness_input = input('두께를 입력하세요 (단위: cm, 기본값 1): ')

    # 함수 호출
    sphere_area(diameter_input, material_input, thickness_input)
