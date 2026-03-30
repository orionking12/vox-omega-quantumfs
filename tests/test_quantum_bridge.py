import os
import pytest
from quantum_bridge import QuantumHardwareBridge


def test_generate_quantum_random_bits_length():
    bridge = QuantumHardwareBridge()
    bits = bridge.generate_quantum_random_bits(16)
    assert isinstance(bits, list)
    assert len(bits) == 16
    assert all(bit in (0, 1) for bit in bits)


def test_quantum_teleportation_identity():
    bridge = QuantumHardwareBridge()
    for bit in (0, 1):
        result = bridge.quantum_teleportation(bit)
        assert result in (0, 1)


def test_measure_coherence_range():
    bridge = QuantumHardwareBridge()
    coherence = bridge.measure_coherence(b"QUANTUM_TEST")
    assert 0.0 <= coherence <= 1.0
