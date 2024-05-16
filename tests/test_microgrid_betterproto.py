# License: MIT
# Copyright © 2024 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.microgrid package."""

from frequenz.microgrid.betterproto.frequenz.api.common.v1.microgrid import components
from frequenz.microgrid.betterproto.frequenz.api.microgrid import v1 as microgrid


def test_microgrid_betterproto_generated_something() -> None:
    """Test that the generated betterproto code is importable."""
    r = microgrid.ListComponentsRequest(
        [1, 2, 3], [components.ComponentCategory.COMPONENT_CATEGORY_BATTERY]
    )
    assert r.component_ids == [1, 2, 3]
    assert r.categories == [components.ComponentCategory.COMPONENT_CATEGORY_BATTERY]
