from packaging.version import parse
import torch
print(parse(torch.__version__).base_version)
print(parse(torch.__version__).base_version <= parse("2.5.0").base_version)
