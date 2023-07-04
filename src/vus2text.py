#!/usr/bin/env python3

import argparse
from pathlib import Path

from asdc.schema.example import VanillaUtterances


def operation(
    *,
    path_in: Path,
    path_out: Path,
) -> None:
    path_out.mkdir(exist_ok=True, parents=True)
    with path_in.open() as inf:
        for line in inf:
            vus = VanillaUtterances.model_validate_json(line)
            with path_out.joinpath(f"{vus.docid.id}.tsv").open("w") as outf:
                for uttr in vus.utterances:
                    outf.write(f"{uttr.name}\t{uttr.text}\n")


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument(
        "--input", "-i", type=Path, default="/dev/stdin", required=False
    )
    oparser.add_argument(
        "--output",
        "-o",
        type=Path,
        required=True,
    )
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(
        path_in=opts.input,
        path_out=opts.output,
    )


if __name__ == "__main__":
    main()
