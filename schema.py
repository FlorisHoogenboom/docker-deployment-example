import pandas as pd
from marshmallow import Schema, fields, post_load, ValidationError


class ModelSchema(Schema):
    airFlow = fields.Integer(required=True)
    waterTemp = fields.Integer(required=True)
    acidConc = fields.Integer(required=True)

    @post_load
    def to_pandas(self, data):
        return pd.DataFrame(
            [list(data.values())],
            columns=list(data.keys())
        )
