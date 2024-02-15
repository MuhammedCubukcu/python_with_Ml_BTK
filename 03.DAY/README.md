# Çoklu Doğrusal Regresyon (Multiple Linear Regression)

Çoklu doğrusal regresyon, istatistik ve makine öğrenmesinde sıkça kullanılan bir tekniktir. Bu yöntem, bir bağımlı değişkenin bir veya daha fazla bağımsız değişkenle ilişkisini modellemek için kullanılır. İşte çoklu doğrusal regresyonun temel prensipleri ve detayları:

1. **Model**: Çoklu doğrusal regresyon, bir bağımlı değişkenin (genellikle "y") bir veya daha fazla bağımsız değişkenle ("x1", "x2", ..., "xn") ilişkisini modellemek için kullanılır. Bu model şu şekilde ifade edilir:

* y = β0 + β1x1 + β2x2 + ... + βn*xn + ε


Burada, β0, β1, β2,..., βn katsayıları temsil eder ve bağımsız değişkenlerin katsayılarını ifade eder. ε ise hata terimidir.

2. **Katsayılar (βk)**: Bu katsayılar, her bir bağımsız değişkenin bağımlı değişken üzerindeki etkisini temsil eder. Model, bu katsayıları tahmin ederek bağımsız değişkenlerin bağımlı değişken üzerindeki etkisini hesaplar.

3. **Hata Terimi (ε)**: Model, gerçek veriler ile tahmin edilen değerler arasındaki farkı temsil eden hata terimini içerir. Bu hata terimi, modelin ne kadar iyi uyum sağladığını ölçer.

4. **Model Uyumu**: Çoklu doğrusal regresyon modelinin uygunluğu, R-kare (R²) değeri ile değerlendirilir. R-kare, bağımsız değişkenlerin bağımlı değişken üzerindeki varyansını açıklama yüzdesini ifade eder. Yüksek R-kare değeri, modelin verilere iyi uyum sağladığını gösterir.

5. **Modelin Tahmini**: Model, verilen bağımsız değişken değerleri üzerinden bağımlı değişkenin tahmin edilmesi için kullanılabilir. Modelin tahmin ettiği değer, β0 + β1*x1 + β2*x2 + ... + βn*xn şeklinde hesaplanır.

6. **Modelin Değerlendirilmesi**: Çoklu doğrusal regresyon modeli, katsayıların ve R-kare değerinin yanı sıra, hata terimi ve diğer istatistiksel ölçütlerle de değerlendirilir. Modelin doğruluğunu artırmak için çeşitli ön işleme teknikleri ve model uyumu iyileştirme yöntemleri kullanılabilir.

7. **Önkoşullar**: Çoklu doğrusal regresyon analizi için bazı ön koşullar vardır. Örneğin, bağımsız değişkenler arasında çoklu doğrusallık olmamalıdır (yani, bağımsız değişkenler arasında yüksek bir korelasyon olmamalıdır). Ayrıca, hata terimi normal dağılıma sahip olmalıdır.

8. **Aşırı Uyum**: Aşırı uyum (overfitting), modelin eğitim verilerine çok iyi uyması ancak genelleme yeteneğinin zayıf olması durumudur. Aşırı uyum, modelin karmaşıklığını azaltarak veya regülarizasyon teknikleri kullanarak engellenebilir.

Çoklu doğrusal regresyon, değişkenler arasındaki ilişkileri anlamak, gelecekteki değerleri tahmin etmek ve kararlar almak için kullanışlı bir araçtır. Ancak, modelin doğru kullanımı ve yorumlanması için istatistiksel bilgiye ve analitik becerilere ihtiyaç vardır.

# Çoklu Doğrusal Regresyon Örneği

Otomobil satıcısı, araçlarının fiyatını belirlemek için çoklu doğrusal regresyon kullanmak istiyor. Veri seti şu şekildedir:

- **Bağımlı Değişken (Y)**: Araç fiyatı (TL cinsinden)
- **Bağımsız Değişkenler (X)**:
   1. Araç model yılı
   2. Araç kilometresi
   3. Motor hacmi (cc cinsinden)
   4. Araç tipi (örneğin, sedan, hatchback, SUV, vb.)
   5. Araç markası (örneğin, BMW, Mercedes, Audi, vb.)

Modelimiz şu şekildedir:

* Y = β0 + β1X1 + β2X2 + β3X3 + β4X4 + β5*X5 + ε


