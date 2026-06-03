# Probability and Statistics

## 1. Probability

Events. In probability theory, one begins with a set of fundamental outcomes, often denoted $\Omega$ or $S$. An event is a subset of $\Omega$.

The probability of an event$^1 A$ is typically denoted $P(A)$ but the following notations are also used: $\operatorname{Pr}(A)$ and $\mathbb{P}(A)$.

Given two events, $A$ and $B$, we have the following notations:

- $P(A \cap B)$ is the probability of $A$ and $B$. It is also sometimes denoted $P(AB)$ and $P(A \land B)$.
- $P(A \cup B)$ is the probability of $A$ or $B$. It is also sometimes denoted $P(A \lor B)$.
- $P(A \mid B)$ is the conditional probability of $A$ given $B$.

Random variables. Random variables (often abbreviated rv) are generally denoted with capital letters, $X$. The notation $X(\omega)$ is the value of $X$ at the point $\omega$ of the underlying probability space on which $X$ is defined. Notation such as $P(X \geq 0)$ is a shorthand for $P\{\omega : X(\omega) \geq 0\}$.

Given an event $A$, the notation $1_A$ is an indicator random variable defined by

$$
1_A(\omega) = \begin{cases} 1 &amp; \text{if } \omega \in A \text{ and} \\ 0 &amp; \text{otherwise}. \end{cases}
$$

Some authors write $I_A$ for indicator random variables.

The following are fundamental notations associated with random variables.

- Expected value. For a random variable $X$, its expected value is $E(X)$. Sometimes a different style $E$ is used, e.g., $\operatorname{E}(X)$ or $\mathbb{E}(X)$.

The letter $\mu$ (standing for mean) is often used for the expected value of a random variable. If more than one random variable is under consideration, one may subscript $\mu$ with the name of that random variable; that is, $\mu_X$ is the expected value of $X$.

In some disciplines, the notation $\langle X \rangle$ is used to denote the expected value of $X$.

$^1$More formally and abstractly, a probability space is a triple $(\Omega, \mathcal{F}, P)$ where $\Omega$ is a set, $\mathcal{F}$ is a $\sigma$-algebra of events, and $P$ is the probability function. In case $\Omega$ is finite or countably infinite, the probability space is called discrete and $\mathcal{F}$ can be ignored (as it can be taken to be $2^{\Omega}$).


- Conditional expectation.  $E(X \mid Y)$  denotes the conditional expected value of  $X$  given  $Y$ . This is also written  $\mu_{X|Y}$ .
- Variance. For a random variable  $X$ ,  $\operatorname{Var}(X)$  denotes the variance of  $X$  defined by  $\operatorname{Var}(X) = E\left[(X - \mu)^2\right] = E(X^2) - E(X)^2$ . Often  $\sigma^2$  denotes the variance. This may be subscripted with the name of the random variable:  $\sigma_X^2$ .

The square root of the variance is known as the standard deviation and is denoted  $\sigma$ .

- Covariance. Given two random variables  $X$  and  $Y$ , their covariance is  $\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y)$ .

If  $\mathbf{X}$  is a random vector, i.e.,

$$
\mathbf {X} = \left[ \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right]
$$

then the covariance matrix of  $\mathbf{X}$  is often denoted  $\Sigma$ . This is an  $n \times n$ -matrix whose  $i, j$ -entry is  $\operatorname{Cov}(X_i, X_j)$ .

- Correlation coefficient. Given two random variables  $X$  and  $Y$ , their correlation coefficient is

$$
\operatorname {C o r r} (X, Y) = \frac {\operatorname {C o v} (X , Y)}{\sigma_ {X} \sigma_ {Y}}.
$$

- Entropy. The entropy of a random variable  $X$  is denoted  $H(X)$ . For discrete random variables,

$$
H (X) = - \sum_ {x} P (X = x) \log P (X = x)
$$

where the sum is over all values  $x$  that  $X$  may take (and with the convention  $0\log 0 = 0$ ). For a continuous random variable,

$$
H (X) = - \int_ {- \infty} ^ {\infty} f (x) \log f (x) d x
$$

where  $f(x)$  is the PDF (see the entry on the facing page) of  $X$ . In both cases, the base of the logarithm depends on the application (with the most popular choices being 2,  $e$ , and 10).

