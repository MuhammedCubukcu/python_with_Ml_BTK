## Denetimsiz Öğrenme

Denetimsiz öğrenme, makine öğrenimi alanında bir alt dal olarak kabul edilir ve genellikle veri kümesindeki desenleri ve ilişkileri belirlemek için kullanılır. Denetimsiz öğrenme, girdi verilerindeki düzeni ortaya çıkarmak için kullanılırken, bir etiket veya hedef çıktıya dayanmaz. Yani, denetimsiz öğrenme algoritmaları, veri kümesindeki yapıları öğrenir ve verileri tanımlamak, sınıflandırmak veya kümelemek gibi görevleri gerçekleştirirken, bir öğretmen sinyali veya doğru çıktı kullanmazlar.

Denetimsiz öğrenme, çeşitli teknikleri içerir, ancak en yaygın olanları şunlardır:

### 1. Kümeleme (Clustering)
Benzer özelliklere sahip veri noktalarını gruplamak için kullanılır. K-means gibi algoritmalar, veri noktalarını farklı kümelerde gruplandırmak için sıklıkla kullanılır.

### 2. Boyutsal Azaltma (Dimensionality Reduction)
Yüksek boyutlu veri kümelerini daha az boyutta bir temsil ile ifade etmek için kullanılır. Örneğin, PCA (Principal Component Analysis) veya t-SNE (t-Distributed Stochastic Neighbor Embedding) gibi algoritmalar, veri setlerindeki özellikler arasındaki ilişkileri bulmak için kullanılabilir.

### 3. Doğrusal Olmayan Öğrenme (Non-linear Learning)
Veri setindeki gizli yapıları bulmak için kullanılır. Örneğin, otomatik kodlayıcılar veya derin öğrenme algoritmaları gibi teknikler, veri setlerindeki karmaşık ilişkileri öğrenmek için kullanılabilir.

Denetimsiz öğrenme, veri setlerindeki gizli yapıları keşfetmek ve verilerin doğasını daha iyi anlamak için güçlü bir araçtır. Bu teknikler, özellikle etiketlenmemiş veya eksik veriye sahip olduğumuz durumlarda faydalı olabilir. Ancak, denetimsiz öğrenme tekniklerinin sonuçları genellikle yorumlanması daha zor olabilir, çünkü bir öğretmen sinyali olmadığından, algoritmanın keşfettiği yapılar açıkça tanımlanmamış olabilir.

## En Çok Kullanılan Denetimsiz Öğrenme Algoritmaları

1. **K-means Kümeleme (K-means Clustering)**: Veri noktalarını k belirli sayıda küme veya grup halinde kümelemek için kullanılan bir kümeleme algoritmasıdır. Her küme, o kümedeki noktaların merkezini temsil eder.

2. **Hiyerarşik Kümeleme (Hierarchical Clustering)**: Veri noktalarını hiyerarşik bir yapıda kümelemek için kullanılan bir kümeleme algoritmasıdır. Kümeleme, aglomere edici (birleştirici) veya bölücü (bölücü) yaklaşımlarla gerçekleştirilebilir.

3. **Gaussian Karışım Modelleri (Gaussian Mixture Models)**: Her bir veri noktasının birden fazla Gaussian dağılımı ile modellendiği bir olasılık tabanlı bir modeldir. Veri setini birkaç Gaussian bileşeniyle modellere dönüştürerek kümeleme yapar.

4. **Boyutsal Azaltma (Dimensionality Reduction)**: Boyut azaltma algoritmaları, yüksek boyutlu veri kümelerini daha düşük boyutlu bir uzayda temsil etmek için kullanılır. PCA (Principal Component Analysis) ve t-SNE (t-Distributed Stochastic Neighbor Embedding) bu kategoride en yaygın kullanılan algoritmalardır.

5. **Doğrusal Olmayan Boyutsal Azaltma (Non-linear Dimensionality Reduction)**: Veri setindeki non-lineer ilişkileri bulmak ve temsil etmek için kullanılır. İyi bilinen bir örnek, Kernel PCA gibi çeşitli Kernel yöntemlerini kullanan algoritmalardır.

6. **Apriori Algoritması**: Bir veri kümesinde sık görülen öğe kümelerini bulmak için kullanılır. Özellikle pazar sepeti analizi gibi alanlarda kullanılır.

7. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: Yoğunluk tabanlı bir kümeleme algoritmasıdır. Veri noktalarını yoğunluk tabanlı olarak gruplar ve ayrık kümeler oluştururken gürültüyü tanır.

8. **Mean Shift**: Yoğunluğu en yüksek olan bölgeye doğru hareket ederek veri noktalarını kümelemek için kullanılan bir algoritmadır. Özellikle nesne algılama ve görüntü işleme alanlarında kullanılır.

Bu, denetimsiz öğrenme alanında en çok kullanılan bazı algoritmaların sadece birkaç örneğidir. Uygulanacak görevin doğası ve veri setinin özellikleri, hangi algoritmanın en uygun olduğunu belirler.


