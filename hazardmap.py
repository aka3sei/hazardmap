import streamlit as st

# 1. ページ構成（paddingを0にして余白を極限まで削ります）
st.set_page_config(page_title="物件安全調査", layout="wide")

# CSSで高さを固定し、3本線・ヘッダー・フッターを隠す
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 画面全体の余白をゼロにする */
    .block-container { 
        padding-top: 0rem; 
        padding-bottom: 0rem; 
        padding-left: 0rem; 
        padding-right: 0rem; 
    }
    
    /* アプリ全体の背景 */
    .stApp { background-color: #ffffff; }
    
    /* ヘッダーの調整 */
    .main-header { 
        color: #d32f2f; 
        font-size: 20px; 
        font-weight: bold; 
        padding: 10px 20px;
        background-color: #fff;
        border-bottom: 1px solid #ddd;
    }
    
    /* iframeの高さを画面の高さに合わせる */
    .map-container iframe {
        width: 100%;
        height: 90vh; /* 画面高の90%を使用 */
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 最小限のタイトル
st.markdown('<div class="main-header">🛡️ 物件安全調査（ハザードマップポータル）</div>', unsafe_allow_html=True)

# 国交省ハザードマップポータルの埋め込み
# heightを明示的に大きく指定（1000px）し、CSS側でも制御します
hazard_portal_url = "https://disaportal.gsi.go.jp/maps/index.html?number=disaster1"

st.components.v1.iframe(hazard_portal_url, height=1000, scrolling=True)

# 予備のリンクボタン（モバイルで見切れる場合用）
st.link_button("🌐 全画面で開く（国交省サイトへ）", hazard_portal_url, use_container_width=True)
