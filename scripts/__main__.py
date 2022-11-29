import test
import argparse
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--data_type', type=str, default='klines')
    parser.add_argument('-feq','--data_frequency', type=str, default='1m')
    parser.add_argument('-tick','--tickers', nargs='+', required=True)
    parser.add_argument('-start','--date_start', type=str, default='2021-10-01')
    parser.add_argument('-end','--date_end', type=str, default='2021-10-02')
    parser.add_argument('-save-dir','--save_dir', type=str, default='.')
    return parser.parse_args()
if __name__ == "__main__":
    opt = parse_opt()
    test.test_script(opt)