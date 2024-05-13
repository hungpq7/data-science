class BaseTest:
    def __init__(self):
        pass

    def _compute_pvalue(self, test_stat, distribution, alternative):
        if alternative in ['two-sided', '2s', 'other than']:
            sign_h1 = '!='
            p_value = distribution.sf(np.abs(test_stat)) * 2
        elif alternative in ['larger', 'right']:
            sign_h1 = '>'
            p_value = distribution.sf(test_stat)
        elif alternative in ['smaller', 'left']:
            sign_h1 = '<'
            p_value = distribution.cdf(test_stat)
        return sign_h1, p_value

    def _make_decision(self, p_value, alpha):
        if p_value <= alpha:
            sign_test = '<'
            msg = 'reject H0'
        elif p_value > alpha:
            sign_test = '>'
            msg = 'fail to reject H0'
        return sign_test, msg