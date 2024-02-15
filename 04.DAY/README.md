#  Polinomal Regresyon

**Tanım:**
Polinom regresyonu, bir bağımlı değişken ile bir veya daha fazla bağımsız değişken arasındaki ilişkiyi ifade etmek için polinom denklemlerini kullanır. Bu denklemler, veri noktaları arasındaki karmaşık ilişkileri temsil etmek için kullanılır.

**Amaç:**
Polinom regresyonunun temel amacı, veri noktaları arasındaki ilişkiyi daha doğru bir şekilde modellemektir. Doğrusal regresyonun yetersiz kaldığı durumlarda, polinom regresyonu daha uygun bir seçenek olabilir.

**Polinom Derecesi:**
Polinom regresyonunda, polinom derecesi önemlidir. Polinom derecesi, polinomun içerdiği en yüksek dereceli terim sayısını belirtir. Örneğin, ikinci dereceden bir polinom, birinci dereceden (doğrusal) terimlerin yanı sıra kare terimlerini de içerir.

## Polinom Regresyonu Modeli:

**Polinom Regresyonu Denklemi:**
Polinom regresyonu denklemi genellikle aşağıdaki gibi ifade edilir:

* Y = β₀ + β₁X + β₂X² + ... + βₙXⁿ + ε


Burada:
- `Y` bağımlı değişkeni temsil eder.
- `X` bağımsız değişkeni temsil eder.
- `β₀, β₁, ..., βₙ` polinomun katsayılarını temsil eder.
- `ε` hata terimini temsil eder.

**Polinom Katsayılarının Tahmini:**
Polinom regresyonunda, katsayılar genellikle en küçük kareler yöntemiyle tahmin edilir. Bu yöntem, gerçek veri noktaları ile polinom arasındaki hata karelerinin toplamını minimize eder.

**En Küçük Kareler Yöntemi ve Polinom Regresyonu:**
En küçük kareler yöntemi, polinom regresyonunda çok yaygın olarak kullanılan bir optimizasyon tekniğidir. Bu yöntem, polinom katsayılarını bulmak için veri noktalarına en iyi uyan polinomu bulur.

**En Küçük Kareler Yöntemi:**

**Tanım:**
En küçük kareler yöntemi, veri noktaları arasındaki ilişkiyi anlamak ve tahmin etmek için kullanılan bir istatistiksel yöntemdir. Özellikle, bağımlı bir değişkenin bir veya daha fazla bağımsız değişkenle olan ilişkisini belirlemek amacıyla kullanılır.

**Amaç:**
En küçük kareler yöntemi, veri noktaları ile bir doğrusal model arasındaki farkın karelerinin toplamını (hata karelerinin toplamını) minimize ederek, bu modelin parametrelerini tahmin etmeyi amaçlar.

**Formül:**
Bir doğrusal model genellikle şu şekilde ifade edilir:

* y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

En küçük kareler yöntemi, bu modelin tahmin edilen değerleri ile gerçek veri noktaları arasındaki hata karelerinin toplamını minimize etmek için kullanılır. Matematiksel olarak, bu formul ile ifade edilir:

* min_{β₀, β₁, ..., βₙ} Σ_{i=1}^{N} (yᵢ - (β₀ + β₁x_{i1} + β₂x_{i2} + ... + βₙx_{in}))²

Bu formüldeki `Σ_{i=1}^{N}` ifadesi, veri setindeki tüm noktaların üzerinde toplandığını belirtir.

**Çözüm:**
En küçük kareler yöntemi genellikle normal denklemler kullanılarak çözülür. Bu, matris cebiri kullanılarak gerçekleştirilir ve en iyi tahmin edilmiş parametrelerin hesaplanmasını sağlar.

**Gradient İnişi:**

**Tanım:**
Gradient inişi, bir fonksiyonun minimumunu bulmak için kullanılan bir optimizasyon algoritmasıdır. Bu yöntem, bir fonksiyonun negatif gradyan yönünde adım adım ilerleyerek minimuma yaklaşır.

**Amaç:**
Gradient inişinin amacı, optimize edilmek istenen bir fonksiyonun (genellikle hata fonksiyonu) minimumunu bulmaktır. Bu, model parametrelerini güncellemek için kullanılır.

**Formül:**
Gradient inişi formülü şu şekildedir:


* θ = θ - α∇J(θ)

Bu formülde:

- `θ` güncellenen parametre vektörünü temsil eder.
- `α` adım boyutunu (öğrenme oranını) ifade eder.
- `J(θ)` optimize edilmek istenen fonksiyonu (genellikle bir hata fonksiyonu) temsil eder.
- `∇J(θ)` fonksiyonunun `θ` noktasındaki gradyanını ifade eder.

**Uygulama:**
Gradient inişi, özellikle büyük veri kümeleriyle çalışırken ve analitik çözümler mümkün olmadığında, veriye dayalı makine öğrenimi algoritmalarında sıklıkla kullanılır. Model parametrelerini optimize etmek ve hata fonksiyonunu minimuma indirmek için kullanılır.



