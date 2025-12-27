import streamlit as st
import urllib.parse

# 1. ページ構成
st.set_page_config(page_title="物件安全調査", layout="wide", initial_sidebar_state="collapsed")

# 3本線とヘッダーを消すCSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    .main-header { 
        color: #d32f2f; 
        font-size: 28px; 
        font-weight: bold; 
        border-bottom: 3px solid #d32f2f; 
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    iframe { border-radius: 10px; border: 1px solid #ddd; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🛡️ 物件安全調査（ハザードマップ）</div>', unsafe_allow_html=True)

# ① 住所入力
address = st.text_input("物件の住所を入力してください", placeholder="例：東京都三鷹市大沢２丁目")

if not address:
    st.info("💡 住所を入力してください。")
else:
    # 国交省サイトの仕様に合わせたエンコード
    # addressパラメータを使い、ズームレベル(z=16)を指定します
    encoded_address = urllib.parse.quote(address)
    
    # 【重要】埋め込み用のURLを検索結果を維持する形式に変更
    hazard_url = f"https://disaportal.gsi.go.jp/maps/?address={encoded_address}#base=pale&ls=seamless%7Cborder%7Cdisaster1&disp=111&lcd=seamless&vs=c1j0l0u0f0&z=16"
    
    st.markdown(f"### 📍 調査地点：{address}")
    
    # マップ表示
    # 住所が反映されない場合、まずはこのiframeが表示されます
    st.components.v1.iframe(hazard_url, height=750, scrolling=True)

    # 確実にその住所を開くためのバックアップボタン
    st.markdown("---")
    st.write("⚠️ もし地図が動かない場合は、下のボタンを押すと別タブで確実にこの住所のマップが開きます。")
    st.link_button(f"🌐 {address} の詳細マップを別タブで開く", hazard_url, use_container_width=True)

    st.success("✅ ハザード情報の読み込みを試行しました。")
