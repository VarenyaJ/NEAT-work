import bisect

from typing import Union
from scipy.stats import poisson

import numpy as np
from numpy.random import Generator

from source.constants_and_defaults import LOW_PROBABILITY_THRESHOLD
from source.error_handling import premature_exit, log_mssg
from source.Options import Options


def mean_ind_of_weighted_list(candidate_list: list) -> int:
    """
    Returns the index of the mean of a weighted list

    :param candidate_list: weighted list
    :return: index of mean
    """
    my_mid = sum(candidate_list) / 2.0
    my_sum = 0.0
    for i in range(len(candidate_list)):
        my_sum += candidate_list[i]
        if my_sum >= my_mid:
            return i


class DiscreteDistribution:
    def __init__(self, values, weights, degenerate_val=None):
        # some sanity checking
        if not len(weights) or not len(values):
            log_mssg('Weight or value vector given to DiscreteDistribution() are 0-length.', 'error')
            premature_exit(1)

        sum_weight = float(sum(weights))

        self.degenerate = False
        self.degenerate_value = None

        # if probability of all input events is 0, consider it degenerate and always return the first value
        if sum_weight < LOW_PROBABILITY_THRESHOLD or len(values) == 1 or len(weights) == 1:
            self.degenerate = True
            if degenerate_val:
                self.degenerate_value = degenerate_val
            else:
                self.degenerate_value = values[0]
        else:
            self.weights = np.divide(weights, sum_weight)
            self.values = values
            if len(self.values) != len(self.weights):
                log_mssg('Length and weights and values vectors must be the same.', 'error')
                premature_exit(1)

            self.cum_prob = np.zeros_like(self.weights)
            self.cum_prob[1:] = np.cumsum(self.weights)[:-1]

    def sample(self, options: Options) -> Union[int, float]:
        """
        This is one of the slowest parts of the code. Or it just gets hit the most times. Will need
        to investigate at some point.
        :return: Since this function is selecting an item from a list, and the list could theoretically be anything,
        then in a broad sense this function returns a list item or a generic object. But I'm fairly confident that most
        of these uses will be lists of ints or floats, but will investigate further
        """

        if self.degenerate:
            return self.degenerate_value

        else:
            r = options.rng.random()
            return self.values[bisect.bisect(self.cum_prob, r) - 1]


# takes k_range, lambda, returns a DiscreteDistribution object
# corresponding to a poisson distribution
def poisson_list(k_value: int, input_mu: float) -> DiscreteDistribution:
    min_weight = 1e-12
    k_range = np.arange(k_value)
    poisson_pmf = poisson.pmf(k_range, input_mu)
    peak_zone = np.where(poisson_pmf >= min_weight)[0]

    if len(peak_zone) == 1:
        return DiscreteDistribution([0], [1], degenerate_val=k_range[peak_zone])
    elif len(peak_zone) == 0:
        return DiscreteDistribution([0], [1], degenerate_val=0)
    return DiscreteDistribution(k_range[peak_zone], poisson_pmf[peak_zone])


# quantize a list of values into blocks
def quantize_list(list_to_quantize):
    min_prob = 1e-12
    quant_blocks = 10
    sum_list = float(sum(list_to_quantize))
    sorted_list = sorted([n for n in list_to_quantize if n >= min_prob * sum_list])
    if len(sorted_list) == 0:
        return None
    qi = []
    for i in range(quant_blocks):
        # qi.append(sorted_list[int((i)*(len(sorted_list)/float(quant_blocks)))])
        qi.append(sorted_list[0] + (i / float(quant_blocks)) * (sorted_list[-1] - sorted_list[0]))
    qi.append(1e12)
    running_list = []
    prev_bi = None
    prev_i = None
    for i in range(len(list_to_quantize)):
        if list_to_quantize[i] >= min_prob * sum_list:
            bi = bisect.bisect(qi, list_to_quantize[i])
            # print i, l[i], qi[bi-1]
            if prev_bi is not None:
                if bi == prev_bi and prev_i == i - 1:
                    running_list[-1][1] += 1
                else:
                    running_list.append([i, i, qi[bi - 1]])
            else:
                running_list.append([i, i, qi[bi - 1]])
            prev_bi = bi
            prev_i = i
    return running_list
