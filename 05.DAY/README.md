# Destek Vektör Regresyonu (Support Vector Regression)


Destek Vektör Regresyonu (SVR), bir makine öğrenimi tekniğidir ve regresyon problemlerini çözmek için kullanılır. Regresyon, bir bağımlı değişkenin (genellikle sürekli bir sayısal değer) bağımsız değişkenler tarafından nasıl etkilendiğini modellemeye çalışır.

SVR, özellikle gürültülü veriyle çalışırken etkili olan bir regresyon yöntemidir. Temel fikir, veri noktalarını bir hiperdüzlem etrafında bir destek vektörüne (support vector) dayalı olarak bir araya getirmektir.

## İşleyiş

1. **Veri Noktaları**: Öncelikle, bir eğitim veri seti alınır. Bu veri seti, bağımlı değişkenin (hedef değişkenin) bilinen bağımsız değişkenlerle eşleştirildiği verilerden oluşur.

2. **Hiperdüzlem Oluşturma**: SVR, veri noktalarını bir hiperdüzlem etrafında gruplamaya çalışır. Bu hiperdüzlem, tüm veri noktalarını mümkün olduğunca iyi bir şekilde ayırmayı amaçlar. Ancak, tüm noktaları kesin olarak ayıramazsınız, bu yüzden bir hata marjı (epsilon) tanımlanır.

3. **Destek Vektörlerini Bulma**: SVR, hiperdüzlemi oluştururken kullanılan destek vektörlerini belirler. Bu destek vektörler, hiperdüzlemi tanımlamak için en önemli veri noktalarıdır.

4. **Modeli Optimize Etme**: SVR, belirlenen hiperdüzlemi kullanarak modeli optimize etmeye çalışır. Bu, hiperdüzlemi oluşturmak için kullanılan parametrelerin ayarlanması ve destek vektörlerinin belirlenmesini içerir.

5. **Tahmin**: Son olarak, model eğitildikten sonra, yeni veri noktaları üzerinde tahmin yapmak için kullanılabilir. Model, veri noktalarını hiperdüzlem etrafında nasıl gruplandırdıysa, yeni veri noktalarını da aynı şekilde gruplandırır ve tahminler yapar.

SVR'nin temel amacı, belirli bir hiperdüzlem etrafında veri noktalarını olabildiğince iyi bir şekilde sığdırmaktır. Bu, regresyon problemlerinde etkili bir şekilde çalışabilir ve özellikle gürültülü veri setlerinde güçlü sonuçlar verir.


### Model Hiperdüzlemi:
* f(x) = w · x + b
Burada:
- f(x) hedef değişkenin tahmini,
- x giriş özellik vektörü,
- w ağırlık vektörü (katsayılar),
- b bias (kesme terimi) olarak adlandırılır.

### Hata Terimi ve Marjinal Epsilon (ε):
* |y - f(x)| ≤ ε
Burada:
- y gerçek hedef değeridir,
- f(x) hedef değişkenin tahmini (model tarafından verilen).

### Destek Vektörler ve Dual Formülasyon:
SVR'de, hiperdüzlemi tanımlayan noktalar "destek vektörleri" olarak adlandırılır. Bunlar, hiperdüzlemi belirleyen en önemli veri noktalarıdır. SVR, veri noktalarını doğrusal veya doğrusal olmayan bir hiperdüzlem etrafında gruplandırmaya çalışırken, çoğu zaman verilerin dönüştürüldüğü bir dual formülasyon kullanır.

Dual formülasyon, veri noktaları arasındaki iç çarpımı hesaplamak için bir çekirdek fonksiyonu kullanır. Bu, verilerin yüksek boyutlu özellik uzayına dönüştürülmesine izin verir, böylece doğrusal olmayan ilişkileri ifade etmek mümkün olur.
