"""
RiscEmu (c) 2021 Anton Lydike

SPDX-License-Identifier: BSD-2-Clause
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, init=True)
class RunConfig:
    preffered_stack_size: Optional[int] = None
    include_scall_symbols: bool = True
    add_accept_imm: bool = False
    # debugging
    debug_instruction: bool = True
    debug_on_exception: bool = True
    # allowed syscalls
    scall_input: bool = True
    scall_fs: bool = False

