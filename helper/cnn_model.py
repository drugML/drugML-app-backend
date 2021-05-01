import os
from tensorflow.keras.models import load_model\



def classifier_engine(drug_properties, indication):
    """[summary]

    Args:
        drug_properties (list): list of drug properties
        indication (string): not currently used

    Returns:
        bool: True if drug is predicted for indication, otherwise False
    """
    path = os.path.join(os.getcwd(), 'resources', 'multiclass.model')
    model = load_model(path)
    prediction = model.predict(drug_properties)
    print(prediction)
    return prediction
    # if prediction >= 0.5:
    #     return True
    # else:
    #     return False
