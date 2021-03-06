from itertools import product
import editdistance
from bit import PrivateKeyTestnet


def split_sentence_to_words(sentence):
    return set(filter(lambda x: x != '' and len(x) > 1, sentence.split(' ')))


def find_best_matches(num_of_matches, target, data_set):
    """
    :param num_of_matches: amount of matches to return
    :param target: iterable (preferably string)
    :param data_set: bunch of iterables in which the most similair will be searched
    :return: iterable of best matches
    """
    words = split_sentence_to_words(target)
    value_map = []
    for entry in data_set:
        entry_words = split_sentence_to_words(entry.title)
        pairs = list(product(words, entry_words))
        best_distance = sum(sorted([editdistance.eval(*pair) for pair in pairs])[:len(words)])
        value_map.append((best_distance, entry))
    return [entry[1] for entry in sorted(value_map, key=lambda x: x[0])[:min(num_of_matches, len(value_map))]]


def create_new_wallet():
    new_key = PrivateKeyTestnet()
    return new_key.to_wif(), new_key.address


def pay_with_btc(sender_wif, receiver_address, amount_btc):
    """
    :param sender_wif: sender wallet id
    :param receiver_address: receiver wallet id
    :param amount_btc:
    :param fee: fee to use during transaction (transaction priority depends on it)
    :return: hash which can be used to follow transaction status on blockchain.info
    """
    s_key = PrivateKeyTestnet(sender_wif)
    payment = (receiver_address, amount_btc, 'btc')
    return s_key.send([payment], unspents=s_key.get_unspents())


def get_btc_wallet_balance(wallet_wif):
    key = PrivateKeyTestnet(wallet_wif)
    return key.get_balance('btc')
