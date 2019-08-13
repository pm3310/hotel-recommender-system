# This is the file that implements a flask server to do inferences. It's
# the file that you will modify to implement the scoring for your own
# algorithm.

from __future__ import print_function

import json
import os

import flask

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

# A singleton for holding the model. This simply loads the model and holds
# it.
# It has a predict function that does a prediction based on the model and
# the input data.


class ScoringService(object):
    model = None

    @classmethod
    def get_model(cls):
        """Get the model object for this instance, loading it if it's not
        already loaded."""
        if cls.model is None:
            import gensim

            model_file_path = os.path.join(model_path, 'hotelcluster2vec.bin')
            cls.model = gensim.models.KeyedVectors.load_word2vec_format(
                model_file_path,
                binary=True
            )
        return cls.model

    @classmethod
    def predict(cls, hotel_cluster_id, top_n):
        """For the input, do the predictions and return them.

        Args:
            hotel_cluster_id (str): Hotel cluster id
            top_n (int): Number of top-N similar hotel cluster ids to return
        """
        clf = cls.get_model()
        return clf.wv.most_similar(hotel_cluster_id, topn=top_n)


# The flask app for serving predictions
app = flask.Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample
    container, we declare it healthy if we can load the model
    successfully."""
    health = ScoringService.get_model() is not None

    status = 200 if health else 404
    return flask.Response(
        response='\n', status=status, mimetype='application/json'
    )


@app.route('/invocations', methods=['POST'])
def transformation():
    """
    Example:

     {
        "hotel_cluster_id": "5",
        "top_n": 5
     }
    """
    if flask.request.content_type == 'application/json':
        data = flask.request.get_json()
    else:
        return flask.Response(
            response='This predictor only supports JSON data',
            status=415,
            mimetype='application/json'
        )

    predictions = ScoringService.predict(
        hotel_cluster_id=data['hotel_cluster_id'],
        top_n=data['top_n']
    )

    resp_json = {
        'predictions': predictions
    }

    return flask.Response(
        response=json.dumps(resp_json),
        status=200,
        mimetype='application/json'
    )
