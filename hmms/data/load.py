from matplotlib.pyplot import imread


def load_letters():
    letters = []
    # n missing
    for letter in 'abcdefghijklmopqrst':
        letters.append(imread('letters/%s.png' % letter).mean(axis=2))
    return letters


def letters_stats(letters):
    wmin, wmax, wmean = 300, 0, 0
    hmin, hmax, hmean = 300, 0, 0
    for letter in letters:
        h, w = letter.shape
        wmin = min(w, wmin)
        wmax = max(w, wmax)
        wmean += w
        hmin = min(h, hmin)
        hmax = max(h, hmax)
        hmean += h
    wmean /= len(letters)
    hmean /= len(letters)
    return (wmin, wmax, wmean, hmin, hmax, hmean)
