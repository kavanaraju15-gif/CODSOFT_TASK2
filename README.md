# 🎮 Tic-Tac-Toe AI

An AI-powered Tic-Tac-Toe game built using **Python, Streamlit, and the Minimax algorithm** as part of the **CODSOFT Internship – Task 2**.

## 📌 Project Overview

This project is an interactive Human vs AI Tic-Tac-Toe game.

The AI uses the **Minimax algorithm** to analyze possible game states and select the best move.

The game provides three difficulty levels:

- 🟢 **Easy** – AI makes random moves
- 🟡 **Medium** – AI combines intelligent and random moves
- 🔴 **Hard** – AI uses the Minimax algorithm for optimal play

## ✨ Features

- 🎮 Human vs AI gameplay
- 🧠 Minimax-based AI
- 🎚️ Three difficulty levels
- 🏆 Scoreboard
- 🔄 New Game option
- 🤝 Draw detection
- 🎉 Win/Loss detection
- 💻 Interactive Streamlit interface
- 📱 Clean and responsive UI

## 🧠 Algorithm Used

### Minimax Algorithm

Minimax is a decision-making algorithm commonly used in two-player games.

The algorithm:

1. Generates possible future moves.
2. Evaluates each possible game state.
3. Maximizes the AI's score.
4. Minimizes the opponent's score.
5. Selects the best available move.

In this project:

- **X = Human**
- **O = AI**

The AI evaluates possible moves and chooses the move with the highest score.

## 🛠️ Technologies Used

- Python 🐍
- Streamlit
- Minimax Algorithm
- Git & GitHub

## 📂 Project Structure

```text
CODSOFT_TASK2/
│
├── app.py
├── ai.py
├── game.py
├── requirements.txt
├── .gitignore
└── README.md
