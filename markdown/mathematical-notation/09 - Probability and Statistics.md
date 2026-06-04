# Probability and Statistics

In the summer of 1654, the Chevalier de Mere posed a gambling question to Blaise Pascal: how should two players divide the stakes of an unfinished game? Pascal wrote to Pierre de Fermat, and in a few weeks of correspondence they invented probability theory. The key move was not philosophical — it was notational. By assigning a *number* between 0 and 1 to each possible outcome, and manipulating those numbers with arithmetic, they turned gut-feeling uncertainty into something you could calculate.

Three and a half centuries later, the notation they seeded — refined by Bernoulli, Laplace, Kolmogorov, and Fisher — is how we write everything from A/B test results to machine learning loss functions. If you've used `random.random()` or `scipy.stats`, you've been speaking this language already. The notation just makes the grammar explicit.

## Probability

### Sample space and events

In probability theory, one begins with a set of fundamental outcomes, often denoted $\Omega$ or $S$. An event is a subset of $\Omega$.

The probability of an event$^1$ $A$ is typically denoted $P(A)$ but the following notations are also used: $\operatorname{Pr}(A)$ and $\mathbb{P}(A)$.

| Notation | Meaning | Python analogy |
| --- | --- | --- |
| $\Omega$ (or $S$) | sample space — set of all outcomes | `set(all_outcomes)` |
| $A \subseteq \Omega$ | event — a subset of outcomes | `event = {o for o in omega if ...}` |
| $P(A)$ | probability of event $A$ | `len(event) / len(omega)` (uniform) |

Given two events, $A$ and $B$, we have the following notations:

- $P(A \cap B)$ is the probability of $A$ and $B$. It is also sometimes denoted $P(AB)$ and $P(A \land B)$.
- $P(A \cup B)$ is the probability of $A$ or $B$. It is also sometimes denoted $P(A \lor B)$.
- $P(A \mid B)$ is the conditional probability of $A$ given $B$.

The inclusion-exclusion formula connects these:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

And Bayes' theorem — arguably the most important single formula in applied probability — inverts a conditional:

$$
P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}
$$

Thomas Bayes' paper was published posthumously in 1763. Two centuries later, his theorem became the foundation of an entire school of statistics.

$^1$More formally and abstractly, a probability space is a triple $(\Omega, \mathcal{F}, P)$ where $\Omega$ is a set, $\mathcal{F}$ is a $\sigma$-algebra of events, and $P$ is the probability function. In case $\Omega$ is finite or countably infinite, the probability space is called discrete and $\mathcal{F}$ can be ignored (as it can be taken to be $2^{\Omega}$).

### Random variables

Random variables (often abbreviated rv) are generally denoted with capital letters, $X$. The notation $X(\omega)$ is the value of $X$ at the point $\omega$ of the underlying probability space on which $X$ is defined. Notation such as $P(X \geq 0)$ is a shorthand for $P\{\omega : X(\omega) \geq 0\}$.

Given an event $A$, the notation $1_A$ is an indicator random variable defined by

$$
1_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \text{ and} \\ 0 & \text{otherwise}. \end{cases}
$$

Some authors write $I_A$ for indicator random variables. In NumPy, indicator variables are just boolean arrays: `(data > threshold).astype(int)`.

### Expected value, variance, and friends

The following are fundamental notations associated with random variables. Each has a direct code equivalent.

| Notation | Name | Definition | Code (scipy/numpy) |
| --- | --- | --- | --- |
| $E(X)$ or $\mathbb{E}(X)$ | expected value | $\sum_x x \, P(X=x)$ or $\int x \, f(x)\,dx$ | `dist.mean()` or `np.mean(data)` |
| $\mu_X$ | mean (synonym) | $E(X)$ | same |
| $\operatorname{Var}(X)$ or $\sigma_X^2$ | variance | $E[(X - \mu)^2]$ | `dist.var()` or `np.var(data)` |
| $\sigma_X$ | standard deviation | $\sqrt{\operatorname{Var}(X)}$ | `dist.std()` or `np.std(data)` |
| $\operatorname{Cov}(X, Y)$ | covariance | $E(XY) - E(X)E(Y)$ | `np.cov(x, y)[0,1]` |
| $\operatorname{Corr}(X, Y)$ | correlation | $\frac{\operatorname{Cov}(X,Y)}{\sigma_X \sigma_Y}$ | `np.corrcoef(x, y)[0,1]` |
| $E(X \mid Y)$ | conditional expectation | expected value of $X$ given $Y$ | (no one-liner) |

