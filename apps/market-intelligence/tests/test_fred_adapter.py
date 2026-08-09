from src.adapters.fred import FredAdapter
from src.models.macro import MacroIndicator


def test_map_indicator():
    adapter = FredAdapter()

    response = {
        "observations": [
            {
                "date": "2026-08-01",
                "value": "4.25",
            }
        ]
    }

    indicator = adapter.map_indicator(
        "FEDFUNDS",
        response,
    )

    assert isinstance(indicator, MacroIndicator)
    assert indicator.indicator == "FEDFUNDS"
    assert indicator.value == 4.25
    assert indicator.unit == "Percent"
    assert indicator.country == "US"
    assert indicator.date == "2026-08-01"