from packaging.version import Version
import torch
print(Version(torch.__version__))
print(Version("2.5.0"))
print(Version(torch.__version__) <= Version("2.5.0"))
