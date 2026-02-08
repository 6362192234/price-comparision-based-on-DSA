# ==================== pages/4_About.py (ABOUT & DOCUMENTATION) ====================
import streamlit as st
from utils.theme import apply_dark_theme

st.set_page_config(page_title="About System", page_icon="ℹ️", layout="wide")
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

# ==================== ABOUT HEADER ====================
st.markdown("## ℹ️ About This System")

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 20px; color: #94a3b8 !important;'>
        An academic simulator demonstrating practical applications of<br>
        <b style='color: #60a5fa !important;'>Data Structures & Algorithms</b> in E-Commerce
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==================== PROBLEM STATEMENT ====================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class='info-section'>
        <h3>💡 Problem Statement</h3>
        <p style='color: #cbd5e1 !important; line-height: 1.8;'>
            In today's digital marketplace, consumers face a significant challenge: comparing prices across 
            multiple e-commerce platforms is time-consuming and inefficient. Shoppers often miss better deals 
            because they cannot quickly evaluate all available options.
            <br><br>
            <b>Our Solution:</b> A simulator that demonstrates how efficient data structures can solve this 
            real-world problem by enabling instant price comparisons and smart recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='info-section'>
        <h3>🎯 Project Objectives</h3>
        <ul style='color: #cbd5e1 !important; line-height: 2;'>
            <li>Design a simulator with structured product and price storage</li>
            <li>Implement efficient searching using HashMap and Trie</li>
            <li>Compare prices using Min-Heap priority logic</li>
            <li>Recommend alternatives via Graph traversal (BFS)</li>
            <li>Demonstrate practical DSA applications</li>
            <li>Provide decision-making clarity for users</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ==================== DATA STRUCTURES DEEP DIVE ====================
st.markdown("---")
st.markdown("## 🔧 Data Structures Implementation")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "HashMap", "Min-Heap", "Trie/Prefix Tree", "Graph + BFS", "Stack", "Queue"
])

with tab1:
    st.markdown("""
    ### HashMap (Hash Table)
    
    **Purpose:** Fast product lookup by name
    
    **Implementation:**
    ```python
    class ProductHashMap:
        def __init__(self):
            self.map = {}
        
        def insert(self, key, value):
            if key not in self.map:
                self.map[key] = []
            self.map[key].append(value)
        
        def get(self, key):
            return self.map.get(key, [])
    ```
    
    **Time Complexity:**
    - Insert: O(1) average
    - Lookup: O(1) average
    - Space: O(n)
    
    **Usage in System:**
    - Maps `product_name → [list of seller entries]`
    - Enables instant product search
    - Stores all seller variants for each product
    """)

with tab2:
    st.markdown("""
    ### Min-Heap (Priority Queue)
    
    **Purpose:** Extract minimum price efficiently
    
    **Implementation:**
    ```python
    class MinHeap:
        def __init__(self):
            self.heap = []
        
        def insert(self, price, product):
            self.heap.append((price, product))
            self._bubble_up(len(self.heap) - 1)
        
        def extract_min(self):
            # Returns product with lowest price
            return self._extract_root()
    ```
    
    **Time Complexity:**
    - Insert: O(log n)
    - Extract Min: O(log n)
    - Get Min: O(1)
    
    **Usage in System:**
    - Identifies cheapest product automatically
    - Maintains sorted price order efficiently
    - Powers "Best Price" recommendation
    """)

with tab3:
    st.markdown("""
    ### Trie (Prefix Tree)
    
    **Purpose:** Auto-complete search suggestions
    
    **Implementation:**
    ```python
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
    
    class Trie:
        def insert(self, word):
            # Insert word character by character
        
        def search_prefix(self, prefix):
            # Return all words starting with prefix
    ```
    
    **Time Complexity:**
    - Insert: O(m) where m = word length
    - Search: O(m + k) where k = results
    - Space: O(total characters)
    
    **Usage in System:**
    - Provides real-time search suggestions
    - Enables prefix-based filtering
    - Improves user search experience
    """)

