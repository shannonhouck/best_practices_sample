import pickle

def make_pickle(a, b, c):
    """
    Creates a new Python pickle with a, b, and c.
    """
    with open('output_pickle.pickle', 'wb') as f:
        pickle.dump({'a': a, 'b': b, 'c': c}, f, pickle.HIGHEST_PROTOCOL)

