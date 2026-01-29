import numpy as np
import matplotlib.pyplot as plt

f"""
### Hypothesis Test Result: {self.objective.title()}
---
* **Null Hypothesis ($H_0$):** ${self.objective} = {self.const}$
* **Alternative Hypothesis ($H_a$):** ${self.objective} {self.sign_h1} {self.const}$
* **Test Statistic:** `{self.test_stat:.4f}`
* **p-value:** `{self.p_value:.4f}`

**Decision:** At $\\alpha = {alpha}$, $p \\text{{-value}} {self.sign_test} \\alpha$.
We **<span style='color:{color}'>{self.h0_conclusion.upper()}</span>** the null hypothesis.
"""

class BaseTest:
    def __init__(self):
        self.objective = None
        self.const = None
        self.p_value = None
        self.test_stat = None
        self.dist = None
    
    def _compute_stats(self):
        self.test_stat = None
    
    def _set_dist(self):
        self.dist = None

    def _compute_pvalue(self, test_stat, dist, alternative):
        if alternative in ('two-sided', '2s', 'other than'):
            self.sign_h1 = '!='
            self.p_value = dist.sf(abs(test_stat)) * 2
        elif alternative in ('larger', 'right', 'greater'):
            self.sign_h1 = '>'
            self.p_value = dist.sf(test_stat)
        elif alternative in ('smaller', 'left', 'less'):
            self.sign_h1 = '<'
            self.p_value = dist.cdf(test_stat)

    def _make_decision(self, p_value, alpha):
        if p_value <= alpha:
            self.sign_test = '<'
            self.h0_conclusion = 'reject'
        elif p_value > alpha:
            self.sign_test = '>'
            self.h0_conclusion = 'fail to reject'

    def conduct(self, alternative='two-sided', alpha=0.05, print_result=True):
        self._compute_stats()
        self._set_dist()
        self._compute_pvalue(self.test_stat, self.dist, alternative)
        self._make_decision(self.p_value, alpha)

        if print_result is True:
            print(
                f'Alternative hypothesis H1: {self.objective} {self.sign_h1} {self.const}\n'
                f'p-value = {self.p_value:.4f} {self.sign_test} {alpha}\n'
                f'Conclusion: {self.h0_conclusion} H0'
            )
    
    def plot(self):
            if self.dist is None or self.p_value is None:
                print("Please run .conduct() before plotting.")
                return

            fig, ax = plt.subplots(figsize=(6, 4))
            
            # 1. Define x-range (covering 99.9% of the distribution)
            x = np.linspace(self.dist.ppf(0.001), self.dist.ppf(0.999), 500)
            y = self.dist.pdf(x)
            ax.plot(x, y, color='grey', ls='-', lw=2, label=f'{self.dist.dist.name} distribution')

            # 2. Handle Rejection Regions based on the Alternative Hypothesis
            # We need alpha from the conduct step; assuming it's stored or using 0.05 default
            alpha = 0.05 
            
            if self.sign_h1 == '!=':
                # Two-sided
                cv_low = self.dist.ppf(alpha / 2)
                cv_high = self.dist.ppf(1 - alpha / 2)
                
                x_left = np.linspace(x.min(), cv_low, 100)
                x_right = np.linspace(cv_high, x.max(), 100)
                
                ax.fill_between(x_left, self.dist.pdf(x_left), color='darkorange', alpha=0.3, label='Rejection Region')
                ax.fill_between(x_right, self.dist.pdf(x_right), color='darkorange', alpha=0.3)
                ax.axvline(cv_low, color='darkorange', linestyle='--', lw=1)
                ax.axvline(cv_high, color='darkorange', linestyle='--', lw=1)
                
            elif self.sign_h1 == '>':
                # Right-tailed
                cv = self.dist.ppf(1 - alpha)
                x_rej = np.linspace(cv, x.max(), 100)
                ax.fill_between(x_rej, self.dist.pdf(x_rej), color='darkorange', alpha=0.3, label='Rejection Region')
                ax.axvline(cv, color='darkorange', linestyle='--', lw=1)
                
            elif self.sign_h1 == '<':
                # Left-tailed
                cv = self.dist.ppf(alpha)
                x_rej = np.linspace(x.min(), cv, 100)
                ax.fill_between(x_rej, self.dist.pdf(x_rej), color='darkorange', alpha=0.3, label='Rejection Region')
                ax.axvline(cv, color='darkorange', linestyle='--', lw=1)

            # 3. Plot the actual Test Statistic
            ax.axvline(self.test_stat, color='indianred', lw=2, label=f'Test Stat: {self.test_stat:.2f}')
            
            # Formatting
            # ax.set_title(f'Hypothesis Test Visualization ({self.objective})', fontsize=14)
            ax.set_xlabel('Value')
            ax.set_ylabel('Probability Density')
            ax.legend()
            ax.grid(False)
            # sns.despine()
            plt.show()