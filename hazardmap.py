import streamlit as st

# 1. ページ構成
st.set_page_config(page_title="物件安全調査（ハザードマップ）", layout="wide")

# 3本線・メニュー・ヘッダーを完全に消すCSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 0rem; padding-bottom: 0rem; }
    
    /* アプリ全体の背景を調整 */
    .stApp { background-color: #ffffff; }
    
    .main-header { 
        color: #d32f2f; 
        font-size: 24px; 
        font-weight: bold; 
        padding: 15px;
        background-color: #fff;
        border-bottom: 2px solid #d32f2f;
    }
    iframe { 
        border: none; 
        width: 100%;
        height: calc(100vh - 80px); /* 画面いっぱいに表示 */
    }
    </style>
""", unsafe_allow_html=True)

# タイトル（営業時に分かりやすくするため最小限のヘッダーを残しています）
st.markdown('<div class="main-header">🛡️ 物件安全調査（ハザードマップポータル）</div>', unsafe_allow_html=True)

# 国交省ハザードマップポータルのトップページ（「重ねるハザードマップ」）
# このURLは、最初に「住所から探す」「現在地から探す」の選択肢が出る画面です。
hazard_portal_url = "https://disaportal.gsi.go.jp/maps/index.html?number=disaster1"

# ハザードマップポータルを埋め込み表示
# st.components.v1.iframe を使い、画面全体をマップにします
st.components.v1.iframe(hazard_portal_url, scrolling=True)

# 補足：全画面で開くためのボタンをページ下部に小さく配置
st.markdown("---")
st.link_button("🌐 ブラウザの全画面で開く（国交省サイト）", hazard_portal_url, use_container_width=True)
