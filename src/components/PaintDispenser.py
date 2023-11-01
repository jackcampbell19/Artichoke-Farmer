from MakerToolbox import PWMPin
from .ThreeWayValve import ThreeWayValve


class PaintDispenser:

    def __init__(self, base_pin: PWMPin, cyan_pin: PWMPin, magenta_pin: PWMPin, yellow_pin: PWMPin, black_pin: PWMPin):
        self._base_valve: ThreeWayValve = ThreeWayValve(pin=base_pin)
        self._cyan_valve: ThreeWayValve = ThreeWayValve(pin=cyan_pin)
        self._magenta_valve: ThreeWayValve = ThreeWayValve(pin=magenta_pin)
        self._yellow_valve: ThreeWayValve = ThreeWayValve(pin=yellow_pin)
        self._black_valve: ThreeWayValve = ThreeWayValve(pin=black_pin)

