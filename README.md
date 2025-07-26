# Water‑Crisis‑Driven Emigration: Algorithm Audit & Simulation

## Project Overview
This repository contains the code and analysis for a critical algorithm audit exploring how water‑governance dynamics drive cross‑border emigration in water‑stressed regions. By combining a Critical Political Economy lens with a modified gradient‑boosted tree model (LaGaBoost [1]), the study shows how displacement is defined by structural drivers beyond physical water scarcity.

The report was part of a group assignment during semester 4 of my bachelor in Computational Social Science. The code is entirely produced by me.
## Methodology
1. **Data Assembly**  
   - **Emigration:** UN migration stock data (1990–2024) at 5‑year intervals. [2]
   - **Water & Socioeconomic Indicators:** FAO AQUASTAT (water stress, agricultural withdrawal), GDP per capita, HDI.  [3]
   - **Conflict Events:** Pacific Institute water‑triggered conflict chronology.  [4]
2. **Feature Engineering**  
   - Five‑year lagging of annual variables to align with migration intervals.  
   - Log‑transformation of GDP per capita and water‑stress metrics to capture diminishing returns.  
3. **Modeling Approach**  
   - **LaGaBoost:** LightGBM adapted for negative‑binomial panel data, tuned via 5‑fold group cross‑validation (groups = countries).  
   - **Fairness Audit:** Post‑hoc residual and SMAPE analyses across GDP per capita quartiles; mitigated bias through SMOGN oversampling and multi‑objective hyperparameter optimization to balance performance and equity.  
4. **Interpretability & Deployment**  
   - SHAP values to quantify feature impacts on emigration predictions.  
   - Interactive simulation tool hosted at [emigration‑simulation.onrender.com](https://emigration-simulation.onrender.com) (the website takes about a minute to load due to using free hosting.)

## Main Findings
- **Governance Over Scarcity:** Effective water‑infrastructure access (‘economic water scarcity’) predicts emigration more strongly than absolute water availability :contentReference[oaicite:3]{index=3}.  
- **Entrapment Effect:** Lowest‑GDP, high‑agriculture countries show constrained mobility, despite high water stress.  
- **Key Predictors:**  
  - **↑ HDI** and **↑ agricultural water withdrawal** → more emigration  
  - **Water‑triggered conflicts** significantly amplify outflows  
  - **Very low or very high renewable water per capita** → lower emigration (resilience or entrapment)  
- **Policy Implications:** Technical metrics (e.g., SDG 6.4.2) must be complemented by equity‑centered, context‑sensitive governance to avoid reproducing displacement drivers.


![Migration map] (https://github.com/Maximilian-Koch/water-trigger-emigration/blob/main/analysis/migration_map.png?raw=true)

## Repository Contents
- `analysis/` – Data, analysis, and auditing
- `static/` and `templates/` –  website content
- `requirements.txt` – Python dependencies  
- `README.md`        – Project summary and usage instructions  

## Getting Started
```bash
git clone https://github.com/Maximilian-Koch/water-trigger-emigration/
cd water‑trigger-emigration
pip install -r requirements.txt
```

## Data references
[1] Sigrist, F. (2022). Latent Gaussian model boosting. IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(2), 1894-1905.

[2] United Nations Department of Economic and Social Affairs, Population Division (2024). International Migrant Stock 2024. https://www.un.org/development/desa/pd/content/international-migrant-stock. Retrieved March 1, 2025. 

[3] Food and Agriculture Organization of the United Nations (FAO). (n.d.). AQUASTAT: FAO’s global information system on water and agriculture. https://www.fao.org/aquastat/en/. Retrieved March 1, 2025.

[4] Pacific Institute (2024) Water Conflict Chronology. Pacific Institute, Oakland, CA. https://www.worldwater.org/water-conflict/. Retrieved April 5, 2025.