Extensions of this notation include the joint entropy  $H(X,Y)$  and the conditional entropy  $H(X\mid Y)$  of the two random variables  $X$  and  $Y$ .

Distributions. Random variables are often best described by their distribution. Distributions, in turn, can be described in one of three principal ways, each with its own acronym.


- PMF: Discrete random variables can be specified by their *probability mass function*, or PMF, which specifies the probability associated with each possible value of the random variable: $F(x)=P(X=x)$.
- CDF: Real-valued, continuous random variables can be specified by their *cumulative distribution function*, or CDF: $F(x)=P(X\leq x)$. Most authors denoted cumulative distribution functions with uppercase letters.

The inverse function of the CDF is the *quantile function* which is often denoted $Q$.
- PDF: Real-valued, continuous random variables can also be specified by their *probability density function* $f(x)$. The relation to the cumulative distribution function $F(x)$ is $f(x)=F^{\prime}(x)$ which gives

$P(X\in[a,b])=\int_{a}^{b}f(x)\,dx.$

Most authors use lower case letters that correspond to the upper case letter for the random variable’s CDF.

We write $X\sim\mathcal{D}$ if the random variable $X$ has distribution $\mathcal{D}$. For example, if $X$ is a (standard) normal random variable, we write $X\sim N(0,1)$. (See the discussion of the normal distribution on the next page.)

A collection of random variables with the same distribution are called *identically distributed*. In particular, if a collection of random variables are (mutually) independent and identically distributed, we write that they are iid (or IID).

There are many standard distributions of random variables that have been studied by mathematicians and arise in a host of applications. The following are among the best-known and each have their own notation.

- Binomial. Let $n$ be a nonnegative integer and $0\leq p\leq 1$. A discrete random variable $X$ has the *binomial distribution* $\operatorname{Bin}(n,p)$ or $B(n,p)$ if its probability mass function is

$P(X=k)={n\choose k}p^{k}(1-p)^{n-k}$

where $k\in\{0,1,\ldots,n\}$.
- Poisson. Let $\lambda$ be a positive real number. A discrete random variable $X$ has *Poisson distribution* $\operatorname{Pois}(\lambda)$ provided

$P(X=k)=\frac{\lambda^{k}}{k!}e^{-\lambda}.$

where $k$ is a nonnegative integer.

The use of $\lambda$ for the parameter (and hence the mean) of the Poisson distribution is quite common.

2Discrete random variables take values in a finite or countably infinite set. Continuous random variables generally yield values in all of
\mathbb{R}
or an interval in
\mathbb{R}


- Exponential distribution. For a positive real number $\alpha$, the exponential distribution is denoted $\operatorname{Exp}(\alpha)$. The CDF for a random variable with this distribution is $F(t) = 1 - \exp\{-\alpha t\}$ (where $t \geq 0$).
- Normal/Gaussian. A standard normal or Gaussian random variable $X$ has a probability density function typically denoted $\phi(x)$ where

$$
\phi(x) = \frac{1}{\sqrt{2\pi}} \exp\left\{-x^2\right\}.
$$

The corresponding CDF is often denoted $\Phi(x)$ which is closely related to the error function $\operatorname{erf}(x)$ (see page 28).

More generally, if $\mu$ is a real number and $\sigma^2$ is a positive real number, then $N(\mu, \sigma^2)$, or sometimes $\mathcal{N}(\mu, \sigma^2)$, is the distribution of a normal random variable $X$ with mean $\mu$ and variance $\sigma^2$. Its probability density function is

$$
\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{-\frac{(x - \mu)^2}{2\sigma^2}\right\}.
$$

Thus a standard normal random variable has $X \sim N(0,1)$.

The multivariable normal random variable $N_k(\vec{\mu}, \Sigma)$ is a random $k$-vector with mean $\vec{\mu}$ and covariance matrix $\Sigma$.

- Chi-squared. The chi-squared distribution is denoted $\chi^2$; more specifically, the chi-square distribution with $k$-degrees of freedom is denoted $\chi_k^2$. If $X_1, X_2, \ldots, X_k$ are IID standard normal random variables, then the sum of their squares $X = X_1^2 + \dots + X_k^2$ is chi-squared distributed $\chi_k^2$. Its probability density function is given by

