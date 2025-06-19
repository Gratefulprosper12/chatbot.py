# CryptoBuddy - A simple crypto recommendation chatbot

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def recommend_crypto(user_query):
    query = user_query.lower()
    
    if "sustainable" in query or "eco" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy 🌱: You should check out {recommend}! It's eco-friendly and future-ready!")
    
    elif "trending" in query or "rising" in query:
        rising = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if rising:
            print(f"CryptoBuddy 🚀: {', '.join(rising)} are on the rise! Look into them for growth potential!")
        else:
            print("CryptoBuddy 🤔: No coins are trending up at the moment.")
    
    elif "long-term" in query or "growth" in query:
        best = None
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                best = coin
        if best:
            print(f"CryptoBuddy 🔍: {best} is trending up and has strong sustainability! Good for long-term growth.")
        else:
            print("CryptoBuddy 🤷: I couldn't find a perfect match for long-term and sustainable growth.")
    
    else:
        print("CryptoBuddy 🤖: I'm not sure how to help with that. Try asking about trending or sustainable cryptos!")

print("👋 Hey! I'm CryptoBuddy. Ask me about crypto trends or sustainability.")
print("💬 Type 'exit' to leave.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("CryptoBuddy 👋: See you next time! Stay green and savvy!")
        break
    recommend_crypto(user_input)
