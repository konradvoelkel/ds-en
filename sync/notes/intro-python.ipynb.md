# intro-python.ipynb

## Style pass

55 of 79 prose blocks changed, in 26 markdown cells; headings, link texts, maths, the
HTML-commented section stubs in cell 37, the xkcd block and all 26 code cells untouched
(`check_untouched.py HEAD` passes, as do `sync.py align`, `check_english.py`, `nbtext.py
check` and `nbtext.py syntax`).

This is the chapter most readers meet first in the practical half, so the pass was
thorough; "Four things to remember" got the most attention.

Kinds of change:

* **"one" → "you"** everywhere the German *man* had become "one": "Instead of `a == b`
  one writes" → "you write"; "That is why one writes `if items:`" → "you write";
  "Anyone who prefers stricter types can by now work with" → "If you prefer stricter types,
  … are available these days"; "Anyone who would like to learn something about the more
  bizarre corners" → "If you want to explore the more bizarre corners".
* **Verb-final and subject-last shapes turned round.** "By compiling a program … and having
  Python execute the bytecode, more complex tasks can be solved" → "The second is to compile
  a program … and have Python execute that, which is how more complex tasks get done" (and
  the REPL paragraph before it now says "The first is …", so the "two classical ways" are
  actually enumerated); "*Membership of a type* we test with the method `isinstance`" →
  "*Membership of a type* is tested with `isinstance`"; "Object attributes, too, are managed
  in a `dict`" → "live in a `dict`".
* **Nominalisations to verbs.** "a comparison of the representing strings (which is
  something other than a type conversion to the type `str`)" → "comparing the string
  representations (which is not the same as converting to the type `str`)"; "In a method
  declaration there is the option of allowing" → "A method declaration can allow";
  "**Slicing** is what it is called when you select part of a list" → "**Slicing** is the
  name for selecting part of a list".
* **Calques and near-calques replaced.** "is supposed to deliver a string" → "is meant to
  return a string"; "the place where the value sits" → "the slot where the value sits";
  "without taking them over" (*übernehmen*) → "without claiming them"; "whoever really
  means the outer variable has to declare it" → "if you really mean the outer variable, you
  have to say so"; "hang `()` after it" → "put `()` after it"; "takes a little searching
  for" → "takes a little finding"; "it does not become correct by running" → "running it
  does not make it right".
* **The stray "say".** "It draws on the PyPI (Python Package Index), say (the analogue of
  …)" – the German *etwa* had landed in the wrong place. Now "It fetches them from a package
  index, typically PyPI, the Python Package Index (the analogue of CPAN for Perl, CRAN for R
  and CTAN for TeX)". Same meaning (pip is not tied to PyPI), readable sentence.
* **Rhythm in "Four things to remember".** "the interpreter can be used interactively" →
  "the interpreter is there to be used interactively"; "run it instead of thinking about
  it" → "run it rather than puzzling over it"; "Blocks in Python are not delimited by curly
  braces but by indentation. This enforces readable code and punishes sloppiness
  immediately" → "Python marks its blocks by indentation, not by curly braces. That enforces
  readable code, and it punishes sloppiness on the spot"; "Of all programming languages,
  Python is the one with the most public code available" → "No programming language has
  more public code behind it than Python". The closing line "Check it as you would check
  somebody else's code: generated code is somebody else's code" was already English and
  was left exactly as it was; so was "Numbers too, functions too, modules too."
* **Padding cut.** "There is of course a great deal of material on Python by now" → "There
  is, of course, no shortage of material on Python by now"; "it is worth making sure that
  you are working with python3" → "make sure you are working with python3"; "These days that
  usually means in practice that" → "In practice that means … these days".
* **Punctuation.** A few comma splices resolved with the book's spaced en dash
  ("Quotation marks may be single or double – `'Data'` and `"Data"` are the same thing –
  which is handy …"); "and so, when the list is copied, the contents … are not copied with
  it (only the pointers to them are)" style nesting flattened where it occurred.

Deliberately not touched:

* "with the method `isinstance`" (c27.0): `isinstance` is a built-in function, not a method.
  I removed the noun rather than correct it – the German says *Methode*, and
  `programming-stochastics.ipynb`'s notes (decision 3) already flag the same question
  for a human. The same word survives untouched in "A method declaration can allow
  arbitrarily many positional arguments" (c45.0), where the examples are plain functions
  too.
* The "two classical ways of using Python" (c0.5–c0.6) are now explicitly "The first …" /
  "The second …". That is a connective, not a meaning change, but it does make the two
  paragraphs lean on each other; if an upstream edit ever drops one, the other needs a look.
* Cell 12 ("**Dictionaries** are maps with a finite domain; the mathematical statement
  … is written as") and cell 17 ("**Sets** are unordered lists") were already idiomatic
  and are unchanged.
* The bolded lead-ins (**Numbers**, **Strings**, **Truth values and `None`.**, **1. The REPL
  is our friend.** …) are kept verbatim: they function like admonition titles.
* "Python 3.14 … The most recent version as these lines are written" became "The latest
  version at the time of writing"; the version numbers themselves are the book's claim and
  were not touched.

## Title lengthened (2026-10-16)

The chapter title diverges from the German original, deliberately. Both editions had
left this one thin; this edition lengthened it, the original did not (checked at
`2784f10`). `sync.py check` hashes the German side, so the divergence is invisible to it:
if this block ever comes back as stale, re-translate the German sentence and then
re-apply the longer title rather than restoring the short one.

The constraint that shaped the wording is that a chapter title is also the printed
heading in the PDF, so it had to read as a heading and not as a search phrase -- the same
call the original made for its own twelve titles (`todo/seo-kritik-bewertung.md`,
[SEO-8], Variante 2). `short_title` keeps the sidebar short.
