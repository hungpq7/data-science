from .config import config_display
config_display()

from .alias import (
    np, pd,
    linalg, stats,
    plt, sns,
    sym, nx,
)

from .plotting import plot_vectors

from .hypothesis_testing.z_test import MeanZTest, ProportionZTest