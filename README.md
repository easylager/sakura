# Sakura - The Backgammon Board Evaluator

**fastApiProject** is a top-notch Backgammon Evaluation Service built with FastAPI. It is designed to understand and evaluate the state of a Backgammon board and provide insightful strategic guidance based on that.

## What does it do?

**fastApiProject** hosts an `EvaluateBoardService` class containing functionality to evaluate the game's board and determine the winning strategy. 

### Main methods of EvaluateBoardService class:

- `__init__`: Initializes the EvaluateBoardService with board and start position.
- `evaluate_board`: Evaluates the current state of the Backgammon board.
- `determine_winner`: Determines the player with a higher chance of winning given the current position.
- `all_checkers_off`: Verifies if a player has all their checkers off the board.
- `determine_game_type`: Determines the type of game (standard, gammon, backgammon) based on the position of the counters.
- `has_checkers_on_bar_or_first_quarter`: Checks if any checker is on the bar or in the first quarter of the board.
- `has_checkers_outside_home`: Checks if some counters are outside the home board.
- `checkers_in_zone`: Checks the number of counters in a certain zone on the board.

Certainly! Here's a cleaner, more concise markdown version of your "Getting Started" and "Usage" sections for the README, formatted for readability and aesthetics:

---

## Getting Started

To set up and start using the **fastApiProject**, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   ```

2. **Utilize Docker** for installing dependencies and effortlessly running the project:
   ```
   docker build -t fastApiProject .
   docker run -p 80:80 fastApiProject
   ```

3. **Access the API documentation**:
   FastAPI includes an automatic interactive API documentation UI (Swagger UI), which you can access at [http://localhost](http://localhost).

## Usage

Here are some practical examples of how to interact with the FastAPI Server:

### Check win_type = oin:
Execute a POST request to `/evaluate-board` with the following JSON payload:
```
{
  "board": {
    "bar_counts": {
      "12345678-90ab-cdef-1234-567890abcdef": 0,
      "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0
    },
    "points": [
      {
        "checkers_count": 0,
        "number": 24,
        "occupied_by": "12345678-90ab-cdef-1234-567890abcdef"
      }
    ]
  },
  "start_position": {
    "12345678-90ab-cdef-1234-567890abcdef": 0,
    "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0
  }
}
```

### Check win_type = koks:
Execute a POST request to `/evaluate-board` with this JSON:
```
{
  "board": {
    "bar_counts": {
      "12345678-90ab-cdef-1234-567890abcdef": 1,
      "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0
    },
    "points": [
      {
        "checkers_count": 2,
        "number": 2,
        "occupied_by": "12345678-90ab-cdef-1234-567890abcdef"
      }
    ]
  },
  "start_position": {
    "12345678-90ab-cdef-1234-567890abcdef": 0,
    "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0
  }
}
```

### Check win_type = mars:
Execute a POST request to `/evaluate-board` with the following payload:
```
{
  "board": {
    "bar_counts": {
      "12345678-90ab-cdef-1234-567890abcdef": 0,
      "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0
    },
    "points": [
      {
        "checkers_count": 5,
        "number": 15,
        "occupied_by": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  },
  "start_position": {
    "12345678-90ab-cdef-1234-567890abcdef": 0,
    "3fa85f64-5717-4562-b3fc-2c963f66afa6": 0
  }
}
```

---
