import logging
import sys
from threading import Thread

import app.models
from app.controllers.streamdata import stream
from app.controllers.webserver import start

import settings


logging.basicConfig(level=logging.INFO, stream=sys.stdout)


if __name__ == "__main__":

    from app.models.dfcandle import DataFrameCandle
    df = DataFrameCandle()    
    df.set_all_candles(limit=1000)
    print(df.optimize_params().__dict__)

    # # streamThread = Thread(target=stream.stream_ingestion_data)
    # serverThread = Thread(target=start)

    # # streamThread.start()
    # serverThread.start()

    # # streamThread.join()
    # serverThread.join()