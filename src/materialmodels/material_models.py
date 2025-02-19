import numpy as np

class KinematicHardeningModel:
    def __init__(self, E, sigma_y, H):
        self.E = E
        self.sigma_y = sigma_y
        self.H = H
        self.alpha = 0  # Back stress (kinematic hardening)
        self.epsilon_p = 0  # Plastic strain

    def calculate_stress(self, strain):
        # Trial stress
        stress_trial = self.E * (strain - self.epsilon_p)
        
        # Yield condition
        f = np.abs(stress_trial - self.alpha) - self.sigma_y
        
        if f <= 0:
            # Elastic behavior
            return stress_trial, False, self.epsilon_p
        else:
            # Plastic behavior
            delta_gamma = f / (self.E + self.H)
            self.epsilon_p += delta_gamma * np.sign(stress_trial - self.alpha)
            self.alpha += self.H * delta_gamma * np.sign(stress_trial - self.alpha)
            stress = stress_trial - self.E * delta_gamma * np.sign(stress_trial - self.alpha)
            return stress, True, self.epsilon_p
        
class IsotropicHardeningModel:
    def __init__(self, E, sigma_y, H):
        self.E = E
        self.sigma_y = sigma_y
        self.H = H
        self.epsilon_p = 0  # Plastic strain

    def calculate_stress(self, strain):
        # Trial stress
        stress_trial = self.E * (strain - self.epsilon_p)
        
        # Yield condition
        f = np.abs(stress_trial) - (self.sigma_y + self.H * self.epsilon_p)
        
        if f <= 0:
            # Elastic behavior
            return stress_trial, False, self.epsilon_p
        else:
            # Plastic behavior
            delta_gamma = f / (self.E + self.H)
            self.epsilon_p += delta_gamma * np.sign(stress_trial)
            stress = stress_trial - self.E * delta_gamma * np.sign(stress_trial)
            return stress, True, self.epsilon_p