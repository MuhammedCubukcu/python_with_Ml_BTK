## Destek Vektör Makinesi (SVM) Sınıflandırma

Destek Vektör Makinesi (SVM), sınıflandırma ve regresyon problemlerini çözmek için kullanılan güçlü bir makine öğrenimi algoritmasıdır. İşte SVM'nin sınıflandırma için adım adım nasıl çalıştığının detaylı açıklaması:

1. **Lineer Ayrılabilir Durum:**
   - Öncelikle, eğer veri setiniz lineer olarak ayrılabilirse (yani, sınıflar arasında bir doğru veya düzlemle ayrılabilirse), SVM, bu sınıfları ayıran en iyi karar sınırını (hiper düzlemi) bulmaya çalışır. Bu hiper düzlem, veri setinin boyutuna bağlı olarak bir doğru, düzlem veya hiper düzlem olabilir.

2. **Optimal Karar Sınırını Belirleme:**
   - SVM, sınıflar arasındaki marjı maksimize etmeyi amaçlar. Marj, sınıflar arasındaki en yakın veri noktaları (destek vektörler) arasındaki mesafeyi ifade eder. SVM, bu marjı maksimize eden ve doğru sınıflandırma yapabilen bir karar sınırı bulmaya çalışır.

3. **Karar Sınırını Belirleme Süreci:**
   - SVM'nin bu optimal karar sınırını bulmak için çeşitli optimizasyon teknikleri vardır. Genellikle, doğrusal programlama veya çözümleme teknikleri kullanılır.

4. **Kernel Hükerleri:**
   - SVM, doğrusal olarak ayrılamayan veri setlerini işlemek için kernel hükerlerini kullanabilir. Kernel hükerleri, veri setinin yüksek boyutlu uzayda dönüştürülmesini sağlar ve lineer olarak ayrılabilir hale getirir. Bunlar, polinom, RBF (radial basis function), sigmoid vb. olabilir.

5. **Sınıflandırma:**
   - Eğitim aşamasının tamamlanmasının ardından, SVM, yeni veri noktalarını sınıflandırmak için karar sınırını kullanır. Veri noktası hangi tarafında kalıyorsa, ilgili sınıfa atanır.

### Avantajları ve Dezavantajları:

- **Avantajlar:**
  - Yüksek boyutlu veri setleriyle iyi çalışır.
  - Kernel hükerleri sayesinde doğrusal olarak ayrılamayan veri setlerini işleyebilir.
  - Overfitting'e karşı dirençlidir.
  
- **Dezavantajlar:**
  - Hiper parametrelerin (C ve kernel parametreleri gibi) ayarlanması gerekebilir.
  - Büyük veri setleriyle çalışırken hesaplama maliyeti yüksek olabilir.
  - Karar sınırının yorumlanması bazen zor olabilir.

SVM, geniş bir uygulama yelpazesine sahiptir ve özellikle sınıflandırma problemleri için güçlü bir araçtır.


## Kernel Fonksiyonları

Kernel fonksiyonları, destek vektör makinesi (SVM) gibi bazı makine öğrenimi algoritmalarında kullanılan önemli bir bileşendir. Kernel fonksiyonları, veri setinin boyutunu artırmadan doğrusal olarak ayrılamayan veri setlerini işlemek için kullanılır. Özellikle, SVM'nin doğrusal olmayan veri setlerini işlemesine ve çeşitli sınıflandırma problemlerini çözmesine yardımcı olurlar.

### Temel İdea

- **Doğrusal Olmayan Ayrılabilirlik:**
  - Doğrusal olarak ayrılamayan veri setleri, tek bir düzlem veya doğru ile ayrılamazlar. Bu tür veri setleri için, SVM'nin doğrusal karar sınırlarını bulması zordur.

- **Yüksek Boyutlu Uzay:**
  - Kernel fonksiyonları, veri setini yüksek boyutlu bir uzaya dönüştürerek, doğrusal olarak ayrılabilir hale getirir. Bu, veri setinin daha karmaşık yapılarını yakalamak için daha fazla boyuta genişletilmesini sağlar.

- **Dönüşümün Maliyeti:**
  - Kernel fonksiyonları, veri setinin boyutunu artırmadan bu yüksek boyutlu uzayı hesaplamak için kullanılır. Bu, hesaplama maliyetini minimize eder ve zaman ve bellek açısından verimli bir çözüm sunar.

### Popüler Kernel Fonksiyonları

1. **Polinomiyal Kernel:**
   - Veriyi yüksek boyutlu bir uzaya dönüştürmek için polinomiyal fonksiyonları kullanır. Formülü şu şekildedir:
     \[ K(x, y) = (x^Ty + c)^d \]
   - Burada \( c \) bir sabittir ve \( d \) polinom derecesidir.

2. **RBF (Radial Basis Function) Kernel:**
   - RBF, veriyi sonsuz boyutlu bir uzaya dönüştürmek için kullanılan popüler bir kernel fonksiyonudur. Formülü şu şekildedir:
     \[ K(x, y) = \exp \left( -\frac{\|x - y\|^2}{2\sigma^2} \right) \]
   - Burada \( \sigma \) bir parametredir ve RBF fonksiyonunun genişliğini kontrol eder.

3. **Sigmoid Kernel:**
   - Sigmoid fonksiyonu, veriyi yüksek boyutlu bir uzaya dönüştürmek için kullanılan bir başka kernel fonksiyonudur. Formülü şu şekildedir:
     \[ K(x, y) = \tanh(\alpha x^Ty + c) \]
   - Burada \( \alpha \) ve \( c \) sabitlerdir.

### Kernel Fonksiyonlarının Seçimi

- Kernel fonksiyonunun seçimi, veri setinin yapısına ve sınıflandırma problemine bağlıdır.
- Deneme yanılma yöntemiyle farklı kernel fonksiyonları denenebilir ve en iyi sonuç veren seçilebilir.
- Kernel fonksiyonu seçiminde ayrıca, kernel parametrelerinin (örneğin, \( \sigma \) veya \( d \)) ayarlanması da önemlidir.
