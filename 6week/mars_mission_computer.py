# mars_mission_computer.py

import random


class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = random.randint(18, 30)
        self.env_values['mars_base_external_temperature'] = random.randint(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.randint(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.randint(500, 715)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4.0, 7.0), 2)

    def get_env(self):
        values = self.env_values
        log_line = (
            "LOG_ENTRY, "
            + str(values['mars_base_internal_temperature']) + "C, "
            + str(values['mars_base_external_temperature']) + "C, "
            + str(values['mars_base_internal_humidity']) + "%, "
            + str(values['mars_base_external_illuminance']) + "W/m2, "
            + str(values['mars_base_internal_co2']) + "%, "
            + str(values['mars_base_internal_oxygen']) + "%\n"
        )

        with open('log.txt', 'a') as file:
            file.write(log_line)

        return values


ds = DummySensor()
ds.set_env()
print(ds.get_env())
