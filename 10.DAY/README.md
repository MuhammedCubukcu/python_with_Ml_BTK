# Sınıflandırma Nedir?

Sınıflandırma, makine öğrenimi (machine learning) alanında yaygın olarak kullanılan bir tekniktir. Sınıflandırma, veri setlerindeki örneklerin belirli bir kategoriye veya sınıfa atanması veya etiketlenmesi işlemidir. Bu, genellikle mevcut veri özelliklerine dayanarak yapılır.

Örneğin, bir e-posta mesajını spam veya spam olmayan olarak sınıflandırmak, bir hasta için bir tıbbi teşhis koymak veya bir görüntüdeki nesneleri tanımlamak gibi uygulamalarda sınıflandırma kullanılabilir.

Sınıflandırma genellikle denetimli öğrenme (supervised learning) kategorisine girer. Denetimli öğrenme, etiketlenmiş verilerle eğitilir, yani her veri örneği için doğru çıktılar sağlanır. Sınıflandırma algoritmaları, bu etiketlenmiş verileri kullanarak verileri öğrenir ve daha sonra yeni gelen verileri belirli sınıflara tahmin etmek için kullanılır.

Sınıflandırma algoritmalarının bazı örnekleri şunlardır:
1. Naive Bayes
2. Karar Ağaçları (Decision Trees)
3. Destek Vektör Makineleri (Support Vector Machines)
4. K-En Yakın Komşu (K-Nearest Neighbors)
5. Lojistik Regresyon (Logistic Regression)
6. Derin Öğrenme (Deep Learning) Modelleri, örneğin Yapay Sinir Ağları (Artificial Neural Networks)

Bu algoritmalar farklı veri türlerine ve problem alanlarına göre uygun olabilir. Örneğin, görüntü tanıma problemlerinde derin öğrenme modelleri genellikle en iyi sonuçları verirken, daha basit sınıflandırma problemlerinde Naive Bayes gibi daha temel algoritmalar da kullanılabilir.


# Logistic Regression

Logistic regression, makine öğrenimi ve istatistik alanlarında sınıflandırma problemlerini çözmek için kullanılan bir denetimli öğrenme algoritmasıdır. Adına rağmen, logistic regression bir regresyon tekniği değil, sınıflandırma algoritmasıdır. İki veya daha fazla sınıf arasında ayrım yapmak için kullanılır.

## Nasıl Çalışır?

Logistic regression, giriş verileri ve bu verilere karşılık gelen sınıf etiketleri arasındaki ilişkiyi modellemeye çalışır. Ancak, çıktı bir sayı değil, bir olasılık değeri veya belirli bir sınıfa ait olma olasılığını temsil eder. 

Logistic regression, giriş verileriyle bir ağırlık vektörü ve bir bias terimi arasındaki lineer bir ilişkiyi öğrenir. Ancak, bu lineer kombinasyonu direkt olarak sınıflandırma yapmak için kullanmak mümkün değildir çünkü bu değerler doğal olarak 0 ile 1 arasında değil ve sınıflandırma problemi için uygun değildir.

Bu nedenle, logistic regression, lineer kombinasyon sonucunu 0 ile 1 arasında değerler veren bir aktivasyon fonksiyonu ile sıkıştırır. Genellikle kullanılan aktivasyon fonksiyonu, sigmoid fonksiyonu olarak adlandırılan, S şekilli bir eğri olan fonksiyondur. Sigmoid fonksiyonu, herhangi bir giriş değerini 0 ile 1 arasında bir çıktıya dönüştürür, bu da sonucun bir olasılık değeri olarak yorumlanmasını sağlar.

## Eğitim ve Tahmin

Logistic regression modeli, veri setindeki örneklerin giriş özelliklerini ve bu özelliklere karşılık gelen sınıf etiketlerini kullanarak eğitilir. Eğitim sürecinde, modelin parametreleri (ağırlık vektörü ve bias terimi) veri setine uyarlanır.

Eğitim tamamlandıktan sonra, model yeni veri noktaları için sınıflandırma tahminleri yapabilir. Model, giriş verilerini alır, bu verileri öğrenilmiş parametrelerle kullanarak bir tahmin olasılığı üretir ve belirlenen bir kesme eşiği üzerinden bu olasılığı bir sınıfa atar.

## Avantajları ve Dezavantajları

**Avantajları:**
- Basit ve yüksek performanslı bir sınıflandırma algoritmasıdır.
- Eğitimi hızlıdır ve genellikle büyük veri kümeleriyle iyi çalışır.
- Sonuçlar yorumlanabilir, modelin hangi özelliklerin sınıflandırmada etkili olduğunu görmek kolaydır.

**Dezavantajları:**
- Lineer bir modeldir, bu nedenle daha karmaşık ilişkileri modellemekte sınırlıdır.
- Çoklu sınıf problemleri için doğrudan uygulanamaz, genellikle one-vs-all veya one-vs-one stratejileriyle genişletilir.

Logistic regression, özellikle iki sınıflı (binary) sınıflandırma problemlerinde yaygın olarak kullanılır ve genellikle temel bir başlangıç noktası olarak tercih edilir.

# Logistic regression'ın matematiksel formülü şu şekildedir:

h_θ(x) = σ(θ^T x)

Burada:
- h_θ(x) modelin tahmin ettiği çıktıdır.
- θ modelin parametrelerini (ağırlık vektörü) temsil eder.
- x giriş özelliklerini temsil eder.
- θ^T parametrelerin transpozu alınmış halidir.
- σ(z) sigmoid (logistic) fonksiyonudur ve şu şekildedir: 

σ(z) = 1 / (1 + e^-z)

Bu formül, lineer kombinasyon θ^T x elde edilir ve daha sonra sigmoid fonksiyonuna sokularak 0 ile 1 arasında bir olasılık değeri elde edilir. Bu olasılık, giriş özelliklerinin verilen sınıfa ait olma olasılığını temsil eder. Eğitim sürecinde, modelin parametreleri (θ) veri setine uyarlanır ve optimum değerlerini bulmak için bir optimizasyon algoritması kullanılır. Bu optimizasyon genellikle maksimum olabilirlik tahminini (maximum likelihood estimation) veya gradyan inişi (gradient descent) gibi teknikleri içerir.







