import streamlit as st
import urllib.parse

# 1. ページ構成
st.set_page_config(page_title="物件安全調査", layout="wide")

# 3本線・ヘッダー・フッターを完全に消すCSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    .main-header { 
        color: #d32f2f; 
        font-size: 26px; 
        font-weight: bold; 
        border-bottom: 3px solid #d32f2f; 
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .hazard-box {
        background-color: #fff5f5;
        border: 2px solid #d32f2f;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🛡️ 物件安全調査（ハザードマップ）</div>', unsafe_allow_html=True)

# ① 住所入力
address = st.text_input("物件の住所を入力してください", placeholder="例：東京都三鷹市大沢２丁目")

if not address:
    st.info("💡 住所を入力してください。")
else:
    # エンコード
    encoded_address = urllib.parse.quote(address)
    
    # 国交省の検索済みURL
    hazard_url = f"https://disaportal.gsi.go.jp/maps/?address={encoded_address}#base=pale&ls=seamless%7Cborder%7Cdisaster1&disp=111&lcd=seamless&vs=c1j0l0u0f0&z=16"
    
    st.markdown(f"### 📍 調査地点：{address}")

    # 確実に動作させるための「2段階」表示
    st.markdown(f"""
    <div class="hazard-box">
        <h4>✅ 住所が特定されました</h4>
        <p>国交省ハザードマップで <strong>{address}</strong> のリスクを表示します。</p>
        <p style="font-size: 0.9em; color: #666;">※iframe制限回避のため、以下のボタンより公式マップを直接展開してください。</p>
    </div>
    """, unsafe_allow_html=True)

    # ボタンを大きく表示
    st.link_button(f"🚩 {address} のハザードマップを表示（別タブで開く）", hazard_url, use_container_width=True)

    # 補助的にGoogleマップを表示（場所の確認用）
    st.markdown("---")
    st.caption("地点確認用マップ")
    google_map_url = f"https://www.google.com/maps?q={encoded_address}&output=embed&z=16"
    st.components.v1.iframe(google_map_url, height=400)

    st.success("✅ 準備が整いました。上の赤いボタンを押してハザード情報を確認してください。")
