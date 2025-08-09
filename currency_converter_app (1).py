import streamlit as st

# عنوان التطبيق
st.title("محول SAR ↔ USDT - أبو راشد")

# اختيار نوع التحويل
choice = st.radio("اختر نوع التحويل:", ["ريال → USDT", "USDT → ريال"])

# إدخال المبلغ
amount = st.number_input("أدخل المبلغ:", min_value=0.0, format="%.2f")

# دوال التحويل
def sar_to_usdt(amount):
    rate = 3.75
    fees = 0.02
    return (amount / rate) * (1 - fees)

def usdt_to_sar(amount):
    rate = 3.75
    fees = 0.02
    return (amount * rate) * (1 - fees)

# زر الحساب
if st.button("احسب"):
    if choice == "ريال → USDT":
        st.success(f"{amount} ريال سعودي = {sar_to_usdt(amount):.6f} USDT بعد الخصومات")
    else:
        st.success(f"{amount} USDT = {usdt_to_sar(amount):.2f} ريال سعودي بعد الخصومات")

# حقوق الملكية
st.caption("● الحقوق محفوظة لـ أبو راشد")
