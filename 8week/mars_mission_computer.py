import time
import platform
import psutil
import os

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
        self.settings = self.read_settings()

    def read_settings(self):
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setting.txt")
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                settings = [line.strip() for line in lines if line.strip() != ""]
                print("설정 항목 확인:", settings)
                return settings
        except Exception as e:
            print("setting.txt 읽기 실패:", e)
            return []

    def get_mission_computer_info(self):
        info = {
            "OS": "unknown",
            "OS_version": "unknown",
            "CPU_type": "unknown",
            "CPU_cores": "unknown",
            "Memory": "unknown"
        }

        try:
            info["OS"] = platform.system()
        except:
            pass

        try:
            info["OS_version"] = platform.version()
        except:
            pass

        try:
            info["CPU_type"] = platform.processor()
        except:
            pass

        try:
            info["CPU_cores"] = psutil.cpu_count(logical=True)
        except:
            pass

        try:
            mem = psutil.virtual_memory()
            mem_mb = round(mem.total / (1024 * 1024))
            info["Memory"] = str(mem_mb) + " MB"
        except:
            pass

        print("{")
        lines = []
        for key in info:
            if key in self.settings:
                value = info[key]
                if isinstance(value, int):
                    lines.append('  "' + key + '": ' + str(value))
                else:
                    lines.append('  "' + key + '": "' + str(value) + '"')
        print(",\n".join(lines))
        print("}")

    def get_mission_computer_load(self):
        load = {
            "CPU_usage": "unknown",
            "Memory_usage": "unknown"
        }

        try:
            load["CPU_usage"] = psutil.cpu_percent(interval=1)
        except:
            pass

        try:
            mem = psutil.virtual_memory()
            load["Memory_usage"] = mem.percent
        except:
            pass

        print("{")
        lines = []
        for key in load:
            if key in self.settings:
                value = load[key]
                if isinstance(value, (float, int)):
                    lines.append('  "' + key + '": ' + str(value))
                else:
                    lines.append('  "' + key + '": "' + str(value) + '"')
        print(",\n".join(lines))
        print("}")


# 실행부
if __name__ == "__main__":
    runComputer = MissionComputer()
    print("=== 시스템 정보 ===")
    runComputer.get_mission_computer_info()
    print("\n=== 시스템 부하 ===")
    runComputer.get_mission_computer_load()
