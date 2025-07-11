# Language Learner - Python

This repo is part of the language learner series.

This repo will be filled with exercises and produce a single product

## Repo Structure

```shell

    📁 language-learner-python
    ╠═ 📁 src
    ║  ╠═ 📄 cli.py
    ║  ╠═ 📄 __main__.py
    ║  ╠═ 📁 01-{EX_NAME}
    ║  ╠═ 📁 02-{EX_NAME}
    ║  ╚═ 📁 NN-{EX_NAME}
    ║
    ╠═ 📁 tests
    ║  ╠═ 📁 01-{EX_NAME}
    ║  ╠═ 📁 02-{EX_NAME}
    ║  ╚═ 📁 NN-{EX_NAME}
    ║
    ╠═ 📄 README.md
    ╠═ 📄 HISTORY.md
    ╚═ 📄 EXERCISES.md

Each exercise will have its own subpackage but share a common CLI for triggering and using them

Each exercise will also have its own tests subpackage

`Exercises.md` will contain the descriptions and requirements for each exercise to be completed.

The entire repo should be treated as a single python code base that is pakcaged together and extended 
with new functionaility with each exercise.
