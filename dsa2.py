# ==================== app.py (MAIN DASHBOARD) ====================
import streamlit as st
from utils.theme import apply_dark_theme

st.set_page_config(
    page_title="Price Comparison System",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_dark_theme()

# Initialize session state
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'comparison_history' not in st.session_state:
    st.session_state.comparison_history = []  # Stack

# ==================== TOP NAVIGATION ====================
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

with col1:
    st.markdown("## 🛍️ **Price Comparison System**")

with col2:
    if st.button("🏠 Home", use_container_width=True):
        st.rerun()

with col3:
    if st.button("ℹ️ About", use_container_width=True):
        st.switch_page("pages/4_About.py")

with col4:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/3_Profile.py")

with col5:
    cart_count = len(st.session_state.cart)
    st.button(f"🛒 Cart ({cart_count})", use_container_width=True)

st.markdown("---")

# ==================== HERO SECTION ====================
st.markdown("""
<div style='text-align: center; padding: 40px 0 20px 0;'>
    <h1 style='color: #60a5fa !important; font-size: 48px; margin-bottom: 10px;'>
        Find the Best Deals Instantly
    </h1>
    <p style='color: #94a3b8 !important; font-size: 20px;'>
        Compare prices across multiple sellers using advanced data structures
    </p>
</div>
""", unsafe_allow_html=True)
# ==================== SMART SHOPPING DECISION ASSISTANT ====================
st.markdown("### 🧠 Smart Shopping Decision Assistant")

st.info("""
This system goes beyond price comparison.

✔ Tracks recent price history using Queue  
✔ Analyzes price trends dynamically  
✔ Advises users whether to **BUY NOW** or **WAIT**

👉 Compare a product to see intelligent buying advice in action.
""")


# ==================== CATEGORY CARDS ====================
st.markdown("### 🏷️ Browse by Category")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

categories = [
    ('Electronics', '📱', col1),
    ('Clothing', '👕', col2),
    ('Accessories', '⌚', col3),
    ('Beauty', '💄', col4)
]

for category, icon, col in categories:
    with col:
        st.markdown(f"""
        <div class='category-card'>
            <div class='category-icon'>{icon}</div>
            <p class='category-title'>{category}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Explore {category}", key=f"btn_{category}", use_container_width=True):
            st.session_state.selected_category = category
            st.switch_page("pages/1_Search.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================== INFORMATION SECTION ====================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='info-section'>
        <h3>💡 Problem Statement</h3>
        <p style='color: #cbd5e1 !important; line-height: 1.8;'>
            Online shoppers face difficulty comparing prices across multiple e-commerce platforms. 
            This system uses efficient data structures to quickly search, compare, and recommend 
            the best deals, saving time and money.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-section'>
        <h3>🎯 Key Objectives</h3>
        <ul style='color: #cbd5e1 !important; line-height: 2;'>
            <li>Store product data using structured storage (Arrays/HashMap)</li>
            <li>Enable efficient searching with hashing and prefix trees</li>
            <li>Compare prices using Min-Heap priority logic</li>
            <li>Recommend alternatives using Graph + BFS traversal</li>
            <li>Demonstrate practical DSA applications in real scenarios</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='info-section'>
        <h3>🔧 Data Structures Used</h3>
        <ul style='color: #cbd5e1 !important; line-height: 2;'>
            <li><b>HashMap:</b> Fast O(1) product lookup by name</li>
            <li><b>Min Heap:</b> Extract cheapest price in O(log n)</li>
            <li><b>Trie/Prefix Tree:</b> Auto-complete search suggestions</li>
            <li><b>Graph + BFS:</b> Find similar product alternatives</li>
            <li><b>Queue:</b> Maintain ordered display of results</li>
            <li><b>Stack:</b> Track comparison history (undo feature)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-section'>
        <h3>✨ How This Helps You</h3>
        <ul style='color: #cbd5e1 !important; line-height: 2;'>
            <li>⚡ Compare prices from 10+ sellers in seconds</li>
            <li>💰 Automatically find the lowest price option</li>
            <li>🎯 Get smart alternative product recommendations</li>
            <li>📊 Make data-driven purchase decisions</li>
            <li>💡 Save money on every purchase</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ==================== LAST SMART DECISION SUMMARY ====================
if 'comparison_history' in st.session_state and st.session_state.comparison_history:
    last = st.session_state.comparison_history[-1]

    st.markdown("### 📊 Recent Comparison Insight")
    st.success(
        f"Recently compared **{last['product']}**\n\n"
        f"Best Price: ₹{last['best_price']:,} from {last['seller']}\n\n"
        f"👉 Smart BUY / WAIT advice available on Compare page"
    )

# ==================== FOOTER ====================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p><b>Academic Project:</b> Data Structures & Algorithms Simulator</p>
    <p>This system demonstrates algorithmic efficiency without real-time API integration</p>
</div>
""", unsafe_allow_html=True)