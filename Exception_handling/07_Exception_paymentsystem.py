# Example: Online Payment System
try:
    amount = int(input("Enter payment amount: ₹"))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero!")
    print("✅ Payment of ₹", amount, "processed successfully.")
except ValueError as e:
    print("❌ Error:", e)
except Exception:
    print("⚠️ Something went wrong. Please try again.")
else:
    print("🎉 Transaction Completed Successfully!")
finally:
    print("🧾 Thank you for using our payment system.")
