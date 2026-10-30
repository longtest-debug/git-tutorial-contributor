import numpy as np

def beam_energy(gamma):
    """Calculate electron beam energy in MeV."""
    print('test')
    return gamma * 0.511

print(beam_energy(1000))

def gamma_from_energy(energy):
    """Convert beam energy in MeV to gamma."""
    return energy / 0.511

def kinetic_energy(gamma):
    """Calculate electron kinetic energy in MeV."""
    return (gamma - 1) * 0.511

def momentum_from_gamma(gamma):
    """Calculate electron momentum in MeV/c."""
    return 0.511 * (gamma**2 - 1)**0.5
