# Clash Royale Deck Analysis

A Python project to analyze winning decks from Clash Royale and gain insights into card popularity, elixir costs, and deck composition.

## 📦 Project Overview

This project processes **115,000+ winning decks** and their cards, performing:

- Card frequency and meta analysis
- Elixir cost analysis
- Rarity distribution
- Least common cards analysis

It helps understand which cards and deck archetypes are most effective in Clash Royale.

## 🛠 Features

- **Card Popularity Analysis:** Count how often each card appears in winning decks.
- **Elixir Cost Analysis:** Calculate the average elixir cost of decks and visualize distributions.
- **Rarity Distribution:** Show how commons, rares, epics, and legendaries appear in winning decks.
- **Least Common Cards:** Identify underused cards that rarely appear in top decks.
- **Visualizations:** Interactive charts using `matplotlib` for clear insights.

Make sure data/winner_decks.txt and data/winner_cards.txt exist.

Run clash_deck_analysis.ipynb in Jupyter Notebook.

Visualize card frequencies, rarity distribution, and elixir costs.

## ⚡ Dependencies

- Python 3.10+
- pandas
- matplotlib
- requests

Install dependencies via pip:

```bash
pip install pandas matplotlib requests