Burada:
- **Y**, araç fiyatını temsil eder.
- **X1**, **X2**, **X3**, **X4** ve **X5** sırasıyla model yılı, kilometresi, motor hacmi, araç tipi ve markasını temsil eder.
- **β0**, **β1**, **β2**, **β3**, **β4** ve **β5** katsayıları temsil eder.
- **ε** hata terimidir.

Veri seti kullanılarak katsayılar tahmin edilir ve model eğitilir. Modeli eğitirken, veri seti eğitim ve test verisi olarak ayrılır. Model eğitim verisi üzerinde eğitilir ve test verisi üzerinde performansı değerlendirilir.

Son olarak, model kullanılarak yeni bir araç için fiyat tahmini yapılabilir. Örneğin, 2018 model, 50.000 kilometrede, 1600cc motor hacmine sahip bir sedan araba için tahmini fiyat hesaplanabilir.

Bu örnek, çoklu doğrusal regresyon kullanarak bir otomobil satıcısının araç fiyatlarını tahmin edebileceği bir senaryoyu göstermektedir. Regresyon modeli aracılığıyla araç fiyatını tahmin etmek için çeşitli faktörler kullanılabilir.




# Dummy Variable (Kukla Değişken)

Dummy variable (kukla değişken) kavramı, makine öğrenimi alanında da önemlidir ve genellikle kategorik verilerin işlenmesinde kullanılır. Makine öğrenimi algoritmaları genellikle sayısal verilerle çalışır, bu nedenle kategorik verileri sayısal formata dönüştürmek için dummy variable kullanılır.

Özellikle doğrusal regresyon, lojistik regresyon, destek vektör makineleri (SVM), karar ağaçları ve derin öğrenme gibi birçok makine öğrenimi modeli, kategorik değişkenleri doğru şekilde işlemek için dummy variable kullanımını gerektirir.

Örneğin, bir görüntü sınıflandırma problemi ele alalım. Veri setinizde "köpek", "kedi" ve "kuş" gibi kategorik sınıflarınız varsa, bu sınıfları dummy variable olarak kodlamak için one-hot encoding yöntemini kullanabilirsiniz. Bu durumda, her bir sınıf için bir dummy variable oluşturulur. Örneğin:

- "Köpek" sınıfı için [1, 0, 0]
- "Kedi" sınıfı için [0, 1, 0]
- "Kuş" sınıfı için [0, 0, 1]

Bu şekilde, kategorik sınıflar sayısal formata dönüştürülür ve makine öğrenimi modeliniz tarafından doğru şekilde işlenebilir.

Dummy variable kullanımı, kategorik verilerin işlenmesinde yaygın bir uygulamadır ve makine öğrenimi modellerinin doğru şekilde eğitilmesi için önemlidir. Ancak, modelin doğruluğunu artırmak için gereksiz dummy variable'ların önlenmesi ve gerektiğinde özellik seçimi yapılması da önemlidir.

## p-value Nedir?

**p-value** (veya p-değeri), istatistiksel bir test sonucunda elde edilen bir bulgunun, rastgelelikten kaynaklanıp kaynaklanmadığını değerlendirmek için kullanılan bir ölçüdür. Bir başka deyişle, p-value, bir hipotezin doğruluğunu veya bir ilişkinin anlamlılığını belirlemek için kullanılır.

### Nasıl Yorumlanır?

- Bir hipotezin **null (H0) hipotezi** olarak adlandırılan bir varsayımı vardır. Bu varsayım genellikle "hiçbir etki yok" veya "hiçbir fark yok" şeklinde ifade edilir.
- Bir istatistiksel test yapılır ve bu test sonucunda bir **p-value** elde edilir.
- p-value, null hipotezi doğruysa, gözlemlenen verilerin veya daha fazla "şansa" dayalı olduğu olasılığını gösterir. Yani, **küçük bir p-value**, null hipotezinin doğru olma olasılığının düşük olduğunu gösterir.
- Eğer elde edilen p-value, belirlenen bir **anlamlılık düzeyinden (genellikle α olarak adlandırılır) daha küçükse** (yani, p < α), o zaman null hipotezi reddedilir ve verilerin null hipotezden önemli şekilde farklı olduğu sonucuna varılır.
- Eğer elde edilen p-value, α'dan **büyükse** (yani, p ≥ α), o zaman null hipotezi reddedilemez ve veriler null hipotezle tutarlı olarak kabul edilir.

### Özet

p-value, bir hipotezin doğruluğunu belirlemek için kullanılan istatistiksel bir ölçüdür. Daha düşük bir p-value, verilerin null hipotezle tutarlı olmadığını ve bir ilişkinin veya etkinin anlamlı olduğunu gösterir.

## p-value Örneği

