from __future__ import annotations

import qulacs_core

__all__ = ["QuantumCircuitOptimizer", "from_json"]

class QuantumCircuitOptimizer:
    def __init__(self) -> None:
        """
        Constructor
        """
    def merge_all(
        self, circuit: qulacs_core.QuantumCircuit
    ) -> qulacs_core.QuantumGateMatrix: ...
    def optimize(self, circuit: qulacs_core.QuantumCircuit, block_size: int) -> None:
        """
        Optimize quantum circuit
        """
    def optimize_light(self, circuit: qulacs_core.QuantumCircuit) -> None:
        """
        Optimize quantum circuit with light method
        """

def from_json(arg0: str) -> qulacs_core.QuantumCircuit:
    """
    from json string
    """
