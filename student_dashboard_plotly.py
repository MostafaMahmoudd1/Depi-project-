import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# إعداد الصفحة
st.set_page_config(page_title="📊 Student Performance Dashboard", layout="wide")

# تحميل البيانات
scores_df = pd.read_csv("average_scores_month.csv")
att_df = pd.read_csv("attendance_trends.csv")

# تحويل التواريخ
scores_df["month"] = pd.to_datetime(scores_df["month"], errors="coerce")
att_df["date"] = pd.to_datetime(att_df["date"], errors="coerce")

# العنوان الرئيسي
st.title("📈 Student Performance Dashboard")
st.markdown("Interactive visualization of **Scores** and **Attendance Trends**")

# =============================
# 1️⃣ رسم معدل الدرجات الشهري
# =============================
st.subheader("Average Scores by Month")

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(scores_df["month"], scores_df["average_score"], marker="o", color="royalblue", linewidth=2)
ax1.set_title("Average Student Scores by Month", fontsize=14)
ax1.set_xlabel("Month")
ax1.set_ylabel("Average Score")
ax1.grid(True)
st.pyplot(fig1)

# =============================
# 2️⃣ خريطة حرارية للحضور
# =============================
st.subheader("Attendance Heatmap")

att_df["month"] = att_df["date"].dt.to_period("M").astype(str)
att_df["day"] = att_df["date"].dt.day
pivot = att_df.pivot_table(index="day", columns="month", values="count", aggfunc="sum", fill_value=0)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot, cmap="YlOrBr", ax=ax2)
ax2.set_title("Attendance Heatmap (Days vs Months)", fontsize=14)
st.pyplot(fig2)

# =============================
# 3️⃣ Insights
# =============================
st.subheader("Quick Insights")

col1, col2, col3 = st.columns(3)
col1.metric("📅 Total Months", f"{scores_df['month'].nunique()}")
col2.metric("📈 Average Score", f"{scores_df['average_score'].mean():.2f}")
col3.metric("👥 Attendance Records", f"{len(att_df)}")

st.success("✅ Dashboard loaded successfully!")
