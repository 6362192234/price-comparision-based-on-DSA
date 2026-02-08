# ==================== pages/2_Compare.py (COMPARISON & RECOMMENDATION) ====================
import streamlit as st
from dsa.heap_utils import MinHeap, find_best_price
from dsa.graph_recommend import ProductGraph, find_alternatives_bfs
from dsa.price_trend import PriceAnalyzer
from data.products import PRODUCT_DATA
from utils.theme import apply_dark_theme



st.set_page_config(page_title="Compare Products", page_icon="⚖️", layout="wide")
apply_dark_theme()



# ==================== TOP NAVIGATION ====================
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

with col1:
    st.markdown("## 🛍️ **Price Comparison System**")

with col2:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

with col3:
    if st.button("🔍 Search", use_container_width=True):
        st.switch_page("pages/1_Search.py")

with col4:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/3_Profile.py")

with col5:
    cart_count = len(st.session_state.get('cart', []))
    st.button(f"🛒 Cart ({cart_count})", use_container_width=True)

st.markdown("---")

# ==================== BACK BUTTON ====================
if st.button("⬅️ Back to Search"):
    st.switch_page("pages/1_Search.py")

# ==================== CHECK IF PRODUCTS SELECTED ====================
if 'selected_products' not in st.session_state or not st.session_state.selected_products:
    st.warning("⚠️ No products selected for comparison. Please go back and select products.")
    if st.button("🔍 Go to Search"):
        st.switch_page("pages/1_Search.py")
    st.stop()

# ==================== GET PRODUCT DATA ====================
products = st.session_state.selected_products
product_name = st.session_state.get('selected_product_name', products[0]['name'])

st.markdown(f"## ⚖️ Price Comparison: **{product_name}**")

# ==================== STATISTICS SECTION ====================
prices = [p['price'] for p in products]
ratings = [p['rating'] for p in products]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>₹{min(prices):,}</div>
        <div class='stats-label'>Lowest Price</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>₹{max(prices):,}</div>
        <div class='stats-label'>Highest Price</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>₹{max(prices) - min(prices):,}</div>
        <div class='stats-label'>You Can Save</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>{max(ratings):.1f}</div>
        <div class='stats-label'>Best Rating</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==================== MIN HEAP IMPLEMENTATION ====================
st.info("🔧 **Min-Heap Data Structure:** Using heap to extract minimum price in O(log n) time")

# Build Min-Heap
min_heap = MinHeap()
for p in products:
    min_heap.insert(p['price'], p)

# Extract best prices
best_product = min_heap.extract_min()



# Calculate value scores
for p in products:
    price_norm = (max(prices) - p['price']) / (max(prices) - min(prices)) if max(prices) != min(prices) else 1
    rating_norm = (p['rating'] - min(ratings)) / (max(ratings) - min(ratings)) if max(ratings) != min(ratings) else 1
    p['value_score'] = (price_norm * 0.6) + (rating_norm * 0.4)

best_value = max(products, key=lambda x: x['value_score'])

# ==================== SMART DECISION ASSISTANT ====================
st.markdown("### 🧠 Smart Shopping Decision Assistant")
st.info("🔧 **Queue Data Structure:** Managing simulated price history for trend analysis")

# Analysis Logic
analyzer = PriceAnalyzer()
price_history = analyzer.generate_simulated_history(best_product['price'])
recommendation, reason = analyzer.analyze_recommendation(best_product['price'])

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"#### Recommendation for **{best_product['seller']}**")
    if "BUY" in recommendation:
        st.success(f"# {recommendation}")
    else:
        st.error(f"# {recommendation}")
    st.write(f"**Reason:** {reason}")

with col2:
    st.write("**Price Trend (Last 15 Days)**")
    # visual enhancement: Add current price to history for the chart
    chart_data = price_history + [best_product['price']]
    st.line_chart(chart_data)

st.markdown("---")

# ==================== BEST DEAL CARDS ====================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class='comparison-card'>
        <span class='best-deal-badge'>🏆 BEST PRICE</span>
        <h2 style='margin-top: 15px;'>{best_product['seller']}</h2>
        <h1 style='font-size: 42px; margin: 15px 0;'>₹{best_product['price']:,}</h1>
        <p style='font-size: 18px;'>⭐ Rating: {best_product['rating']}/5.0</p>
        <p style='margin-top: 20px; opacity: 0.9;'>
            <b>Why this is recommended:</b><br>
            ✅ Lowest price extracted using Min-Heap algorithm<br>
            ✅ Guaranteed cheapest option among all sellers
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='comparison-card' style='background: linear-gradient(135deg, #800000 0%, #4a0000 100%);'>
        <span class='best-deal-badge' style='background: green; color: #10b981;'>💎 BEST VALUE</span>
        <h2 style='margin-top: 15px;'>{best_value['seller']}</h2>
        <h1 style='font-size: 42px; margin: 15px 0;'>₹{best_value['price']:,}</h1>
        <p style='font-size: 18px;'>⭐ Rating: {best_value['rating']}/5.0</p>
        <p style='margin-top: 20px; opacity: 0.9;'>
            <b>Why this is recommended:</b><br>
            ✅ Optimal balance of price (60%) and rating (40%)<br>
            ✅ Value Score: {best_value['value_score']:.3f}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)



