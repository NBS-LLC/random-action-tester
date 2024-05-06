# Random Action Tester

![logo - an image of a cute looking rat, in the 3d animation style of ratatouille, part robot, testing software on a mobile device](/docs/logo-400.jpeg)

## Prerequisites

- Python 3.11
- [pipenv](https://pypi.org/project/pipenv/#installation)

## Installation

1. pipenv shell
1. pipenv install

## Visual Studio Code

- Install the workspace recommendations

## Usage

```bash
> ./start.sh # Starts the app under test, keeps the process running
> python main.py # Execute in a new shell
```

Executes a `WORKFLOW_COUNT` number of workflows, using `STEP_COUNT` number of steps per workflow.

A workflow ends immediately if the `END_GOAL` step is encountered.

Results are sent to standard out in the following format (example workflow run):

```bash
App Under Test: Calculator
Workflow Count: 1
Step Count: 10
End Goal: Clicking: =

Workflow Seed: 1714853697
        Element Count Before Workflow Run: 46

        Clicking: 0
        Clicking: C
        Clicking: 7
        Clicking: C
        Clicking: .
        Clicking: 1
        Clicking: .
        Clicking: 5
        Clicking: =
        End Goal Reached

        Element Count After Workflow Run: 46
        Value of root['(Result)/html[1]/body[1]/div[1]/div[1]/div[2]/input[1]'].value changed from "" to ".1.5".
```