## K-means Algoritması

K-means, veri kümesini kümelemek için yaygın olarak kullanılan bir kümeleme algoritmasıdır. Bu algoritma, veri noktalarını k adet küme veya grubuna atar. Her bir kümenin merkezi, o küme içindeki noktaların ortalaması olarak hesaplanır. Algoritma, veri noktalarını belirli bir kritere göre (genellikle Euclidean uzaklık kullanılarak) kümelere atar ve ardından her bir veri noktasının ait olduğu kümeyi yeniden hesaplar. Bu süreç, küme merkezlerinin güncellenmesi ve veri noktalarının en yakın küme merkezine atanması adımları arasında tekrarlanır. Genellikle, küme merkezlerinin güncellenmesi ve veri noktalarının yeniden atanması, değişiklik olmadığına veya belirli bir tolerans sınırına ulaşılana kadar devam eder.

### Adımlar

1. Başlangıçta, k adet küme merkezi rastgele seçilir.
2. Her veri noktası, en yakın küme merkezine atanır.
3. Her bir kümenin merkezi, o kümeye ait veri noktalarının ortalaması olarak güncellenir.
4. Yeni küme merkezleri belirlendikten sonra, her veri noktası tekrar en yakın küme merkezine atanır.
5. Küme merkezlerinin değişimi belirli bir eşik değerinin altına düşene kadar adımlar 3 ve 4 tekrarlanır.

### Avantajlar

- Basit ve hızlıdır.
- Büyük veri kümeleriyle iyi başa çıkar.
- Uygulaması kolaydır ve genellikle iyi sonuçlar verir.

### Dezavantajlar

- Küme sayısı k'nın önceden belirlenmesi gerekmektedir.
- Başlangıç merkezlerin rastgele seçilmesi sonuçları etkileyebilir, bazı durumlarda optimal olmayan sonuçlar elde edilebilir.
- Küme merkezlerinin rastgele seçilmesi veya outlier varlığı, algoritmanın yanlış sonuçlar üretmesine neden olabilir.

Bu nedenle, K-means algoritması genellikle başlangıç merkezlerin seçimi, outlier'ların ele alınması ve uygun küme sayısının belirlenmesi gibi faktörlerle dikkatlice kullanılmalıdır.

### Hiyerarşik Kümeleme (Hierarchical Clustering)

**Açıklama**: Veri noktalarını hiyerarşik bir yapıda kümelemek için kullanılan bir kümeleme algoritmasıdır. Kümeleme, aglomere edici (birleştirici) veya bölücü (bölücü) yaklaşımlarla gerçekleştirilebilir.

**Adımlar**:
1. Her bir veri noktası, tek elemanlık kümelere atanır.
2. Belirli bir mesafe metriği kullanılarak, en yakın iki küme birleştirilir.
3. 2. adım belirli bir kriter sağlanana kadar (mesela uzaklık, küme sayısı veya benzerlik değeri) tekrarlanır.
4. Sonuç olarak, birleştirme ağacı (dendrogram) oluşturulur veya kümeleme sonlandırılır.

### Gaussian Karışım Modelleri (Gaussian Mixture Models)

**Açıklama**: Her bir veri noktasının birden fazla Gaussian dağılımı ile modellendiği bir olasılık tabanlı bir modeldir. Veri setini birkaç Gaussian bileşeniyle modellere dönüştürerek kümeleme yapar.

**Adımlar**:
1. Başlangıçta, her bir Gaussian dağılımın parametreleri rastgele seçilir veya EM (Expectation-Maximization) algoritmasıyla tahmin edilir.
2. Her bir veri noktası için, her bir Gaussian bileşeninin katkısının olasılığı hesaplanır.
3. EM algoritması kullanılarak, Gaussian bileşenlerinin parametreleri yeniden tahmin edilir.
4. Parametreler belirli bir kriter sağlanana kadar (örneğin, maksimum iterasyon sayısı veya parametre değişimi) 2. ve 3. adımlar tekrarlanır.
5. Sonuç olarak, her veri noktasının ait olduğu küme, en yüksek olasılığa sahip Gaussian bileşenine göre belirlenir.

### Boyutsal Azaltma (Dimensionality Reduction)

**Açıklama**: Boyut azaltma algoritmaları, yüksek boyutlu veri kümelerini daha düşük boyutlu bir uzayda temsil etmek için kullanılır. PCA (Principal Component Analysis) ve t-SNE (t-Distributed Stochastic Neighbor Embedding) bu kategoride en yaygın kullanılan algoritmalardır.

**Adımlar (PCA)**:
1. Veri setinin kovaryans matrisi hesaplanır.
2. Kovaryans matrisi, özdeğer ayrışımı yapmak için kullanılır.
3. Özdeğerler ve özvektörler elde edilir.
4. Özvektörler, veri setini yeni bir boyutta temsil etmek için kullanılır.
