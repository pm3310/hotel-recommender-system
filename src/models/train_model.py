# -*- coding: utf-8 -*-
import os
import pickle
import logging

import click
import gensim


def train(input_file, output_model_file):
    with open(input_file, 'rb') as f:
        sentences = pickle.load(f)

    model = gensim.models.Word2Vec(sentences, window=2, sg=1)

    model.wv.save_word2vec_format(
        output_model_file,
        binary=True,
    )


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_model_filepath', type=click.Path())
def main(input_filepath, output_model_filepath):
    """
    Train hotel cluster embeddings model on data saved in ../processed.
    """
    logger = logging.getLogger(__name__)
    logger.info('training hotel cluster embeddings models')

    input_file = os.path.join(input_filepath, 'sentences.pkl')
    output_model_file = os.path.join(output_model_filepath, 'hotelcluster2vec.bin')

    train(input_file, output_model_file)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
