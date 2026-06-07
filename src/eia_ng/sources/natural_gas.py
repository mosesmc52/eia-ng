from typing import Any, Optional

from ..datasets.natural_gas_series import (
    BASE_GAS_STORAGE_SERIES_BY_GEOGRAPHY,
    CONSUMPTION_SERIES_BY_STATE,
    EXPORT_SERIES_BY_COUNTRY,
    FUTURES_SERIES_BY_CONTRACT,
    IMPORT_SERIES_BY_COUNTRY,
    NG_EFP_DRY_BY_STATE,
    NG_PROVED_WET_ASSOC_BY_STATE,
    NG_PROVED_WET_NONASSOC_BY_STATE,
    NGL_PROVED_BY_STATE,
    PRODUCTION_SERIES_BY_STATE,
    UNDERGROUND_STORAGE_INJECTIONS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_NET_WITHDRAWALS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_TOTAL_GAS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_WITHDRAWALS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_WORKING_GAS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_WORKING_GAS_YOY_PERCENT_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_WORKING_GAS_YOY_VOLUME_SERIES_BY_GEOGRAPHY,
    WEEKLY_WORKING_STORAGE_SERIES_BY_REGION,
)
from .base import BaseSource


class NaturalGas(BaseSource):
    def __init__(self, client):
        super().__init__(client, base_endpoint="natural-gas/")

    def storage(
        self,
        start: str,
        end: Optional[str] = None,
        region: str = "lower48",
        frequency: str = "weekly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.weekly_working_storage(
            start=start,
            end=end,
            region=region,
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def weekly_working_storage(
        self,
        start: str,
        end: str = None,
        region: str = "lower48",
        frequency: str = "weekly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        endpoint = "stor/wkly/data/"

        try:
            series = WEEKLY_WORKING_STORAGE_SERIES_BY_REGION[region]
        except KeyError as e:
            valid = ", ".join(sorted(WEEKLY_WORKING_STORAGE_SERIES_BY_REGION.keys()))
            raise ValueError(
                f"Invalid region='{region}'. Valid: {valid}, or 'all'."
            ) from e

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def underground_storage_all_operators(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        metric_type: str = "working_gas",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        # EIA serves both monthly and annual underground storage summaries from
        # the shared summary endpoint.
        endpoint = "stor/sum/data/"

        series_maps = {
            "base_gas": BASE_GAS_STORAGE_SERIES_BY_GEOGRAPHY,
            "working_gas": UNDERGROUND_STORAGE_WORKING_GAS_SERIES_BY_GEOGRAPHY,
            "total_gas": UNDERGROUND_STORAGE_TOTAL_GAS_SERIES_BY_GEOGRAPHY,
            "working_gas_yoy_volume_change": UNDERGROUND_STORAGE_WORKING_GAS_YOY_VOLUME_SERIES_BY_GEOGRAPHY,
            "working_gas_yoy_pct_change": UNDERGROUND_STORAGE_WORKING_GAS_YOY_PERCENT_SERIES_BY_GEOGRAPHY,
            "injections": UNDERGROUND_STORAGE_INJECTIONS_SERIES_BY_GEOGRAPHY,
            "withdrawals": UNDERGROUND_STORAGE_WITHDRAWALS_SERIES_BY_GEOGRAPHY,
            "net_withdrawals": UNDERGROUND_STORAGE_NET_WITHDRAWALS_SERIES_BY_GEOGRAPHY,
        }

        if frequency not in {"monthly", "annual"}:
            raise ValueError(
                f"Invalid frequency='{frequency}'. Valid: annual, monthly."
            )

        try:
            series_map = series_maps[metric_type]
        except KeyError as e:
            valid = ", ".join(sorted(series_maps.keys()))
            raise ValueError(
                f"Invalid metric_type='{metric_type}'. Valid: {valid}."
            ) from e

        try:
            series = series_map[geography]
        except KeyError as e:
            valid = ", ".join(sorted(series_map.keys()))
            raise ValueError(
                f"Invalid geography='{geography}' for metric_type='{metric_type}'. Valid: {valid}."
            ) from e

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def underground_storage_base_gas(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="base_gas",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_working_gas(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="working_gas",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_total_gas(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="total_gas",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_working_gas_yoy_volume_change(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="working_gas_yoy_volume_change",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_working_gas_yoy_pct_change(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="working_gas_yoy_pct_change",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_injections(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="injections",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_withdrawals(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="withdrawals",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_storage_net_withdrawals(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_storage_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="net_withdrawals",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def spot_prices(
        self,
        start: str,
        end: str = None,
        frequency: str = "daily",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "pri/fut/data/"
        series = "RNGWHHD"
        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
        )
        return self.get_series(payload)

    def production(
        self,
        start: str,
        end: str = None,
        state: str = "united_states_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "sum/snd/data/"

        series = PRODUCTION_SERIES_BY_STATE[state]

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def consumption(
        self,
        start: str,
        end: str = None,
        state: str = "united_states_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "sum/snd/data/"
        series = CONSUMPTION_SERIES_BY_STATE[state]

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def imports(
        self,
        start: str,
        end: str = None,
        frequency: str = "monthly",
        country: str = "united_states_pipeline_total",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "move/impc/data/"
        try:
            series = IMPORT_SERIES_BY_COUNTRY[country]
        except KeyError:
            raise ValueError(f"Unsupported export destination: {country}")

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def exports(
        self,
        start: str,
        end: str = None,
        frequency: str = "monthly",
        country: str = "united_states_pipeline_total",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "move/expc/data/"
        try:
            series = EXPORT_SERIES_BY_COUNTRY[country]
        except KeyError:
            raise ValueError(f"Unsupported export destination: {country}")

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def futures_prices(
        self,
        start: str = None,
        end: str = None,
        contract: int = 1,
        frequency: str = "daily",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "pri/fut/data/"
        try:
            series = FUTURES_SERIES_BY_CONTRACT[contract]
        except KeyError:
            raise ValueError(f"Unsupported futures contract: {contract}")

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            data_fields=["value"],
            frequency=frequency,
        )
        return self.get_series(payload)

    def exploration_and_reserves(
        self,
        start: str = None,
        end: str = None,
        frequency: str = "annual",  # locked default
        offset: int = 0,
        length: int = 5000,
        state: str = "all",
        resource_category: str = "proved_associated_gas",
    ):
        """
        Fetch EIA Exploration & Reserves (ENR) data.
        NOTE: ENR data is annual only.
        """

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency='{frequency}'. "
                "Exploration & Reserves data is annual only."
            )

        endpoint = "enr/sum/data/"

        st = (state or "all").strip().lower()

        category_map = {
            "proved_associated_gas": NG_PROVED_WET_ASSOC_BY_STATE,
            "proved_nonassociated_gas": NG_PROVED_WET_NONASSOC_BY_STATE,
            "proved_ngl": NGL_PROVED_BY_STATE,
            "expected_future_gas_production": NG_EFP_DRY_BY_STATE,
        }

        if resource_category not in category_map:
            raise ValueError(
                f"Unsupported resource category: {resource_category}. "
                f"Valid: {sorted(category_map.keys())}"
            )

        series_map = category_map[resource_category]

        try:
            series = series_map[st]
        except KeyError as e:
            raise KeyError(
                f"Unknown state '{state}' (normalized '{st}'). "
                "Expected 2-letter state code or 'us'/'all'."
            ) from e

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            data_fields=["value"],
            frequency="annual",
            offset=offset,
            length=length,
        )
        return self.get_series(payload)
