import streamlit as st

# Function to generate the campaign URL
def generate_url(root_url, product_type, page_name, offer_type):
    # Create the URL parts based on provided inputs
    url_parts = [root_url, "splash"]
    
    if product_type:
        url_parts.append(product_type)
    if page_name:
        if offer_type:
            url_parts.append(f"{page_name}-{offer_type}.html")
        else:
            url_parts.append(f"{page_name}.html")
    
    # Join the parts to form the final URL
    return "/".join(url_parts).rstrip('/')

# Streamlit app
st.title("Campaign URL Generator")
st.text("Created By: Brandon Lazovic")
st.markdown("""
This tool helps you generate campaign URLs based on the following inputs. You can leave certain fields blank if they aren't applicable, and the tool will handle the URL generation accordingly. As an example, the generated URL for the example fields below will be:
`https://www.example.com/splash/business-checking/business-checking-offer-a.html`. Hover over the help toggles to the right of each of the fields for more context on format.
""")

# Input fields with descriptors
root_url = st.text_input("Root Domain", value="", help="The root domain for the URL, e.g., 'https://www.example.com'")
product_type = st.text_input("Product Type", value="", help="The type of product, e.g., 'business-checking', 'business-savings', 'business-checking-trigger,' etc.")
page_name = st.text_input("Page Name", value="", help="A descriptor for the URL slug, e.g., 'business-checking-offer', 'special-deal', 'promo', etc.")
offer_type = st.text_input("Offer Type", value="", help="The offer variant, e.g., 'a', 'b', 'c', etc. Leave blank if not applicable.")

# Generate URL button
if st.button("Generate URL"):
    campaign_url = generate_url(root_url, product_type, page_name, offer_type)
    st.success(f"Generated URL: {campaign_url}")
