#### Vocabulary for Spanish

This project contains several lists of vocabulary --- words and phrases --- for Spanish (Español), as well as other materials like grammar and conjugation.

The local directory also has some scans of stories that are marked up with new vocabulary, but these are not in the repo.

One item of interest is a python script to drill vocabulary.  For example

```
> cd ~/Github/Español
> python drill.py
el tazón	bowl
Si!
el auto	car
..
```

The drill can be run in *either* direction.  Thus

```
> python drill.py rev
English to Spanish
school	escuela
Si!
meat	carne
Si!
..
```

There are only two flags so far.  One is ``new``, which drills only on new words, and the other is ``rev``, which drills English-to-Spanish.