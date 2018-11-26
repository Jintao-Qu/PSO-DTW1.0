import inspyred.ec
import collections
import copy
import functools
import itertools
import logging
import math
import time


class bounder(object):
    """Defines a basic bounding function for numeric lists.

    This callable class acts as a function that bounds a
    numeric list between the lower and upper bounds specified.
    These bounds can be single values or lists of values. For
    instance, if the candidate is composed of five values, each
    of which should be bounded between 0 and 1, you can say
    ``Bounder([0, 0, 0, 0, 0], [1, 1, 1, 1, 1])`` or just
    ``Bounder(0, 1)``. If either the ``lower_bound`` or
    ``upper_bound`` argument is ``None``, the Bounder leaves
    the candidate unchanged (which is the default behavior).

    As an example, if the bounder above were used on the candidate
    ``[0.2, -0.1, 0.76, 1.3, 0.4]``, the resulting bounded
    candidate would be ``[0.2, 0, 0.76, 1, 0.4]``.

    A bounding function is necessary to ensure that all
    evolutionary operators respect the legal bounds for
    candidates. If the user is using only custom operators
    (which would be aware of the problem constraints), then
    those can obviously be tailored to enforce the bounds
    on the candidates themselves. But the built-in operators
    make only minimal assumptions about the candidate solutions.
    Therefore, they must rely on an external bounding function
    that can be user-specified (so as to contain problem-specific
    information).

    In general, a user-specified bounding function must accept
    two arguments: the candidate to be bounded and the keyword
    argument dictionary. Typically, the signature of such a
    function would be the following::

        bounded_candidate = bounding_function(candidate, args)

    This function should return the resulting candidate after
    bounding has been performed.

    Public Attributes:

    - *lower_bound* -- the lower bound for a candidate
    - *upper_bound* -- the upper bound for a candidate

    """

    def __init__(self, len, lower_bound=None, upper_bound=None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.len = len
        if self.lower_bound is not None and self.upper_bound is not None:
            if not isinstance(self.lower_bound, collections.Iterable):
                self.lower_bound = itertools.repeat(self.lower_bound)
            if not isinstance(self.upper_bound, collections.Iterable):
                self.upper_bound = itertools.repeat(self.upper_bound)

    def __call__(self, candidate, args):
        # The default would be to leave the candidate alone
        # unless both bounds are specified.
        if self.lower_bound is None or self.upper_bound is None:
            return candidate
        else:
            if not isinstance(self.lower_bound, collections.Iterable):
                self.lower_bound = [self.lower_bound] * len(candidate)
            if not isinstance(self.upper_bound, collections.Iterable):
                self.upper_bound = [self.upper_bound] * len(candidate)
            bounded_candidate = candidate
            if candidate[3] == 0:
                print("$$$$$$$$$$$$$$",candidate)
            for i, (c, lo, hi) in enumerate(zip(candidate, self.lower_bound,
                                                self.upper_bound)):
                bounded_candidate[i] = int(max(min(c, hi), lo))

            if (bounded_candidate[0] + bounded_candidate[1] > self.len):
                sublen = bounded_candidate[0] + bounded_candidate[1] - self.len
                bounded_candidate[0] = bounded_candidate[0] - sublen
                #bounded_candidate[1] = bounded_candidate[1] - sublen
            if (bounded_candidate[2] + bounded_candidate[3] > self.len):
                sublen = bounded_candidate[2] + bounded_candidate[3] - self.len
                bounded_candidate[2] = bounded_candidate[2] - sublen
                #bounded_candidate[3] = bounded_candidate[3] - sublen
            if bounded_candidate[3] ==0:
                print("#################bounded error##############")
            return bounded_candidate
