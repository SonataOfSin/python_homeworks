import requests

def get_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            user = response.json()
            return {
                "name": user.get("name"),
                "email": user.get("email"),
                "city": user.get("address", {}).get("city"),
                "company": user.get("company", {}).get("name")
            }
        else:
            return None
            
    except requests.exceptions.RequestException:
        return None


user_info = get_user_data(1)
print(user_info)