- **Expected value.** For a random variable $X$, its expected value is $E(X)$. Sometimes a different style $E$ is used, e.g., $\operatorname{E}(X)$ or $\mathbb{E}(X)$.

  The letter $\mu$ (standing for mean) is often used for the expected value of a random variable. If more than one random variable is under consideration, one may subscript $\mu$ with the name of that random variable; that is, $\mu_X$ is the expected value of $X$.

  In some disciplines, the notation $\langle X \rangle$ is used to denote the expected value of $X$. (Physics especially favors this bracket notation.)

- **Conditional expectation.** $E(X \mid Y)$ denotes the conditional expected value of $X$ given $Y$. This is also written $\mu_{X|Y}$.

- **Variance.** For a random variable $X$, $\operatorname{Var}(X)$ denotes the variance of $X$ defined by $\operatorname{Var}(X) = E\left[(X - \mu)^2\right] = E(X^2) - E(X)^2$. Often $\sigma^2$ denotes the variance. This may be subscripted with the name of the random variable: $\sigma_X^2$.

  The square root of the variance is known as the standard deviation and is denoted $\sigma$.

  The alternative form $E(X^2) - [E(X)]^2$ is the "computational formula" — useful both on paper and in code, since you can compute it in one pass.

- **Covariance.** Given two random variables $X$ and $Y$, their covariance is $\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y)$.

  If $\mathbf{X}$ is a random vector, i.e.,

  $$
  \mathbf{X} = \left[ \begin{array}{c} X_{1} \\ X_{2} \\ \vdots \\ X_{n} \end{array} \right]
  $$

  then the covariance matrix of $\mathbf{X}$ is often denoted $\Sigma$. This is an $n \times n$-matrix whose $i, j$-entry is $\operatorname{Cov}(X_i, X_j)$. In NumPy: `np.cov(data, rowvar=True)` returns exactly this matrix.

- **Correlation coefficient.** Given two random variables $X$ and $Y$, their correlation coefficient is

  $$
  \operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sigma_{X} \sigma_{Y}}.
  $$

  The result always lies in $[-1, 1]$. The value $\pm 1$ means perfect linear relationship; $0$ means no linear relationship (but not necessarily independence).

### Notation to code: SymPy's stats module

SymPy lets you declare random variables symbolically and compute $E(X)$, $\operatorname{Var}(X)$, and probabilities exactly — the notation maps almost one-to-one:

| Math notation | SymPy code |
| --- | --- |
| $X \sim N(\mu, \sigma^2)$ | `X = Normal('X', mu, sigma)` |
| $E(X)$ | `E(X)` |
| $\operatorname{Var}(X)$ | `variance(X)` |
| $P(X > 130)$ | `P(X > 130)` |

```python
<!-- include: code/mathematical-notation/09 - Probability and Statistics/01_python.py -->
```

### Entropy

The entropy of a random variable $X$ is denoted $H(X)$. It measures the average "surprise" of observing $X$ — the less predictable the outcomes, the higher the entropy. Claude Shannon introduced this in 1948, borrowing the name from thermodynamics on John von Neumann's advice (allegedly: "no one understands entropy, so you'll always have the advantage in arguments").

For discrete random variables,

$$
H(X) = - \sum_{x} P(X = x) \log P(X = x)
$$

where the sum is over all values $x$ that $X$ may take (and with the convention $0\log 0 = 0$). For a continuous random variable,

$$
H(X) = - \int_{-\infty}^{\infty} f(x) \log f(x) \, dx
$$

where $f(x)$ is the PDF of $X$. In both cases, the base of the logarithm depends on the application (with the most popular choices being 2, $e$, and 10). Base 2 gives bits; base $e$ gives nats.

Extensions of this notation include the joint entropy $H(X,Y)$ and the conditional entropy $H(X\mid Y)$ of the two random variables $X$ and $Y$.

