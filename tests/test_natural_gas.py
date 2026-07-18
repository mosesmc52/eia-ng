# tests/test_natural_gas_new_methods.py
from __future__ import annotations

import pytest

# Update this import path to match your project structure.
# Example options:
#   from eia_ng.source.natural_gas import NaturalGas
#   from eia_ng.sources.natural_gas import NaturalGas
from eia_ng.sources.natural_gas import NaturalGas


@pytest.fixture
def ng():
    """
    Instantiate NaturalGas without relying on its __init__ signature.
    We stub the instance methods used by the public API methods.
    """
    return NaturalGas(client=None)


def _install_spies(monkeypatch, ng, *, fetch_return=None, series_return=None):
    """
    Replace _fetch_data and get_series to:
    - capture call arguments (so we can assert correctness)
    - return deterministic outputs
    """
    calls = {}

    if fetch_return is None:
        fetch_return = {"raw": "payload"}

    if series_return is None:
        series_return = [{"period": "2020-01", "value": 1.0}]

    def _fetch_v2(
        *, start, endpoint, series, frequency, end, data_fields, offset=0, length=5000
    ):
        calls["fetch"] = {
            "start": start,
            "endpoint": endpoint,
            "series": series,
            "frequency": frequency,
            "end": end,
            "data_fields": data_fields,
            "offset": offset,
            "length": length,
        }
        return fetch_return

    def get_series(payload):
        calls["series_payload"] = payload
        return series_return

    for source in (ng, ng.storage, ng.consumption):
        monkeypatch.setattr(source, "_fetch_v2", _fetch_v2, raising=False)
        monkeypatch.setattr(source, "get_series", get_series, raising=False)

    return calls, series_return


