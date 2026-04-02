from datetime import datetime

class AlignmentMatrix:
    def __init__(self):
        self.system_status = "OBSERVATIONAL_MODE"
        self.ram_threshold = 20.0
        self.orbital_periods = {
            "Sun": 365.25,
            "Moon": 27.32,
            "Mercury": 87.97,
            "Venus": 224.70,
            "Mars": 686.98,
            "Jupiter": 4332.59,
            "Saturn": 10759.22,
        }

    def calculate_planetary_longitude(self, planet, days_since_epoch):
        if planet not in self.orbital_periods:
            return 0.0
        period = self.orbital_periods[planet]
        mean_motion = 360.0 / period
        longitude = (mean_motion * days_since_epoch) % 360.0
        return round(longitude, 2)

    def generate_chart(self, target_date: datetime):
        epoch = datetime(2000, 1, 1, 12, 0, 0)
        delta = target_date - epoch
        days_since_epoch = delta.total_seconds() / 86400.0
        return {
            planet: self.calculate_planetary_longitude(planet, days_since_epoch)
            for planet in self.orbital_periods.keys()
        }
