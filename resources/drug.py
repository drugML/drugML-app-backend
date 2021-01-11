from flask_restplus import Resource, reqparse, Namespace

drug_ns = Namespace('drug', 'Drug methods')


@drug_ns.route('/')
class Drug(Resource):
    """
    API Resource for drug model
    """
    @drug_ns.doc(
        responses={
            200: "Successful",
            400: "Unsuccessful",
        },
        # params={
        #     'username': {'in': 'json', 'required': True},
        #     'email': {'in': 'json', 'required': True},
        #     'password': {'in': 'json', 'required': True},
        #     'name': {'in': 'json', 'required': True},
        # }
    )
    def get(self):
        return {'message': 'Successful'}, 200

    def post(self):
        return {'message': 'Successful'}, 200