In code: `scipy.stats.entropy(pk)` computes $H$ from a probability vector, defaulting to natural log.

## Distributions

Random variables are often best described by their distribution. Distributions, in turn, can be described in one of three principal ways, each with its own acronym.

### PMF, CDF, and PDF

- **PMF:** Discrete random variables can be specified by their *probability mass function*, or PMF, which specifies the probability associated with each possible value of the random variable: $f(x) = P(X = x)$.

- **CDF:** Real-valued random variables can be specified by their *cumulative distribution function*, or CDF: $F(x) = P(X \leq x)$. Most authors denote cumulative distribution functions with uppercase letters.

  The inverse function of the CDF is the *quantile function* which is often denoted $Q$. In scipy: `dist.ppf(q)` (percent point function) computes $Q(q) = F^{-1}(q)$.

- **PDF:** Real-valued, continuous random variables can also be specified by their *probability density function* $f(x)$. The relation to the cumulative distribution function $F(x)$ is $f(x) = F'(x)$ which gives

  $$
  P(X \in [a,b]) = \int_{a}^{b} f(x)\,dx.
  $$

  Most authors use lower case letters that correspond to the upper case letter for the random variable's CDF.

$^2$Discrete random variables take values in a finite or countably infinite set. Continuous random variables generally yield values in all of $\mathbb{R}$ or an interval in $\mathbb{R}$.

### The $\sim$ notation

We write $X \sim \mathcal{D}$ if the random variable $X$ has distribution $\mathcal{D}$. For example, if $X$ is a (standard) normal random variable, we write $X \sim N(0,1)$.

A collection of random variables with the same distribution are called *identically distributed*. In particular, if a collection of random variables are (mutually) independent and identically distributed, we write that they are iid (or IID).

### Notation-to-scipy mapping

There are many standard distributions of random variables, each with its own notation. The table below shows how the mathematical notation maps to `scipy.stats`:

| Math notation | Name | scipy constructor |
| --- | --- | --- |
| $\operatorname{Bin}(n, p)$ | Binomial | `binom(n, p)` |
| $\operatorname{Pois}(\lambda)$ | Poisson | `poisson(lam)` |
| $\operatorname{Exp}(\alpha)$ | Exponential | `expon(scale=1/alpha)` |
| $N(\mu, \sigma^2)$ | Normal | `norm(mu, sigma)` |
| $\chi_k^2$ | Chi-squared | `chi2(k)` |
| $t_\nu$ | Student's $t$ | `t(nu)` |
| $F(\nu_1, \nu_2)$ | Fisher–Snedecor | `f(nu1, nu2)` |

Note the parameter conventions: $N(\mu, \sigma^2)$ is parametrized by the *variance* $\sigma^2$, but `scipy.stats.norm` takes the *standard deviation* $\sigma$. Similarly, $\operatorname{Exp}(\alpha)$ uses the *rate*, but scipy's `expon` takes `scale = 1/alpha`. These mismatches are a perennial source of bugs.

### Standard distributions

The following are among the best-known distributions, each with their own notation.

- **Binomial.** Let $n$ be a nonnegative integer and $0 \leq p \leq 1$. A discrete random variable $X$ has the *binomial distribution* $\operatorname{Bin}(n,p)$ or $B(n,p)$ if its probability mass function is

  $$
  P(X = k) = \binom{n}{k} p^{k} (1-p)^{n-k}
  $$

  where $k \in \{0, 1, \ldots, n\}$. This counts the number of successes in $n$ independent trials, each with success probability $p$.

- **Poisson.** Let $\lambda$ be a positive real number. A discrete random variable $X$ has *Poisson distribution* $\operatorname{Pois}(\lambda)$ provided

  $$
  P(X = k) = \frac{\lambda^{k}}{k!} e^{-\lambda}
  $$

  where $k$ is a nonnegative integer. The Poisson distribution models the count of rare events in a fixed interval (server requests per second, typos per page). The use of $\lambda$ for the parameter (and hence the mean) is quite standard.

- **Exponential distribution.** For a positive real number $\alpha$, the exponential distribution is denoted $\operatorname{Exp}(\alpha)$. The CDF for a random variable with this distribution is $F(t) = 1 - \exp\{-\alpha t\}$ (where $t \geq 0$). It models the waiting time between Poisson events.