# ==================== DETAILED COMPARISON TABLE ====================
st.markdown("### 📋 All Seller Comparisons (Sorted by Price)")

# Sort products by price
sorted_products = sorted(products, key=lambda x: x['price'])

for idx, p in enumerate(sorted_products, 1):
    savings = max(prices) - p['price']
    savings_percent = (savings / max(prices) * 100) if max(prices) > 0 else 0
    
    col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 2, 2])
    
    with col1:
        if idx == 1:
            st.markdown("🥇")
        elif idx == 2:
            st.markdown("🥈")
        elif idx == 3:
            st.markdown("🥉")
        else:
            st.markdown(f"**{idx}**")
    
    with col2:
        st.markdown(f"**{p['seller']}**")
    
    with col3:
        st.markdown(f"₹{p['price']:,}")
    
    with col4:
        st.markdown(f"⭐ {p['rating']}")
    
    with col5:
        if savings > 0:
            st.success(f"💰 Save ₹{savings:,} ({savings_percent:.1f}%)")
        else:
            st.error("❌ Most Expensive")

st.markdown("---")

# ==================== GRAPH + BFS ALTERNATIVES ====================
st.markdown("### 🔄 Similar Product Alternatives")
st.info("🔧 **Graph + BFS:** Finding cheaper alternatives using breadth-first graph traversal")

# Build product graph
category = st.session_state.get('selected_category', 'Electronics')
graph = ProductGraph(category)

# Find alternatives using BFS
alternatives = find_alternatives_bfs(product_name, best_product['price'], category)

if alternatives:
    st.markdown(f"Found **{len(alternatives)}** cheaper alternatives with similar specifications:")
    
    for alt in alternatives:
        min_price = min([p['price'] for p in alt['variants']])
        max_rating = max([p['rating'] for p in alt['variants']])
        savings = best_product['price'] - min_price
        
        st.markdown(f"""
        <div class='product-card'>
            <h4>{alt['name']}</h4>
            <p><b>Starting from:</b> ₹{min_price:,} | <b>Rating:</b> ⭐ {max_rating} | <b>Save:</b> ₹{savings:,}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"View {alt['name']}", key=f"alt_{alt['name']}"):
            st.session_state.selected_products = alt['variants']
            st.session_state.selected_product_name = alt['name']
            st.rerun()
else:
    st.warning("✅ This is already the cheapest option in this category!")

st.markdown("---")

# ==================== COMPARISON HISTORY (STACK) ====================
st.markdown("### 📚 Comparison History")
st.info("🔧 **Stack Data Structure:** Track previous comparisons with LIFO access (undo feature)")

# Add current comparison to stack
if 'comparison_history' not in st.session_state:
    st.session_state.comparison_history = []

# Push to stack
comparison_entry = {
    'product': product_name,
    'best_price': best_product['price'],
    'seller': best_product['seller'],
    'num_sellers': len(products)
}

if not st.session_state.comparison_history or st.session_state.comparison_history[-1]['product'] != product_name:
    st.session_state.comparison_history.append(comparison_entry)

# Display stack (recent first)
if st.session_state.comparison_history:
    for idx, entry in enumerate(reversed(st.session_state.comparison_history[-5:]), 1):
        st.markdown(f"""
        **{idx}.** {entry['product']} - Best: ₹{entry['best_price']:,} from {entry['seller']} ({entry['num_sellers']} sellers)
        """)
else:
    st.info("No comparison history yet")

# ==================== FINAL ACTIONS ====================
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📊 View Summary", use_container_width=True, type="primary"):
        st.switch_page("pages/5_Summary.py")

with col2:
    if st.button("🛒 Add Best Price to Cart", use_container_width=True):
        if 'cart' not in st.session_state:
            st.session_state.cart = []
        st.session_state.cart.append(best_product)
        st.success(f"✅ Added {product_name} to cart!")

with col3:
    if st.button("💎 Add Best Value to Cart", use_container_width=True):
        if 'cart' not in st.session_state:
            st.session_state.cart = []
        st.session_state.cart.append(best_value)
        st.success(f"✅ Added {product_name} to cart!")

with col4:
    if st.button("🔍 Search Again", use_container_width=True):
        st.switch_page("pages/1_Search.py")

# ==================== DATA STRUCTURE EXPLANATION ====================
st.markdown("<br>", unsafe_allow_html=True)

with st.expander("🔧 Data Structures in Action (Click to Expand)", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Min-Heap
        - **Purpose:** Extract minimum price efficiently
        - **Time Complexity:** O(log n) for insert/extract
        - **Implementation:** Binary heap with smallest price at root
        
        ### Stack
        - **Purpose:** Comparison history tracking
        - **Time Complexity:** O(1) for push/pop
        - **Implementation:** LIFO structure for undo functionality
        """)
    
    with col2:
        st.markdown("""
        ### Graph
        - **Purpose:** Model product similarity relationships
        - **Structure:** Nodes = Products, Edges = Similar specs
        
        ### BFS (Breadth-First Search)
        - **Purpose:** Find nearest cheaper alternatives
        - **Time Complexity:** O(V + E) where V=vertices, E=edges
        - **Implementation:** Level-by-level traversal from source product
        """)

st.markdown("<br>", unsafe_allow_html=True)