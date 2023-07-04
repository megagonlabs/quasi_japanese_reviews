#!/usr/bin/env python3
import argparse
from pathlib import Path

from asdc.schema.example import VanillaUtterances


def operation(
    *,
    path_in: Path,
    path_hotel: Path,
    path_spot: Path,
) -> None:
    hotel_ids = set()
    with path_hotel.open() as inf:
        for line in inf:
            vus = VanillaUtterances.model_validate_json(line)
            hotel_ids.add(vus.docid)

    spot_ids = set()
    with path_spot.open() as inf:
        for line in inf:
            vus = VanillaUtterances.model_validate_json(line)
            spot_ids.add(vus.docid)

    hotel_cnt: int = 0
    spot_cnt: int = 0
    with path_in.open() as inf:
        for line in inf:
            if line.startswith("### Hotel reviews"):
                hotel_cnt = int(line.split("(")[1].split()[0])
            elif line.startswith("### Sightseeing spot reviews"):
                spot_cnt = int(line.split("(")[1].split()[0])

    assert len(hotel_ids) == hotel_cnt
    assert len(spot_ids) == spot_cnt


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, default="/dev/stdin", required=False)
    oparser.add_argument(
        "--hotel",
        type=Path,
        required=True,
    )
    oparser.add_argument(
        "--spot",
        type=Path,
        required=True,
    )
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(
        path_in=opts.input,
        path_hotel=opts.hotel,
        path_spot=opts.spot,
    )


if __name__ == "__main__":
    main()
