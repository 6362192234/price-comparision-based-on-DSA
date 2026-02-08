# ==================== pages/3_Profile.py (USER PROFILE & HISTORY) ====================
import streamlit as st
from utils.theme import apply_dark_theme

st.set_page_config(page_title="User Profile", page_icon="👤", layout="wide")
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
    if st.button("ℹ️ About", use_container_width=True):
        st.switch_page("pages/4_About.py")

with col5:
    cart_count = len(st.session_state.get('cart', []))
    st.button(f"🛒 Cart ({cart_count})", use_container_width=True)

st.markdown("---")

# ==================== PROFILE HEADER ====================
st.markdown("## 👤 User Profile")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 30px;'>
        <div style='font-size: 80px; margin-bottom: 20px;'>👤</div>
        <h2 style='color: #60a5fa !important;'>Guest User</h2>
        <p style='color: #94a3b8 !important;'>Smart Price Comparison Shopper</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== COMPARISON HISTORY ====================
st.markdown("### 📚 Comparison History")
st.info("🔧 **Stack Data Structure:** Your comparison history stored in LIFO order")

if 'comparison_history' in st.session_state and st.session_state.comparison_history:
    history = st.session_state.comparison_history
    
    st.markdown(f"**Total Comparisons:** {len(history)}")
    
    for idx, entry in enumerate(reversed(history), 1):
        with st.expander(f"{idx}. {entry['product']} - ₹{entry['best_price']:,}", expanded=(idx==1)):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                - **Product:** {entry['product']}
                - **Best Price:** ₹{entry['best_price']:,}
                - **Seller:** {entry['seller']}
                """)
            
            with col2:
                st.markdown(f"""
                - **Sellers Compared:** {entry['num_sellers']}
                - **Status:** ✅ Completed
                """)
            
            if st.button(f"🔄 Compare Again", key=f"recompare_{idx}"):
                st.info("Navigate to Search page to compare this product again")
else:
    st.warning("No comparison history yet. Start comparing products!")
    if st.button("🔍 Start Shopping"):
        st.switch_page("pages/1_Search.py")

st.markdown("---")

# ==================== CART ====================
st.markdown("### 🛒 Shopping Cart")
st.info("🔧 **Queue Data Structure:** Cart items processed in FIFO order")

if 'cart' in st.session_state and st.session_state.cart:
    cart = st.session_state.cart
    
    total_price = sum([item['price'] for item in cart])
    total_items = len(cart)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='stats-box'>
            <div class='stats-number'>{total_items}</div>
            <div class='stats-label'>Items in Cart</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='stats-box'>
            <div class='stats-number'>₹{total_price:,}</div>
            <div class='stats-label'>Total Amount</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_rating = sum([item['rating'] for item in cart]) / len(cart)
        st.markdown(f"""
        <div class='stats-box'>
            <div class='stats-number'>{avg_rating:.1f}</div>
            <div class='stats-label'>Avg Rating</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display cart items
    for idx, item in enumerate(cart, 1):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        
        with col1:
            st.markdown(f"**{idx}. {item.get('name', 'Product')}**")
        
        with col2:
            st.markdown(f"₹{item['price']:,}")
        
        with col3:
            st.markdown(f"⭐ {item['rating']} - {item['seller']}")
        
        with col4:
            if st.button("🗑️", key=f"remove_{idx}"):
                st.session_state.cart.pop(idx-1)
                st.rerun()
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.rerun()
    
    with col2:
        if st.button("✅ Checkout", use_container_width=True, type="primary"):
            st.success(f"✅ Order placed! Total: ₹{total_price:,}")
            st.balloons()
            st.session_state.cart = []

else:
    st.warning("Your cart is empty")
    if st.button("🛍️ Start Shopping"):
        st.switch_page("pages/1_Search.py")

st.markdown("---")

# ==================== STATISTICS ====================
st.markdown("### 📊 Your Shopping Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    comparisons = len(st.session_state.get('comparison_history', []))
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>{comparisons}</div>
        <div class='stats-label'>Products Compared</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    cart_items = len(st.session_state.get('cart', []))
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>{cart_items}</div>
        <div class='stats-label'>Cart Items</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # Calculate potential savings
    if st.session_state.get('comparison_history'):
        st.markdown(f"""
        <div class='stats-box'>
            <div class='stats-number'>💰</div>
            <div class='stats-label'>Smart Shopper</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='stats-box'>
            <div class='stats-number'>🎯</div>
            <div class='stats-label'>New User</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)