$$
\frac{1}{2^{k/2} \Gamma(k/2)} x^{\frac{k}{2} - 1} e^{-x/2}
$$

where $\Gamma$ is the gamma function described on page 28.

- Student's $t$-distribution. This distribution is denoted $t_{\nu}$ where $\nu$ is a positive integer. It is given by $Z / \sqrt{V / \nu}$ where $Z$ and $V$ are independent random variables, $Z$ is a standard normal, and $V$ is $\chi_{\nu}^2$.
- $F$-distribution. Also known as the Fisher-Snedecor distribution, this is written $F(\nu_1, \nu_2)$ where the $\nu_i$ are positive integers. It is given by

$$
\frac{X_1 / \nu_1}{X_2 / \nu_2}
$$

where $X_1, X_2$ are independent $\chi^2$-random variables with $\nu_1, \nu_2$ degrees of freedom, respectively.

Convergence of random variables. Let $X$ and $X_1, X_2, \ldots$ be random variables. There are various notions of the sequence $X_i$ converging to $X$, each with its own notation.


- Convergence in distribution (in law). This is denoted in various ways including these:

$$
X _ {n} \xrightarrow {d} X
$$

$$
X _ {n} \xrightarrow {\mathcal {D}} X
$$

$$
X _ {n} \xrightarrow {\mathcal {L}} X
$$

$$
\mathcal {L} (X _ {n}) \longrightarrow \mathcal {L} (X)
$$

- Convergence in probability. This is denoted

$$
X _ {n} \xrightarrow {p} X \qquad \text {or} \qquad X _ {n} \xrightarrow {p} X.
$$

- Almost sure convergence. This is denoted

$$
X _ {n} \xrightarrow {\mathrm {a . s .}} X.
$$

-  $L^2$  convergence. This is denoted

$$
X _ {n} \xrightarrow {L ^ {2}} X.
$$

Some authors place the notation as a subscript to the arrow rather than above, like this:  $X_{n}\to_{d}X$

## 2. Statistics

The following is a potpourri of notation one encounters in statistics.

Given numerical data  $X_{1},X_{2},\ldots ,X_{n}$  we have the following notations:

- Average. The (sample) average is denoted  $\bar{X}$ :

$$
\bar {X} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k}.
$$

- Median. The (sample) median is denoted  $\bar{X}$  or  $\bar{X}$ .
- Standard Deviation. The (sample) standard deviation is denoted  $s$ :

$$
s = \sqrt {\frac {\sum (X _ {i} - \bar {X}) ^ {2}}{n - 1}}.
$$

-  $z$ -score. A common way to standardize data is express it as the number of standard deviations above (or below) the mean. For this one uses the  $z$ -score:

$$
Z _ {i} = \frac {X _ {i} - \mu}{\sigma}
$$

where  $\mu$  is the population mean and  $\sigma$  is the population standard deviation.

- Order statistics. The notation  $X_{(1)}, X_{(2)}, \ldots, X_{(n)}$  represents the same values but in nondecreasing order. That is  $X_{(1)}$  is the smallest  $X_i$ ,  $X_{(n)}$  is the largest, and in general

$$
X _ {(1)} \leq X _ {(2)} \leq \dots \leq X _ {(n)}.
$$


In hypothesis testing, the null hypothesis is typically denoted $H_0$ and the alternative hypothesis by $H_A$ or $H_1$. Incorrectly rejecting $H_0$ when, in fact, it is true is known as a type I error and the probability of committing such a mistake is typically denoted by $\alpha$. Accepting the null hypothesis when, in fact, it is false is known as a type II error and the probability of making this mistake is typically denoted $\beta$.

In statistical models, error (or noise) terms are often denoted with the letter $e$ or $\epsilon$; these can be subscripted if there are multiple error terms.

Often one is trying to determine some numerical quantity for a population (e.g., the proportion of a population that watch a certain television show) and this is done by computing an estimate from a random sample. It is conventional to place a hat on the estimator of the true parameter; that is, if $\theta$ is the parameter whose value we seek, then $\hat{\theta}$ is the estimator of $\theta$.
