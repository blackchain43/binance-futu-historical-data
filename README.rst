========================
binance_futu_historical_data
========================

.. contents:: **Table of Contents**


Installation dependencies:
======================

.. code-block:: bash

    poetry install

How to use it
===========================

Run the script with the following command
---------------------------------------------

.. code-block:: bash

    poetry run python scripts -t klines -feq 1m -tick BTCUSDT ETHUSDT -start 2021-10-01 -end 2021-10-3 -save-dir

Arguments:

#. **t**:
    | data type: data type to dump: [aggTrades, klines, trades]
#. **feq**:
    | One of [1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h]
    | Frequency of price-volume data candles to get
#. **tick**:
    | Multiple value argument for tickers to get data for
#. **start**:
    | Start date of data to get
#. **end**:
    | End date of data to get
#. **save-dir**:
    | Directory to save data to



License
=======

This project is licensed under the MIT License.