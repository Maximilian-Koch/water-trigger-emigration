from flask import Flask, request, jsonify, render_template
import gpboost as gpb
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
MODEL_PATH = os.path.join(app.root_path, 'static', 'Main_Model.json')
AREA_MAP_PATH = os.path.join(app.root_path, 'static', 'area_id.csv')

bst = gpb.Booster(model_file=MODEL_PATH)
area_map_df = pd.read_csv(AREA_MAP_PATH)
area_map = dict(zip(area_map_df["Area"], area_map_df["panel_id"]))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    # 1) Extract the selected area
    area = data.get("Area", "")
    if area not in area_map:
        return jsonify({"error": f"Area '{area}' not found in area_id.csv"}), 400

    panel_id = int(area_map[area])

    # 2) Build the feature array for GPBoost: shape (1, 6)
    try:
        features = np.array([[data['log_GDPpC'],data['Water_Stress'],
        data['log_TIRWRpC'],data['Agri'],
        data['bEvents'],data['HDI'],data['agr_GDP']]])
    except KeyError as e:
        return jsonify({"error": f"Missing feature: {e}"}), 400

    try:
        pred_result = bst.predict(data=features, group_data_pred=[panel_id])
        migration_pred = float(pred_result["response_mean"][0])
    except Exception as e:
        return jsonify({"error": f"GPBoost prediction failed: {e}"}), 500

    return jsonify({"prediction": migration_pred})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
