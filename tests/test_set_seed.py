from __future__ import annotations

import torch

from mteb._set_seed import _set_seed


def test_set_seed_cudnn() -> None:
    # First, make sure they are in an altered state (to test if _set_seed actually changes them)
    torch.backends.cudnn.deterministic = False
    torch.backends.cudnn.benchmark = True

    _set_seed(42)

    assert torch.backends.cudnn.deterministic is True
    assert torch.backends.cudnn.benchmark is False
