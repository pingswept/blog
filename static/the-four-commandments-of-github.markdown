---
layout: default
title: The four commandments of Github
---

    git pull git@github.com:user/repository.git
    git add .
    git commit -m "This is the commit message"
    git push git@github.com:user/repository.git master

But wait, you screwed up the commit message!

    git commit --amend
    git push -f origin master

