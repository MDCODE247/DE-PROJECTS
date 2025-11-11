# import requests

# def get_quote():
#     #"""Fetch a motivational quote from ZenQuotes API."""#
#     try:
#         url = "https://zenquotes.io/api/random"
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         data = response.json()
#         if isinstance(data, list) and len(data) > 0:
#             quote = data[0].get("q")
#             author = data[0].get("a")
#             if quote and author:
#                 return f'"{quote}" — {author}'
#             else:
#                 print("⚠️ Unexpected data structure:", data)
#                 return None
#         else:
#             print("⚠️ Invalid response format from API")
#             return None
#     except requests.exceptions.RequestException as e:
#         print("❌ Network or API error:", e)
#         return None

# # Test the function
# if __name__ == "__main__":
#     quote = get_quote()
#     if quote:
#         print("\n✅ Quote fetched successfully!\n")
#         print(quote)
#     else:
#         print("\n❌ Failed to fetch quote.")


import requests

def get_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} — {data[0]['a']}"
        else:
            return None
    except Exception as e:
        print("❌ Failed to fetch quote:", e)
        return None
