import requests
import streamlit as st

st.set_page_config(page_title="Fake Store Browser", layout="wide")
st.title("🛒 Fake Store Products")


# მონაცემების წამოღება API-დან
@st.cache_data
def fetch_products():
    try:
        response = requests.get("https://fakestoreapi.com/products", timeout=10)
        if response.status_code == 200: #200 status code means success
            return response.json()
        return None
    except Exception:
        return None


# Loading ინდიკატორი მონაცემების ჩატვირთვისას
with st.spinner("Loading products..."):
    products = fetch_products()

# Error handling
if products is None:
    st.error("Failed to load products")
    st.stop()

# Sidebar ფილტრები
st.sidebar.header("Filter Products")

# კატეგორიების სია
categories = ["All"] + sorted(list({p["category"] for p in products}))
selected_category = st.sidebar.selectbox("Category", categories)

# მაქსიმალური ფასის გამოთვლა დინამიურად
max_api_price = float(max(p["price"] for p in products))
selected_price = st.sidebar.slider(
    "Maximum Price",
    min_value=0.0,
    max_value=max_api_price,
    value=max_api_price,
    step=1.0,
)

# საძიებო ველის ტექსტი
search_query = st.sidebar.text_input("Search").strip().lower()

# მონაცემების გაფილტვრა
filtered_products = []
for p in products:
    # 1. კატეგორიის ფილტრი
    if selected_category != "All" and p["category"] != selected_category:
        continue

    # 2. ფასის ფილტრი
    if p["price"] > selected_price:
        continue

    # 3. ძებნის ფილტრი (title-სა და description-ში)
    if search_query:
        matches_title = search_query in p["title"].lower()
        matches_desc = search_query in p["description"].lower()
        if not (matches_title or matches_desc):
            continue

    filtered_products.append(p)

# შედეგების გამოტანა
st.write(f"Showing **{len(filtered_products)}** products")

if not filtered_products:
    st.warning("No products found matching your criteria.")
else:
    # პროდუქტების გამოტანა ბადის (Grid) სახით - 3 სვეტად
    cols = st.columns(3)

    for idx, product in enumerate(filtered_products):
        with cols[idx % 3]:
            with st.container(border=True):
                # ფოტოს გამოტანა
                st.image(product["image"], use_container_width=True)

                # ძირითადი ინფორმაცია
                st.subheader(product["title"])
                st.write(f"**ID:** {product['id']}")
                st.write(f"**Category:** `{product['category']}`")
                st.write(f"**Price:** ${product['price']:.2f}")

                # რეიტინგი (rate და count)
                rating = product.get("rating", {})
                rate = rating.get("rate", "N/A")
                count = rating.get("count", "N/A")
                st.write(f"⭐ **Rating:** {rate} ({count} reviews)")

                # დეტალური აღწერა expander-ში
                with st.expander("View details"):
                    st.write(product["description"])