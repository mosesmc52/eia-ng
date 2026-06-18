# eia-ng
A Python client for the EIA v2 natural gas API with structured access to production, storage, consumption, imports, exports, prices, and natural-gas-fired electricity generation.

## EIA API Documentation

This library is built on top of the official U.S. Energy Information Administration
(EIA) Open Data API.

For detailed information about datasets, endpoints, parameters, and data definitions,
refer to the official EIA API documentation:

https://www.eia.gov/opendata/documentation.php

## Installation

```bash
pip install eia-ng-client
```

## 3. API key setup

You need a free EIA API key.

1. Register at: https://www.eia.gov/opendata/register.php
2. Set the key as an environment variable:

```bash
export EIA_API_KEY="your_api_key_here"
```
---
## 4. Quick start

```python
from eia_ng import EIAClient

client = EIAClient()

# U.S. natural gas production (monthly)
production = client.natural_gas.production(start="2020-01")
print(production[:3])

# Lower 48 natural gas storage (weekly)
weekly_storage = client.natural_gas.weekly_working_storage(start="2022-01-01")
print(weekly_storage[:3])

# Henry Hub spot prices (daily)
prices = client.natural_gas.spot_prices(start="2023-01-01")
print(prices[:3])
```
---
## 5. Natural gas API overview

### Natural Gas Data

The `natural_gas` source provides access to:

- Production (U.S. total and by state)
- Consumption (U.S. total and by state)
- Weekly working gas storage (by region)
- Underground storage all operators (by geography and metric)
- Imports (pipeline, LNG, compressed)
- Exports (pipeline, LNG, truck, compressed)
- Spot prices (Henry Hub)
- Futures prices (front-month and deferred contracts)

#### Production by State

```python
# Texas natural gas production
tx_prod = client.natural_gas.production(
    start="2020-01",
    state="tx",
)
```


#### Weekly working storage by region

```python
# Lower 48 weekly working gas storage
weekly_storage = client.natural_gas.weekly_working_storage(
    start="2022-01-01",
    region="lower48",
)
```

#### Underground storage all operators

```python
# Texas monthly working gas in underground storage
texas_working_gas = client.natural_gas.underground_storage_all_operators(
    start="2020-01",
    geography="tx",
    metric_type="working_gas",
    frequency="monthly",
)

# U.S. working gas percent change from year ago
us_yoy_pct = client.natural_gas.underground_storage_all_operators(
    start="2020-01",
    geography="us_total",
    metric_type="working_gas_yoy_pct_change",
    frequency="monthly",
)

# Thin wrapper example
base_gas = client.natural_gas.underground_storage_base_gas(
    start="2020-01",
    geography="pa",
)
```

#### Underground storage by type

```python
# U.S. monthly working gas by storage type dataset
storage_type_working_gas = client.natural_gas.underground_storage_type(
    start="2020-01",
    storage_type="working_gas",
    frequency="monthly",
)

# U.S. annual salt cavern withdrawals
salt_withdrawals = client.natural_gas.underground_storage_type(
    start="2015",
    storage_type="salt_withdrawals",
    frequency="annual",
)
```

#### Underground storage capacity and count

```python
# U.S. monthly total underground storage capacity
total_capacity = client.natural_gas.underground_storage_capacity(
    start="2020-01",
    geography="us_total",
    type="total",
    frequency="monthly",
)

# Texas annual working gas storage capacity
tx_working_capacity = client.natural_gas.underground_storage_capacity(
    start="2015",
    geography="tx",
    type="working_gas",
    frequency="annual",
)

# Lower 48 monthly storage field count
lower48_storage_count = client.natural_gas.underground_storage_count(
    start="2020-01",
    geography="lower48",
    frequency="monthly",
)
```

#### LNG storage

```python
# U.S. LNG storage additions
lng_additions = client.natural_gas.lng_storage_additions(
    start="2020-01",
    geography="us_total",
    frequency="monthly",
)

# Texas LNG storage withdrawals
tx_lng_withdrawals = client.natural_gas.lng_storage_withdrawls(
    start="2020-01",
    geography="tx",
    frequency="monthly",
)

# U.S. LNG storage net withdrawals
lng_net_withdrawals = client.natural_gas.lng_storage_net_withdrawls(
    start="2020-01",
    geography="us_total",
    frequency="monthly",
)
```


#### Imports / exports



```python
# Pipeline imports from Canada
imports = client.natural_gas.imports(
    start="2021-01",
    country="canada_pipeline",
)

# Pipeline exports to Mexico
exports = client.natural_gas.exports(
    start="2021-01",
    country="mexico_pipeline",
)
```


#### Futures prices

```python
# Front-month natural gas futures
futures = client.natural_gas.futures_prices(
    start="2023-01-01",
    contract=1,
)
```

### Exploration & Reserves (Annual)

The `exploration_and_reserves` method provides access to EIA **Exploration & Reserves**
(Form-23) data. This data is **annual only** and represents reserve stocks or expected
future production, not current output.

Supported categories:

- Proved associated natural gas reserves (wet)
- Proved nonassociated natural gas reserves (wet)
- Proved natural gas plant liquids (NGL) reserves
- Expected future production of dry natural gas

#### Proved associated natural gas reserves

```python
# U.S. total proved associated natural gas reserves (annual)
reserves_us = client.natural_gas.exploration_and_reserves(
    start="2010",
    resource_category="proved_associated_gas",
)
print(reserves_us[:3])

# Texas proved associated natural gas reserves
reserves_tx = client.natural_gas.exploration_and_reserves(
    start="2010",
    state="tx",
    resource_category="proved_associated_gas",
)
print(reserves_tx[:3])

# Pennsylvania proved nonassociated gas reserves
pa_nonassoc = client.natural_gas.exploration_and_reserves(
    start="2010",
    state="pa",
    resource_category="proved_nonassociated_gas",
)


# U.S. proved NGL reserves
ngl_reserves = client.natural_gas.exploration_and_reserves(
    start="2010",
    resource_category="proved_ngl",
)

# Expected future production of dry natural gas (U.S.)
efp = client.natural_gas.exploration_and_reserves(
    start="2010",
    resource_category="expected_future_gas_production",
)
```



---

## 7. Electricity generation (Natural Gas)


```python
# U.S. electricity generation from natural gas
gen_us = client.electricity.generation_natural_gas(
    start="2020-01",
)

# Utah electricity generation from natural gas
gen_ut = client.electricity.generation_natural_gas(
    start="2020-01",
    state="UT",
)
```



## Returned Data Format

All methods return a list of dictionaries corresponding to rows returned by the EIA API.


You can easily convert the results to pandas using this approach.

```python
import pandas as pd
df = pd.DataFrame(production)

```

---

## 🧪 Testing

This project uses **pytest** for unit and integration tests and runs inside the Poetry virtual environment.

Run the full test suite with:

```bash
poetry run pytest -q

```


## License

MIT
