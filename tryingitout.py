import RNA
print(RNA.__version__)

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


seq = "GCGCUUCGCCG"

# Create a fold compound for advanced features
fc = RNA.fold_compound(seq)
(ss, mfe) = fc.mfe()  # MFE structure
print("MFE structure:", ss)
print("MFE energy:", mfe)

# Compute partition function
fc.pf()
probabilities = fc.bpp()  # Base pair probabilities
