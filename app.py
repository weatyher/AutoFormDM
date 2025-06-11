import streamlit as st

st.title("✅ AutoFormDM 起動テスト中")
st.write("このメッセージが見えたら、Streamlitは正しく動作しています。")

# secrets 確認ログ
st.write("🔐 Firebase API:", "***" if "firebase_api_key" in st.secrets else "❌ Not Found")
st.write("🔐 SendGrid API:", "***" if "sendgrid_api_key" in st.secrets else "❌ Not Found")

# その他の基本チェック
try:
    st.success("✅ Streamlit レンダリングOK！")
except Exception as e:
    st.exception(e)
# Main Streamlit app
