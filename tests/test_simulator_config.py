from src.quantum.simulator_config import SimulatorConfig

config = SimulatorConfig()

# ----------------------------------
# Qiskit
# ----------------------------------

qiskit_backend = config.get_qiskit_simulator()

print("\nQiskit Backend Loaded")

print(qiskit_backend)

# ----------------------------------
# PennyLane
# ----------------------------------

device = config.get_pennylane_device(
    wires=4
)

print("\nPennyLane Device Loaded")

print(device)