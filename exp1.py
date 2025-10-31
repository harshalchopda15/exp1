from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from IPython.display import display

# 1. Create a 1-qubit circuit
qc = QuantumCircuit(1)

# 2. Set the initial state to |1⟩
# By default, qubits start at |0⟩. We apply an X-gate to flip it to |1⟩.
qc.x(0)

# 3. Apply the sequential circuit: H → S → H → T
qc.h(0)
qc.s(0)
qc.h(0)
qc.t(0)

print("Circuit Diagram:")
display(qc.draw('mpl'))

# --- Analysis Part 1: Final Bloch Vector ---
# We use the statevector_simulator to get the pure quantum state
sv_sim = Aer.get_backend('statevector_simulator')
statevector = sv_sim.run(qc).result().get_statevector()

print("\nAnalysis 1: Final Bloch Vector")
display(plot_bloch_multivector(statevector))

# --- Analysis Part 2: Histogram ---
# We add a measurement and use the qasm_simulator to get counts
qc.measure_all()
qasm_sim = Aer.get_backend('qasm_simulator')
counts = qasm_sim.run(qc, shots=1024).result().get_counts()

print("\nAnalysis 2: Measurement Histogram")
display(plot_histogram(counts))
