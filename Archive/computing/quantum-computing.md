# Quantum Computing

Qbit: 
Superposition? 
Parallel Computing?
A function with a secret key within a given range (1- 100)?
On average, how many tries to find secret key?
scaled up N times?
how about processing time?
sqrt(N), log(N) log(log(N)), O(1), 

## Grover's Algorithm

Grover's algorithm can find a specific item in an unsorted database of N items in O(\sqrt{N}) time, whereas a classical algorithm would require O(N) time.

Key Concepts
Quantum Superposition: Quantum bits (qubits) can exist in multiple states simultaneously, allowing the algorithm to explore many possibilities at once.
Quantum Interference: The algorithm uses interference to amplify the probability of the correct solution while reducing the probability of incorrect solutions.
Oracle: A quantum subroutine that marks the correct solution by flipping its phase.
Steps of Grover's Algorithm
Initialization: Prepare the qubits in a superposition of all possible states. This is done using the Hadamard gate, which transforms each qubit into an equal superposition of 0 and 1.

Oracle Query: Apply the oracle function, which flips the phase of the correct solution. This step marks the correct item without revealing its position.

Grover Diffusion Operator: Apply the Grover diffusion operator, which amplifies the probability of the correct solution. This operator consists of:

Inversion about the mean: Reflect the amplitudes of the qubits around their average value.
Iteration: Repeat the oracle query and Grover diffusion operator O(\sqrt{N}) times. Each iteration increases the probability of the correct solution.

Measurement: Measure the qubits. The result will be the index of the correct item with high probability.

Mathematical Representation
The algorithm can be mathematically represented as follows:

Initialization: \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle
Oracle Query:
-|x\rangle & \text{if } x \text{ is the correct solution} \\ |x\rangle & \text{otherwise} \end{cases} $$
Grover Diffusion Operator: D = 2|\psi\rangle \langle \psi| - I where |\psi\rangle is the equal superposition state.
Visualization
Imagine you have a list of items and you want to find one specific item. Grover's algorithm allows you to check multiple items simultaneously and use quantum interference to zero in on the correct item much faster than classical methods.

Applications
Grover's algorithm is useful in various fields, including:

Database Search: Finding a specific record in a large database.
Cryptography: Breaking symmetric cryptographic keys faster than classical brute-force methods.
Optimization Problems: Solving certain types of optimization problems more efficiently.


## Superposition

Classical vs. Quantum States
Classical Bit: In classical computing, a bit can be in one of two states: 0 or 1.
Quantum Bit (Qubit): In quantum computing, a qubit can be in a state of 0, 1, or any quantum superposition of these states.
Superposition Explained
A qubit in superposition is described by a linear combination of its basis states. Mathematically, this is represented as: |\psi\rangle = \alpha |0\rangle + \beta |1\rangle where:

|0\rangle and |1\rangle are the basis states.
\alpha and \beta are complex numbers representing the probability amplitudes of the states.
The probabilities must satisfy |\alpha|^2 + |\beta|^2 = 1.
Visualization
Imagine a sphere (the Bloch sphere) where the north pole represents the state |0\rangle and the south pole represents the state |1\rangle. Any point on the surface of the sphere represents a possible superposition state of the qubit.

Measurement
When you measure a qubit in superposition, it collapses to one of the basis states (0 or 1) with probabilities determined by the amplitudes \alpha and \beta. For example:

If |\alpha|^2 = 0.6 and |\beta|^2 = 0.4, there is a 60% chance of measuring 0 and a 40% chance of measuring 1.
Quantum Gates and Superposition
Quantum gates, such as the Hadamard gate, are used to create and manipulate superposition states. The Hadamard gate, for instance, transforms a qubit from a definite state into an equal superposition of 0 and 1: H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)

Importance in Quantum Computing
Superposition allows quantum computers to process a vast amount of information simultaneously. For example, with n qubits, a quantum computer can represent 2^n states at once, enabling parallel computation on an exponential scale.

Real-World Analogy
Think of a qubit in superposition like a spinning coin. While spinning, the coin is in a state that is neither heads nor tails but a combination of both. Only when you stop and observe the coin does it settle into one of the two states.

## NP problems

NP problems, or Non-deterministic Polynomial time problems, are a class of problems in computational complexity theory. Here’s a detailed explanation:

Definition
NP (Non-deterministic Polynomial time): NP problems are those for which a proposed solution can be verified as correct or incorrect in polynomial time by a deterministic Turing machine. In other words, if you have a solution to an NP problem, you can check its correctness relatively quickly.
Key Concepts
Polynomial Time: An algorithm runs in polynomial time if its running time is upper-bounded by a polynomial expression in the size of the input. For example, O(n^2) or O(n^3) are polynomial times.
Verification: For NP problems, while finding a solution might be difficult, verifying a given solution is efficient (polynomial time).
Examples of NP Problems
Traveling Salesman Problem: Given a list of cities and distances between them, find the shortest possible route that visits each city exactly once and returns to the origin city.
Knapsack Problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
Boolean Satisfiability Problem (SAT): Determine if there exists an assignment of truth values to variables that makes a given Boolean formula true.
NP-Complete Problems
NP-Complete: These are the hardest problems in NP. If any NP-complete problem can be solved in polynomial time, then every problem in NP can be solved in polynomial time. Examples include the SAT problem, the Traveling Salesman Problem, and the Knapsack Problem.
NP vs. P
P (Polynomial time): P problems are those that can be solved in polynomial time by a deterministic Turing machine. All P problems are also NP problems because if you can solve a problem quickly, you can also verify the solution quickly.
Open Question: The famous open question in computer science is whether P = NP. This asks whether every problem whose solution can be quickly verified (NP) can also be quickly solved (P). This is one of the seven "Millennium Prize Problems" with a reward of $1 million for a correct solution.
Real-World Implications
Cryptography: Many cryptographic systems rely on the assumption that certain problems are hard to solve (NP problems). If P = NP were proven true, it could undermine the security of these systems.
Optimization: NP problems are common in optimization scenarios, where finding the best solution among many possibilities is computationally challenging.

