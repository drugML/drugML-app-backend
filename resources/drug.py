from flask_cors import cross_origin
from flask_restplus import Resource, reqparse, Namespace
from helper.cnn_model import classifier_engine

from numpy import array as np_array

drug_ns = Namespace('drug', 'Drug methods')


_drug_parser = reqparse.RequestParser()
_drug_parser.add_argument(
    'molecular_weight',
    type=float,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'hydrogen_bond_donor_count',
    type=int,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'hydrogen_bond_acceptor_count',
    type=int,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'topological_polar_surface_area',
    type=float,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'heavy_atom_count',
    type=int,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'complexity',
    type=int,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'melting_point',
    type=float,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'solubility',
    type=float,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)
_drug_parser.add_argument(
    'logp',
    type=float,
    required=True,
    location=['form', 'json'],
    help="This field cannot be blank."
)


@drug_ns.route('/')
class Drug(Resource):
    """
    API Resource for drug classifier prediction
    """

    def get(self):
        return {'message': 'Successful'}, 200

    @drug_ns.doc(
        responses={
            200: "Successful",
            400: "Unsuccessful",
        },
        params={
            "molecular_weight": {'in': 'formData', 'required': True},
            "hydrogen_bond_donor_count": {'in': 'formData', 'required': True},
            "hydrogen_bond_acceptor_count": {'in': 'formData', 'required': True},
            "topological_polar_surface_area": {'in': 'formData', 'required': True},
            "heavy_atom_count": {'in': 'formData', 'required': True},
            "complexity": {'in': 'formData', 'required': True},
            "melting_point": {'in': 'formData', 'required': True},
            "solubility": {'in': 'formData', 'required': True},
            "logp": {'in': 'formData', 'required': True}
        }
    )
    @cross_origin()
    def post(self):
        data = _drug_parser.parse_args()
        drug_prop = []
        for value in data.values():
            drug_prop.append(value)

        drug_prop = np_array([drug_prop])

        prediction = classifier_engine(drug_prop, 'hypertension')
        print(prediction)

        return {'message': {
            'prediction-diabetes': str(prediction[0][0]),
            'prediction-hypertension': str(prediction[0][1]),
            'prediction-pain': str(prediction[0][2])
        }}, 200
