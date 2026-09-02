"""
Sistem Presensi Mahasiswa & Kelas — Lab Micro Teaching FisMat
Web App berbasis Streamlit
"""
import streamlit as st
import datetime
import database
from config import load_config

# ─── Inisialisasi ─────────────────────────────────────────────────────────────
database.init_db()
config = load_config()

st.set_page_config(
    page_title=f"{config.get('app_title', 'Presensi Mahasiswa')} — {config.get('company_name', 'Lab FisMat')}",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS Global ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Sidebar */
[data-testid="stSidebar"] { background: #0F172A; }
[data-testid="stSidebar"] * { color: #94A3B8 !important; }

/* Metric cards */
.metric-card {
    background: #1E293B;
    border-radius: 12px;
    padding: 18px 16px;
    text-align: center;
    border: 1px solid #334155;
    margin-bottom: 6px;
}
.metric-card .val { font-size: 2rem; font-weight: 800; line-height: 1.1; }
.metric-card .lbl { font-size: 0.75rem; font-weight: 600; margin-top: 4px; }

/* Tombol aksi presensi */
div[data-testid="stButton"] > button {
    width: 100%;
    height: 60px;
    font-weight: 700;
    border-radius: 10px;
}

/* Alert box */
.alert-success { background:#064E3B; border-left:4px solid #10B981; padding:12px 16px; border-radius:8px; color:#34D399; margin:8px 0; }
.alert-error   { background:#7F1D1D; border-left:4px solid #EF4444; padding:12px 16px; border-radius:8px; color:#FCA5A5; margin:8px 0; }
.alert-info    { background:#1E3A8A; border-left:4px solid #3B82F6; padding:12px 16px; border-radius:8px; color:#93C5FD; margin:8px 0; }

/* Badge status */
.badge { display:inline-block; padding:3px 10px; border-radius:999px; font-size:0.72rem; font-weight:700; }
.badge-hadir   { background:#064E3B; color:#34D399; }
.badge-kelas   { background:#78350F; color:#FCD34D; }
.badge-tugas   { background:#1E3A8A; color:#60A5FA; }
.badge-pulang  { background:#581C87; color:#C084FC; }
.badge-belum   { background:#334155; color:#94A3B8; }
.badge-late    { background:#7F1D1D; color:#FCA5A5; }

/* Header jam */
.jam-besar { font-size:2.8rem; font-weight:800; color:#38BDF8; font-family:Consolas,monospace; }
.tanggal-besar { font-size:1.1rem; font-weight:700; color:#F8FAFC; }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar Navigasi ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚡ PRESENSI MAHASISWA")
    st.markdown(f"*{config.get('company_name','Lab Micro Teaching FisMat')}*")
    st.markdown("---")

    PAGES = {
        "🕒  Presensi Mahasiswa": "presensi",
        "📊  Dashboard Live": "dashboard",
        "🎓  Data Mahasiswa": "pegawai",
        "📑  Rekap & Laporan": "laporan",
        "⚙️  Pengaturan": "settings",
    }

    if "active_page" not in st.session_state:
        st.session_state.active_page = "presensi"

    for label, key in PAGES.items():
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.active_page = key

    st.markdown("---")
    st.markdown("<small style='color:#475569'>Versi 2.0 Web Edition</small>", unsafe_allow_html=True)

# ─── Routing ──────────────────────────────────────────────────────────────────
page = st.session_state.active_page

if page == "presensi":
    from pages_st.presensi_page import render
    render()
elif page == "dashboard":
    from pages_st.dashboard_page import render
    render()
elif page == "pegawai":
    from pages_st.pegawai_page import render
    render()
elif page == "laporan":
    from pages_st.laporan_page import render
    render()
elif page == "settings":
    from pages_st.settings_page import render
    render()
