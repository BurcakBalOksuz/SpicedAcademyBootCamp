# Loss Function of Logistic Regression
21/01/2022

* Linear Function (01)
    * Independent variable: x (consumption)
    * Dependent variable: y (cost)
    * Constants: m, b (price, basecost)
    $$\text{cost}[Euros] = \text{consumption} [kWh] \times \text{price} [kWh/Euros] + \text{basecost} [Euros]$$ 
    $$y = m\times x + b$$
    $$f(x) = y = f(x;m,b)$$
    $$f(X;\theta) = \theta_0 \times X_0 + \theta_1 \times X_1 + \ldots + \theta_i\times X_i$$

* Modelling steps (02)
    * Create model (e.g. linear function)
    * Define obj. function (loss function (e.g. MSE))
    * Optimize (e.g. gradient descent)
* Parameter space (Parameterspace.png)
    * Dimension: number of parameters + 1 
    * global vs. local minima
    * Best case: monotonic, continuous, differentiable
    * Goal: find set of parameter values for which the loss function is minimal

* Logistic Regression (03)
    * Non-linear, gives probabilities
    * Can be transformed into a linear function in log(odds)
    * odds vs. probability (Advantage of odds?)
    * Advantages of logarithmic function
    * MSE is not a reasonable loss function (not convex, only small range, many local minima)

* Coin flip (Bernoulli experiment) (04)
    * Use of exponents to get probability for Head (1) or Tails (0) 
    * Turn piece-wise function into one function
$$P(y) = \hat{p}^{y}\times(1-\hat{p})^{(1-y)}$$ 

* Bernoulli Trials (Binomial Dist) 
    * What is the probability of the sequence [H,H,H,T]?
    * What is the most probable value of $\hat{p}$ for this sequence? $\Rightarrow$ Maximum likelihood or better maximum log likelihood

* likelihood function, log likelihood, log loss: 
$$ L(y,\hat{p}) = \binom{n}{k} \Pi_{i=1}^n\ \hat{p}(X_i)^{y_i} \times (1-\hat{p}(X_i))^{(1-y_i)}$$
$$l(y,\hat{p}) = \log(\binom{n}{k})+ \sum_{i=1}^n y_i \times \log(\hat{p}(X_i)) + (1-y_i)\times\log(1-\hat{p}(X_i))$$
$$L(y,\hat{p}) = -\frac{1}{n}\bigl(\sum_{i=1}^n y_i \times \log(p(X_i)) + (1-y_i)\times\log(1-p(X_i))\bigr)$$

Additional info:
* https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a
* Video on LogisticRegression: https://www.youtube.com/watch?v=vN5cNN2-HWE&t=433s

