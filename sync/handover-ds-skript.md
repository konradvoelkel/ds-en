# Prompt for the ds-skript agent

Rewritten 2026-10-17 from ds-en, against ds-skript `772d001` and its live site. The
previous version listed six items; **all of them are done on your side**, verified today by
measuring the live page `deskriptive-statistik/` rather than by reading your commit log:
Google Fonts 0, CDN stylesheets 0, `og:url` 1, `og:site_name` 1, broken `\,^\circ` 0,
`lang="de"` present, 6 lazy images. Nothing from that list is repeated below.

**Re-measure before acting on anything here.** This file has no more authority than a
critique does, and it has been wrong before — four of its items were already fixed upstream
the last time it was rewritten.

---

## The one item: push a mirror to GitHub after every commit

### Why you are being asked

The HHU GitLab refuses git over HTTP to anyone who is not logged in. Measured today:

    GET /voelkel/ds-skript                             -> 200
    GET /voelkel/ds-skript.git/info/refs?service=...   -> 401
    API visibility                                     -> "public"

So the project is public to a browser and closed to a clone. A GitHub runner therefore
cannot read ds-skript at all, and ds-en's staleness check — the thing that tells this
edition when a German block has moved — has **never once succeeded**. Every dispatch since
it was built failed: first on reachability, then, once that was diagnosed, on credentials.
No retry strategy fixes a 401.

Konrad's decision: mirror to GitHub. A second reason he gave for it, which is worth knowing
because it shapes what the mirror is for — **issues are much easier to file on GitHub**, so
the mirror is also where problems with the German edition can be reported.

The repository already exists and is empty:

    https://github.com/konradvoelkel/ds-skript-mirror   (public)

### Why the job belongs to you and not to ds-en

ds-en has no secrets, deliberately, and that property is worth keeping — it is the reason
its whole pipeline can be read by anyone and audited without trust. If ds-en pulled from
GitLab it would need a GitLab token; if it pushed to the mirror it would need a GitHub
token as well. Pushing from your side needs exactly one credential, stored where Konrad
already administers CI variables.

**GitLab stays the source of truth.** The mirror is downstream of you and nothing writes to
it except this job. ds-en only ever reads it.

### What to build

A job in `.gitlab-ci.yml` that runs on pushes to the default branch and mirrors to GitHub.
The shape, not necessarily the wording:

```yaml
mirror-to-github:
  stage: deploy          # or its own; it must not gate pages
  image: alpine/git:latest
  variables:
    GIT_STRATEGY: none   # this job makes its own mirror clone
  script:
    - git clone --mirror "$CI_REPOSITORY_URL" repo.git
    - cd repo.git
    - git push --mirror "https://x-access-token:${GITHUB_MIRROR_TOKEN}@github.com/konradvoelkel/ds-skript-mirror.git"
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

Four things to get right, each of which has a way of going wrong quietly:

* **`--mirror` on both sides.** A plain `git push` sends one branch and leaves the mirror's
  history diverging from yours. ds-en resolves arbitrary commits in it (`git show
  <sha>:<file>` for any commit between two pins), so it needs the real history, not a tip.
* **The token never reaches the log.** Put it in a masked, protected CI variable
  (`GITHUB_MIRROR_TOKEN`) and keep it out of `echo`. A fine-grained GitHub PAT scoped to
  that one repository with Contents: write is enough — nothing broader.
* **`allow_failure: false`.** A silently failing mirror is worse than no mirror: ds-en would
  go on comparing against a frozen copy and reporting "up to date" forever. ds-en now
  refuses to judge staleness if the mirror's newest commit is more than two days old, so a
  stopped job surfaces there within two days — but it should surface in your pipeline the
  same minute.
* **Do not mirror what you do not want published.** `git push --mirror` sends every ref and
  every tag. Check that no branch carries anything you would not put on a public GitHub
  repository; the repository contents themselves are the book, which is already public and
  CC BY-SA, and `todo/`, `transcripts` and `slides25` are gitignored and so are not in git
  at all.

### How to know it worked

Not "the job went green". From ds-en's side the test is:

    git clone --filter=blob:none https://github.com/konradvoelkel/ds-skript-mirror.git
    git -C ds-skript-mirror rev-parse HEAD      # must equal ds-skript's own HEAD

and then, the real one: push a trivial commit to ds-skript and watch ds-en's "upstream
check" workflow run to completion for the first time in its existence.

### The seeding is Konrad's, not yours

The mirror is empty right now. The first push can come from your job once it exists — no
separate seeding step is needed, because `--mirror` sends the whole history whether the
target is empty or not.

---

## Deliberately not suggested

* **Mirroring in the other direction.** GitHub → GitLab would make GitHub the place people
  push to, and the book's home is the university. One direction only.
* **Switching ds-en to read from the mirror permanently as a substitute for talking to
  you.** It already does read the mirror, but the dispatch that triggers the check still
  comes from your pipeline, and the handover of findings still goes through files like this
  one. The mirror is plumbing, not a channel.
