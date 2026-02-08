# ==================== utils/theme.py (DARK THEME STYLING) ====================

import streamlit as st


def apply_dark_theme():
    """Apply dark Persian Blue theme to Streamlit app"""
    
    st.markdown("""
    <style>
        /* ========== MAIN THEME COLORS ========== */
        :root {
            --persian-blue: #1e40af;
            --light-blue: #3b82f6;
            --bright-blue: #60a5fa;
            --dark-bg: #0f172a;
            --card-bg: #1e293b;
            --darker-gray: #0a0f1e;
            --slate: #334155;
            --light-text: #e2e8f0;
            --muted-text: #cbd5e1;
            --gray-text: #94a3b8;
        }
        
        /* ========== HIDE STREAMLIT BRANDING ========== */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* ========== BACKGROUND ========== */
        .stApp {
            background: linear-gradient(135deg, #0a0f1e 0%, #1e293b 100%);
            color: #e2e8f0;
        }
        
        /* ========== TEXT COLORS ========== */
        .stMarkdown, .stText, p, li, span, div, label {
            color: #e2e8f0 !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #60a5fa !important;
        }
        
        /* ========== CATEGORY CARDS ========== */
        .category-card {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transition: all 0.3s ease;
            border: 2px solid #334155;
            cursor: pointer;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .category-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(59, 130, 246, 0.5);
            border-color: #3b82f6;
            background: linear-gradient(135deg, #334155 0%, #475569 100%);
        }
        
        .category-icon {
            font-size: 50px;
            margin-bottom: 15px;
        }
        
        .category-title {
            font-size: 24px;
            font-weight: bold;
            color: #60a5fa !important;
            margin: 0;
        }
        
        /* ========== INFO SECTIONS ========== */
        .info-section {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-radius: 15px;
            padding: 25px;
            margin-top: 30px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            border: 1px solid #334155;
        }
        
        .info-section h3 {
            color: #60a5fa !important;
            border-bottom: 3px solid #3b82f6;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        
        .info-section p, .info-section li {
            color: #cbd5e1 !important;
        }
        
        /* ========== PRODUCT CARDS ========== */
        .product-card {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            border-left: 4px solid #3b82f6;
        }
        
        .product-card h4 {
            color: #60a5fa !important;
        }
        
        .product-card p {
            color: #cbd5e1 !important;
        }
        
        /* ========== COMPARISON CARDS ========== */
        .comparison-card {
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
        }
        
        .best-deal-badge {
            background: #10b981;
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin: 10px 0;
        }
        
        /* ========== STATS BOXES ========== */
        .stats-box {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            border-top: 4px solid #3b82f6;
        }
        
        .stats-number {
            font-size: 36px;
            font-weight: bold;
            color: #60a5fa !important;
        }
        
        .stats-label {
            font-size: 14px;
            color: #94a3b8 !important;
            margin-top: 5px;
        }
        
        /* ========== BUTTONS ========== */
        .stButton>button {
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px 30px;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
        }
        
        .stButton>button[kind="primary"] {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        
        /* ========== INPUT FIELDS ========== */
        .stTextInput input {
            background: #1e293b !important;
            color: #e2e8f0 !important;
            border: 2px solid #334155 !important;
            border-radius: 8px;
        }
        
        .stTextInput input:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
        }
        
        /* ========== DATAFRAME / TABLE ========== */
        .stDataFrame {
            background: #1e293b !important;
        }
        
        .stDataFrame table {
            background: #1e293b !important;
            color: #e2e8f0 !important;
        }
        
        .stDataFrame th {
            background: #334155 !important;
            color: #60a5fa !important;
            font-weight: bold;
        }
        
        .stDataFrame td {
            background: #1e293b !important;
            color: #cbd5e1 !important;
            border-bottom: 1px solid #334155 !important;
        }
        
        /* ========== ALERTS / INFO BOXES ========== */
        .stAlert {
            background: #1e293b !important;
            border: 1px solid #334155 !important;
            color: #e2e8f0 !important;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
            border: none !important;
        }
        
        .stWarning {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
            border: none !important;
        }
        
        .stError {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
            border: none !important;
        }
        
        .stInfo {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
            border: none !important;
        }
        
        /* ========== EXPANDER ========== */
        .streamlit-expanderHeader {
            background: #1e293b !important;
            color: #60a5fa !important;
            border-radius: 8px;
            border: 1px solid #334155 !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: #334155 !important;
        }
        
        .streamlit-expanderContent {
            background: #1e293b !important;
            border: 1px solid #334155 !important;
            border-top: none !important;
        }
        
        /* ========== TABS ========== */
        .stTabs [data-baseweb="tab-list"] {
            background: #1e293b !important;
            border-radius: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            color: #94a3b8 !important;
            background: transparent !important;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            color: #60a5fa !important;
        }
        
        .stTabs [aria-selected="true"] {
            color: #60a5fa !important;
            border-bottom: 3px solid #3b82f6 !important;
        }
        
        /* ========== SIDEBAR (if used) ========== */
        .css-1d391kg, .st-emotion-cache-1d391kg {
            background: #1e293b !important;
        }
        
        /* ========== HORIZONTAL RULE ========== */
        hr {
            border-color: #334155 !important;
        }
        
        /* ========== MARKDOWN CODE BLOCKS ========== */
        code {
            background: #0a0f1e !important;
            color: #60a5fa !important;
            padding: 2px 6px;
            border-radius: 4px;
        }
        
        pre {
            background: #0a0f1e !important;
            border: 1px solid #334155 !important;
            border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)