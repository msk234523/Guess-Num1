# Guess-Num1

A Python number guessing game with Japanese and English prompts.

## 🎮 Game Features

- **Random number generation** — Picks a secret number between 1 and 100
- **Feedback** — Shows "Too high" or "Too low" after each guess
- **Attempt tracking** — Counts how many guesses it takes to win
- **Game statistics** — Displays total games played and average attempts per game
- **Bilingual prompts** — Japanese and English messages
- **Replay support** — Play multiple rounds in one session
- **Input validation** — Handles non-numeric and out-of-range input gracefully

## 🚀 How to Run

```bash
python guessing_game.py
```

## 📝 Example Gameplay

```
==================================================
🎮 数字当てゲームへようこそ！
Welcome to the Number Guessing Game!
==================================================

🎯 新しいゲームを開始します。1～100の数字を当ててください。
New game started. Guess a number between 1 and 100.

➜ あなたの予想: 50
📉 もっと小さい数字です！ (Too high!) - 試行回数: 1回

➜ あなたの予想: 25
📈 もっと大きい数字です！ (Too low!) - 試行回数: 2回

...

🎉 ========================================
🎊 恭喜通過！おめでとうございます！
   Congratulations! You got it right!
========================================
✨ 正解の数字: 37
   Correct number: 37
✨ 試行回数: 5回
   Attempts: 5
```