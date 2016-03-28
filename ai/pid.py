class PID:
    def __init__(self, p=3.0, i=0.0, d=0.0, derivator=0, integrator=0, integrator_max=50, integrator_min=-50):
        self.kp = p
        self.ki = i
        self.kd = d

        self.derivator = derivator
        self.integrator = integrator
        self.integrator_max = integrator_max
        self.integrator_min = integrator_min

        self.set_point = 0.0
        self.error = 0.0

    def update(self, cur_val):
        self.error = self.set_point - cur_val

        self.p_val = self.kp * self.error
        self.d_val = self.kd * (self.error-self.derivator)
        self.derivator = self.error

        self.integrator = self.integrator + self.error

        if self.integrator > self.integrator_max:
            self.integrator = self.integrator_max
        elif self.integrator < self.integrator_min:
            self.integrator = self.integrator_min

        self.i_val = self.integrator*self.ki

        pid = self.p_val + self.i_val + self.d_val

        return pid

    def setPoint(self, set_point):
        self.set_point = set_point
        self.integrator = 0
        self.derivator = 0