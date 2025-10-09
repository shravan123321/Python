# Dictionary comprehension

tea_prices_inr = {
    "masala chai ": 40,
    "Green tea ": 50,
    "lemon chai ": 60,
    "coffi ": 70
}

tea_prices_usd = {tea: prices /80 for tea, prices in tea_prices_inr.items()}  # assuming ₹1 = $0.0125

print(tea_prices_usd)
