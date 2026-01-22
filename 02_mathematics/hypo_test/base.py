class BaseTest:
    def __init__(self, alternative='two-sided', alpha=0.05):
        self.alternative = alternative
        self.alpha = alpha
        self.objective = None
        self.const = None
    
    def _compute_stats(self):
        self.test_stat = None
    
    def _set_dist(self):
        self.dist = None

    def _compute_pvalue(self, test_stat, dist):
        if self.alternative in ('two-sided', '2s', 'other than'):
            self.sign_h1 = '!='
            self.p_value = dist.sf(abs(test_stat)) * 2
        elif self.alternative in ('larger', 'right'):
            self.sign_h1 = '>'
            self.p_value = dist.sf(test_stat)
        elif self.alternative in ('smaller', 'left'):
            self.sign_h1 = '<'
            self.p_value = dist.cdf(test_stat)

    def _make_decision(self, p_value):
        if p_value <= self.alpha:
            self.sign_test = '<'
            self.h0_conclusion = 'reject'
        elif p_value > self.alpha:
            self.sign_test = '>'
            self.h0_conclusion = 'fail to reject'

    def conduct(self):
        self._compute_stats()
        self._set_dist()
        self._compute_pvalue(self.test_stat, self.dist)
        self._make_decision(self.p_value)

        print(
            f'H1: {self.objective} {self.sign_h1} {self.const}\n'
            f'p-value = {self.p_value:.4f} {self.sign_test} {self.alpha}\n'
            f'Conclusion: {self.h0_conclusion} H0'
        )