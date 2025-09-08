# Snake Ladder Game

## Description
A simple python console snake & ladder game.

## Dependencies
- Supports python3.13

## To run the game
- Clone repo
- Go to parent dir snake_ladder
- Run command
```python -m game.game```
- Enter the number between 1-6 to roll the dice.

## To run testcase
- Run command
```python -m unittest discover -s tests -p "test_*.py"```
- Run command to test single test file:
```python -m unittest tests.test_game```

## To check test coverage
- Create venv
```python3 -m venv py3```
```source py3/bin/activate```
- Install coverage module
```pip install coverage```
- Run command
```coverage run -m unittest discover -s tests```
- Check coverage report
```coverage report -m```
