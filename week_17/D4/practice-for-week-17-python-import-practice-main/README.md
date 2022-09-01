# Python Import Practice

In this exercise, you will practice importing in Python.

## Phase 1: Exploration

In the `/javascript` directory, you will find a simple command-line game.
Take a look through the code and play with it to get a feel for what the
program is doing.

You can run the game from the `/javascript` directory:

```plaintext
> npm install
> node main.js
```

Make sure to take note of the imports and exports in each file.

## Phase 2: Importing with Python

In the `/python` directory, the same game has been transcribed into Python.
However, it's missing some `import` statements. Your job will be to add these
imports where needed.

Once you're done importing, run the following in the `/python` directory:

```plaintext
> python3 main.py
```

If you are successful, all of the choices should work, except for "4: Slack off"
in the work menu. Move on to phase 3 to implement that choice.

## Phase 3: Transcription

As a final task, transcribe `javascript/office/idle.js` to
`python/office/idle.py`. Take note of the random factor in the `chat` and
`useSocialMedia` functions. You may need to look up how random number
generation can be done in Python!

Once you've completed this, `main.py` should run exactly as `main.js` did!