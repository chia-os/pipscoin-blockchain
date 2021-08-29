from dataclasses import dataclass

from pipscoin.types.blockchain_format.sized_bytes import bytes32
from pipscoin.util.ints import uint32
from pipscoin.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class PoolTarget(Streamable):
    puzzle_hash: bytes32
    max_height: uint32  # A max height of 0 means it is valid forever
