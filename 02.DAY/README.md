# Tahmin (Prediction) ve Öngörü (Forecasting)

**Tahmin (Prediction):**
- Tahmin, genellikle veriye dayalı gelecekteki bir olayın veya değerin tahmin edilmesi anlamına gelir.
- Genellikle sınıflandırma veya regresyon problemleri olarak tanımlanır. Sınıflandırma, kategorik bir hedef değişkeni tahmin etmeye odaklanırken, regresyon, sürekli bir hedef değişkeni tahmin etmeye odaklanır.
- Örneğin, bir evin fiyatını tahmin etmek (regresyon) veya bir e-postanın spam olup olmadığını tahmin etmek (sınıflandırma) gibi problemler bir tahmin problemi olarak kabul edilebilir.

**Öngörü (Forecasting):**
- Öngörü, genellikle zaman serisi verileri üzerinde gerçekleştirilen bir işlemdir ve gelecekteki bir olayın veya değerin tahmin edilmesini içerir.
- Geçmiş verilere dayalı olarak gelecekteki bir trendi, deseni veya modeli belirlemeye çalışır.
- Öngörü, tahminlemenin bir alt kümesidir ve genellikle belirli bir zaman aralığı boyunca (genellikle gelecek zamanlar) değerlerin tahmin edilmesini hedefler.
- Örneğin, bir şirketin gelecek ayki satışlarını tahmin etmek veya bir hisse senedinin gelecekteki fiyatını tahmin etmek gibi problemler bir öngörü problemi olarak kabul edilebilir.

Makine öğrenimi kullanılarak tahmin ve öngörü yapılabilir. Regresyon ve zaman serisi analizi gibi çeşitli makine öğrenimi teknikleri bu tür problemleri çözmek için kullanılabilir. Örneğin, doğrusal regresyon, destek vektör makineleri, karar ağaçları, rastgele ormanlar gibi algoritmalar tahmin problemlerini çözmek için kullanılabilirken, zaman serisi analizi için ARIMA (Oto Regresif Entegre Hareketli Ortalama), LSTM (Uzun Kısa Vadeli Bellek Ağları) gibi özel algoritmalar kullanılabilir.


### Basit Doğrusal Regresyon (Simple Linear Regression)

Basit doğrusal regresyon, bir bağımsız değişkenin (X) bir bağımlı değişkene (y) olan etkisini inceleyen ve bu ilişkiyi bir doğru ile modelleyen bir regresyon tekniğidir.

Temel olarak, basit doğrusal regresyon, bir X değeri verildiğinde, bu X değerine karşılık gelen bir y değerini tahmin etmeye çalışır. Bu tahmin, X ve y arasındaki ilişkiyi ifade eden bir doğru denklemi kullanılarak yapılır. 


* y = b0 + b1 * X

Burada:
- `y`: Bağımlı değişkenin tahmini değeri.
- `b0`: Kesme terimi (intercept), doğrunun y eksenini kestiği noktanın değerini temsil eder.
- `b1`: Eğim katsayısı (slope), doğrunun eğimini ve X değişkeninin y değişkenine olan etkisini temsil eder.
- `X`: Bağımsız değişkenin değeri.

Doğrusal regresyon modeli, veri seti üzerinde en uygun `b0` (kesme terimi) ve `b1` (eğim katsayısı) değerlerini bulmaya çalışır. Bu işlem, genellikle en küçük kareler yöntemi gibi istatistiksel teknikler kullanılarak yapılır.

Python'da, `scikit-learn` kütüphanesi kullanılarak basit doğrusal regresyon modelleri oluşturulabilir. Örneğin:

```python
from sklearn.linear_model import LinearRegression

# Modeli oluştur
model = LinearRegression()

# Modeli eğit
model.fit(X_train, y_train)

# Modelden tahmin yap
y_pred = model.predict(X_test)

```
Bu kod, LinearRegression sınıfını kullanarak bir doğrusal regresyon modeli oluşturur, bu modeli eğitir ve ardından test veri kümesi üzerinde tahminler yapar. Tahminler, modelin bağımsız değişkenlerin (X) değerlerine dayalı olarak bağımlı değişkenin (y) tahmini değerlerini içerir.

### Grafiği:

![Scatter Plot](02.DAY/basit_linear_regrasyon_img.png)
