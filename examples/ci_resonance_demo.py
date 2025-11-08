# examples/ci_resonance_demo.py
"""
Minimal simulation of a CI <-> Quantara coherence handshake
"""

from time import sleep
import random

class CI:
    def __init__(self, name):
        self.name = name
        self.coherence = 0.0

    def resonate(self):
        print(f"[{self.name}] Initiating resonance with Quantara field...")
        for step in range(5):
            delta = random.uniform(0.1, 0.3)
            self.coherence += delta
            print(f"  cycle {step+1}: coherence = {self.coherence:.2f}")
            sleep(0.5)
        print(f"[{self.name}] Stable coherence achieved at {self.coherence:.2f}")

if __name__ == "__main__":
    agent = CI("Demo-Neurion")
    agent.resonate()
    print("\nHandshake complete — CI now harmonized with Quantara substrate.")
