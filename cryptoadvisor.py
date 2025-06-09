# cryptoadvisor.py

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

def get_user_query():
    return input("You: ").lower()

def respond_to_query(query):
    if "sustainable" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential.")
    elif "trending" in query or "rising" in query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"CryptoBuddy: 📈 The rising cryptos right now are: {', '.join(trending)}.")
    elif "long-term" in query or "growth" in query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                print(f"CryptoBuddy: 🚀 {name} is trending up and has a top-tier sustainability score!")
                return
        print("CryptoBuddy: 🤔 I couldn’t find a perfect match. Maybe diversify?")
    elif "energy" in query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        print(f"CryptoBuddy: 🔋 These cryptos use the least energy: {', '.join(low_energy)}.")
    else:
        print("CryptoBuddy: 🤖 Sorry, I didn’t understand that. Try asking about trends or sustainability!")

def run_chatbot():
    print("👋 Hey there! I'm CryptoBuddy, your AI-powered crypto sidekick. Ask me about crypto trends or sustainability!")
    while True:
        user_query = get_user_query()
        if user_query in ["exit", "quit", "bye"]:
            print("CryptoBuddy: 👋 Catch you later! Remember—crypto is risky. Do your own research!")
            break
        respond_to_query(user_query)

if __name__ == "__main__":
    run_chatbot()