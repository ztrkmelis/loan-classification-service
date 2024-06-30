import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def call_model():
    model = pickle.load(open('/Users/melisozturk/Downloads/loan_classification_model.sav', 'rb'))
    return model


def get_user_details(loan_id_):
    df = pd.read_csv(r"/Users/melisozturk/PycharmProjects/loan_model/loan_approval_dataset_updated.csv",
                     sep=";",
                     engine='python',
                     encoding="latin-1")
    df["loan_id"] = df["loan_id"].astype(str)
    # val = "_" + str(df.loan_id.unique()[0]) + "_"
    if str(loan_id_) in df.loan_id.unique():
        df = df[df["loan_id"] == str(loan_id_)]
        def column_scaler(column_name, df_):
            scaler = StandardScaler()
            return scaler.fit_transform(df_[[column_name]])

        df.columns = [x.strip() for x in df.columns]
        df.columns = [x.lower() for x in df.columns]
        numeric_columns = ["no_of_dependents", "income_annum", "loan_amount", "cibil_score", "residential_assets_value",
                           "commercial_assets_value", "luxury_assets_value", "bank_asset_value"]
        for num_col in numeric_columns:
            df[num_col] = column_scaler(column_name=num_col, df_=df)
        df = pd.get_dummies(df, columns=['city'])
        df = pd.get_dummies(df, columns=['education'])
        df = pd.get_dummies(df, columns=['self_employed'])
        df.columns = ["_".join(x.lower().split(" ")).replace("ý", "i") for x in df.columns]
        df = df.drop(columns=["loan_id", "loan_status"])
        all_columns = ['no_of_dependents', 'income_annum', 'loan_amount', 'loan_term',
                       'cibil_score', 'residential_assets_value', 'commercial_assets_value',
                       'luxury_assets_value', 'bank_asset_value', 'city_ankara', 'city_bursa',
                       'city_erzurum', 'city_istanbul', 'city_izmir', 'education__graduate',
                       'education__not_graduate', 'self_employed__no', 'self_employed__yes']
        rest_columns = list(set(all_columns) - set(df.columns))
        df[rest_columns] = 0
        df = df[all_columns]
        return df
    else:
        return "please provide a valid user key"


def get_prediction(loan_id_):
    user_df = get_user_details(loan_id_)
    if isinstance(user_df, str):
        return {"Exception": user_df}
    else:
        model = call_model()
        print("model is here")
        print(user_df.T)
        pred = model.predict(user_df)
        print("pred: ", pred[0])
        status_dict = {1: "Rejected", 0: "Approved"}
        return {"loan_id": loan_id_, "prediction":status_dict[pred[0]]}