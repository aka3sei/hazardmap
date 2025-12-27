import streamlit as st
import urllib.parse

# 1. ページ設定
st.set_page_config(page_title="不動産プロツール：立地＆安全", layout="wide")

# デザイン調整
st.markdown("""
    <style>
    .stSidebar { background-color: #f8f9fa; }
    .main-header { color: #1a73e8; font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    iframe { border-radius: 10px; border: 1px solid #ddd; }
    </style>
""", unsafe_allow_html=True)

# サイドバーメニュー
with st.sidebar:
    st.header("📋 営業メニュー")
    menu = st.radio(
        "調査項目を選択してください",
        ["利便性（立地・最寄り駅）", "安全性（ハザードマップ）"]
    )
    st.write("---")
    st.caption("完成済み機能：内装・立地・査定・駅検索・進捗・ローン診断")

# 住所共通入力
st.markdown(f'<div class="main-header">🏠 物件調査：{menu}</div>', unsafe_allow_html=True)
address = st.text_input("物件の住所を入力してください", placeholder="例：東京都三鷹市大沢２丁目")

# ---------------------------------------------------------
# メイン表示
# ---------------------------------------------------------

if not address:
    st.info("左のメニューを選択し、住所を入力して調査を開始してください。")

else:
    if menu == "利便性（立地・最寄り駅）":
        st.subheader("🚉 最短・最寄り駅ルート")
        
        # 以前のベストな設定（経路モード）を採用
        origin = urllib.parse.quote(address)
        destination = urllib.parse.quote("駅")
        map_url = f"https://maps.google.com/maps?f=d&saddr={origin}&daddr={destination}&dirflg=w&output=embed&z=16"
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.components.v1.iframe(map_url, height=550)
        with col2:
            st.success("最短駅への徒歩ルートです。")
            st.markdown("""
            **【営業のポイント】**
            - 坂道の有無を確認
            - 夜道の明るさをヒアリング
            - 信号待ちを含めた実歩数
            """)
            st.link_button("🚀 アプリでナビを開く", f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=walking")

    elif menu == "安全性（ハザードマップ）":
        st.subheader("🛡️ 国交省ハザードマップ一括照会")
        
        encoded_address = urllib.parse.quote(address)
        # 国交省の「重ねるハザードマップ」URL
        hazard_url = f"https://disaportal.gsi.go.jp/maps/?address={encoded_address}"
        
        st.warning("※赤いエリアは浸水、黄色/茶色のエリアは土砂災害のリスクが高い場所です。")
        
        # ハザードマップ表示
        st.components.v1.iframe(hazard_url, height=700, scrolling=True)
        
        st.info("💡 地図左上のメニューから「洪水」「土砂災害」などを切り替えて説明してください。")
        st.link_button("🌐 公式サイトを全画面で開く", hazard_url)

# ---------------------------------------------------------