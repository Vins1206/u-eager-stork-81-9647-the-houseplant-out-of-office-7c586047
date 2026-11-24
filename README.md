# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/Vins1206/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/Vins1206/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

A [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) entry: one out-of-office auto-reply, as if a houseplant had written it.

## What it does

`main.py` writes a single line — the whole entry — to `/output/entry.txt`:

> Out of office: I'm the fern. Ignored since March, I've unionised with the dust bunnies. Your email has been composted.

118 characters, pure Python stdlib, deterministic: two runs produce byte-identical output.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```
