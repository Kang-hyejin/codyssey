# NumPy 라이브러리 불러오기
import numpy as np

# 파일들을 ndarray로 읽어오기 - 두 번째 열(강도 값)만 읽기
try:
    # usecols=[1]을 사용하여 두 번째 열(인덱스 1)만 가져옵니다
    arr1 = np.genfromtxt("mars_base_main_parts-001.csv", delimiter=",", skip_header=1, usecols=[1], dtype=float)
    print("첫 번째 파일 로드 완료")
except Exception as e:
    print("첫 번째 파일을 읽는 중 오류 발생:", e)
    arr1 = np.array([])

try:
    arr2 = np.genfromtxt("mars_base_main_parts-002.csv", delimiter=",", skip_header=1, usecols=[1], dtype=float)
    print("두 번째 파일 로드 완료")
except Exception as e:
    print("두 번째 파일을 읽는 중 오류 발생:", e)
    arr2 = np.array([])

try:
    arr3 = np.genfromtxt("mars_base_main_parts-003.csv", delimiter=",", skip_header=1, usecols=[1], dtype=float)
    print("세 번째 파일 로드 완료")
except Exception as e:
    print("세 번째 파일을 읽는 중 오류 발생:", e)
    arr3 = np.array([])

# 1차원 배열을 2차원으로 변환 (열 벡터로)
if arr1.size > 0:
    arr1 = arr1.reshape(-1, 1)
if arr2.size > 0:
    arr2 = arr2.reshape(-1, 1)
if arr3.size > 0:
    arr3 = arr3.reshape(-1, 1)

# 3개의 배열을 하나로 병합
parts = np.vstack((arr1, arr2, arr3))
print("배열 병합 완료. 형태:", parts.shape)

# 각 항목(열)의 평균값 계산
column_means = np.mean(parts, axis=0)
print("각 항목의 평균값:", column_means)

# 평균값이 50보다 작은 열만 선택
mask = column_means < 50
parts_to_work_on = parts[:, mask]
print("50보다 작은 평균값을 가진 항목의 수:", np.sum(mask))
print("필터링된 배열의 형태:", parts_to_work_on.shape)

# 원본 데이터 파일에서 부품 이름도 함께 읽어오기
try:
    # 세 파일의 부품 이름(첫 번째 열)만 읽기
    names1 = np.genfromtxt("mars_base_main_parts-001.csv", delimiter=",", skip_header=1, usecols=[0], dtype=str)
    names2 = np.genfromtxt("mars_base_main_parts-002.csv", delimiter=",", skip_header=1, usecols=[0], dtype=str)
    names3 = np.genfromtxt("mars_base_main_parts-003.csv", delimiter=",", skip_header=1, usecols=[0], dtype=str)
    
    # 모든 부품 이름 합치기
    all_names = np.concatenate((names1, names2, names3))
    
    # 강도가 50 미만인 부품들만 선택
    # parts_to_work_on은 강도값만 담고 있으므로 해당하는 부품 이름을 찾아야 함
    # 원본 parts 배열에서 강도가 50 미만인 행의 인덱스 찾기
    low_strength_indices = np.where(parts < 50)[0]
    selected_names = all_names[low_strength_indices]
    
    # 부품 이름과 강도값을 함께 저장하기 위한 배열 준비
    combined_data = np.column_stack((selected_names, parts[low_strength_indices]))
    
    # 결과 출력
    print(f"강도가 50 미만인 부품 수: {len(low_strength_indices)}")
    
    # CSV 파일로 저장 (np.savetxt는 문자열과 숫자가 혼합된 배열을 처리할 수 없음)
    with open('parts_to_work_on.csv', 'w') as f:
        f.write("Part,Strength\n")  # 헤더 추가
        for part, strength in zip(selected_names, parts[low_strength_indices]):
            f.write(f"{part},{strength[0]:.2f}\n")
    
except Exception as e:
    print("부품 이름 처리 중 오류가 발생했습니다:", e)
    # 이름 정보 없이 강도값만 저장
    try:
        np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',', fmt='%.2f')
        print("부품 이름 없이 parts_to_work_on.csv 파일이 저장되었습니다.")
    except Exception as e:
        print("파일 저장 중 오류가 발생했습니다:", e)

# 보너스 과제: parts_to_work_on.csv 파일 읽기
try:
    # 헤더가 있으므로 skip_header=1을 추가하고 이름과 강도 모두 읽기
    parts2_names = np.genfromtxt('parts_to_work_on.csv', delimiter=',', skip_header=1, usecols=[0], dtype=str)
    parts2_values = np.genfromtxt('parts_to_work_on.csv', delimiter=',', skip_header=1, usecols=[1], dtype=float)
    parts2 = parts2_values  # 강도값만 포함하는 배열
    
    print("parts2 배열 로드 완료. 형태:", parts2.shape)
    print("로드된 부품 이름 예시(처음 5개):", parts2_names[:5] if len(parts2_names) > 5 else parts2_names)
    
    # 전치행렬 계산 - 1차원 배열인 경우 2차원으로 변환 후 전치
    if parts2.ndim == 1:
        parts2_2d = parts2.reshape(-1, 1)
        parts3 = parts2_2d.T
    else:
        parts3 = parts2.T
        
    print("parts3(전치행렬)의 형태:", parts3.shape)
    print("parts3의 내용(처음 5행):")
    if parts3.shape[1] > 5:
        print(parts3[:, :5])
    else:
        print(parts3)
except Exception as e:
    print("보너스 과제 수행 중 오류가 발생했습니다:", e)
    print("오류 상세 정보:", e)