Örneğin, bir ilaç şirketi, yeni bir ilacın hastalar üzerinde mevcut bir tedaviden daha etkili olduğunu iddia ediyor. Bu iddiayı test etmek için bir klinik deney yapılıyor. Deney iki grup üzerinde gerçekleştiriliyor:

- **Kontrol grubu**: Mevcut tedavi yöntemini alan hastalar.
- **Deney grubu**: Yeni ilacı alan hastalar.

Deney sonucunda, deney grubundaki hastaların belirli bir süre sonra daha az semptom gösterdiği gözlemleniyor. Ancak, bu gözlem yeterli değil, çünkü bu sonucun rastgelelikten mi yoksa gerçek bir etkiden mi kaynaklandığını belirlemek gerekiyor.

Bu durumu değerlendirmek için bir hipotez testi yapılabilir. **Null hipotez (H0)**, "Yeni ilaç ile mevcut tedavi arasında herhangi bir fark yoktur" şeklinde ifade edilebilir. **Alternatif hipotez (H1)** ise, "Yeni ilaç, mevcut tedaviden daha etkilidir" şeklinde olabilir.

Deney sonuçlarına göre, istatistiksel bir test yapılır ve bir **p-value** elde edilir. Varsayalım ki bu p-value, 0.02 olarak bulunmuştur ve belirlenen anlamlılık düzeyi (**α**) ise 0.05'tir.

- Eğer elde edilen p-value, α'dan (0.05) daha küçükse (yani, p < α), o zaman null hipotezi reddedilir.
- Dolayısıyla, p-value = 0.02 < 0.05 olduğu için, null hipotezi reddedilir ve bu, yeni ilacın mevcut tedaviye göre daha etkili olduğunu düşündürebilir.

Sonuç olarak, **p-value** hipotez testlerinde, bir hipotezin doğruluğunu değerlendirmek için kullanılan önemli bir ölçüdür. Daha düşük bir p-value, verilerin null hipotezle tutarlı olmadığını ve bir ilişkinin veya etkinin anlamlı olduğunu gösterir.



## Çoklu Linear Regresyonda Değişken Seçimi

Çoklu doğrusal regresyon modellerinde değişken seçimi, modelin doğruluğunu artırmak ve gereksiz değişkenlerin etkisini azaltmak için önemlidir. Burada bazı yaygın değişken seçimi teknikleri:

1. **İleriye Yönlü Seçim (Forward Selection)**:
   - Bu yöntemde, modele başlangıçta en anlamlı olduğu düşünülen değişken eklenir.
   - Ardından, her bir değişkenin modele eklenmesinin ardından, eklenen değişkenin modeldeki etkisinin değerlendirilir.
   - En fazla iyileştirmeyi sağlayan değişken bir sonraki adıma eklenir.
   - Bu işlem, belirli bir kriter karşılanana kadar devam eder (örneğin, AIC veya BIC kriterlerine göre).

2. **Geriye Yönlü Eleme (Backward Elimination)**:
   - Bu yöntemde, modele başlangıçta tüm değişkenler eklenir.
   - Ardından, her bir değişkenin modeldeki etkisi değerlendirilir.
   - En az iyileştirmeyi sağlayan değişken bir sonraki adımda modele çıkartılır.
   - Bu işlem, belirli bir kriter karşılanana kadar devam eder.

3. **Karmaşık Modellerin Basitleştirilmesi**:
   - Modeldeki karmaşık etkileşimleri ve çoklu doğrusallığı azaltmak için değişkenler birleştirilebilir veya dönüştürülebilir.
   - Örneğin, iki değişkenin çarpımı olarak yeni bir değişken oluşturulabilir veya logaritmik dönüşümler uygulanabilir.

4. **AIC ve BIC Kriterleri**:
   - AIC (Akaike Bilgi Kriteri) ve BIC (Bayes Bilgi Kriteri) gibi bilgi kriterleri, farklı modellerin karşılaştırılması için kullanılabilir.
   - Bu kriterler, daha basit modelleri (daha az değişken içeren) daha karmaşık modellere tercih eder.
   - Model seçiminde AIC veya BIC değeri en düşük olan model tercih edilir.

5. **Çapraz Doğrulama (Cross-Validation)**:
   - Veri seti üzerinde çapraz doğrulama kullanılarak, farklı alt veri setleri üzerinde modeller değerlendirilir.
   - Bu, modelin aşırı uyumu (overfitting) önlemeye yardımcı olur ve daha genelleştirilebilir bir model elde etmeye yardımcı olur.

