# Decision Tree Classification Nedir?

Decision Tree classification, karar ağacı sınıflandırması olarak da adlandırılır, makine öğrenimi ve istatistiksel bir sınıflandırma tekniğidir. Bu teknik, veri setlerini bir dizi karar kuralı ve koşul kullanarak sınıflandıran bir ağaç yapısı oluşturur.

## Adım Adım İşleyiş:

1. **Kök Düğüm (Root Node)**: Karar ağacının başlangıç noktasıdır. Veri setindeki tüm örnekler burada bulunur. Kök düğüm, en önemli özniteliği seçmek için bir karar kuralı oluşturur. Bu karar kuralı, veri setini alt kümelerine böler.

2. **Karar Kuralları (Decision Rules)**: Her düğüm, belirli bir öznitelik ve bu özniteliğin değeri arasında bir karar kuralı içerir. Örneğin, bir düğüm "yaş < 30" şeklinde bir karar kuralı olabilir.

3. **Dallanma (Splitting)**: Kök düğümde belirlenen karar kuralı, veri setini alt kümelerine böler. Her bir alt küme, belirli bir öznitelik değerine sahip örnekleri içerir.

4. **Yaprak Düğümler (Leaf Nodes)**: Dallanma işlemi tekrarlanarak ağaç oluşturulur. Her adımda yeni bir düğüm oluşturulur ve veri seti daha küçük alt kümelerine bölünür. Sonunda, hiçbir bölme yapılmayacak duruma gelindiğinde, yaprak düğümlerine ulaşılır. Yaprak düğümlerinde sınıflandırma yapılarak bir sınıf etiketi atanır.

5. **Veri Kümesinin Bölünmesi (Data Splitting)**: Veri seti, karar ağacı oluşturulurken alt kümelerine bölünür. Bu bölme işlemi, veri kümesinin homojenliğini artıracak şekilde yapılır. Yani, bir alt kümedeki örnekler aynı sınıfa ait olacak şekilde bölünür.

6. **Karar Ağacı Oluşturma Algoritması**: Karar ağacı oluşturmak için birçok algoritma kullanılabilir, örneğin CART (Classification and Regression Trees), ID3 (Iterative Dichotomiser 3), C4.5 ve Random Forest gibi. Bu algoritmalar, veri kümesindeki özniteliklerin değerlerine göre en iyi bölme noktalarını ve karar kuralını belirler.

7. **Model Değerlendirme ve Ayarlanması**: Oluşturulan karar ağacının performansı, veri kümesinin bir kısmını eğitim için kullandıktan sonra geriye kalan kısmını test etmek suretiyle değerlendirilir. Ayrıca, ağacın aşırı uyuma (overfitting) eğilimini azaltmak için çeşitli yöntemler kullanılabilir, örneğin ağacın derinliği sınırlandırılabilir veya ağacın büyüklüğünü kontrol etmek için kesme (pruning) işlemi yapılabilir.

Karar ağacı sınıflandırması, yüksek derecede yorumlanabilir ve açıklanabilir bir model sağlar. Ayrıca, kategorik ve sayısal öznitelikleri işleyebilir ve veri ön işleme gereksinimini minimumda tutar. Bu nedenle, birçok uygulama alanında tercih edilir.
