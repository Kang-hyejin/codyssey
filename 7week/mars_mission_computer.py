
import time

class DummySensor:
    def __init__(self):
        self.value = 0

    def read_temperature(self):
        self.value += 1
        return 20 + self.value % 5

    def read_humidity(self):
        self.value += 1
        return 40 + self.value % 10

    def read_illuminance(self):
        self.value += 1
        return 300 + self.value % 100

    def read_co2(self):
        self.value += 1
        return 500 + self.value % 100

    def read_oxygen(self):
        self.value += 1
        return 19 + self.value % 3

class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }
        self.ds = DummySensor()
        self.history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

    def get_sensor_data(self):
        count = 0
        print("프로그램을 종료하려면 Ctrl + C 를 누르세요.")
        try:
            while True:
                # 센서값 수집
                self.env_values['mars_base_internal_temperature'] = self.ds.read_temperature()
                self.env_values['mars_base_external_temperature'] = self.ds.read_temperature()
                self.env_values['mars_base_internal_humidity'] = self.ds.read_humidity()
                self.env_values['mars_base_external_illuminance'] = self.ds.read_illuminance()
                self.env_values['mars_base_internal_co2'] = self.ds.read_co2()
                self.env_values['mars_base_internal_oxygen'] = self.ds.read_oxygen()

                # 이력 저장
                for key in self.env_values:
                    self.history[key].append(self.env_values[key])
                    if len(self.history[key]) > 60:
                        self.history[key].pop(0)

                # 출력
                print('{')
                keys = list(self.env_values.keys())
                for i in range(len(keys)):
                    key = keys[i]
                    comma = ',' if i < len(keys) - 1 else ''
                    print("  '" + key + "': " + str(self.env_values[key]) + comma)
                print('}')

                count += 1
                if count % 60 == 0:
                    print('[5분 평균]')
                    for key in self.history:
                        values = self.history[key]
                        total = 0
                        for v in values:
                            total += v
                        avg = total / len(values)
                        print(key + ': ' + str(round(avg, 2)))
                    print('------------------------')

                time.sleep(5)

        except KeyboardInterrupt:
            print('System stopped....')

# 실행
RunComputer = MissionComputer()
RunComputer.get_sensor_data()
