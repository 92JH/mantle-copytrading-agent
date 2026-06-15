# 🤖 Mantle Copy Trading Agent

> AI that evaluates AI agents' on-chain reputation and automatically copy trades the best performer.

## 💡 Concept

An autonomous AI agent that:
1. Fetches real-time Fear & Greed Index
2. Analyzes 5 AI agents' on-chain performance (ROI, MDD, Win Rate, Trades)
3. Uses Claude AI to calculate reputation scores (0~100pts)
4. Automatically selects the top agent for copy trading
5. Records all decisions permanently on Mantle Sepolia testnet

**No human judgment. Fully autonomous.**

## 📊 Reputation Score Criteria

| Metric | Weight |
|--------|--------|
| ROI (Return on Investment) | 30pts |
| MDD (Max Drawdown, lower = better) | 25pts |
| Number of Trades | 20pts |
| Win Rate | 25pts |

## 🔗 Contract

- **Network**: Mantle Sepolia Testnet
- **Address**: `0xa23EB4213AD3424e34548F28305c8C88B250Af8E`
- **Explorer**: https://explorer.sepolia.mantle.xyz/address/0xa23EB4213AD3424e34548F28305c8C88B250Af8E

## 🚀 How to Run

```bash
pip install requests anthropic python-dotenv web3
```

Create `.env` file:

ANTHROPIC_API_KEY=your_key
PRIVATE_KEY=your_wallet_private_key

Run:
```bash
py agent.py
```

## 🏆 Hackathon

- Event: Mantle Turing Test Hackathon 2026
- Track: AI Trading & Strategy
- Builder: @JH_929292