## Classical and Quantum Computing

- CC: state = what I see
- QC: state <> what I see
- the state vector
  - continuous
  - the thing the computer actually operates on
  - it has a very unusual relationship with the values that I actually read out.
- the value
  - I read out, and it looks like random.
- run a program on a quantum computer
  - the program doesn't necessarily determine a particular output.
  - it determines a probability distribution across all possible outputs.
  - a k-qubit quantum computer -> there are 2^k distinct possible outputs
  - any program gives a distribution across all of those.
  - and the thing that I read out has k distinct bits.
  - This distribution is implicit. I never actually see it directly.
  - I see what it must be based on the program that I run.
  - I never see all bit strings coexisting at once in some kind of way.
  - I just see one of them, drawn at random, according to this distribution.
- at a lower layer:
  - What I'm describing as reading out from memory looks like a physical measurement.
  - and the randomness stems from the laws of QM.
  - After read out from memory (see a particular value), the underlying state of the computer changes.
- Distribution?
  - where this distribution comes from?
  - The state of the computer as being described by a big vector.
  - State vector -> components in each state(component)? -> 
  - 4 qubit -> 2^4 = 16 components 
  - the state vector <> the probability distribution.
  - take the magnitude of each component -> the probability
  - the observable implication of this -> when I read out from the memory.
  - scale down to 2 bits - two possible outputs 0 and 1
  - a state vector = x|0> + y|1> 
  - P(0) = x^2, 
  - P(1) = y^2,
  - x^2 + y^2 = 1
  - the state vector is bounded onto a unit circle (in 2D)
  - N-Dim -> N-Dim unit sphere 
  - a qubit = a unit vector in a 2-Dim space
  - When see a qubit -> the vector collapses to fall onto the corresponding direction.
- Logic Gates
  - AND
  - OR
  - NOT
- Quantum Gates
  - Applied to a Qubit: flipping or rotating the state vector
  - Hadamard gate: 
    - H|0> -> 1/sqrt(2) (|0> + |1>)
    - H|1> -> 1/sqrt(2) (|1> - |1>)
    - H = 1/sqrt(2) [[1,1],[1,-1]]
    - determining state into a 50-50 equal valanced state
  - Algorithm:
    - compose a bunch of different quantum gates together that will progressively manipulate the state vector.
  - N Qubit -> 2^N component state vector
  - But I have no direct access to the values inside this vector
  - The only way it can be useful is if I have a way to manipulate it in such a way that all of the probability, or at least most of it, gets concentrated on one single component. and if that component corresponds to answer to a question that I care about.
- Grover's Algorithm?
  - Initial State Vector - an equal balance of probability across all possible outcomes.
  - One of the outcomes is going to be the secret key that I'm searching for.
  - The tool that I'll have available, is to flip the sign of the sate vector at that coordinate (the secret key state)
  - the probability mass slowly starts to get concentrated over the secret key value -> read out -> then get the secret key
  - But how do I know the coordinate and make/get the tool?
  - classical logic gates -> translate -> quantum gates
  - the solution -> quantum gate -> unchanged
  - all the quantum operation is linear -> the state is a combination of multiple pure coordinate directions.
  - classical case, the function maps some binary input to 0,
  - quantum translation -> leave the corresponding state unchanged.
  - Any NP problem (verify solution quickly) -> I'm able to create an operation on a quantum computer that flips the sign of a state vector at the position corresponding to a solution of that problem.
  - looks like useless, 
  - another step: slowly amplifies the probability of that key value
  - component of key: 
    - sin(theta) = 1/sqrt(N)
    - theta = 1/sqrt(N) for small theta
  - Quantum Gates -> flip the sign of the key component, all other components keep the same sign
  - let key component -> y axis, other component -> x axis,
  - flip (change sign of the key component) -> flip along x axis 
  - then flop around the off-diagonal direction
  - then the state now points slightly more in the vertical direction 
  - repeat this over and over until the vector points as close as it can get to the secret key direction.
  - How many repetition should be.
  - Overall effect is rotation (theta, 2 theta, 2 theta, under pi/2)
  - repetitions = pi/2 / 2 theta = pi/(4 theta) = pi/(2 * 1/sqrt(N))
  - pi * sqrt(N)/4

## Grover's Algorithm

- Initialization:
  - all qubits into a superposition of all possible states using Hadamard gates
  - |s> = 1/sqrt(N) sum_x_from_0_to_(N-1) |x>
- Oracle Implementation
  - identifies the correct state by flipping its amplitude's phase
  - U_w = 1 - 2|w><w| 
  - Inversion marks the target state without revealing it directly
- Grover Diffusion Operator:
  - reflect all state amplitudes around their average affectively amplifying the probability of the correct state wile reducing that of the incorrect ones.
- Repetition and Measurement:
  - repeated approximately Pi/(4/sqrt(N)) = pi*sqrt(N)/4 
- O(N) problem -> O(sqrt(N)) problem 