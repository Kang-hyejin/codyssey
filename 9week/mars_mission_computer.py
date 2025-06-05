import time
import threading
import multiprocessing

# 전역 변수 선언
stop_threads = False

class MissionComputer:
    def get_mission_computer_info(self):
        global stop_threads
        while not stop_threads:
            print("[Info] CPU: 정상 / Memory: 양호 / Disk: 여유")
            time.sleep(20)

    def get_mission_computer_load(self):
        global stop_threads
        while not stop_threads:
            print("[Load] CPU Load: 23% / Memory Load: 45% / Disk Load: 17%")
            time.sleep(20)

    def get_sensor_data(self):
        global stop_threads
        while not stop_threads:
            print("[Sensor] 온도: 37.5도 / 습도: 12% / 압력: 1013hPa")
            time.sleep(20)

def thread_mode():
    global stop_threads
    runComputer = MissionComputer()

    t1 = threading.Thread(target=runComputer.get_mission_computwer_info)
    t2 = threading.Thread(target=runComputer.get_mission_computer_load)
    t3 = threading.Thread(target=runComputer.get_sensor_data)

    t1.start()
    t2.start()
    t3.start()

    print("스레드 실행 중... 종료하려면 Ctrl+C")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n스레드 종료 중...")
        stop_threads = True

    t1.join()
    t2.join()
    t3.join()
    print("스레드 종료 완료")

def process_mode():
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    print("프로세스 실행 중... 종료하려면 Ctrl+C")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n프로세스 종료 중...")
        p1.terminate()
        p2.terminate()
        p3.terminate()

    p1.join()
    p2.join()
    p3.join()
    print("프로세스 종료 완료")

if __name__ == "__main__":
    print("모드 선택: 1 = 멀티스레드 / 2 = 멀티프로세스")
    mode = input("선택: ").strip()
    if mode == "1":
        thread_mode()
    elif mode == "2":
        process_mode()
    else:
        print("잘못된 입력입니다.")
