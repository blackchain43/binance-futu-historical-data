def test_script(opt):
    from binance_historical_data import BinanceDataDumper
    import datetime

    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump=opt.save_dir,
        data_type=opt.data_type,  # aggTrades, klines, trades
        data_frequency=opt.data_frequency,  # argument for data_type="klines"
    )
    data_dumper.dump_data(
        tickers=opt.tickers,
        date_start=datetime.datetime.strptime(opt.date_start, "%Y-%m-%d").date(),
        date_end=datetime.datetime.strptime(opt.date_end, "%Y-%m-%d").date(),
        is_to_update_existing=False
    )