Değişken seçimi, modelin doğruluğunu artırmak ve modelin genelleme yeteneğini iyileştirmek için kritik bir adımdır. Bu tekniklerin kullanılması, modelin daha basit ve daha etkili olmasına yardımcı olabilir.


## Çoklu Linear Regresyonda Değişken Seçimi Örneği

**Not:Tüm makine öğrenim algortimaları için yapılabilir**

Örneğin, bir ev fiyatlarını tahmin etmek için çoklu doğrusal regresyon modeli kullanmak istiyoruz. Elimizdeki veri seti şu özelliklere sahip:

- **Bağımlı Değişken (Y)**: Ev fiyatı
- **Bağımsız Değişkenler (X)**:
   1. Ev büyüklüğü (metrekare cinsinden)
   2. Yatak odası sayısı
   3. Banyo sayısı
   4. Konumun mahalle puanı (örneğin, 1 ile 10 arasında bir değer)

Bizim amacımız, ev fiyatını doğru bir şekilde tahmin edebilecek en iyi modeli oluşturmak için uygun değişkenleri seçmektir.

### Örnek Değişken Seçimi İşlemi:

1. İlk adım olarak, tüm bağımsız değişkenleri modele ekliyoruz ve AIC veya BIC gibi bir bilgi kriteri kullanarak en iyi modeli seçiyoruz.

2. Modelimizi oluşturduk ve AIC veya BIC değerine göre en iyi modeli seçtik. Şimdi, bu modele dayanarak her bir değişkenin etkisini değerlendiriyoruz.

3. Örneğin, banyo sayısı değişkeni modelimiz için istatistiksel olarak anlamlı değilse (yüksek p-value), bu değişkeni modelden çıkarabiliriz.

4. Ardından, banyo sayısı değişkenini modelden çıkardıktan sonra, AIC veya BIC kriterine göre tekrar bir değerlendirme yapabiliriz. Eğer modelimiz daha iyi bir AIC veya BIC değeri elde ederse, banyo sayısı değişkenini çıkarmak mantıklı olabilir.

5. Bu süreci tüm değişkenler için tekrarlayarak, en iyi modeli elde edene kadar devam ederiz. Bu süreçte, değişkenlerin modeldeki etkisi (p-value) ve AIC veya BIC değerleri gibi bilgi kriterlerini dikkate alırız.

Sonuç olarak, bu örnekte, değişken seçimi sürecinde hangi değişkenlerin modele dahil edileceği ve hangilerinin çıkarılacağı konusunda kararlar vererek, en iyi modeli oluştururuz. Bu, modelin daha basit ve daha etkili olmasını sağlar, ayrıca modelin genelleme yeteneğini artırır.

## AIC ve BIC Nedir?

**AIC (Akaike Bilgi Kriteri)** ve **BIC (Bayes Bilgi Kriteri)**, bir modelin kalitesini değerlendirmek için kullanılan istatistiksel bilgi kriterleridir. Bu kriterler, bir modelin ne kadar iyi uyuştuğunu değerlendirirken modelin karmaşıklığını da dikkate alır.

- **AIC (Akaike Bilgi Kriteri)**: Modelin uyumunun ve karmaşıklığının bir dengesini sağlar. Daha küçük AIC değerleri, modelin daha iyi uyması ve daha az karmaşık olması anlamına gelir. AIC, modelin tahmin etme başarısını ve genelleme yeteneğini iyileştirmeye çalışır.

- **BIC (Bayes Bilgi Kriteri)**: AIC'ye benzer şekilde, model uyumunu ve karmaşıklığını dengeler. Ancak, BIC, AIC'den farklı olarak, model karmaşıklığını daha fazla cezalandırır. Bu nedenle, BIC daha basit modelleri (daha az değişken içeren) tercih eder. BIC, modelin genelleme yeteneğini iyileştirmeye çalışırken, daha da büyük bir önem atfeder.

AIC ve BIC değerleri, farklı modeller arasında karşılaştırma yaparken kullanılır. Genellikle, daha küçük AIC veya BIC değerine sahip olan model, verileri daha iyi açıklar ve daha az karmaşıktır, bu nedenle daha tercih edilir.

Ancak, AIC ve BIC değerleri bir modelin mutlak kalitesini değil, farklı modeller arasındaki göreceli kaliteyi gösterir. Bu nedenle, AIC veya BIC değeri en düşük olan model, en iyi model olmayabilir, ancak diğer modellere göre daha iyi performans gösterir.

AIC ve BIC, model seçimi ve değişken seçimi gibi istatistiksel analizlerde yaygın olarak kullanılır. Bu kriterler, modelin doğruluğunu artırmak ve gereksiz karmaşıklığı azaltmak için faydalı bir araçtır.



