material_models import KinematicHardeningModel, IsotropicHardeningModel
import numpy as np
import matplotlib.pyplot as plt

# Example 1: Basic Usage of Kinematic and Isotropic Hardening Models
# Kinematic Hardening Example
model_kinematic = KinematicHardeningModel(E=210000, sigma_y=250, H=1000)
strain = 0.002
stress_k, is_plastic_k, epsilon_p_k = model_kinematic.calculate_stress(strain)
print(f"Kinematic Hardening - Stress: {stress_k}, Plastic: {is_plastic_k}, Plastic Strain: {epsilon_p_k}")

# Isotropic Hardening Example
model_isotropic = IsotropicHardeningModel(E=210000, sigma_y=250, H=1000)
strain = 0.002
stress_i, is_plastic_i, epsilon_p_i = model_isotropic.calculate_stress(strain)
print(f"Isotropic Hardening - Stress: {stress_i}, Plastic: {is_plastic_i}, Plastic Strain: {epsilon_p_i}")

# Example 2: Cyclic Loading with Kinematic Hardening
# Define material properties
E = 210000  # Young's modulus (MPa)
sigma_y = 250  # Initial yield stress (MPa)
H = 1000  # Hardening modulus (MPa)

# Initialize the model
model = KinematicHardeningModel(E, sigma_y, H)

# Define strain increments (cyclic loading)
strains = np.linspace(0, 0.003, 100)  # Loading
strains = np.concatenate([strains, np.linspace(0.003, -0.003, 200)])  # Unloading and reverse loading
strains = np.concatenate([strains, np.linspace(-0.003, 0, 100)])  # Return to zero

# Calculate stresses
stresses = []
for strain in strains:
    stress, _, _ = model.calculate_stress(strain)
    stresses.append(stress)

# Plot the results
plt.plot(strains, stresses, label="Stress-Strain Curve")
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Cyclic Loading with Kinematic Hardening")
plt.legend()
plt.grid()
plt.show()

# Example 3: Isotropic Hardening with Increasing Plastic Strain
# Define material properties
E = 210000  # Young's modulus (MPa)
sigma_y = 250  # Initial yield stress (MPa)
H = 1000  # Hardening modulus (MPa)

# Initialize the model
model = IsotropicHardeningModel(E, sigma_y, H)

# Define strain increments
strains = np.linspace(0, 0.005, 200)

# Calculate stresses and plastic strains
stresses = []
plastic_strains = []
for strain in strains:
    stress, _, epsilon_p = model.calculate_stress(strain)
    stresses.append(stress)
    plastic_strains.append(epsilon_p)

# Plot the results
plt.plot(strains, stresses, label="Stress-Strain Curve")
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Isotropic Hardening with Increasing Plastic Strain")
plt.legend()
plt.grid()
plt.show()

# Example 4: Comparison of Kinematic and Isotropic Hardening
# Define material properties
E = 210000  # Young's modulus (MPa)
sigma_y = 250  # Initial yield stress (MPa)
H = 1000  # Hardening modulus (MPa)

# Initialize models
model_kinematic = KinematicHardeningModel(E, sigma_y, H)
model_isotropic = IsotropicHardeningModel(E, sigma_y, H)

# Define strain increments
strains = np.linspace(0, 0.004, 200)

# Calculate stresses
stresses_kinematic = []
stresses_isotropic = []
for strain in strains:
    stress_k, _, _ = model_kinematic.calculate_stress(strain)
    stress_i, _, _ = model_isotropic.calculate_stress(strain)
    stresses_kinematic.append(stress_k)
    stresses_isotropic.append(stress_i)

# Plot the results
plt.plot(strains, stresses_kinematic, label="Kinematic Hardening")
plt.plot(strains, stresses_isotropic, label="Isotropic Hardening")
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Comparison of Kinematic and Isotropic Hardening")
plt.legend()
plt.grid()
plt.show()

# Example 5: Unloading After Plastic Deformation
# Define material properties
E = 210000  # Young's modulus (MPa)
sigma_y = 250  # Initial yield stress (MPa)
H = 1000  # Hardening modulus (MPa)

# Initialize the model
model = KinematicHardeningModel(E, sigma_y, H)

# Define strain increments (loading and unloading)
strains = np.linspace(0, 0.003, 100)  # Loading
strains = np.concatenate([strains, np.linspace(0.003, 0, 100)])  # Unloading

# Calculate stresses
stresses = []
for strain in strains:
    stress, _, _ = model.calculate_stress(strain)
    stresses.append(stress)

# Plot the results
plt.plot(strains, stresses, label="Stress-Strain Curve")
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Unloading After Plastic Deformation")
plt.legend()
plt.grid()
plt.show()
