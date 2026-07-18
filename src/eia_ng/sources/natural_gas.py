from typing import Any, Optional

from ..datasets.natural_gas_series import (
    BASE_GAS_STORAGE_SERIES_BY_GEOGRAPHY,
    CONSUMPTION_DELIVERED_COMMERCIAL_PERCENTAGE,
    CONSUMPTION_DELIVERED_ELECTRIC_PERCENTAGE,
    CONSUMPTION_DELIVERED_INDUSTRIAL_PERCENTAGE,
    CONSUMPTION_DELIVERED_RESIDENTIAL_PERCENTAGE,
    CONSUMPTION_DELIVERED_VEHICLE_PERCENTAGE,
    CONSUMPTION_END_USE_COMMERCIAL,
    CONSUMPTION_END_USE_DELIVERED_CONSUMERS,
    CONSUMPTION_END_USE_ELECTRIC,
    CONSUMPTION_END_USE_FUEL_CONSUMPTION,
    CONSUMPTION_END_USE_INDUSTRIAL,
    CONSUMPTION_END_USE_RESIDENTIAL,
    CONSUMPTION_HEAT_CONTENT,
    CONSUMPTION_SHARE_COMMERCIAL_END_USE,
    CONSUMPTION_SHARE_ELECTRIC_END_USE,
    CONSUMPTION_SHARE_INDUSTRIAL_END_USE,
    CONSUMPTION_SHARE_RESIDENTIAL_END_USE,
    CONSUMPTION_SHARE_VEHICLE_END_USE,
    EXPORT_SERIES_BY_COUNTRY,
    FUTURES_SERIES_BY_CONTRACT,
    IMPORT_SERIES_BY_COUNTRY,
    LNG_STORAGE_ADDITIONS,
    LNG_STORAGE_NET_WITHDRAWLS,
    LNG_STORAGE_WITHDRAWLS,
    NG_EFP_DRY_BY_STATE,
    NG_PROVED_WET_ASSOC_BY_STATE,
    NG_PROVED_WET_NONASSOC_BY_STATE,
    NGL_PROVED_BY_STATE,
    PRODUCTION_SERIES_BY_STATE,
    UNDERGROUND_STORAGE_CAPACITY,
    UNDERGROUND_STORAGE_COUNT,
    UNDERGROUND_STORAGE_INJECTIONS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_NET_WITHDRAWALS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_TOTAL_GAS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_TYPE,
    UNDERGROUND_STORAGE_WITHDRAWALS_SERIES_BY_GEOGRAPHY,
    UNDERGROUND_STORAGE_WORKING_GAS_CAPACITY,
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

    def underground_storage_type(
        self,
        start: str,
        end: Optional[str] = None,
        storage_type: str = "working_gas",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        endpoint = "stor/type/data/"

        if frequency not in {"monthly", "annual"}:
            raise ValueError(
                f"Invalid frequency='{frequency}'. Valid: annual, monthly."
            )

        try:
            series = UNDERGROUND_STORAGE_TYPE[storage_type]
        except KeyError as e:
            valid = ", ".join(sorted(UNDERGROUND_STORAGE_TYPE.keys()))
            raise ValueError(
                f"Invalid storage_type='{storage_type}'. Valid: {valid}."
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

    def consumption_delivered_to_consumers(
        self,
        start: str,
        end: str = None,
        state: str = "us_total",
        type: str = "residential",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "cons/num/data/"
        series_maps = {
            "residential": CONSUMPTION_DELIVERED_RESIDENTIAL_PERCENTAGE,
            "commercial": CONSUMPTION_DELIVERED_COMMERCIAL_PERCENTAGE,
            "industrial": CONSUMPTION_DELIVERED_INDUSTRIAL_PERCENTAGE,
            "vehicle": CONSUMPTION_DELIVERED_VEHICLE_PERCENTAGE,
            "electric": CONSUMPTION_DELIVERED_ELECTRIC_PERCENTAGE,
        }

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency='{frequency}'. Consumption delivered to consumers only supports annual."
            )

        try:
            series_map = series_maps[type]
        except KeyError as e:
            valid = ", ".join(sorted(series_maps.keys()))
            raise ValueError(f"Invalid type='{type}'. Valid: {valid}.") from e

        try:
            series = series_map[state]
        except KeyError as e:
            valid = ", ".join(sorted(series_map.keys()))
            raise ValueError(
                f"Invalid state='{state}' for type='{type}'. Valid: {valid}."
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

    def consumption_end_use(
        self,
        start: str,
        end: str = None,
        state: str = "us_total",
        type: str = "residential",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "cons/sum/data/"
        series_maps = {
            "residential": CONSUMPTION_END_USE_RESIDENTIAL,
            "commercial": CONSUMPTION_END_USE_COMMERCIAL,
            "industrial": CONSUMPTION_END_USE_INDUSTRIAL,
            "vehicle": CONSUMPTION_END_USE_FUEL_CONSUMPTION,
            "electric": CONSUMPTION_END_USE_ELECTRIC,
            "total": CONSUMPTION_END_USE_DELIVERED_CONSUMERS,
        }

        try:
            series_map = series_maps[type]
        except KeyError as e:
            valid = ", ".join(sorted(series_maps.keys()))
            raise ValueError(f"Invalid type='{type}'. Valid: {valid}.") from e

        try:
            series = series_map[state]
        except KeyError as e:
            valid = ", ".join(sorted(series_map.keys()))
            raise ValueError(
                f"Invalid state='{state}' for type='{type}'. Valid: {valid}."
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

    def consumption_heat_content(
        self,
        start: str,
        end: str = None,
        state: str = "us_total",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "cons/heat/data/"

        try:
            series = CONSUMPTION_HEAT_CONTENT[state]
        except KeyError as e:
            valid = ", ".join(sorted(CONSUMPTION_HEAT_CONTENT.keys()))
            raise ValueError(f"Invalid state='{state}'. Valid: {valid}.") from e

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

    def consumption_share_delivered_to_consumers(
        self,
        start: str,
        end: str = None,
        type: str = "residential",
        state: str = "us_total",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "cons/pns/data/"
        series_maps = {
            "residential": CONSUMPTION_SHARE_RESIDENTIAL_END_USE,
            "commercial": CONSUMPTION_SHARE_COMMERCIAL_END_USE,
            "industrial": CONSUMPTION_SHARE_INDUSTRIAL_END_USE,
            "vehicle": CONSUMPTION_SHARE_VEHICLE_END_USE,
            "electric": CONSUMPTION_SHARE_ELECTRIC_END_USE,
        }

        try:
            series_map = series_maps[type]
        except KeyError as e:
            valid = ", ".join(sorted(series_maps.keys()))
            raise ValueError(f"Invalid type='{type}'. Valid: {valid}.") from e

        try:
            series = series_map[state]
        except KeyError as e:
            valid = ", ".join(sorted(series_map.keys()))
            raise ValueError(
                f"Invalid state='{state}' for type='{type}'. Valid: {valid}."
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

    def lng_storage_additions(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "stor/lng/data/"

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency='{frequency}'. LNG storage additions only supports annual."
            )

        try:
            series = LNG_STORAGE_ADDITIONS[geography]
        except KeyError as e:
            valid = ", ".join(sorted(LNG_STORAGE_ADDITIONS.keys()))
            raise ValueError(f"Invalid geography='{geography}'. Valid: {valid}.") from e

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

    def lng_storage_withdrawls(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "stor/lng/data/"

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency='{frequency}'. LNG storage withdrawls only supports annual."
            )

        try:
            series = LNG_STORAGE_WITHDRAWLS[geography]
        except KeyError as e:
            valid = ", ".join(sorted(LNG_STORAGE_WITHDRAWLS.keys()))
            raise ValueError(f"Invalid geography='{geography}'. Valid: {valid}.") from e

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

    def lng_storage_net_withdrawls(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "stor/lng/data/"

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency='{frequency}'. LNG storage net withdrawls only supports annual."
            )

        try:
            series = LNG_STORAGE_NET_WITHDRAWLS[geography]
        except KeyError as e:
            valid = ", ".join(sorted(LNG_STORAGE_NET_WITHDRAWLS.keys()))
            raise ValueError(f"Invalid geography='{geography}'. Valid: {valid}.") from e

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

    def underground_storage_capacity(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        type: str = "total",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "stor/cap/data/"
        series_maps = {
            "total": UNDERGROUND_STORAGE_CAPACITY,
            "working_gas": UNDERGROUND_STORAGE_WORKING_GAS_CAPACITY,
        }

        if frequency not in {"monthly", "annual"}:
            raise ValueError(
                f"Invalid frequency='{frequency}'. Valid: annual, monthly."
            )

        try:
            series_map = series_maps[type]
        except KeyError as e:
            valid = ", ".join(sorted(series_maps.keys()))
            raise ValueError(f"Invalid type='{type}'. Valid: {valid}.") from e

        try:
            series = series_map[geography]
        except KeyError as e:
            valid = ", ".join(sorted(series_map.keys()))
            raise ValueError(
                f"Invalid geography='{geography}' for type='{type}'. Valid: {valid}."
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

    def underground_storage_count(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "stor/cap/data/"

        if frequency not in {"monthly", "annual"}:
            raise ValueError(
                f"Invalid frequency='{frequency}'. Valid: annual, monthly."
            )

        try:
            series = UNDERGROUND_STORAGE_COUNT[geography]
        except KeyError as e:
            valid = ", ".join(sorted(UNDERGROUND_STORAGE_COUNT.keys()))
            raise ValueError(f"Invalid geography='{geography}'. Valid: {valid}.") from e

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
