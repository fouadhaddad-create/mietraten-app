import streamlit as st

st.title("Mietraten Rechner (EXAKT wie Excel – Formelmodus)")

# Eingaben exakt nach Spalte B
ek_vs_gesamt = st.number_input("EK + VS gesamt", value=330.00, step=0.01)
mietrate1_gesamt = st.number_input("1. Mietrate gesamt", value=500.00, step=0.01)
mietrate2_gesamt = st.number_input("2.-6. Mietrate gesamt", value=699.00, step=0.01)
tank_gesamt = st.number_input("Tank gesamt", value=60.00, step=0.01)
auslieferung_gesamt = st.number_input("Auslieferung gesamt", value=269.00, step=0.01)
abholung_gesamt = st.number_input("Abholung gesamt", value=149.00, step=0.01)
tage_gesamt = st.number_input("Gesamtlaufzeit (Tage)", value=90, step=1)

# Automatische Nebenwerte
tage_ab_2_monat = max(0, tage_gesamt - 30)

if st.button("Berechnen"):
    # Tageswerte
    ek_vs_tag = ek_vs_gesamt / tage_gesamt
    mietrate2_tag = mietrate2_gesamt / tage_gesamt
    tank_tag = tank_gesamt / tage_gesamt
    auslieferung_tag = auslieferung_gesamt / tage_gesamt
    auslieferung_monat = auslieferung_tag * 30
    abholung_tag = abholung_gesamt / tage_gesamt
    abholung_monat = abholung_tag * 30

    # Ergebnis "Summe" wie Formel B12: (C4*30) + (C5*B10) + (C6*30) + D7 + D8
    summe = (ek_vs_tag * 30) + (mietrate2_tag * tage_ab_2_monat) + (tank_tag * 30) + auslieferung_monat + abholung_monat

    # B13: Marge pro Monat = Summe – EK+VS_gesamt
    marge_pro_monat = summe - ek_vs_gesamt
    
    # B14: Marge Laufzeit = Marge pro Monat * Monate (Tage/30)
    monate = tage_gesamt / 30 if tage_gesamt else 0
    marge_laufzeit = marge_pro_monat * monate

    st.subheader("Ergebnisse (wie Excel)")
    st.write(f"**Summe (B12): {summe:.2f} €**")
    st.write(f"**Marge pro Monat (B13): {marge_pro_monat:.2f} €**")
    st.write(f"**Marge Laufzeit (B14): {marge_laufzeit:.2f} €**")



