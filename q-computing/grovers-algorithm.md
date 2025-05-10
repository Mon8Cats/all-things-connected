# Grover's Algorithm

- Grovers Algorithm — Programming on Quantum Computers — Coding with Qiskit S2E3

## example

```bash
my_list = [1,3,5,2,4,9,5,8,0,7,6] # find 7
# model this using an oracle (a black box, enter a number, ask, get yes or no)
def the_oracle(my_input):
    winner=7
    if my_input is winner:
        response = True
    else:
        response = False
    return response

## to find the answer, how many times should we call the oracle
for index, trial_number in enumerate(my_list):
    if the_oracle(trial_number) is True:
        print('winder found at index %i'%index)
        print('%i calls to the Oracle used'%(index+1))
        break

## call the oracle N/2 times on average
## two bit: 00, 01, 10, 11 state, let the true state is 11
## |11> -> [CZ] -> -|11> through a unitary matrix : controlled-Z gate
## amplitude amplification: the reflection operator 
## Grover's diffusion operator: [Oracle] + [Reflection]

from giskit import *
import matplotlib.pyplot as plt
import numpy as np

# define the oracle circuit
oracle = QuantumCircuit(2,name='oracle') # two qubit
oracle.cz(0,1) # gate: flips the sign of our winning state
oracle.to_gate() # make the oracle into its own gate
oracle.draw()

## the simulator backend
backend = Aer.get_backend('statevector_simulator)
grover_circ = QuantumCircuit(2,2) 
## two gubits, two classical registers
grover_circ.h([0,1]) 
## add Hadamard gates on both of my qubits 0 and 1
## this prepares my superposition state s
grover_circ.append(oracle,[0,1]) ## query each of the state at the same time
grover_circ.draw()
job = execute(grover_circ,backend)
result = job.result()
sv = result.get_statevector()
np.around(sv,2)
## we prepared the superposition state, 
## and we get back to the same state,
## but with the 11 state flipped.
## need square the state factor in order to get back to probabilities

|w> = [0 0 0 1] = |11>
|s> = (1/2)*[1 1 1 1] 
|s'> = 1/sqrt(3) [1 1 1 0] # orthogonal to |w>
|s> -> oracle -> [1 1 1 -1]
|s><s| - 1
|s> -> ?

reflection = QuantumCircuit(2,name='reflection')
reflection.h([0,1]) # hadmard
reflection.z([0,1]) # what is z?
reflection.cz(0,1) # control z
reflection.h([0,1])
reflection.to_gate()
reflection.draw()

backend = Aer.get_backend('qasm_simulator')
grover_circ=QuantumCircuit(2,2)
grover_circ.h([0,1])
grover_circ.append(oracle,[0,1])
grover_circ.append(reflection,[0,1])
grover_circ.measure([0,1],[0,1])

grover_circ.draw()

job=execute(grover_circ,backend,shots=1)
result=job.result()
result.get_counts() 
## {'11':1}
## we need N calls to the oracle if we have an N size list
```