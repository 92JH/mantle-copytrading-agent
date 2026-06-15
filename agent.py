import requests
import anthropic
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

AGENTS = [
    {"id": 1, "name": "Agent Alpha",   "roi": 23.5, "mdd": 8.2,  "trades": 45, "win_rate": 68},
    {"id": 2, "name": "Agent Beta",    "roi": 15.2, "mdd": 12.1, "trades": 30, "win_rate": 55},
    {"id": 3, "name": "Agent Gamma",   "roi": 31.0, "mdd": 6.5,  "trades": 60, "win_rate": 72},
    {"id": 4, "name": "Agent Delta",   "roi": 9.8,  "mdd": 18.3, "trades": 20, "win_rate": 48},
    {"id": 5, "name": "Agent Epsilon", "roi": 27.3, "mdd": 9.1,  "trades": 50, "win_rate": 65},
]


def get_fear_greed():
    try:
        res = requests.get("https://api.alternative.me/fng/?limit=1")
        data = res.json()
        value = int(data["data"][0]["value"])
        label = data["data"][0]["value_classification"]
        return value, label
    except Exception:
        return 50, "Neutral"


def analyze_agents(agents, fg_value, fg_label):
    prompt = (
        "You are an on-chain AI trading agent analyst.\n\n"
        "Current market: Fear & Greed Index = " + str(fg_value) + " (" + fg_label + ")\n\n"
        "Agent performance data:\n"
        + json.dumps(agents, indent=2) + "\n\n"
        "Score each agent out of 100 using:\n"
        "- ROI: 30pts\n"
        "- MDD (lower is better): 25pts\n"
        "- Number of trades: 20pts\n"
        "- Win rate: 25pts\n\n"
        "Reply ONLY with valid JSON, no explanation, no markdown:\n"
        '{"scores":[{"id":1,"name":"Agent Alpha","score":0,"reason":""},{"id":2,"name":"Agent Beta","score":0,"reason":""},{"id":3,"name":"Agent Gamma","score":0,"reason":""},{"id":4,"name":"Agent Delta","score":0,"reason":""},{"id":5,"name":"Agent Epsilon","score":0,"reason":""}],"selected":{"id":0,"name":"","action":"BUY","reason":""}}'
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    # JSON 블록만 추출
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()
    return json.loads(raw)


def run():
    print("=" * 50)
    print("Mantle Copy Trading Agent")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 50)

    fg_value, fg_label = get_fear_greed()
    print("\nFear & Greed Index: " + str(fg_value) + " (" + fg_label + ")")

    print("\nClaude AI analyzing agents...")
    result = analyze_agents(AGENTS, fg_value, fg_label)

    print("\nAgent Reputation Scores:")
    for s in sorted(result["scores"], key=lambda x: x["score"], reverse=True):
        print("  " + s["name"] + ": " + str(s["score"]) + " pts - " + s["reason"])

    selected = result["selected"]
    print("\nSelected Agent: " + selected["name"])
    print("Action: " + selected["action"])
    print("Reason: " + selected["reason"])
    print("\n" + "=" * 50)


if __name__ == "__main__":
    run()