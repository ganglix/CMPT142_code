# universe_size = 8.8e26  # m
# paper_th = 0.1e-3 # m
#
# def fold_thickness(n_fold, paper_th):
#     thickness = paper_th * 2**n_fold
#     return thickness
#
# guess_n_fold = 103
# if fold_thickness(guess_n_fold, paper_th) > universe_size:
#     print(f"{guess_n_fold} of folds of a piece of newspaper is thicker than the size of universe!")


def pick_weights(weights, target):
    """
    pick the minimum number of weights from a list of weights so the total approaches but not exceeding the target
    :param weights: list, list of weights
    :param target: float, target value
    :return: list, weights got picked
    """
    weights.sort(reverse=True)
    picked_weights = []
    total_weight = 0
    n = 0
    while total_weight < target and n < len(weights):
        total_weight += weights[n]
        if total_weight > target:
            total_weight -= weights[n]
        else:
            picked_weights.append(weights[n])
        n += 1
    return picked_weights


inputs = ([2,3,5], 9)
expected_outputs = [5,3]

if pick_weights(*inputs) != expected_outputs:
    print(f'error found inputs: {inputs} \n expected outputs: {expected_outputs} \n got {pick_weights(*inputs)}' )

