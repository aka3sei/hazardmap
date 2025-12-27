import streamlit as st

# 1. ページ構成（スマホ向けに余白を完全に除去）
st.set_page_config(page_title="物件安全調査", layout="wide")

# スマホに最適化するためのCSS
st.markdown("""
    <style>
    /* 1. 不要なメニュー・ヘッダーをすべて非表示 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 2. スマホの画面端まで地図を広げる設定 */
    .block-container { 
        padding-top: 0rem; 
        padding-bottom: 0rem; 
        padding-left: 0rem; 
        padding-right: 0rem; 
    }
    
    /* 3. タイトルバーのデザイン（スマホで邪魔にならない高さ） */
    .main-header { 
        color: #d32f2f; 
        font-size: 16px; 
        font-weight: bold; 
        padding: 10px;
        text-align: center;
        background-color: #ffffff;
        border-bottom: 1px solid #eee;
    }
    
    /* 4. iframe（地図）のサイズ指定：スマホの縦幅にフィットさせる */
    .stIFrame iframe {
        width: 100vw;   /* 画面の横幅いっぱい */
        height: 75vh;  /* 画面の高さの75%（入力欄やボタンが隠れない高さ） */
        border: none;
    }

    /* 5. リンクボタンの微調整 */
    .stLinkButton {
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 最小限のタイトル
st.markdown('<div class="main-header">🛡️ 物件安全調査（ハザードマップ）</div>', unsafe_allow_html=True)

# 国交省ハザードマップポータル（重ねるハザードマップ）
hazard_portal_url = "https://disaportal.gsi.go.jp/maps/index.html?number=disaster1"

# 埋め込み表示
# heightを明示的に指定しつつ、CSSの75vhが優先されるようにします
st.components.v1.iframe(hazard_portal_url, height=600, scrolling=True)

# 別タブ用の導線（スマホで操作しにくい場合の保険）
st.link_button("🌐 公式サイトを別タブで開く", hazard_portal_url, use_container_width=True)
