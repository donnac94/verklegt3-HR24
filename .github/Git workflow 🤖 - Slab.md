## GitHub Flow

The default branch for most projects is `main` 

The workflow we follow is called GitHub flow and is documented [here by GitHub](https://docs.github.com/en/get-started/quickstart/github-flow). We recommend reading for more in depth understanding of the flow.

All changes to the code should be applied via pull requests based on the default branch. When you start making a changes you should

1. Create a branch
1. Make your changes to the code
1. Open your Pull Request
1. Request a review
1. Wait for approval
1. Address review comments
1. Merge your pull request (Once approved)
1. Delete your branch

Pull requests should contain **ONE** conceptual change to the code. I.e. one feature, one bugfix, refactor etc. To help enforcing this we should follow some **additional conventions** that will be introduced below.

## Branch naming

Name your branch based on the changes your doing. Try to use branch prefixes the reflect the type of the change (see semantic commit messages for types).  Branch names should use dashed syntax.

The following command creates a branch

```
git checkout -b feat/change-customer-email
```

Example of valid branch names

```
feat/change-customer-email

fix/only-accept-valid-emails

refactor/all-button-components-to-typescript
```

Example of invalid branch names+

```
changeCustomerEmail
newfeature/email-changes
fix/only_accept_invalid_emails
```

## Pull requests

Each project should have a pull request template. [Here](https://github.com/nova-hf/ui/blob/main/.github/pull_request_template.md) is an example of a pull request template we use on one of your projects. If template is not present in the project you are working on please add it.

The pull request description should include info on **what, why and how** like included in the template. **** Screenshots, link to the Asana task and anything that helps the reviewer understanding your changes should be included as well. For example when creating new UI components a screenshot can be very useful but when adding api endpoints a list of new routes will help.

### Pull request title

When creating the title of your pull request you should follow [the guidelines of semantic commit messages found below ](https://devnova.slab.com/posts/git-workflow-%F0%9F%A4%96-g194rsdu#hqs99-semantic-commit-messages)to make sure the the squash merge commit will automatically

## Squash merging

Squash merging is a merge option that allows you to condense the Git history of topic branches when you complete a pull request. Instead of each commit on the topic branch being added to the history of the default branch, a squash merge adds all the file changes to a single new commit on the default branch.

Squash merging should be enforced in all repositories. The main reasons are

1. Keep the history on `main`  is clean and readable and easier to see what work was done in each pull request
1. Helps enforcing the practice of using semantic commit messages so when working on a branch you can do multiple commits, changes, fixes and review addresses but can apply a structured commit message when merging. 

## Semantic commit messages

When squash merging a pull request you should make sure the the commit messages you create follow the guidelines of semantic commit messages. **If you make sure of that you won't need to to any changes when merging.**



![](https://slabstatic.com/prod/uploads/b5eqay87/posts/images/Csq6PvHIC9GxViL1F-RGeZDW.png)

![The title of your pull request automatically becomes the commit message.](https://slabstatic.com/prod/uploads/b5eqay87/posts/images/sVhNy7ww3MHc6-nhUT53E0JR.png)



In short semantic commit messages describes the format of a commit message to ensure cleaner and more readable history and ensures machine readability of commit messages for tasks like autogenerating a change log.

The format is described like this

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

A simple example

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

An example using scope and body

```
refactor(checkout): payment page to typescript

Introcuded typescript in the checkout flow making all forms type safe and
all graphql queries and mutations with typed hooks
```

### Types of commit messages

When setting a type for your pull request commit message (and preferably branch prefix) you should use a type from the spec

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)
- `perf`: (performance improvement)
- `content`: (only changing content that's not in the cms, text, images, etc) 

### Further reading on semantic commit messages

[https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

[https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)

[https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/#ci](https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/#ci)
