
# Battleships Game

## Deployment

### Heroku Deployment

1. Sign up for a Heroku account [here](https://www.heroku.com/).
2. Install the Heroku CLI on your local machine.
3. Open a terminal and log in to your Heroku account using the command: `heroku login`.
4. Create a new Heroku app using the command: `heroku create`.
5. Deploy your Battleships game to Heroku using: `git push heroku master`.

### GitHub/Heroku Integration

1. Commit your changes to the local repository: `git commit -m "Your commit message"`.
2. Push the changes to GitHub: `git push origin master`.
3. Heroku will automatically pick up the changes from GitHub and deploy the updated version.

### Local Setup

1. Clone the repository: `git clone [<repository-url>](https://github.com/cinko95/battleships)`.
2. Navigate to the project directory: `cd battleships`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the game locally: `python3 run.py`.


## Screenshot

![image](https://github.com/cinko95/battleships/assets/137789244/cb813f9a-7076-4b0a-95f6-512162e3cc0b)
*Battleships game in action.*


## Testing

### Functionality

#### Test 1: Placing Ships
- **Description:** Ensure that ships are placed randomly on the board.
- **Expected Outcome:** Ships are placed without overlapping or going out of bounds.
- **Result:** Passed

#### Test 2: User Guess
- **Description:** Validate user input for row and column guesses.
- **Expected Outcome:** Accept only valid numeric input within the range (0 to 4).
- **Result:** Passed

#### Test 3: Computer Guess
- **Description:** Ensure the computer generates valid random guesses.
- **Expected Outcome:** Computer guesses are within the board's range.
- **Result:** Passed
#### Test 4: Checking Guess
- **Description:** Verify the correctness of hit or miss detection.
- **Expected Outcome:** Correctly identify hits and misses on the board.
- **Result:** Passed
#### Test 5: Game Win
- **Description:** Check if the game correctly identifies a winner.
- **Expected Outcome:** Declare a winner when all ships are sunk.
- **Result:** Passed


### Reach

#### Test 1: Browser Compatibility
- **Description:** Test the game on different browsers (Chrome, Firefox, Safari).
- **Expected Outcome:** Game functions correctly on all browsers.
- **Result:** Passed

#### Test 2: Responsiveness
- **Description:** Test the game's responsiveness on different screen sizes.
- **Expected Outcome:** Game elements adjust appropriately to different screen sizes.
- **Result:** Passed

## Technologies Used

- Python

## Credits

### Content
- Game logic inspired by https://en.wikipedia.org/wiki/Battleship_(game).

### Acknowledgements

- Special thanks to Brian for guidance.
