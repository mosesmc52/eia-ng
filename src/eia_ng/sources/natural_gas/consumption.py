from ...datasets.natural_gas_series import (
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
)
from ..base import BaseSource


class NaturalGasConsumption(BaseSource):
    """Natural-gas consumption data queries."""

    def __init__(self, client):
        super().__init__(client, base_endpoint="natural-gas/")

    def delivered_to_consumers(
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

