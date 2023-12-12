class ResponseVariable:
    _value = None

    @classmethod
    def set_value(cls, value):
        cls._value = value

    @classmethod
    def get_value(cls):
        return cls._value