with tab4:
    st.markdown("""
    ### Graph + BFS (Breadth-First Search)
    
    **Purpose:** Find similar product alternatives
    
    **Structure:**
    - **Nodes:** Products
    - **Edges:** Similarity (same category/specs)
    
    **BFS Algorithm:**
    ```python
    def find_alternatives_bfs(source, max_price):
        queue = [source]
        visited = set()
        alternatives = []
        
        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if neighbor.price < max_price:
                    alternatives.append(neighbor)
        
        return alternatives
    ```
    
    **Time Complexity:**
    - BFS: O(V + E) where V=vertices, E=edges
    - Space: O(V)
    
    **Usage in System:**
    - Recommends cheaper alternatives
    - Traverses product similarity network
    - Finds products with similar specifications
    """)

with tab5:
    st.markdown("""
    ### Stack (LIFO - Last In First Out)
    
    **Purpose:** Track comparison history with undo capability
    
    **Implementation:**
    ```python
    class ComparisonStack:
        def __init__(self):
            self.stack = []
        
        def push(self, comparison):
            self.stack.append(comparison)
        
        def pop(self):
            return self.stack.pop() if self.stack else None
        
        def peek(self):
            return self.stack[-1] if self.stack else None
    ```
    
    **Time Complexity:**
    - Push: O(1)
    - Pop: O(1)
    - Peek: O(1)
    
    **Usage in System:**
    - Stores comparison history
    - Enables "undo" functionality
    - Tracks user navigation path
    """)

with tab6:
    st.markdown("""
    ### Queue (FIFO - First In First Out)
    
    **Purpose:** Ordered display of search results
    
    **Implementation:**
    ```python
    class ProductQueue:
        def __init__(self):
            self.queue = []
        
        def enqueue(self, product):
            self.queue.append(product)
        
        def dequeue(self):
            return self.queue.pop(0) if self.queue else None
    ```
    
    **Time Complexity:**
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Space: O(n)
    
    **Usage in System:**
    - Maintains ordered loading of products
    - Sequential result display
    - Cart checkout processing order
    """)

# ==================== SYSTEM FLOW ====================
st.markdown("---")
st.markdown("## 📋 System Flow")

st.markdown("""
<div class='info-section'>
    <h4>Page 1: Home/Dashboard</h4>
    <p style='color: #cbd5e1 !important;'>
        → User selects category (Electronics, Clothing, etc.)<br>
        → Category cards with hover effects<br>
        → Information about problem statement and objectives
    </p>
    
    <h4>Page 2: Search & Product Listing</h4>
    <p style='color: #cbd5e1 !important;'>
        → Search bar with Trie-based suggestions<br>
        → HashMap lookup for fast product retrieval<br>
        → Display results from multiple sellers<br>
        → Queue maintains ordered display
    </p>
    
    <h4>Page 3: Comparison & Recommendation</h4>
    <p style='color: #cbd5e1 !important;'>
        → Min-Heap extracts best price<br>
        → Calculate value scores (price + rating)<br>
        → Graph + BFS finds cheaper alternatives<br>
        → Stack tracks comparison history
    </p>
    
    <h4>Page 4: Profile & Cart</h4>
    <p style='color: #cbd5e1 !important;'>
        → View comparison history (Stack)<br>
        → Manage shopping cart (Queue)<br>
        → User statistics and insights
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== WHY NO APIs ====================
st.markdown("---")
st.markdown("## 🤔 Why No Real-Time APIs?")

st.markdown("""
<div class='info-section'>
    <h3 style='color: #60a5fa !important;'>Academic Focus</h3>
    <p style='color: #cbd5e1 !important; line-height: 1.8;'>
        <b>This project is a simulator focused on demonstrating how data structures can efficiently manage, 
        search, compare, and recommend products.</b>
        <br><br>
        The emphasis is on <b>algorithmic design</b> and <b>structured decision-making</b> rather than 
        real-time data fetching. This allows us to:
        <br><br>
        ✅ Focus purely on DSA implementation<br>
        ✅ Avoid external dependencies and API rate limits<br>
        ✅ Demonstrate algorithmic efficiency clearly<br>
        ✅ Create a controlled testing environment<br>
        ✅ Showcase data structure operations transparently
        <br><br>
        <b>Real-world Extension:</b> The same algorithms and structures can be applied to live API data 
        without changing the core logic.
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 30px;'>
    <h3 style='color: #60a5fa !important;'>Academic Project</h3>
    <p>Data Structures & Algorithms Practical Implementation</p>
    <p><b>Course:</b> Computer Science Engineering</p>
    <p><b>Focus:</b> Demonstrating DSA concepts through real-world problem solving</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)