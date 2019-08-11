#### Vocabulary for Spanish

This project contains several lists of vocabulary --- words and phrases --- for Spanish (Español), as well as other materials like grammar and conjugation.  They are *beginner's* lists totaling around 1000 words.

In my local copy I have some scans of stories that are then marked up with new vocabulary, but these are not in the repo for copyright reasons.

The main item of interest is a python script to drill me on vocabulary.  For example:

```
> cd ~/Github/Español/scripts
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

#### Arguments

- ``new`` drills only on new items
- ``rev`` drills English-to-Spanish
- ``phrases`` drills on phrases
- ``verbs`` drills on verbs
- ``words`` drills on words
- ``words new`` drills on new words

The default is everything.

In addition, there are some experimental flags.  One can provide a number and only that many words are shown, repeatedly.

Also, one can list the first letters of the words to drill on.  For example 'abc' chooses only words starting with those letters.

####

Shell script.  I have a ``bin`` directory on my ``$PATH`` and in there I put ``drill``, which is an executable.  It has one line

```
python ~/Github/Español/scripts/drill.py $1 $2 $3
```

This is a hack.  We don't actually count the environmental vars passed to Python.  But it seems to work fine.

Now I don't have to ``cd`` to the directory or invoke but just do this from the command line:

```
> drill
el huevo
```