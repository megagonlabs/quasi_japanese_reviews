# Quasi Japanese Reviews

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Attribution 4.0 International License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
[![CI](https://github.com/megagonlabs/quasi_japanese_reviews/actions/workflows/ci.yml/badge.svg)](https://github.com/megagonlabs/quasi_japanese_reviews/actions/workflows/ci.yml)
[![Typos](https://github.com/megagonlabs/quasi_japanese_reviews/actions/workflows/typos.yml/badge.svg)](https://github.com/megagonlabs/quasi_japanese_reviews/actions/workflows/typos.yml)

## Overview

This repository contains quasi Japanese reviews written by crowd workers.
Some annotations are also included.

### Hotel reviews (507 reviews)

- [Text](data/text/hotel): ``data/text/hotel/*.txt``
- [JSON](data/vanilla/hotel/quasi_hotel.VanillaUtterance.jsonl): ``data/vanilla/hotel/quasi_hotel.VanillaUtterance.jsonl``
- [SCUD](data/scud/hotel/quasi_hotel.Example.jsonl): ``data/scud/hotel/quasi_hotel.Example.jsonl``

```txt
10月下旬に、札幌市内の●●ホテルに1人で泊まりました。
1人部屋で、広すぎず快適な客室でした。
駅から徒歩で行ける距離で、アクセスが良かったです。
周辺に飲食店街があり、お店選びで結構迷いました。
...
```

### Sightseeing spot reviews (251 reviews)

- [Text](data/text/spot): ``data/text/spot/*.txt``
- [JSON](data/vanilla/spot/quasi_spot.VanillaUtterance.jsonl): ``data/vanilla/spot/quasi_spot.VanillaUtterance.jsonl``
- [SCUD](data/scud/spot/quasi_spot.Example.jsonl): ``data/scud/spot/quasi_spot.Example.jsonl``

```txt
3月に●●ミュージアムに行きました。
新しくリニューアルされてから初めてでしたが、素晴らしかったです。
外観も前の文化遺産の形を残しつつ、でも新しさもあるデザインで個人的にはかなり大好きです。
中も階段は今まで通りで、昔のデザインが楽しめます。
...
```

## Format

Formats of all files in [data](data) are the same as used in [asdc](https://github.com/megagonlabs/asdc).

## License

[Creative Commons Attribution 4.0 International License](LICENSE.txt)

## Citation

```tex
@misc{megagonlabs_quasi_japanese_reviews,
  title={Quasi Japanese Reviews},
  url={https://github.com/megagonlabs/quasi_japanese_reviews},
  author={Yuta Hayashibe},
  year={2023},
}
```
