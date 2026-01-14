This project uses a Monte Carlo simulation to determine the win probability of a single-player, luck-based card game.

Rules:
- A standard 52-card deck is shuffled
- The player flips cards one-by-one while naming increasing ranks in order: _ace, 2, 3, ..., king (repeated 4 times)_
- If at any position the flipped card matches the rank named, the player loses
- If the player clears the entire deck without a single match, they win

Current findings:
- Through 1,000,000 simulated trials, the win probability is approximately 1.77%
- The average loss position is 11.19

Future work:
- Solve problem analytically and compare with simulation results

Links:
- [Simulation Solution (Python)](simulation.py)
- [Analytical Solution (PDF)] (coming soon)
