# License: MIT
# Copyright © 2024 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.microgrid package."""

from frequenz.microgrid.betterproto.frequenz.api import microgrid


def test_microgrid_betterproto_generated_something() -> None:
    """Test that the generated betterproto code is importable."""
    c = microgrid.Component(id=1, name="test")
    assert c.id == 1
    assert c.name == "test"
