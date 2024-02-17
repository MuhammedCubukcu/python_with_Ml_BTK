## K-En Yakın Komşu (KNN) Algoritması

K-En Yakın Komşu (KNN), sınıflandırma ve regresyon problemlerini çözmek için kullanılan basit bir makine öğrenimi algoritmasıdır. Temel prensibi, bir veri noktasının sınıfını veya değerini tahmin etmek için bu veri noktasına en yakın olan k adet veri noktasının etiketlerini kullanmaktır.

### Kullanım Alanları:

- **Sınıflandırma Problemleri:** Örneğin, bir kullanıcının bir belirli ürünü satın alıp almama olasılığını tahmin etmek gibi. Bu durumda, KNN algoritması, benzer özelliklere sahip diğer kullanıcıların satın alma alışkanlıklarını dikkate alarak tahminde bulunabilir.

- **Regresyon Problemleri:** Örneğin, bir evin fiyatını tahmin etmek gibi. Bu durumda, KNN algoritması, benzer özelliklere sahip diğer evlerin fiyatlarını dikkate alarak tahminde bulunabilir.

### Nasıl Çalışır?

1. **Eğitim Aşaması:** KNN algoritması eğitim aşamasında sadece veri setini belleğe yükler. Başka bir işlem yapmaz, verileri önceden işleme koymaz veya değiştirmez.

2. **Tahmin Aşaması:** Bir veri noktasının sınıfını veya değerini tahmin etmek istediğinizde, KNN algoritması bu veri noktasına en yakın olan k adet veri noktasını bulur. Bu "yakınlık" genellikle öklid mesafesi veya başka bir mesafe metriği kullanılarak ölçülür.

3. **Sınıflandırma Problemleri İçin:** En yakın k veri noktasının sınıflarını gözlemleyin ve bu sınıfların çoğunluğunu tahmin olarak kullanın. Yani, en çok görülen sınıfı tahmin edilen sınıf olarak atayın.

4. **Regresyon Problemleri İçin:** En yakın k veri noktasının değerlerinin ortalamasını hesaplayın ve bu ortalamayı tahmin olarak kullanın.

### Avantajları ve Dezavantajları:

- **Avantajlar:**
  - Basit ve anlaşılması kolaydır.
  - Model eğitimi maliyeti düşüktür, çünkü eğitim aşamasında gerçekten bir şey yapmaz, sadece verileri belleğe yükler.
  - Esnek ve genişletilebilir, sınıflandırma ve regresyon problemlerine uyarlanabilir.
  
- **Dezavantajlar:**
  - Tahmin yapmak için genellikle tüm veri setini bellekte saklamak gerekir, bu da bellek ve hesaplama maliyetini artırabilir.
  - Büyük veri setleri için hesaplama maliyeti yüksek olabilir, çünkü her tahminde tüm veri setinin uzaklıklarını hesaplamak gerekir.

### Öklid Mesafesi Formülü

Öklid mesafesi, iki nokta arasındaki doğru mesafeyi ölçer. Öklid mesafesi formülü şu şekildedir:

\[ d(x, y) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2} \]

Bu formül, iki nokta arasındaki uzaklığı hesaplamak için kullanılır. Burada, \( x \) ve \( y \) vektörleri, her biri bir veri noktasını temsil eden özellik değerlerini içerir. \( n \), özelliklerin sayısını temsil eder. \( x_i \) ve \( y_i \) ise karşılaştırılan iki veri noktasının ilgili özelliklerinin değerleridir.
