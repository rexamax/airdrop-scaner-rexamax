![CI](https://github.com/rexamax/airdrop-scaner-rexamax/actions/workflows/python-ci.yml/badge.svg)

# RexaMax Airdrop Scanner

🚀 **RexaMax Airdrop Scanner** is a Python-based tool that scrapes airdrop data from websites and filters them based on network and reward value.

## Features
- ✅ **Fetches airdrop data** from [airdrops.io](https://airdrops.io/)
- 🎯 **Filters by network** (Ethereum, Solana, etc.)
- 💰 **Filters by reward amount** (removes small airdrops)
- 📂 **Outputs data in JSON format** for further use

## Installation
1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Run the script:
   ```bash
   python rexamax_airdrop.py
   ```

## Configuration
Modify these variables in `rexamax_airdrop.py` to customize filtering:
```python
network_filter = "Ethereum"  # Set to None to disable filtering
min_reward = 10  # Set to 0 to disable reward filtering
```

## Future Improvements
- 📡 Add more sources (CoinMarketCap, Twitter, etc.)
- 🤖 Integrate with Telegram bot
- 🗂 Save results to a file

### Contributions & Feedback
Open to feedback and contributions! 🚀

## Roadmap

- [ ] Add support for Solana network (#1)
- [ ] Create installation guide for Windows and Linux (#2)
- [ ] Add transaction logging to file (#3)

