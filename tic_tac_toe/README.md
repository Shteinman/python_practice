# A simple two player Tic Tac Toe game.

## Game design.
This is a multiplayer Tic Tac Toe game where two players take turns marking the spaces in a 3x3 grid. 
The first player to mark three of their marks in a row wins.
This is a simple text-based console application.
The game board is represented as a 3x3 grid. Each cell can contain an empty space (' '), an 'X', or an 'O'.

## Gameplay.
The data structture for the game is a 3x3 matrix
Each turn a player chooses a cell and places their mark ('X' or 'O') in a cell represented by a number from 1 to 9.

## Winning conditions.
The winning conditions are as follows:
1. A row of 3 marks in a row.
2. A column of 3 marks in a column.
3. A diagonal of 3 marks in a diagonal.

## Game loop.
1. Display the current game board.
2. Ask the player to choose a cell to mark.
3. Check if the chosen cell is valid (not already marked).
4. Mark the chosen cell with the player's mark ('X' or 'O').
5. Check if the player has won. If yes, display a congratulatory message and end the game.
6. Check if the game board is full. If yes, display a draw message and end the game.

## Additional features.
2. Implement a scoreboard to keep track of the number of wins for each player.
3. Add a timer to limit the time each player has to make a move. (Not yet included)