# AI-Powered Automated Trading Platform

This project is a fully automated trading platform that combines TradingView signals (Pine Script), real-time execution on OKX, historical backtesting, and AI-enhanced signal validation.

---

## 📌 Features

- 🔁 **Real-Time Trading** with TradingView webhook integration
- 📈 **Backtesting Engine** using historical OHLCV + signal replay
- 🧠 **Signal Generation & AI Validation Layer**
- 🧾 **Trade Logging & Monitoring Dashboard**
- 📬 **Telegram/Email Notification System**
- 🔐 Secure API key handling and trade execution
- 🌐 Deployable with Docker on any VPS (DigitalOcean, Hetzner, AWS)

---

## 🧱 System Architecture

[TradingView + Pine Script Alerts]
↓ (webhook)
[Webhook Receiver API]
↓
[Signal Parser & Validator Layer]
↓
[OKX Trading Engine]
↓
[Logs & Notifications]
↓
[Web Dashboard UI]


---

## 🗂️ Modules Overview

| Module | Description |
|--------|-------------|
| `webhook-api` | Accepts and validates incoming signals from TradingView |
| `executor` | Places trades on OKX via REST API |
| `backtester` | Simulates strategy using historical data |
| `ai-validator` | Optional AI layer for smarter trade decision-making |
| `notifier` | Sends updates via Telegram/Email |
| `dashboard` | Web interface for monitoring trades, performance, and system status |

---

## 🧭 Development Plan

### ✅ Phase 1: Signal Intake & Order Execution

- [ ] Create webhook listener API (FastAPI or Express)
- [ ] Define alert JSON structure in Pine Script (symbol, side, qty)
- [ ] Validate and sanitize incoming webhook payloads
- [ ] Integrate OKX trading API (V5 REST)
  - [ ] Market and Limit orders
  - [ ] Testnet + Production switching
- [ ] Implement logging (MongoDB/PostgreSQL)
- [ ] Add retry logic and error handling

### ✅ Phase 2: Backtesting Engine

- [ ] Gather historical OHLCV data (Binance, OKX)
- [ ] Parse historical signals (JSON file or replay logic)
- [ ] Simulate trades based on strategy
- [ ] Calculate metrics:
  - PnL, Win Rate, Sharpe Ratio, Max Drawdown, Trade Frequency
- [ ] Save backtest sessions to DB for comparison

### ✅ Phase 3: Web Dashboard & Monitoring

- [ ] Build UI (React + TailwindCSS)
- [ ] Show:
  - Live trades
  - Signal history
  - Open positions
  - Strategy performance charts
- [ ] Use Socket.IO or polling for live updates

### ✅ Phase 4: Notification System

- [ ] Telegram Bot integration:
  - Signal received
  - Order success/failure
  - Daily performance summary
- [ ] Optional: Email via SendGrid or Mailgun

### ✅ Phase 5: AI-Enhanced Signal Validation (Optional Advanced)

- [ ] Train ML models using historical OHLCV + outcomes
  - Logistic Regression, XGBoost, LSTM
- [ ] Filter low-confidence trades before execution
- [ ] Feature engineering:
  - RSI, MACD, volume, volatility, candle patterns
- [ ] Integrate model into live signal pipeline

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Node.js (Express) or Python (FastAPI) |
| Trading API | OKX REST API V5 |
| Frontend | React + TailwindCSS |
| Database | PostgreSQL or MongoDB |
| Backtesting | Python (pandas, backtrader, numpy) |
| AI (optional) | Scikit-learn, TensorFlow, or PyTorch |
| Messaging | Telegram Bot API |
| Deployment | Docker + VPS (e.g. Hetzner, DigitalOcean) |

---

## 🔐 Security Considerations

- Use `.env` files or secret managers for API keys
- Validate all webhook payloads (HMAC or static key check)
- Log only necessary details for trades (mask secrets)
- Use HTTPS for webhook endpoint
- Implement rate limiting and bot protection

---

## 📦 Folder Structure (Suggested)

```
project-root/
│
├── webhook-api/    # Receives TradingView alerts
├── executor/       # Executes trades via OKX
├── backtester/     # Historical signal replay & backtest
├── ai-validator/   # Optional ML layer
├── notifier/       # Telegram/email alerts
├── dashboard/      # React frontend
├── config/         # API keys, pairs, settings
├── logs/           # Trade and error logs
└── .env           # Secret configs
```


---

## 🚀 Deployment

- [ ] Create `.env` file with OKX credentials, Telegram bot token
- [ ] Run via Docker Compose
- [ ] Expose webhook endpoint securely (Cloudflare Tunnel or Nginx)
- [ ] Set up alerts in TradingView pointing to:  
  `https://yourdomain.com/webhook`

---

## 🧪 Testing

- Use OKX Testnet to simulate trades
- Backtest strategies before activating live trading
- Enable dry-run mode for signal validation without execution

---

## ✅ Status

| Feature | Status |
|--------|--------|
| Real-Time Trade Execution | 🚧 In Progress |
| Webhook Listener | ✅ Done |
| Backtesting Engine | 🔄 Coming Next |
| AI Signal Filter | 🔲 Optional Phase |
| Telegram Notification | ✅ Basic Setup |
| Dashboard UI | 🔄 In Development |

---

## 📬 Contact / Support

Built with 💻 by Darwin.  
Feel free to contribute or open issues.

