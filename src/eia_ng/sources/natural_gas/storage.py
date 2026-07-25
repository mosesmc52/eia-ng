from typing import Any, Optional

from ...datasets.storage_series import (
    BASE_GAS_STORAGE_SERIES_BY_GEOGRAPHY,
    LNG_STORAGE_ADDITIONS,
    LNG_STORAGE_NET_WITHDRAWLS,
    LNG_STORAGE_WITHDRAWLS,
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
from ..base import BaseSource


class NaturalGasStorage(BaseSource):
    """Underground and LNG storage data queries."""

    def __init__(self, client):
        super().__init__(client, base_endpoint="natural-gas/")

    def weekly_working(
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

    def underground_all_operators(
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

    def underground_base_gas(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="base_gas",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_working_gas(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="working_gas",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_total_gas(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="total_gas",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_working_gas_yoy_volume_change(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="working_gas_yoy_volume_change",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_working_gas_yoy_pct_change(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="working_gas_yoy_pct_change",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_injections(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="injections",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_withdrawals(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="withdrawals",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_net_withdrawals(
        self,
        start: str,
        end: Optional[str] = None,
        geography: str = "us_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        return self.underground_all_operators(
            start=start,
            end=end,
            geography=geography,
            metric_type="net_withdrawals",
            frequency=frequency,
            offset=offset,
            length=length,
        )

    def underground_type(
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

    def lng_additions(
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

    def lng_withdrawls(
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

    def lng_net_withdrawls(
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

    def underground_capacity(
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

    def underground_count(
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
