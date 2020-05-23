# Robust Oblivious Transfer Protocol
## Objective
- Build a robust routing scheme where the sender and the receiver have n different connections/routes and the task is to send k blocks of data successfully even if up to any e of the n connections are corrupt.
- Using a public-key cryptosystem, say El Gamal, design a Robust Oblivious Transfer protocol between a client A (who has the index i) and server B (who has the array) such that A and B are part of a large network and reliably communicate via the above robust routing mechanism.

# Protocol
The detailed explanation of the two protocols is given in [Robust Oblivious Transfer](./Robust%20Oblivious%20Transfer.pdf)

# Implementation
The code does not establish any actual connection or simulate a network. Messages to be transmitted are just stored in variables, and method to manually corrupt messages is written.    
- Libraries Used: 
	- Crypto - To generate large primes
	- random
	- math
	- numpy - To solve system of linear equations for reconstruction of k blocks

- The digital signature scheme at [https://github.com/karandeepSJ/Digital-Signature](https://github.com/karandeepSJ/Digital-Signature) , which uses discrete log, was used in the robust routing scheme.
- There are 4 classes for the robust routing scheme:
	- `Signer`: Contains the logic for the digital signature of a value
	- `TransmissionBlock`: Class to represent each of the n blocks that are sent over the network. Contains logic to evaluate the polynomial to obtain its value for a random x. Inherits from `Signer` for the signing logic.
	- `Verifier`: Contains logic to verify the digital signature for a single (value, sign) pair.
	- `Reconstructor` :Contains logic to verify all blocks and reconstruct the k degree polynomial after verification. 

- There are 3 classes for the OT protocol: `NetworkNode`, `Client` and `Server`
`NetworkNode` is a general class from which `Server` and `Client` inherit, to represent every node in the network. It contains functions to generate and share private and public key of the node, and functions to construct the n blocks for transmission using `TransmissionBlock` and reconstruction using `Reconstructor`

# Running The Code
After installing all the libraries, simply run 
`python ot.py`
This will ask for various inputs and then simulate the protocol, printing messages that would be sent over the network at each step and also printing the status of verifications of the signatures. 


