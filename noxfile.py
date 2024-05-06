# License: MIT
# Copyright © 2024 Frequenz Energy-as-a-Service GmbH

"""Configuration file for nox."""

from frequenz.repo.config import nox
from frequenz.repo.config.nox import default

config = default.lib_config.copy()
# We don't really have a source per-se, as all code in "src" is generated.
config.source_paths = []
nox.configure(config)
