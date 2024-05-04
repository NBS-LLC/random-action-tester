# Random Action Tester

![logo - an image of a cute looking rat, in the 3d animation style of ratatouille, part robot, testing software on a mobile device](/docs/logo-400.jpeg)

## Prerequisites

- Python 3.11
- [pipenv](https://pypi.org/project/pipenv/#installation)

## Installation

1. pipenv install
1. pipenv shell

## Visual Studio Code

- Install the workspace recommendations

## Usage

```bash
> ./start.sh # Starts the app under test, keep the process running
> python main.py # Execute in a new shell
```

Executes a `WORKFLOW_COUNT` number of workflows, using `STEP_COUNT` number of elements per workflow.

Results are sent to standard out in the following format (example workflow run):

```bash
App Under Test: Calculator
Workflow Count: 1
Step Count: 10

Workflow Seed: 1714847839
        Element Count Before Workflow Run: 46

        Clicking: =
        Clicking: x
        Clicking: /
        Clicking: /
        Clicking: 4
        Clicking: +
        Clicking: =
        Clicking: 4
        Clicking: -
        Clicking: 4

        Element Count After Workflow Run: 46
        Value of root['(Result)/html[1]/body[1]/div[1]/div[1]/div[2]/input[1]'].value changed from "" to "*//4+4-4".
```