# OLS Regression 

### OLS Regression Results

```python

                           OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.626
Model:                            OLS   Adj. R-squared:                  0.509
Method:                 Least Squares   F-statistic:                     5.361
Date:                Thu, 15 Feb 2024   Prob (F-statistic):            0.00440
Time:                        15:59:31   Log-Likelihood:                -5.1425
No. Observations:                  22   AIC:                             22.29
Df Residuals:                      16   BIC:                             28.83
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             2.2338      1.174      1.903      0.075      -0.254       4.722
x2             2.2461      1.075      2.089      0.053      -0.033       4.525
x3             1.8514      1.122      1.651      0.118      -0.526       4.229
x4            -0.0204      0.010     -2.098      0.052      -0.041       0.000
x5             0.0308      0.008      3.682      0.002       0.013       0.048
x6            -0.0077      0.010     -0.813      0.428      -0.028       0.012
==============================================================================
Omnibus:                        0.140   Durbin-Watson:                   1.516
Prob(Omnibus):                  0.932   Jarque-Bera (JB):                0.212
Skew:                          -0.158   Prob(JB):                        0.899
Kurtosis:                       2.637   Cond. No.                     4.53e+03
==============================================================================

```


- **R-squared (R-kare)**: Bağımsız değişkenlerin bağımlı değişken üzerindeki varyansın açıklama yüzdesi. 0 ile 1 arasında değer alır, 1'e ne kadar yakınsa, model o kadar iyi uyum sağlar.

- **Adjusted R-squared (Düzeltilmiş R-kare)**: R-kare'nin bir düzeltilmiş versiyonudur ve modeldeki ek bağımsız değişkenlerin sayısını dikkate alır. Daha fazla bağımsız değişken eklendiğinde, R-kare artabilir, ancak bu yeni değişkenlerin tahmin edilen değişkeni açıklama yeteneği gerçekten iyileştirmediği durumlar olabilir. Bu nedenle, düzeltilmiş R-kare, eklenen değişkenlerin gerçekten modelin kalitesine katkıda bulunup bulunmadığını görmemize yardımcı olur.

- **F-statistic (F-istatistiği)**: Modelin anlamlılığını test etmek için kullanılan bir istatistik değeri. Büyük bir F-istatistiği, modelin bağımlı değişkeni açıklamada anlamlı olduğunu gösterir.

- **Prob (F-statistic) (F-istatistiği için p-değeri)**: F-istatistiğinin anlamlılığını gösteren p-değeri. Bu değer ne kadar küçükse, modelin anlamlılığı o kadar yüksektir.

- **Coefficients (Katsayılar)**: Bağımsız değişkenlerin katsayıları, her bir bağımsız değişkenin bağımlı değişken üzerindeki etkisini gösterir. Bu katsayılar, bağımsız değişkenlerdeki bir birimlik değişikliğin, bağımlı değişken üzerinde ne kadar bir değişikliğe neden olacağını belirtir.

- **P>|t| (t-istatistiği için p-değeri)**: Katsayıların anlamlılığını test etmek için kullanılan p-değerleri. Her katsayı için, null hipotezi "bu katsayı sıfırdır" şeklinde olur ve küçük p-değerleri (genellikle <0.05) bu null hipotezinin reddedilmesini, yani katsayının anlamlı olduğunu gösterir.

- **Omnibus**: Jarque-Bera normallik testi istatistiğidir. Bu, hata terimlerinin normal olarak dağıldığı bir varsayımı test eder. Eğer p-değeri yeterince yüksekse (genellikle >0.05), bu normal dağılımın kabul edilebilir olduğunu gösterir.

- **Durbin-Watson**: Otokorelasyonun varlığını test eden bir istatistik. Değerler 0 ile 4 arasında olabilir ve 2'ye ne kadar yakınsa, otokorelasyon olasılığı o kadar düşüktür.

- **Prob(Omnibus)**: Omnibus testi için p-değeri.

- **Jarque-Bera (JB)**: Hata terimlerinin normal dağılıma sahip olup olmadığını test eden bir istatistik.

- **Skew (Çarpıklık) ve Kurtosis (Basıklık)**: Hata terimlerinin çarpıklık ve basıklık değerleri.

- **Cond. No. (Kondisyon numarası)**: Bağımsız değişkenler arasındaki çoklu doğrusal bağlantının derecesini ölçer. Büyük bir kondisyon numarası, modelin istikrarsız olduğunu ve tahminlerin güvenilir olmayabileceğini gösterebilir.


