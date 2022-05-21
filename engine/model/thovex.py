from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 5)
        if service_threshold_date < datetime.current_date().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
