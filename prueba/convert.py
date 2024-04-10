from datetime import datetime


def converter(timestamp_ms):
    timestamp_seconds = timestamp_ms / 1000
    fecha = datetime.utcfromtimestamp(timestamp_seconds)

    return fecha
