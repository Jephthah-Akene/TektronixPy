class Oscilloscope:
    def __init__(self, resource_manager, resource_name):
        self.resource_manager = resource_manager
        self.resource_name = resource_name
        self.instrument = None

    def connect(self):
        self.instrument = self.resource_manager.open_resource(self.resource_name)

    def disconnect(self):
        if self.instrument is not None:
            self.instrument.close()

    def get_idn(self):
        if self.instrument is not None:
            return self.instrument.query('*IDN?')
        return None
