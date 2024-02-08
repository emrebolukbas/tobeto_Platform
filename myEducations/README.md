<h1>TEST SENERYOSU 8: EĞİTİM PANELİ</h1>
<b>Açıklama :</b> Tobeto eğitim platformuna kullanıcıların e-posta ve şifre ile sisteme giriş yapmış olduğu platform üzerinde ‘’Eğitim’’ paneli kontrol edilecektir.<br>
<b>Ön koşullar :</b> Kullanıcı panale giriş yapmış olmalı ve eğitimleri atanmış olmalıdır.<br><br>

<h4>Test Case 1: Eğitimlerim Sayfasının Görüntülenmesi</h4>
<b>Açıklama :</b> “Eğitimlerim’’ sekmesi görüntülenmesi test edilecektir.<br>
<b>Ön koşul :</b> Sayfada ‘’Eğitimlerim’’  butonu tıklanabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Ana sayfada ‘’Eğitimlerim’’butonuna tıkla.<br>
<b>2-</b> Tanımlanmış eğitimlerin görünürlüğünü kontrol et.<br><br>
<b>Beklenen sonuç:</b> ‘’Eğitimlerim’’sayfasında 4 adet eğitim görüntülenmelidir. Aşağıda görselleri verilmiştir.<br><br>
<img src="images/Picture1.png" alt="picture1"> 
<h4>Test Case 2: Daha Fazla Göster Butonu</h4> 
<b>Açıklama:</b> Eğitimlerim sekmesi altında ‘’Daha Fazla Göster Butonu’’ test edilecektir.<br>
<b>Ön koşul :</b> Sayfada ‘’Daha Fazla Göster Butonu’’ tıklanabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Ana sayfada ‘’Eğitimlerim’’butonuna tıkla.<br>
<b>2-</b>"Daha Fazla Göster" butonuna tıkla.<br>
<img src="images/Picture2.png" alt="picture2"> 
<b>3-</b> "Eğitimlerim" sayfasına başarıyla yönlendirildiğini ve sayfanın başlığının doğru bir şekilde görüntülendiğini kontrol et. <br><br>
<b>Beklenen sonuç:</b> Eğitimlerim sayfası görüntülenmelidir. Aşağıda görseli verilmiştir.<br><br> 
<img src="images/Picture3.png" alt="picture3"> 
<h4>Test Case 3 : Arama çubuğu başarılı arama</h4>
<b>Açıklama: :</b> Kendilerine atanmış eğitimlere ‘’Arama Çubuğu’’ ile test edilecektir.<br>
<b>Ön koşul :</b>  Daha fazla göster Sayfasında ‘’Arama Çubuğu Görüntülenebilir ’’ kullanılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Arama çubuğuna bir karakter girişi yap.<br>
İnput : mentör<br>
<b>2-</b> Eşleşen karakterlere ait ilgili eğitimlerin listelendiğini kontrol et. <br>
<b>3-</b> Sayfayı yenile ve sayfanın yenilendiğinde arama ayarlarının sıfırlandığını ve tüm eğitimlerin görüntülendiğini kontrol et.<br><br>
<b>Beklenen sonuç:</b>Arama çubuğu ile eşleşen karakterlere ait ilgili eğitimler görüntülenmelidir. Aşağıdaki görseldeki gibi olmalı.<br><br>
 <img src="images/Picture4.png" alt="picture4"> 

<h4>Test Case 4 : Arama çubuğu başarısız arama</h4>
<b>Açıklama: :</b> Kendilerine atanmış eğitimlere ‘’Arama Çubuğu’’ ile test edilecektir.<br>
<b>Ön koşul :</b> Daha fazla göster Sayfasında ‘’Arama Çubuğu Görüntülenebilir ’’ kullanılabilir olmalıdır.<br><br>

<b>Adımlar:</b><br>
<b>1-</b>Arama çubuğuna bir karakter girişi yap.<br>
İnput:tobeto<br>
<b>2-</b> "Size atanan herhangi bir eğitim bulunmamaktadır." yazısının görüntülendiğini kontrol et.<br>
<b>3-</b> Sayfayı yenile ve sayfanın yenilendiğinde arama ayarlarının sıfırlandığını ve tüm eğitimlerin görüntülendiğini kontrol et.<br>
<b>Beklenen sonuç:</b>Arama çubuğuna eşleşmeyen karakter girildiğinde “size atanan herhangi bir eğitim bulunmamaktadır”yazısı görüntülenmelidir.<br><br>
<img src="images/Picture5.png" alt="picture5"> 
<h4>Test Case 5 : Filtreleme çubuğu başarılı listeleme</h4>
<b>Açıklama:</b> ‘’Filtreleme Çubuğu’’kullanımı test edilecektir.<br>
<b>Ön koşul :</b> Daha fazla göster Sayfasında ‘’Filtreleme Çubuğu Görüntülenebilir ’’ kullanılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Filtreleme çubuğunun içerisinde "Kurum Seçiniz" yazısının bulunduğunu kontrol et.<br>
<b>2-</b> Filtreleme çubuğunun üstüne tıkladığında eğitimleri veren kurumların adının açılır listede görüntülendiğini ve karakter girişi yapabildiğini kontrol et.<br>
 <img src="images/Picture6.png" alt="picture6">
