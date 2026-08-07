"""
simulator_config.py
--------------------------------
Phase 4F

Configures quantum simulators used by
the Nestlé Distributed Order Management
project.

Supported Simulators
--------------------
1. Qiskit Aer Simulator
2. PennyLane Default Qubit

Author: Sirama Avinash
"""

try:
    from qiskit_aer import AerSimulator
except ImportError:
    AerSimulator = None

try:
    import pennylane as qml
except ImportError:
    qml = None


class SimulatorConfig:

    def __init__(self):

        print("Quantum Simulator Configuration initialized.")

    # ----------------------------------
    # Qiskit
    # ----------------------------------

    def get_qiskit_simulator(self):

        print("\n========== QISKIT SIMULATOR ==========\n")

        if AerSimulator is None:

            raise ImportError(
                "Qiskit Aer is not installed."
            )

        simulator = AerSimulator()

        print("Backend :", simulator.name)

        return simulator

    # ----------------------------------
    # PennyLane
    # ----------------------------------

    def get_pennylane_device(
        self,
        wires=2
    ):

        print("\n========== PENNYLANE DEVICE ==========\n")

        if qml is None:

            raise ImportError(
                "PennyLane is not installed."
            )

        device = qml.device(

            "default.qubit",

            wires=wires,

            shots=None

        )

        print("Device :", device.name)

        print("Wires  :", wires)

        return device