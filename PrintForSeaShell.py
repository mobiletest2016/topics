import pandas as pd
import time

symbol='NIFTY'
qty_filename="/tmp/tmpfs/oc/" + symbol + "_qtychange.csv"
oi_filename="/tmp/tmpfs/oc/" + symbol + "_bu.csv"

while True:
    oi_df = pd.read_csv(oi_filename)
    oi_df.set_index('timestamp', inplace=True)
    print(oi_df.tail(10)[['pe_buildup', 'ce_buildup']].style.format({'pe_buildup': '{:,}', 'ce_buildup': '{:,}'}).to_string())
    print('\n')

    qty_df = pd.read_csv(qty_filename)
    qty_df.set_index('timestamp', inplace=True)
    print(qty_df.tail(10)[['pe_sellqty_omo', 'ce_sellqty_omo']].style.format({'pe_sellqty_omo': '{:,}', 'ce_sellqty_omo': '{:,}'}).to_string())

    time.sleep(30)