def test_storage_default_region_lower48(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.weekly_working(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/wkly/data/"
    assert calls["fetch"]["series"] == "NW2_EPG0_SWO_R48_BCF"
    assert calls["fetch"]["frequency"] == "weekly"
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


def test_storage_invalid_region_raises_valueerror(monkeypatch, ng):

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.weekly_working(start="2020-01-01", region="bad_region")

    msg = str(e.value)
    assert "Invalid region='bad_region'" in msg
    assert "Valid:" in msg
    assert "lower48" in msg
    assert "east" in msg
    assert "or 'all'." in msg


def test_spot_prices_calls_correct_endpoint_and_series(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.spot_prices(start="2020-01-01", frequency="daily")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "pri/fut/data/"
    assert calls["fetch"]["series"] == "RNGWHHD"
    assert calls["fetch"]["frequency"] == "daily"
    assert calls["fetch"]["data_fields"] == ["value"]


def test_production_default_united_states_total(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.production(start="2020-01", state="united_states_total")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "sum/snd/data/"
    assert calls["fetch"]["series"] == "N9070US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]


def test_production_state_tx(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.production(start="2020-01", state="tx", offset=10, length=123)
    assert out == expected

    assert calls["fetch"]["series"] == "NA1160_STX_2"
    assert calls["fetch"]["offset"] == 10
    assert calls["fetch"]["length"] == 123
    assert calls["fetch"]["data_fields"] == ["value"]


def test_consumption_default_united_states_total(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption(start="2020-01", state="united_states_total")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "sum/snd/data/"
    assert calls["fetch"]["series"] == "N9140US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]


def test_consumption_delivered_to_consumers_default_us_residential(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption.delivered_to_consumers(start="2020")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "cons/num/data/"
    assert calls["fetch"]["series"] == "NA1500_NUS_4"
    assert calls["fetch"]["frequency"] == "annual"
    assert calls["fetch"]["data_fields"] == ["value"]


def test_consumption_delivered_to_consumers_state_and_type(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption.delivered_to_consumers(
        start="2020",
        state="tx",
        type="vehicle",
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "cons/num/data/"
    assert calls["fetch"]["series"] == "NA1570_STX_4"
    assert calls["fetch"]["frequency"] == "annual"


def test_consumption_delivered_to_consumers_invalid_frequency_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.consumption.delivered_to_consumers(
            start="2020",
            frequency="monthly",
        )

    msg = str(e.value)
    assert "Invalid frequency='monthly'" in msg
    assert "only supports annual" in msg


def test_consumption_delivered_to_consumers_invalid_type_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.consumption.delivered_to_consumers(
            start="2020",
            type="bad_type",
        )

    msg = str(e.value)
    assert "Invalid type='bad_type'" in msg
    assert "commercial" in msg
    assert "electric" in msg
    assert "industrial" in msg
    assert "residential" in msg
    assert "vehicle" in msg


def test_consumption_delivered_to_consumers_invalid_state_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.consumption.delivered_to_consumers(
            start="2020",
            state="bad_state",
            type="residential",
        )

    msg = str(e.value)
    assert "Invalid state='bad_state'" in msg
    assert "type='residential'" in msg
    assert "tx" in msg
    assert "united_states_total" in msg


def test_consumption_end_use_selects_type_and_state(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption.end_use(
        start="2020", type="industrial", state="tx"
    )

    assert out == expected
    assert calls["fetch"]["endpoint"] == "cons/sum/data/"
    assert calls["fetch"]["series"] == "N3035TX2"
    assert calls["fetch"]["frequency"] == "annual"


def test_consumption_end_use_invalid_type_raises_valueerror(monkeypatch, ng):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError, match="Invalid type='bad_type'"):
        ng.consumption.end_use(start="2020", type="bad_type")


def test_consumption_heat_content_selects_state(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption.heat_content(start="2020", state="tx")

    assert out == expected
    assert calls["fetch"]["endpoint"] == "cons/heat/data/"
    assert calls["fetch"]["series"] == "NGA_EPG0_VGTH_STX_BTUCF"


def test_consumption_heat_content_invalid_state_raises_valueerror(monkeypatch, ng):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError, match="Invalid state='bad_state'"):
        ng.consumption.heat_content(start="2020", state="bad_state")


def test_consumption_share_selects_type_and_state(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption.share_delivered_to_consumers(
        start="2020", type="commercial", state="tx"
    )

    assert out == expected
    assert calls["fetch"]["endpoint"] == "cons/pns/data/"
    assert calls["fetch"]["series"] == "NA1530_STX_4"


def test_consumption_share_invalid_state_raises_valueerror(monkeypatch, ng):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError, match="Invalid state='bad_state'"):
        ng.consumption.share_delivered_to_consumers(
            start="2020", state="bad_state"
        )


def test_imports_default_united_states_pipeline_total(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.imports(start="2020-01", country="united_states_pipeline_total")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "move/impc/data/"
    assert calls["fetch"]["series"] == "N9102US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]


def test_imports_invalid_country_raises_valueerror(monkeypatch, ng):

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.imports(start="2020-01", country="bad_country")

    assert "Unsupported export destination" in str(e.value)
    assert "bad_country" in str(e.value)


def test_exports_default_united_states_pipeline_total(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.exports(
        start="2020-01", country="united_states_pipeline_total", offset=7, length=77
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "move/expc/data/"
    assert calls["fetch"]["series"] == "N9132US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["offset"] == 7
    assert calls["fetch"]["length"] == 77
    assert calls["fetch"]["data_fields"] == ["value"]


def test_exports_invalid_country_raises_valueerror(monkeypatch, ng):

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.exports(start="2020-01", country="bad_country")

    assert "Unsupported export destination" in str(e.value)
    assert "bad_country" in str(e.value)


def test_futures_prices_default_contract_1(monkeypatch, ng):

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.futures_prices(start="2020-01-01", contract=1)
    assert out == expected

    assert calls["fetch"]["endpoint"] == "pri/fut/data/"
    assert calls["fetch"]["series"] == "RNGC1"
    assert calls["fetch"]["frequency"] == "daily"
    # futures_prices ignores offset/length in your implementation
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


def test_futures_prices_invalid_contract_raises_valueerror(monkeypatch, ng):

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.futures_prices(start="2020-01-01", contract=99)

    assert "Unsupported futures contract" in str(e.value)
    assert "99" in str(e.value)


def test_exploration_and_reserves_default_us_total_proved_associated(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.exploration_and_reserves(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "enr/sum/data/"
    # default state="all" -> US total
    assert calls["fetch"]["series"] == "RNGR41NUS_1"
    # recommended default for ENR is annual, but your function controls this:
    assert calls["fetch"]["frequency"] in (
        "annual",
        "daily",
    )  # keep tolerant if you haven't switched yet
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


@pytest.mark.parametrize(
    "resource_category,state,expected_series",
    [
        ("proved_associated_gas", "tx", "RNGR41STX_1"),
        ("proved_nonassociated_gas", "tx", "RNGR31STX_1"),
        ("proved_ngl", "tx", "RL2R01STX_1"),
        ("expected_future_gas_production", "tx", "RNGR11STX_1"),
        # US total variants
        ("proved_associated_gas", "us", "RNGR41NUS_1"),
        ("proved_associated_gas", "all", "RNGR41NUS_1"),
    ],
)
def test_exploration_and_reserves_series_resolution(
    monkeypatch, ng, resource_category, state, expected_series
):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.exploration_and_reserves(
        start="2019-01-01",
        end="2020-12-31",
        frequency="annual",
        offset=12,
        length=345,
        state=state,
        resource_category=resource_category,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "enr/sum/data/"
    assert calls["fetch"]["series"] == expected_series
    assert calls["fetch"]["frequency"] == "annual"
    assert calls["fetch"]["start"] == "2019-01-01"
    assert calls["fetch"]["end"] == "2020-12-31"
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 12
    assert calls["fetch"]["length"] == 345


def test_exploration_and_reserves_invalid_resource_category_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.exploration_and_reserves(
            start="2020-01-01",
            state="tx",
            resource_category="bad_category",
        )

    msg = str(e.value)
    assert "Unsupported resource category" in msg
    assert "bad_category" in msg


def test_exploration_and_reserves_invalid_state_raises_keyerror(monkeypatch, ng):
    _install_spies(monkeypatch, ng)

    # Your fixed implementation raises KeyError for unknown state keys.
    with pytest.raises(KeyError) as e:
        ng.exploration_and_reserves(
            start="2020-01-01",
            state="bad_state",
            resource_category="proved_associated_gas",
        )

    assert "bad_state" in str(e.value)


def test_exploration_and_reserves_annual_only(monkeypatch, ng):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.exploration_and_reserves(
            start="2020-01-01",
            frequency="monthly",
        )

    msg = str(e.value)
    assert "annual only" in msg.lower()


def test_exploration_and_reserves_frequency_forced_annual(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.exploration_and_reserves(
        start="2015-01-01",
        end="2022-12-31",
        state="tx",
        resource_category="proved_associated_gas",
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "enr/sum/data/"
    assert calls["fetch"]["series"] == "RNGR41STX_1"
    assert calls["fetch"]["frequency"] == "annual"
    assert calls["fetch"]["data_fields"] == ["value"]


def test_underground_storage_all_operators_defaults(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_all_operators(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == "N5020US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


def test_underground_storage_all_operators_annual_yoy_pct_for_state(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_all_operators(
        start="2019-01-01",
        end="2024-12-31",
        geography="tx",
        metric_type="working_gas_yoy_pct_change",
        frequency="annual",
        offset=12,
        length=345,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == "N5040TX4"
    assert calls["fetch"]["frequency"] == "annual"
    assert calls["fetch"]["start"] == "2019-01-01"
    assert calls["fetch"]["end"] == "2024-12-31"
    assert calls["fetch"]["offset"] == 12
    assert calls["fetch"]["length"] == 345


@pytest.mark.parametrize(
    "metric_type,geography,expected_series",
    [
        ("base_gas", "us_total", "N5010US2"),
        ("working_gas", "tx", "N5020TX2"),
        ("total_gas", "east", "N5030832"),
        ("working_gas_yoy_volume_change", "pa", "N5040PA2"),
        ("working_gas_yoy_pct_change", "midwest", "N5040854"),
        ("injections", "south_central", "N5050842"),
        ("withdrawals", "mountain", "N5060862"),
        ("net_withdrawals", "pacific", "N5070912"),
    ],
)
def test_underground_storage_all_operators_series_resolution(
    monkeypatch, ng, metric_type, geography, expected_series
):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_all_operators(
        start="2020-01-01",
        geography=geography,
        metric_type=metric_type,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == expected_series
    assert calls["fetch"]["frequency"] == "monthly"


def test_underground_storage_all_operators_invalid_metric_type_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_all_operators(
            start="2020-01-01",
            metric_type="bad_metric",
        )

    msg = str(e.value)
    assert "Invalid metric_type='bad_metric'" in msg
    assert "working_gas" in msg
    assert "net_withdrawals" in msg


def test_underground_storage_all_operators_invalid_frequency_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_all_operators(
            start="2020-01-01",
            frequency="weekly",
        )

    msg = str(e.value)
    assert "Invalid frequency='weekly'" in msg
    assert "annual" in msg
    assert "monthly" in msg


def test_underground_storage_all_operators_invalid_geography_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_all_operators(
            start="2020-01-01",
            geography="bad_geo",
            metric_type="working_gas",
        )

    msg = str(e.value)
    assert "Invalid geography='bad_geo'" in msg
    assert "metric_type='working_gas'" in msg
    assert "us_total" in msg
    assert "tx" in msg


def test_underground_storage_working_gas_wrapper_delegates(monkeypatch, ng):
    delegated = {}

    def _delegate(**kwargs):
        delegated.update(kwargs)
        return [{"value": 1.0}]

    monkeypatch.setattr(
        ng.storage, "underground_all_operators", _delegate, raising=False
    )

    out = ng.storage.underground_working_gas(
        start="2020-01-01",
        end="2020-12-31",
        geography="tx",
        frequency="annual",
        offset=5,
        length=50,
    )

    assert out == [{"value": 1.0}]
    assert delegated == {
        "start": "2020-01-01",
        "end": "2020-12-31",
        "geography": "tx",
        "metric_type": "working_gas",
        "frequency": "annual",
        "offset": 5,
        "length": 50,
    }


def test_underground_storage_working_gas_yoy_pct_change_wrapper_delegates(
    monkeypatch, ng
):
    delegated = {}

    def _delegate(**kwargs):
        delegated.update(kwargs)
        return [{"value": 2.0}]

    monkeypatch.setattr(
        ng.storage, "underground_all_operators", _delegate, raising=False
    )

    out = ng.storage.underground_working_gas_yoy_pct_change(
        start="2021-01-01",
        geography="pa",
    )

    assert out == [{"value": 2.0}]
    assert delegated == {
        "start": "2021-01-01",
        "end": None,
        "geography": "pa",
        "metric_type": "working_gas_yoy_pct_change",
        "frequency": "monthly",
        "offset": 0,
        "length": 5000,
    }


def test_underground_storage_type_defaults(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_type(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/type/data/"
    assert calls["fetch"]["series"] == "N5020US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


def test_underground_storage_type_annual_salt_withdrawals(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_type(
        start="2019-01-01",
        end="2024-12-31",
        storage_type="salt_withdrawals",
        frequency="annual",
        offset=7,
        length=321,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/type/data/"
    assert calls["fetch"]["series"] == "N5450US2"
    assert calls["fetch"]["frequency"] == "annual"
    assert calls["fetch"]["start"] == "2019-01-01"
    assert calls["fetch"]["end"] == "2024-12-31"
    assert calls["fetch"]["offset"] == 7
    assert calls["fetch"]["length"] == 321


@pytest.mark.parametrize(
    "storage_type,expected_series",
    [
        ("base_gas", "N5010US2"),
        ("working_gas", "N5020US2"),
        ("total_gas", "N5030US2"),
        ("injections", "N5050US2"),
        ("withdrawals", "N5060US2"),
        ("net_withdrawals", "N5070US2"),
        ("salt_working_gas", "N5410US2"),
        ("nonsalt_net_withdrawals", "N5560US2"),
    ],
)
def test_underground_storage_type_series_resolution(
    monkeypatch, ng, storage_type, expected_series
):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_type(
        start="2020-01-01",
        storage_type=storage_type,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/type/data/"
    assert calls["fetch"]["series"] == expected_series
    assert calls["fetch"]["frequency"] == "monthly"


def test_underground_storage_type_invalid_storage_type_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_type(
            start="2020-01-01",
            storage_type="bad_type",
        )

    msg = str(e.value)
    assert "Invalid storage_type='bad_type'" in msg
    assert "working_gas" in msg
    assert "nonsalt_net_withdrawals" in msg


def test_underground_storage_type_invalid_frequency_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_type(
            start="2020-01-01",
            frequency="weekly",
        )

    msg = str(e.value)
    assert "Invalid frequency='weekly'" in msg
    assert "annual" in msg
    assert "monthly" in msg


def test_underground_storage_capacity_defaults(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_capacity(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == "N5290US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


@pytest.mark.parametrize(
    "capacity_type,geography,expected_series",
    [
        ("total", "us_total", "N5290US2"),
        ("total", "lower48", "NGM_EPG0_SAC_R48_MMCF"),
        ("working_gas", "tx", "NGA_EPG0_SACW0_STX_MMCF"),
        ("working_gas", "us_total", "NGA_EPG0_SACW0_NUS_MMCF"),
    ],
)
def test_underground_storage_capacity_series_resolution(
    monkeypatch, ng, capacity_type, geography, expected_series
):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_capacity(
        start="2020-01-01",
        geography=geography,
        type=capacity_type,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == expected_series
    assert calls["fetch"]["frequency"] == "monthly"


def test_underground_storage_capacity_invalid_type_raises_valueerror(monkeypatch, ng):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_capacity(
            start="2020-01-01",
            type="bad_type",
        )

    msg = str(e.value)
    assert "Invalid type='bad_type'" in msg
    assert "total" in msg
    assert "working_gas" in msg


def test_underground_storage_capacity_invalid_geography_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_capacity(
            start="2020-01-01",
            geography="bad_geo",
            type="working_gas",
        )

    msg = str(e.value)
    assert "Invalid geography='bad_geo'" in msg
    assert "type='working_gas'" in msg
    assert "us_total" in msg
    assert "tx" in msg


def test_underground_storage_capacity_invalid_frequency_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_capacity(
            start="2020-01-01",
            frequency="weekly",
        )

    msg = str(e.value)
    assert "Invalid frequency='weekly'" in msg
    assert "annual" in msg
    assert "monthly" in msg


def test_underground_storage_count_defaults(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_count(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == "NA1394_NUS_8"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["value"]
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


@pytest.mark.parametrize(
    "geography,expected_series",
    [
        ("us_total", "NA1394_NUS_8"),
        ("lower48", "NGM_EPG0_SAD_R48_COUNT"),
        ("tx", "NA1394_STX_8"),
    ],
)
def test_underground_storage_count_series_resolution(
    monkeypatch, ng, geography, expected_series
):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage.underground_count(
        start="2020-01-01",
        geography=geography,
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/sum/data/"
    assert calls["fetch"]["series"] == expected_series
    assert calls["fetch"]["frequency"] == "monthly"


def test_underground_storage_count_invalid_geography_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_count(
            start="2020-01-01",
            geography="bad_geo",
        )

    msg = str(e.value)
    assert "Invalid geography='bad_geo'" in msg
    assert "us_total" in msg
    assert "tx" in msg


def test_underground_storage_count_invalid_frequency_raises_valueerror(
    monkeypatch, ng
):
    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage.underground_count(
            start="2020-01-01",
            frequency="weekly",
        )

    msg = str(e.value)
    assert "Invalid frequency='weekly'" in msg
    assert "annual" in msg
    assert "monthly" in msg