- **Normal / Gaussian.** A standard normal or Gaussian random variable $X$ has a probability density function typically denoted $\phi(x)$ where

  $$
  \phi(x) = \frac{1}{\sqrt{2\pi}} \exp\left\{-\frac{x^2}{2}\right\}.
  $$

  The corresponding CDF is often denoted $\Phi(x)$ which is closely related to the error function $\operatorname{erf}(x)$ (see the Functions chapter).

  More generally, if $\mu$ is a real number and $\sigma^2$ is a positive real number, then $N(\mu, \sigma^2)$, or sometimes $\mathcal{N}(\mu, \sigma^2)$, is the distribution of a normal random variable $X$ with mean $\mu$ and variance $\sigma^2$. Its probability density function is

  $$
  \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{-\frac{(x - \mu)^2}{2\sigma^2}\right\}.
  $$

  Thus a standard normal random variable has $X \sim N(0,1)$.

  The multivariable normal random variable $N_k(\vec{\mu}, \Sigma)$ is a random $k$-vector with mean $\vec{\mu}$ and covariance matrix $\Sigma$.

- **Chi-squared.** The chi-squared distribution is denoted $\chi^2$; more specifically, the chi-square distribution with $k$ degrees of freedom is denoted $\chi_k^2$. If $X_1, X_2, \ldots, X_k$ are IID standard normal random variables, then the sum of their squares $X = X_1^2 + \dots + X_k^2$ is chi-squared distributed $\chi_k^2$. Its probability density function is given by

  $$
  \frac{1}{2^{k/2} \Gamma(k/2)} x^{\frac{k}{2} - 1} e^{-x/2}
  $$

  where $\Gamma$ is the gamma function described in the Functions chapter.

- **Student's $t$-distribution.** This distribution is denoted $t_\nu$ where $\nu$ is a positive integer. It is given by $Z / \sqrt{V / \nu}$ where $Z$ and $V$ are independent random variables, $Z$ is a standard normal, and $V$ is $\chi_\nu^2$. William Sealy Gosset published it in 1908 under the pseudonym "Student" because his employer (the Guinness brewery) forbade employees from publishing.

- **$F$-distribution.** Also known as the Fisher-Snedecor distribution, this is written $F(\nu_1, \nu_2)$ where the $\nu_i$ are positive integers. It is given by

  $$
  \frac{X_1 / \nu_1}{X_2 / \nu_2}
  $$

  where $X_1, X_2$ are independent $\chi^2$-random variables with $\nu_1, \nu_2$ degrees of freedom, respectively.

### Convergence of random variables

Let $X$ and $X_1, X_2, \ldots$ be random variables. There are various notions of the sequence $X_i$ converging to $X$, each with its own notation. The distinctions matter: stronger modes of convergence imply weaker ones, but not vice versa.

$$
L^2 \;\Rightarrow\; \text{a.s.} \;\Rightarrow\; \text{in probability} \;\Rightarrow\; \text{in distribution}
$$

- **Convergence in distribution (in law).** This is denoted in various ways including:

  $$
  X_{n} \xrightarrow{d} X \qquad X_{n} \xrightarrow{\mathcal{D}} X \qquad X_{n} \xrightarrow{\mathcal{L}} X \qquad \mathcal{L}(X_{n}) \longrightarrow \mathcal{L}(X)
  $$

  The weakest form — only the CDFs need to converge, the random variables need not even live on the same probability space. The Central Limit Theorem is stated in this mode.

- **Convergence in probability.** This is denoted

  $$
  X_{n} \xrightarrow{p} X.
  $$

  For every $\epsilon > 0$, $P(|X_n - X| > \epsilon) \to 0$. The Weak Law of Large Numbers is stated in this mode.

- **Almost sure convergence.** This is denoted

  $$
  X_{n} \xrightarrow{\mathrm{a.s.}} X.
  $$

  The Strong Law of Large Numbers uses this. Almost sure convergence means $P(\lim_{n \to \infty} X_n = X) = 1$ — the set of outcomes where convergence fails has probability zero.

