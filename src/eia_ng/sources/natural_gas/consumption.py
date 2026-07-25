from typing import Literal, Optional

from ...datasets.consumption_series import (
    CONSUMPTION_COMMERCIAL_ACCOUNT_OF_OTHERS_DELIVERED,
    CONSUMPTION_COMMERCIAL_ACCOUNT_OF_OTHERS_PERCENT,
    CONSUMPTION_COMMERCIAL_AVERAGE_ANNUAL_CONSUMPTION,
    CONSUMPTION_COMMERCIAL_CONSUMERS_COUNT,
    CONSUMPTION_COMMERCIAL_CONSUMERS_SALES_COUNT,
    CONSUMPTION_COMMERCIAL_CONSUMERS_TRANSPORTED,
    CONSUMPTION_END_USE_COMMERCIAL,
    CONSUMPTION_END_USE_DELIVERED_CONSUMERS,
    CONSUMPTION_END_USE_ELECTRIC,
    CONSUMPTION_END_USE_FUEL_CONSUMPTION,
    CONSUMPTION_END_USE_INDUSTRIAL,
    CONSUMPTION_END_USE_RESIDENTIAL,
    CONSUMPTION_HEAT_CONTENT,
    CONSUMPTION_INDUSTRIAL_ACCOUNT_OF_OTHERS_DELIVERED,
    CONSUMPTION_INDUSTRIAL_ACCOUNT_OF_OTHERS_PERCENT,
    CONSUMPTION_INDUSTRIAL_AVERAGE_ANNUAL_CONSUMPTION,
    CONSUMPTION_INDUSTRIAL_CONSUMERS_COUNT,
    CONSUMPTION_INDUSTRIAL_CONSUMERS_SALES_COUNT,
    CONSUMPTION_INDUSTRIAL_CONSUMERS_TRANSPORTED_COUNT,
    CONSUMPTION_RESIDENTIAL_ACCOUNT_OF_OTHERS_DELIVERED,
    CONSUMPTION_RESIDENTIAL_ACCOUNT_OF_OTHERS_PERCENT,
    CONSUMPTION_RESIDENTIAL_CONSUMERS_COUNT,
    CONSUMPTION_RESIDENTIAL_CONSUMERS_SALES_COUNT,
    CONSUMPTION_RESIDENTIAL_CONSUMERS_TRANSPORTED_COUNT,
    CONSUMPTION_SHARE_COMMERCIAL_END_USE,
    CONSUMPTION_SHARE_ELECTRIC_END_USE,
    CONSUMPTION_SHARE_INDUSTRIAL_END_USE,
    CONSUMPTION_SHARE_RESIDENTIAL_END_USE,
    CONSUMPTION_SHARE_VEHICLE_END_USE,
)
from ..base import BaseSource


class NaturalGasConsumption(BaseSource):
    """Natural-gas consumption data queries."""

    ConsumerSector = Literal[
        "residential",
        "commercial",
        "industrial",
    ]

    ConsumerCategory = Literal[
        "total",
        "sales",
        "transported",
    ]

    def __init__(self, client):
        super().__init__(client, base_endpoint="natural-gas/")

    def end_use(
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

    def number_of_consumers(
        self,
        start: str,
        end: Optional[str] = None,
        state: str = "us_total",
        frequency: str = "annual",
        sector: ConsumerSector = "residential",
        category: ConsumerCategory = "total",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "cons/num/data/"
        series_maps = {
            "residential": {
                "total": CONSUMPTION_RESIDENTIAL_CONSUMERS_COUNT,
                "sales": CONSUMPTION_RESIDENTIAL_CONSUMERS_SALES_COUNT,
                "transported": CONSUMPTION_RESIDENTIAL_CONSUMERS_TRANSPORTED_COUNT,
            },
            "commercial": {
                "total": CONSUMPTION_COMMERCIAL_CONSUMERS_COUNT,
                "sales": CONSUMPTION_COMMERCIAL_CONSUMERS_SALES_COUNT,
                "transported": CONSUMPTION_COMMERCIAL_CONSUMERS_TRANSPORTED,
            },
            "industrial": {
                "total": CONSUMPTION_INDUSTRIAL_CONSUMERS_COUNT,
                "sales": CONSUMPTION_INDUSTRIAL_CONSUMERS_SALES_COUNT,
                "transported": CONSUMPTION_INDUSTRIAL_CONSUMERS_TRANSPORTED_COUNT,
            },
        }

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency={frequency!r}. "
                "Number of consumers only supports annual frequency."
            )

        if sector not in series_maps:
            valid_sectors = ", ".join(sorted(series_maps))
            raise ValueError(
                f"Invalid sector={sector!r}. Valid sectors: {valid_sectors}."
            )

        sector_series = series_maps[sector]

        if category not in sector_series:
            valid_categories = ", ".join(sorted(sector_series))
            raise ValueError(
                f"Invalid category={category!r}. Valid categories: {valid_categories}."
            )

        state_series = sector_series[category]

        try:
            series = state_series[state]
        except KeyError as exc:
            valid_states = ", ".join(sorted(state_series))
            raise ValueError(
                f"Invalid state={state!r} for sector={sector!r} "
                f"and category={category!r}. Valid states: {valid_states}."
            ) from exc

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

    def share_delivered_to_consumers(
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

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency={frequency!r}. "
                "Share delivered to consumers only supports annual frequency."
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

    def delivered_for_the_account_of_others(
        self,
        start: str,
        end: Optional[str] = None,
        type: str = "residential",
        measure: str = "delivered",
        state: str = "us_total",
        frequency: str = "annual",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "cons/acct/data/"

        series_maps = {
            "delivered": {
                "residential": (CONSUMPTION_RESIDENTIAL_ACCOUNT_OF_OTHERS_DELIVERED),
                "commercial": (CONSUMPTION_COMMERCIAL_ACCOUNT_OF_OTHERS_DELIVERED),
                "industrial": (CONSUMPTION_INDUSTRIAL_ACCOUNT_OF_OTHERS_DELIVERED),
            },
            "percent": {
                "residential": (CONSUMPTION_RESIDENTIAL_ACCOUNT_OF_OTHERS_PERCENT),
                "commercial": (CONSUMPTION_COMMERCIAL_ACCOUNT_OF_OTHERS_PERCENT),
                "industrial": (CONSUMPTION_INDUSTRIAL_ACCOUNT_OF_OTHERS_PERCENT),
            },
        }

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency={frequency!r}. "
                "Consumption delivered for the account of others "
                "only supports annual frequency."
            )

        if measure not in series_maps:
            valid_measures = ", ".join(sorted(series_maps))
            raise ValueError(
                f"Invalid measure={measure!r}. Valid measures: {valid_measures}."
            )

        measure_series = series_maps[measure]

        if type not in measure_series:
            valid_types = ", ".join(sorted(measure_series))
            raise ValueError(f"Invalid type={type!r}. Valid types: {valid_types}.")

        state_series = measure_series[type]

        try:
            series = state_series[state]
        except KeyError as exc:
            valid_states = ", ".join(sorted(state_series))
            raise ValueError(
                f"Invalid state={state!r} for type={type!r} "
                f"and measure={measure!r}. Valid states: {valid_states}."
            ) from exc

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

    def heat_content(
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
