# Contributing to Keeweb Projects

Thank you for your interest in contributing to our family of Keeweb projects :gift:

Below are a list of ways that you can help contribute to our projects, as well as policies and guides that explain how to get started.

Please review everything on this page before you submit your contribution.

<br />

- [Contributing to Keeweb Projects](#contributing-to-keeweb-projects)
  - [Code of Conduct](#code-of-conduct)
  - [Issues, Bugs, Ideas](#issues-bugs-ideas)
  - [Vulnerabilities](#vulnerabilities)
  - [Development](#development)
    - [Before Submitting Pull Requests](#before-submitting-pull-requests)
    - [Conventional Commit Specification](#conventional-commit-specification)
      - [Types](#types)
        - [Example 1:](#example-1)
        - [Example 2:](#example-2)
    - [Referencing Issues](#referencing-issues)
    - [Commenting](#commenting)
    - [Variable \& Method Casing](#variable--method-casing)
    - [Linting](#linting)
    - [Spaces Instead Of Tabs](#spaces-instead-of-tabs)
    - [LF over CRLF](#lf-over-crlf)
      - [Visual Studio Code Users](#visual-studio-code-users)
    - [CI Tests](#ci-tests)
  - [Documentation / Wiki](#documentation--wiki)
  - [Donations](#donations)
  - [Translations](#translations)
  - [Public Relations](#public-relations)

<br />

---

<br />

## Code of Conduct

This project and everyone participating in it is governed by the [KeeWeb Code of Conduct](https://github.com/keeweb/keeweb/blob/master/.github/CODE_OF_CONDUCT.md#readme).

<br />

By participating, you are expected to uphold this code. Please report unacceptable behavior to `antelle.net@gmail.com`.

<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Issues, Bugs, Ideas

Stuff happens, and sometimes as best as we try, there may be issues with KeeWeb that we are unaware of. That is the great thing about open-source; anyone can use the program and contribute to making it better.

<br />

If you have found a bug, have an issue with any of our projects hosted on Github, or maybe even a cool idea; you can let us know by [submitting it](https://github.com/keeweb/keeweb/issues/new/choose). However, before you submit your new issue, bug report, or feature request; head over to the [Issues Section](https://github.com/keeweb/keeweb/issues) and ensure nobody else has already submitted it.

<br />

Once you are sure that your issue is not already being dealt with; submit it [here](https://github.com/keeweb/keeweb/issues/new/choose). You'll be asked to specify exactly what project you're referring to, and what your new submission is for, such as:

- Bug report
- Feature Suggestion

<br />

When submitting, ensure you fill out any of the questions asked of you. If you do not provide enough information, we cannot help. Be as detailed as possible, and provide any logs or screenshots you may have to help us better understand what you mean. Failure to fill out the submission properly may result in it being closed without a response.

<br />

If you are submitting a bug report:

- Explain the issue in detail
- Describe how you expect for a feature to work, and what you're seeing instead of what you expected.
- Provide screenshots, logs, or anything else that can visually help track down the issue.

<br />

If you have a generic question which isn't a bug or feature; you may want to submit it as a [Discussion](https://github.com/keeweb/keeweb/discussions) so that others in the community can respond.

<br />

<div align="center">

[![Submit Issue](https://img.shields.io/badge/submit%20new%20issue-de1f5c?style=for-the-badge&logo=github&logoColor=FFFFFF&link=mailto%3Aantelle.net%40gmail.com)](https://github.com/keeweb/keeweb/issues) [![Create Discussion](https://img.shields.io/badge/create%20discussion-1e5c92?style=for-the-badge&logo=github&logoColor=FFFFFF&link=mailto%3Aantelle.net%40gmail.com)](https://github.com/keeweb/keeweb/discussions)

</div>

<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Vulnerabilities

If you believe that you have found a vulnerability, we would appreciate [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) from you. Since vulnerabilities can be sensitive, we ask that you email all reports to the following address:

<br />

<div align="center">

[![View](https://img.shields.io/badge/antelle.net%40gmail.com-de1f5c?style=for-the-badge&logo=gmail&logoColor=FFFFFF&link=mailto%3Aantelle.net%40gmail.com)](mailto:antelle.net@gmail.com)

</div>

<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Development

If you are looking to contribute to KeeWeb by actually submitting your own code; please review this section completely. There is important information and policies provided below that you must follow for your pull request to get accepted.

The source is here for everyone to collectively share and colaborate on. If you think you have a possible solution to a problem; don't be afraid to get your hands dirty.

Unless you are fixing a known bug, we strongly recommend discussing it with the team by opening a [GitHub Discussion](https://github.com/keeweb/keeweb/discussions) you start in order to ensure your work does not conflict with future plans.

All contributions are made via **Pull Requests**. To make a pull request, you will need a GitHub account; if you are unclear on this process, see GitHub's documentation on forking and pull requests.

<br />

### Before Submitting Pull Requests

- Follow the repository's code formatting conventions (see below);
- Include tests that prove that the change works as intended and does not add regressions;
- Document the changes in the code and/or the project's documentation;
- Your PR must pass the CI pipeline;
- When you fork our repository, ensure you fork the active `develop/*` branch.
- Include a proper git commit message following the [Conventional Commit Specification](https://conventionalcommits.org/en/v1.0.0/#specification).

<br />

If all of these items are checked, the pull request is ready to be reviewed and your pull request's label will be changed to "**Ready for Review**". At this point, a human will need to step in and manually verify your submission.

Once your submission has been tested and verified; it will be merged.

<br />

Before submitting your pull request, please review the following resources:

- [Architecture](https://github.com/keeweb/keeweb/wiki/Architecture)
- [Engineering](https://github.com/keeweb/keeweb/wiki/Engineering)
- [Unsupported Features](https://github.com/keeweb/keeweb/wiki/Unsupported%20Features)
- [Pull Request Guidelines](https://github.com/keeweb/keeweb/blob/master/.github/PULL_REQUEST_TEMPLATE.md#readme)

<br />

### Conventional Commit Specification

When commiting your changes, we require you to follow the Conventional Commit Specification (with a few additions), described below.

**The Conventional Commits** is a specification for the format and content of a commit message. The concept behind Conventional Commits is to provide a rich commit history that can be read and understood by both humans and automated tools. Conventional Commits have the following format:

<br />

```
<type>[(optional <scope>)]: <description>

[optional <body>]

[optional <footer(s)>]
```

#### Types

| Type        | Description |
| ----------- | ----------- |
| `build`     | Alters the build process. E.g: creating a new build task, updating the release script, etc. |
| `chore`     | Technical / preventative maintenance task that is necessary for managing the app or the repo, such as updating grunt tasks, but is not tied to any specific feature. Usually done for maintanence purposes. |
| `ci`        | Changes Continuous Integration (usually `yml` and other configuration files). |
| `docs`      | Change to the website or markdown documents |
| `feat`      | Introduces a new feature |
| `fix`       | Addresses a bug for the end-user |
| `perf`      | Improves performance of algorithms or general execution time of the app, but does not fundamentally change an existing feature. |
| `refactor`  | Change to production code that leads to no behavior difference, E.g. splitting files, renaming internal variables, improving code style |
| `style`     | Updates or reformats the style of the source code, but does not otherwise change the way the app is implemented. Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc) |
| `test`      | Adds or refactors tests, no production code change. Usually changes the suite of automated tests for the app. |
| `revert`    | Reverts a previous commit |

<br />

##### Example 1:

```
feat(core): allow overriding of webpack config
^───^────^  ^────────────────────────────────^
│   │       │
│   │       └───⫸ (DESC):   Summary in present tense. Use lower case not title case!
│   │
│   └───────────⫸ (SCOPE):  The package(s) that this change affects
│
└───────────────⫸ (TYPE):   See list above
```

<br />

##### Example 2:

```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: api|autotype|core|dev|dist|grunt|hbs|kdbx|lang|logs|
  │                          plugin|settings|ui|ux|web|
  │
  └─⫸ Commit Type: build|chore|ci|docs|feat|fix|perf|refactor
                    style|test|revert
```

<br />

### Referencing Issues

If you are pushing a commit which addresses a submitted issue, reference your issue at the end of the commit message. You may also optionally add the major issue to the end of your commit body.

References should be on their own line, following the word `Ref` or `Refs`

```
Title:          fix(onedrive): could not properly sync password vault [#2002]
Description:    The description of your commit

                Ref: #2002, #3004, #3007
```

<br />

### Commenting

Comment your code. If someone else comes along, they should be able to do a quick glance and have an idea of what is going on. Plus it helps novice readers to better understand the process.

<br />

### Variable & Method Casing

When writing your code, ensure you utilize `camelCase` when naming variables and methods.

<br />

### Linting

This app is developed with the following packages installed:

- [eslint](https://www.npmjs.com/package/eslint)
- [eslint-plugin-prettier](https://www.npmjs.com/package/eslint-plugin-prettier)
- [eslint-plugin-babel](https://www.npmjs.com/package/eslint-plugin-babel)
- [eslint-plugin-n](https://www.npmjs.com/package/eslint-plugin-n)

<br />

Ensure you follow the lint rules supplied within our ESLint config file [eslint.config.cjs](https://github.com/keeweb/keeweb/blob/master/eslint.config.cjs). If ESLint throws any errors, you must fix them prior to submitting your PR. 

<br />

The easiest way to lint quickly is to install the following tools: 
- [Visual Studio Code](https://code.visualstudio.com/) >= v1.95
- [VSC Plugin: ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) >= v3.0.10
- [VSC Plugin: Prettier ESLInt](https://marketplace.visualstudio.com/items?itemName=rvest.vs-code-prettier-eslint) >= v6.0.0

<br />

Once the above tools are installed, you may configure the plugins to load up our [eslint.config.cjs](https://github.com/keeweb/keeweb/blob/master/eslint.config.cjs) and Visual Studio Code should start showing any issues automatically in your Visual Studio Code **Output Window**. You may need to restart Visual Studio Code after you install the plugins.

<br >

> [!NOTE]
> We utilize ESLint v9+ and the new **[flat config](https://eslint.org/blog/2022/08/new-config-system-part-2/)** structure. You cannot load our flat config into ESLint v8 or older.

<br />

### Spaces Instead Of Tabs

When writing your code, set your IDE to utilize **spaces**, with a configured size of `4 characters`. Our repo provides a `.editorconfig` file which defines how the file should be formatted. Load that file into programs like Visual Studio code.

<br />

<br />

### LF over CRLF

When editing or creating new files, ensure you have converted the file over to Unix line feeds `LF` and not Windows `Carriage Return (ASCII 13, \r ) Line Feed (ASCII 10, \n ).`

We provide an `.editorconfig` file which automatically sets the default to `LF`, which includes existing files that you open.

```ini
[*]
end_of_line = lf
```

<br />

#### Visual Studio Code Users

If you are using **[Visual Studio Code](https://code.visualstudio.com/)**, install the plugin:

- **[EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)**

<br />

You can also open your VSC settings, and search for the setting **`EOL`**, then change the default value to **`\n`**.

<br />

<p align="center"><img width="80%" style="text-align: center;" src="/docs/img/CONTRIBUTING/vsc/settings_eol.png"></p>

<br />

### CI Tests

When submitting a pull request, all of your changes will be ran through our CI tests to check for issues, including linting. If any errors were found, you will be notified at the bottom of your PR request. You will need to review the test results and fix whatever was found wrong. You'll be expected to correct these issues before your submission will be transferred over for human review.

<br />
<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Documentation / Wiki

KeeWeb has [Wiki pages](https://github.com/keeweb/keeweb/wiki), however it's not possible to contribute with pull requests.
If you would like to improve it, please [open an issue](https://github.com/keeweb/keeweb/issues/new/choose) and submit your changes in Markdown format.

<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Donations

There are two ways of donating:

- join as backer on [OpenCollective](https://opencollective.com/keeweb#support);
- sponsor the developer directly on [GitHub](https://github.com/sponsors/antelle).

Please note: donation does not imply any type of service contract.

<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Translations

All KeeWeb translations are contributed by the community. To improve a translation or add a missing one,
join us on [OneSky](https://keeweb.oneskyapp.com).

<br />

<div align="center">

**[`^        back to top        ^`](#contributing-to-keeweb)**

</div>

<br />

---

<br />

## Public Relations

We would be happy to support you if you decide to post, blog, or review the project,
or provide any other kind of PR. Please [contact the developer](mailto:antelle.net@gmail.com)
if you have anything to share. You can also poke us on [Twitter](https://twitter.com/kee_web).
