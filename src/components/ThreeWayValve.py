from MakerToolbox import ServoMotor, PWMPin


class ThreeWayValve:
    """
    Represents a three way valve with two available paths. One common tap (C)
    and an output tap of either A or B.
    """

    def __init__(self, pin: PWMPin, angle_range: (int, int) = (10, 55), delay: float = 1):
        self._servo = ServoMotor(pwm=pin)
        self._delay = delay
        self._a_angle, self._b_angle = angle_range

    def set_output_a(self):
        self._servo.set_angle(self._a_angle, self._delay)

    def set_output_b(self):
        self._servo.set_angle(self._b_angle, self._delay)
