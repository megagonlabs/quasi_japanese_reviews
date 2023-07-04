#!/usr/bin/env python3

import argparse
from pathlib import Path

from asdc.schema.example import VanillaUtterances


def operation(
    *,
    path_in: Path,
    path_out: Path,
    validate: bool,
) -> None:
    path_out.mkdir(exist_ok=True, parents=True)
    with path_in.open() as inf:
        for line in inf:
            vus = VanillaUtterances.model_validate_json(line)

            tmp: str = ""
            for uttr in vus.utterances:
                tmp += f"{uttr.name}\t{uttr.text}\n"

            if validate:
                with path_out.joinpath(f"{vus.docid.id}.tsv").open() as inf:
                    assert inf.read() == tmp
            else:
                with path_out.joinpath(f"{vus.docid.id}.tsv").open("w") as outf:
                    outf.write(tmp)


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, default="/dev/stdin", required=False)
    oparser.add_argument(
        "--output",
        "-o",
        type=Path,
        required=True,
    )
    oparser.add_argument(
        "--validate",
        action="store_true",
    )
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(
        path_in=opts.input,
        path_out=opts.output,
        validate=opts.validate,
    )


if __name__ == "__main__":
    main()
