---
title: "docs github and the rascal"
slug: docs-github-and-the-rascal
author: Brandon Stafford
lastmod: 2014-02-22T01:22:11.000Z
date: 2014-02-21T21:49:31.000Z
source: rascalmicro.com
---
## Working with Rascal code on Github ##

All of the code that comes on the Rascal is stored on Github, so you can read it and modify it for your own purposes. The details of how to work with Github are covered fairly well by [the Github help pages][1], but there are some questions that persist. We'll try to nail the most common here.

### Updating a forked repo when a new release comes out ###

If you've forked a copy of the Rascal's web interface, Control Freak, for your own use on Github, eventually you'll want to update it to get new changes. There are three steps to do that: clone your repo to your local machine, update it with the new code, and then push those changes to Github. (Unfortunately, there is no way to import the new code directly to your fork.)

### Step 1: clone your fork and add the official repo as a remote ###
First, you clone your forked repo and add a nickname for the Rascal repo.

```language-bash
git clone https://github.com/your-username-goes-here/control-freak.git
git remote add upstream https://github.com/rascalmicro/control-freak.git
git remote -v # check that it worked
upstream  https://github.com/rascalmicro/control-freak.git (fetch)
upstream  https://github.com/rascalmicro/control-freak.git (push)
```

### Step 2: grab the new code ###
This is the tricky part. The `fetch` step below will likely work fine, but the merge step can often be difficult. Git will try to merge the new code into your repo in a sensible way, but if, for example, you've changed a line and the Rascal folks have also changed the same line, it can't know which one you want. But don't worry-- in the worst case, you can just delete your cloned repo and start fresh. Here are some basic tips for [dealing with merge conflicts][2].

```language-bash
git fetch upstream # This will copy all the new stuff to your local machine
git merge upstream/master # This will try to merge the new stuff into the master branch.
```

### Step 3: push the updated repo back up to Github ###
If you've made it this far, you're probably going to succeed.

```language-bash
git push --tags origin master # the --tags bit pushes new tags as well
```

[1]: https://help.github.com/
[2]: https://github.com/bricoleurs/bricolage/wiki/merging-with-git