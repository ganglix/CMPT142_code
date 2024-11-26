universe_size = 8.8e26  # m
paper_th = 0.1e-3 # m

def fold_thickness(n_fold, paper_th):
    thickness = paper_th * 2**n_fold
    return thickness

guess_n_fold = 103
if fold_thickness(guess_n_fold, paper_th) > universe_size:
    print(f"{guess_n_fold} of folds of a piece of newspaper is thicker than the size of universe!")