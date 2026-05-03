# 🎮 Word Search Puzzle Game

A fast, responsive word search game built with vanilla JavaScript, HTML5, and Tailwind CSS. Find hidden words in an interactive 12×12 grid. No setup required—just open and play!

**[Play Now](#quick-start)** • **[How It Works](#how-to-play)**

---

## ✨ Features

- 🎯 **12×12 Interactive Grid** — Click to select words in any direction
- 🔤 **10-Word Puzzles** — Each game has 10 words to find
- 🌍 **70-Word Bank** — Words across 7 different categories
- ⏱️ **Real-time Timer & Progress** — Track your completion time and find count
- 💡 **Hint System** — Use "Reveal One" to auto-find an unsolved word
- ✨ **Smooth Animations** — Polished UI with hover effects and word-found animations
- 📱 **Fully Responsive** — Works on desktop, tablet, and mobile
- ⚡ **Zero Dependencies** — Pure HTML, CSS, and JavaScript—no build tools needed

---

## 🚀 Quick Start

1. **Clone or download** this repository
2. **Open `app.html`** in your web browser
3. **Start playing!** Find all 10 words to win

That's it. No npm install, no build step, no server needed.

---

## 🎮 How to Play

1. **Select a Word**: Click on a cell to mark your starting position
2. **Complete the Selection**: Click another cell to mark the end position
3. **Valid Selections**: Words must be in a straight line (horizontal, vertical, diagonal, or reverse)
4. **Find All Words**: Locate all 10 hidden words to complete the puzzle
5. **Use Hints**: Click "Reveal One" to automatically find and highlight one word (can be used once per game)
6. **Reset Selection**: Click "Reset Selection" to clear your current selection
7. **Start Over**: Click "New Game" to generate a fresh puzzle

**Pro Tip**: Words can be hidden forwards or backwards, so check both directions!

---

## 📚 Word Categories

Your puzzle includes words from these 7 categories:

| Category | Count | Examples |
|----------|-------|----------|
| 🍎 **Fruits** | 10 | Apple, Banana, Orange, Mango, Cherry |
| 🦁 **Animals** | 10 | Tiger, Elephant, Dolphin, Penguin, Whale |
| 💻 **Technology** | 10 | Computer, Keyboard, Monitor, Network, Software |
| 🖥️ **Programming** | 10 | Python, JavaScript, Rust, Java, TypeScript |
| 🏔️ **Geography** | 10 | Mountain, River, Ocean, Island, Canyon |
| 🎸 **Music** | 10 | Piano, Guitar, Drums, Violin, Saxophone |
| 🛋️ **Furniture** | 10 | Table, Chair, Lamp, Shelf, Mirror |

---

## 🛠️ Technologies Used

- **HTML5** — Page structure and semantic markup
- **CSS3 + Tailwind CSS** — Modern styling with utility-first CSS (CDN)
- **Vanilla JavaScript (ES6+)** — Game logic and interactivity
- **Google Fonts** — Inter font family for typography

---

## 📁 Project Structure

This project is intentionally minimal—it's a **single HTML file** that contains everything:

```
Crossword/
├── app.html          ← Everything you need to run the game
└── README.md         ← This file
```

**Why a single file?** No build step, no dependencies, no friction. Just download and play.

> Note: The `.venv/` directory can be ignored—it's not used by the application.

---

## 📊 Game Specs

- **Grid Size**: 12×12 cells
- **Words Per Puzzle**: 10
- **Total Word Bank**: 70 words across 7 categories
- **Supported Directions**: Horizontal, Vertical, Diagonal, and Reverse (8 directions total)
- **Backend**: None—entirely client-side
- **Data Persistence**: None—all game state is in-memory
- **API Calls**: None required

---

## 🎮 Game Controls

| Action | How |
|--------|-----|
| **Select Word** | Click start cell, then click end cell |
| **Reveal Hint** | Click "Reveal One" button (once per game) |
| **Clear Selection** | Click "Reset Selection" |
| **New Puzzle** | Click "New Game" |
| **View Stats** | Found count, total count, timer, and progress bar visible at top |

---

## 🚀 Future Ideas

Here are some features that could enhance the game:

- 🎯 Difficulty levels (different grid sizes: 8×8 for Easy, 12×12 for Normal, 16×16 for Hard)
- 🎨 Dark mode toggle
- 📊 Leaderboard with fastest completion times
- 💾 Save/load game state (resume later)
- 👥 Multiplayer mode (turn-based or simultaneous)
- 🏷️ Custom word categories selection
- 📱 Progressive Web App (PWA) for offline play
- 🎵 Sound effects and background music

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the game:

1. **Found a Bug?** Open an issue with details about what went wrong
2. **Have a Feature Idea?** Suggest it by opening an issue
3. **Want to Contribute Code?**
   - Fork the repository
   - Create a branch for your feature or fix
   - Make your changes to `app.html`
   - Test thoroughly in your browser
   - Submit a pull request with a clear description

---

## 📝 License

This project is open source and available for anyone to use, modify, and distribute.

---

## 💬 Feedback

If you enjoy the game or have suggestions, feel free to reach out or open an issue on GitHub. Happy word searching! 🎉