<b>3-</b> Karakter girişi yap ve kurum ara.<br>
İnput :İstanbul<br>
<img src="images/Picture7.png" alt="picture7"> 
<b>4-</b> Seçilen kurumların verdiği eğitimlerin listelendiğini kontrol et.<br><br>
<img src="images/Picture8.png" alt="picture8"> 
<b>Beklenen sonuç :</b> Filtreleme sonucu eğitimler listelenmelidir. Aşağıdaki görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture9.png" alt="picture9"> 

<h4>Test Case 6 : Filtreleme çubuğu başarısız listeleme</h4>
<b>Açıklama:</b> ‘’Filtreleme Çubuğu’’kullanımı test edilecektir.<br>
<b>Ön koşul :</b> Daha fazla göster Sayfasında ‘’Filtreleme Çubuğu Görüntülenebilir ’’ kullanılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<p>1-</b>Filtreleme çubuğuna tıkla.<br>
<img src="images/Picture10.png" alt="picture10"> 
<b>2-</b> Karakter girişi yap.<br>
İnput:tobeto<br>
<b>3-</b>Girilen karakterlerle eşleşen kurum adı bulunamadığında "Seçenek Bulunamadı" yazısının görüntülendiğini kontrol et.<br><br>
<b>Beklenen sonuç :</b> Filtreleme çubuğu istenildiği gibi çalışmalıdır.Aşağıdaki görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture11.png" alt="picture11"> 

<h4>Test Case 7 : Sıralama çubuğu adına göre sıralama</h4>
<b>Açıklama:</b> ‘’Sıralama Çubuğu’’kullanımı test edilecektir.<br>
<b>Ön Koşul:</b> Sayfada “Sıralama Çubuğu Görüntülenebilir ’’ kullanılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Sıralama çubuğunun üzerine tıkla.<br>
<b>2-</b> Açılır listede sıralama seçeneklerinin bulunduğunu ve farklı seçeneklerle eğitimlerin sıralandığını kontrol et.“Z-A” ya tıkla.<br>
<img src="images/Picture12.png" alt="picture12"> 
<b>3-</b> Filtrelemenin seçime göre geldiğini kontrol et.<br><br>
<b>Beklenen sonuç :</b> Sıralama çubuğunun işlevselliği adına göre istenildiği gibi çalışmalıdır.Görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture13.png" alt="picture13"> 

<h4>Test Case 8 : Sıralama çubuğu tarihe göre sıralama </h4>
<b>Açıklama:</b> ‘’Sıralama Çubuğu’’kullanımı test edilecektir.<br>
<b>Ön Koşul:</b> Sayfada “Sıralama Çubuğu Görüntülenebilir ’’ kullanılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Sıralama çubuğunun üzerine tıkla.<br>
<b>2-</b> Açılır listede sıralama seçeneklerinin bulunduğunu ve farklı seçeneklerle eğitimlerin sıralandığını kontrol et.“Y-E” ye tıkla.<br>
<b>3-</b> Filtrelemenin seçime göre geldiğini kontrol et.<br><br>

<b>Beklenen sonuç :</b> Sıralama çubuğunun tarihe göre sıralama işlevselliği istenildiği gibi çalışmalıdır.Görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture14.png" alt="picture14">
 


<h4>Test Case 9 : "Tüm Eğitimlerim", "Devam Ettiklerim" ve "Tamamladıklarım"</h4>
<b>Açıklama:</b> "Tüm Eğitimlerim", "Devam Ettiklerim" ve "Tamamladıklarım" butonları test edilecektir.<br>
<b>Ön Koşul:</b> Sayfada "Tüm Eğitimlerim", "Devam Ettiklerim" ve "Tamamladıklarım" sekmeleri görünür ve kullanılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>"Tüm Eğitimlerim" butonuna tıkla. <br>
<img src="images/Picture15.png" alt="picture15"> 
<b>2-</b>"Tüm Eğitimlerim" kısmına gittiğini kontrol et.<br>
<b>3-</b>"Devam Ettiklerim" butonuna tıkla. <br>
<img src="images/Picture16.png" alt="picture16"> 
<b>4-</b>"Devam Ettiklerim" kısmına gittiğini kontrol et.<br>
<b>5-</b> "Tamamladıklarım" butonuna tıkla.<br> 
<img src="images/Picture17.png" alt="picture17"> 
<b>6-</b>"Tamamladıklarım"  kısmına gittiğini kontrol et.<br><br>

<b>Beklenen sonuç :</b> Sayfada "Tüm Eğitimlerim", "Devam Ettiklerim" ve "Tamamladıklarım" sekmelerinin işlevselliği başarıyla çalışmalıdır.<br><br>

<h4>Test Case 10 : 'Eğitime Git' Butonu kontrolleri</h4>
<b>Açıklama :</b> Eğitim içeriğinin görüntülenmesi test edilecektir.<br>
<b>Ön Koşullar:</b>  Eğitim sayfasına giriş yapılmış olmalıdır. <br><br>
<b>Adımlar:</b><br>
<b>1-</b>Eğitime git butonuna tıkla.<br>
<img src="images/Picture18.png" alt="picture18"> 
<b>2-</b>Sayfa içeriğini kontrol et.<br><br>

<b>Beklenen Sonuçlar:</b> Eğitim içeriği görseldeki  gibi görüntülenmelidir. <br><br>
<img src="images/Picture19.png" alt="picture19"> 



 



