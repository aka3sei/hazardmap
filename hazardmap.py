import streamlit as st
import urllib.parse

# 1. ページ構成
st.set_page_config(page_title="物件安全調査（ハザードマップ）", layout="wide", initial_sidebar_state="collapsed")

# デザイン調整
st.markdown("""
    <style>
    /* サイドバーとヘッダーを非表示 */
    [data-testid="stSidebar"] { display: none; }
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding-top: 2rem; }
    
    .main-header { 
        color: #d32f2f; /* 警告・安全を意識した色 */
        font-size: 28px; 
        font-weight: bold; 
        border-bottom: 3px solid #d32f2f; 
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    iframe { 
        border-radius: 10px; 
        border: 2px solid #ddd; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
    }
    .stTextInput > div > div > input {
        background-color: #fffaf0;
    }
    </style>
""", unsafe_allow_html=True)

# タイトル
st.markdown('<div class="main-header">🛡️ 物件安全調査（ハザードマップ）</div>', unsafe_allow_html=True)

# ① 住所入力
address = st.text_input("物件の住所を入力してください", placeholder="例：東京都三鷹市大沢２丁目")

if not address:
    st.info("💡 住所を入力すると、国交省の「重ねるハザードマップ」が自動表示されます。")
else:
    # URL用エンコード
    encoded_address = urllib.parse.quote(address)
    
    # 国交省ハザードマップポータルのURL
    hazard_url = f"https://disaportal.gsi.go.jp/maps/?address={encoded_address}"
    
    st.markdown(f"### 📍 調査地点：{address}")
    st.warning("⚠️ 地図上の色はリスクを示します：赤（浸水）、黄・茶（土砂災害）。左上のメニューで表示内容を切り替えられます。")

    # ハザードマップの埋め込み
    st.components.v1.iframe(hazard_url, height=750, scrolling=True)

    # 外部連携ボタン
    st.link_button("🌐 全画面でハザードマップを開く（国交省サイトへ）", hazard_url, use_container_width=True)

    st.success("✅ ハザード情報の照会が完了しました。")