- **$L^2$ convergence.** This is denoted

  $$
  X_{n} \xrightarrow{L^{2}} X.
  $$

  This means $E[(X_n - X)^2] \to 0$. The strongest of the four.

Some authors place the notation as a subscript to the arrow rather than above, like this: $X_n \to_d X$.

## Statistics

The following is a potpourri of notation one encounters in statistics. Where probability theory builds models of uncertainty, statistics uses data to *infer* those models. The notation shifts accordingly: from $P$ and $E$ to $\bar{X}$ and $\hat{\theta}$.

### Descriptive statistics

Given numerical data $X_1, X_2, \ldots, X_n$ we have the following notations:

- **Average.** The (sample) average is denoted $\bar{X}$:

  $$
  \bar{X} = \frac{1}{n} \sum_{k=1}^{n} X_k.
  $$

- **Median.** The (sample) median is denoted $\tilde{X}$ or $\operatorname{med}(X)$.

- **Standard deviation.** The (sample) standard deviation is denoted $s$:

  $$
  s = \sqrt{\frac{\sum (X_i - \bar{X})^2}{n - 1}}.
  $$

  Note the $n - 1$ in the denominator (Bessel's correction), not $n$. This makes $s^2$ an unbiased estimator of the population variance $\sigma^2$. In NumPy: `np.std(data, ddof=1)` — the `ddof=1` flag triggers Bessel's correction.

- **$z$-score.** A common way to standardize data is to express it as the number of standard deviations above (or below) the mean. For this one uses the $z$-score:

  $$
  Z_i = \frac{X_i - \mu}{\sigma}
  $$

  where $\mu$ is the population mean and $\sigma$ is the population standard deviation. In code: `z = (x - mu) / sigma`. After standardization, the data has mean 0 and standard deviation 1.

- **Order statistics.** The notation $X_{(1)}, X_{(2)}, \ldots, X_{(n)}$ represents the same values but in nondecreasing order. That is $X_{(1)}$ is the smallest $X_i$, $X_{(n)}$ is the largest, and in general

  $$
  X_{(1)} \leq X_{(2)} \leq \dots \leq X_{(n)}.
  $$

  In NumPy: `np.sort(data)` produces the order statistics.

### Hypothesis testing

In hypothesis testing, the null hypothesis is typically denoted $H_0$ and the alternative hypothesis by $H_A$ or $H_1$. Incorrectly rejecting $H_0$ when, in fact, it is true is known as a type I error and the probability of committing such a mistake is typically denoted by $\alpha$. Accepting the null hypothesis when, in fact, it is false is known as a type II error and the probability of making this mistake is typically denoted $\beta$.

| Symbol | Meaning | Typical value |
| --- | --- | --- |
| $H_0$ | null hypothesis | "no effect" |
| $H_A$ or $H_1$ | alternative hypothesis | "there is an effect" |
| $\alpha$ | P(type I error) — false positive rate | 0.05 |
| $\beta$ | P(type II error) — false negative rate | 0.20 |
| $1 - \beta$ | power — probability of detecting a real effect | 0.80 |

The $p$-value is the probability, under $H_0$, of observing data at least as extreme as what was actually observed. When $p < \alpha$, we reject $H_0$. Fisher originally proposed $\alpha = 0.05$ as a convenient threshold, not a law of nature — but it stuck.

### Estimation

In statistical models, error (or noise) terms are often denoted with the letter $e$ or $\epsilon$; these can be subscripted if there are multiple error terms.

Often one is trying to determine some numerical quantity for a population (e.g., the proportion of a population that watch a certain television show) and this is done by computing an estimate from a random sample. It is conventional to place a hat on the estimator of the true parameter; that is, if $\theta$ is the parameter whose value we seek, then $\hat{\theta}$ is the estimator of $\theta$.

This hat convention is universal:

| True parameter | Estimator |
| --- | --- |
| $\mu$ (population mean) | $\hat{\mu} = \bar{X}$ (sample mean) |
| $\sigma^2$ (population variance) | $\hat{\sigma}^2 = s^2$ (sample variance) |
| $\theta$ (any parameter) | $\hat{\theta}$ (the estimate) |
| $f(x)$ (density) | $\hat{f}(x)$ (kernel density estimate) |
