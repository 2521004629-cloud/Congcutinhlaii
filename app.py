import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm Khánh Xuân",
    page_icon="💰",
    layout="centered"
)

st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM KHÁNH XUÂN")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

# ==============================
# NHẬP DỮ LIỆU
# ==============================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# ==============================
# NÚT TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Đổi lãi suất từ % sang số thập phân
    lai_suat_decimal = lai_suat / 100

    # Quy đổi kỳ hạn sang năm
    so_nam = ky_han / 12

    # ==============================
    # TÍNH LÃI THEO HÌNH THỨC
    # ==============================

    if hinh_thuc == "Cuối kỳ":

        # Tổng tiền lãi
        tong_lai = tien_gui * lai_suat_decimal * so_nam

        # Lãi nhận cuối kỳ
        lai_dinh_ky = tong_lai

        # Tổng tiền nhận được
        tong_tien = tien_gui + tong_lai

        ten_ky = "Cuối kỳ"

    elif hinh_thuc == "Hàng tháng":

        # Lãi mỗi tháng
        lai_dinh_ky = tien_gui * lai_suat_decimal / 12

        # Số tháng
        so_ky = ky_han

        # Tổng tiền lãi
        tong_lai = lai_dinh_ky * so_ky

        # Tổng tiền gốc + lãi
        tong_tien = tien_gui + tong_lai

        ten_ky = "mỗi tháng"

    else:  # Hàng quý

        # Lãi mỗi quý
        lai_dinh_ky = tien_gui * lai_suat_decimal / 4

        # Số quý
        so_ky = ky_han / 3

        # Tổng tiền lãi
        tong_lai = lai_dinh_ky * so_ky

        # Tổng tiền gốc + lãi
        tong_tien = tien_gui + tong_lai

        ten_ky = "mỗi quý"

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================

    st.success("✅ TÍNH TOÁN THÀNH CÔNG")

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💰 Tiền lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_lai:,.0f} VNĐ"
        )

    st.metric(
        "💵 Tổng tiền gốc + lãi",
        f"{tong_tien:,.0f} VNĐ"
    )

    # ==============================
    # CHI TIẾT
    # ==============================

    st.divider()

    st.subheader("📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    st.info(
        f"Bạn nhận được **{lai_dinh_ky:,.0f} VNĐ** tiền lãi {ten_ky}."
    )
