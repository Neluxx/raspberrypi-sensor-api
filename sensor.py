class Sensor:
    """Sensor Class"""

    def __init__(self):
        self.mhz19 = self._get_mhz19_data()
        self.bme680 = self._get_bme680_instance()

    def _get_mhz19_data(self):
        try:
            import mh_z19

            return mh_z19.read_all()
        except ImportError:
            # Mock Daten für den Fall, dass mh_z19 nicht verfügbar ist
            return {"co2": 450}

    def _get_bme680_instance(self):
        try:
            import bme680

            bme = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
            bme.set_humidity_oversample(bme680.OS_2X)
            bme.set_pressure_oversample(bme680.OS_4X)
            bme.set_temperature_oversample(bme680.OS_8X)
            bme.set_filter(bme680.FILTER_SIZE_3)

            return bme
        except ImportError:
            # Mock-Instanz für den Fall, dass bme680 nicht verfügbar ist
            class MockBME680:
                def __init__(self):
                    self.data = type(
                        "obj",
                        (object,),
                        {"temperature": 20, "humidity": 40, "pressure": 900},
                    )

            return MockBME680()

    def get_data(self):
        """Get data from sensors"""

        data = {
            "temperature": self.bme680.data.temperature,
            "humidity": self.bme680.data.humidity,
            "pressure": self.bme680.data.pressure,
            "co2": self.mhz19["co2"],
        }

        return data
