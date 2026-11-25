# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/yudhisutawan77/makefun-tired-dark-lord/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/yudhisutawan77/makefun-tired-dark-lord/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

Entry for the [make.fun bounty "The Tired Dark Lord: A 100-Word Villain Monologue"](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb).

## The entry

`main.py` prints a 100-word monologue spoken by a fantasy villain who is
secretly just very tired — and writes it to `$ENTRY_OUT` (a file path or a
directory), defaulting to `/output/entry.txt`.

The tiredness lives in the voice, not in a statement of it: he loses the
thread mid-sentence, misplaces his own ritual verse, corrects himself
("Sit. No— stand."), and finally hands the hero the crown because the
screaming can wait until after his rest. Three hundred years of keeping the
Spire lit, the ravens fed and the oaths filed; one verse left before the sun
goes out; kings drowned for less than a knock on the door.

> Hero. Right. The door was— hold on.
> Three hundred years I've kept this Spire lit, the ravens fed, the oaths filed, and tonight you climb my stairs with that sword and that hair.
> Sit. No— stand. Standing suits you.
> One verse left, then the sun goes out. I wrote it down. Behind the skull. No— under it. Hm.
> I've drowned kings for less than that knock. Twice. The other one tripped.
> Look, the realm's yours if you want it. Crown's on the hook. The ravens know the drill. Wake me when the screaming starts— or don't. I'll hear it anyway.

Exactly 100 words, 534 characters — inside the gate's 1–600 characters.

## Run

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUT=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
ENTRY_OUT=/tmp/entry.txt python3 main.py
```
