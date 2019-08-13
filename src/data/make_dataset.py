# -*- coding: utf-8 -*-
import os
import pickle
import logging

import click
import pandas as pd


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    train = pd.read_csv(os.path.join(input_filepath, 'train.csv'))

    grouped_hotel_clusters = train[train['is_booking'] == 1].groupby('user_id')['hotel_cluster'].apply(
        list).reset_index(
        name='hotel_clusters_list'
    )

    filtered_grouped_hotel_clusters = grouped_hotel_clusters[grouped_hotel_clusters['hotel_clusters_list'].map(len) > 4]

    sentences = [[str(_item) for _item in _list] for _list in filtered_grouped_hotel_clusters['hotel_clusters_list']]

    with open(os.path.join(output_filepath, 'sentences.pkl'), 'wb') as f:
        pickle.dump(sentences, f)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
