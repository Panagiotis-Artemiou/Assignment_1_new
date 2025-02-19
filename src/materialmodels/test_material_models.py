import pytest
import numpy as np
from material_models import KinematicHardeningModel, IsotropicHardeningModel

# Common material properties for testing
E = 210000  # Young's modulus (MPa)
sigma_y = 250  # Initial yield stress (MPa)
H = 1000  # Hardening modulus (MPa)

def test_kinematic_hardening_model_elastic():
    model = KinematicHardeningModel(E, sigma_y, H)
    
    # Test elastic behavior (strain below yield)
    strain = 0.001
    stress, is_plastic, epsilon_p = model.calculate_stress(strain)
    
    # Stress should be E * strain in the elastic region
    assert np.isclose(stress, E * strain)
    assert not is_plastic  # No plastic deformation
    assert np.isclose(epsilon_p, 0)  # No accumulated plastic strain

def test_kinematic_hardening_model_plastic():
    model = KinematicHardeningModel(E, sigma_y, H)
    
    # Test plastic behavior (strain beyond yield)
    strain = 0.002
    stress, is_plastic, epsilon_p = model.calculate_stress(strain)
    
    # Stress should be greater than the initial yield stress
    assert stress > sigma_y
    assert is_plastic  # Plastic deformation should occur
    assert epsilon_p > 0  # Accumulated plastic strain should be positive

def test_kinematic_hardening_model_unloading():
    model = KinematicHardeningModel(E, sigma_y, H)
    
    # Load beyond yield
    strain_load = 0.002
    model.calculate_stress(strain_load)
    
    # Unload to elastic region
    strain_unload = 0.001
    stress, is_plastic, epsilon_p = model.calculate_stress(strain_unload)
    
    # Stress should be less than the yield stress after unloading
    assert stress < sigma_y
    assert not is_plastic  # No plastic deformation during unloading
    assert epsilon_p > 0  # Accumulated plastic strain should remain

def test_isotropic_hardening_model_elastic():
    model = IsotropicHardeningModel(E, sigma_y, H)
    
    # Test elastic behavior (strain below yield)
    strain = 0.001
    stress, is_plastic, epsilon_p = model.calculate_stress(strain)
    
    # Stress should be E * strain in the elastic region
    assert np.isclose(stress, E * strain)
    assert not is_plastic  # No plastic deformation
    assert np.isclose(epsilon_p, 0)  # No accumulated plastic strain

def test_isotropic_hardening_model_plastic():
    model = IsotropicHardeningModel(E, sigma_y, H)
    
    # Test plastic behavior (strain beyond yield)
    strain = 0.002
    stress, is_plastic, epsilon_p = model.calculate_stress(strain)
    
    # Stress should be greater than the initial yield stress
    assert stress > sigma_y
    assert is_plastic  # Plastic deformation should occur
    assert epsilon_p > 0  # Accumulated plastic strain should be positive

def test_isotropic_hardening_model_unloading():
    model = IsotropicHardeningModel(E, sigma_y, H)
    
    # Load beyond yield
    strain_load = 0.002
    model.calculate_stress(strain_load)
    
    # Unload to elastic region
    strain_unload = 0.001
    stress, is_plastic, epsilon_p = model.calculate_stress(strain_unload)
    
    # Stress should be less than the yield stress after unloading
    assert stress < sigma_y
    assert not is_plastic  # No plastic deformation during unloading
    assert epsilon_p > 0  # Accumulated plastic strain should remain

