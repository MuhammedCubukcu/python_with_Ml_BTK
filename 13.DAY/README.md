## Naive Bayes Sınıflandırma Algoritması

Naive Bayes sınıflandırma algoritması, olasılık teorisine dayalı bir makine öğrenimi algoritmasıdır. Özellikle, metin sınıflandırma gibi problemlerde yaygın olarak kullanılır. Bu algoritma, özellikler arasında bağımsızlık varsayımını yapar, yani her özellik diğerleriyle bağımsız olarak kabul edilir. Bu varsayım, algoritmanın hesaplamalarını basitleştirir ve veri setindeki özellikler arasındaki ilişkileri azaltır.

### Nasıl Çalışır?

1. **Eğitim Aşaması:**
   - Naive Bayes algoritması, eğitim veri setindeki özelliklerin sınıf etiketleri ile ilişkisini öğrenir. Bu, her bir sınıf için özelliklerin olasılık dağılımlarını hesaplamayı içerir. Örneğin, bir belgedeki belirli bir kelimenin belirli bir sınıf ile ilişkili olma olasılığını hesaplayabilir.

2. **Tahmin Aşaması:**
   - Bir örneğin sınıfını tahmin etmek için, Naive Bayes algoritması, verilen özelliklerin sınıflar için olasılıklarını hesaplar ve en yüksek olasılığa sahip sınıfı tahmin olarak seçer. Bu genellikle Bayes teoremi kullanılarak yapılır.

### Naive Bayes Türleri:

1. **Gaussian Naive Bayes:**
   - Sürekli özelliklerle çalışır ve özellik dağılımlarını normal (Gaussian) olarak kabul eder.

2. **Multinomial Naive Bayes:**
   - Metin sınıflandırma gibi çoklu kategorik özelliklerle çalışır. Genellikle kelime sayıları veya TF-IDF skorları gibi belge temelli özelliklerle kullanılır.

3. **Bernoulli Naive Bayes:**
   - Multinomial Naive Bayes'in bir türevidir, ancak özelliklerin varlığı veya yokluğu ile çalışır. Özellikler, bir belgedeki bir kelimenin varlığı veya yokluğu gibi ikili değerler olabilir.

### Avantajları:

- Basitlik ve hız: Naive Bayes algoritması, hesaplama açısından hızlı ve basit bir algoritmadır.
- İyi performans: Metin sınıflandırma gibi bazı problemlerde iyi performans gösterir.
- Küçük eğitim veri setleriyle bile etkilidir.

### Dezavantajları:

- Bağımsızlık varsayımı: Özellikler arasında gerçekte bağımlılık varsa, bu varsayım doğru sonuçlar üretmeyebilir.
- Sıfır frekansı: Eğitim veri setinde gözlenmeyen bir özellik için olasılık hesaplanamaz, bu da sıfır frekansı problemine yol açabilir.

Naive Bayes, özellikle metin sınıflandırma gibi basit ve hızlı bir sınıflandırma yöntemi arayan durumlarda kullanışlıdır.
