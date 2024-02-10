<h1>TEST SENERYOSU 9 : DUYURU HABERLERİM VE ANKETLERİM SAYFASININ KONTROLÜ</h1>
<b>Açıklama :</b> Duyuru ve Haberlerim butonu ile birlikte duyurularım sayfasının adının bulunduğu görsel, arama çubuğu ,tür filtreleme, organizasyon filtreleme ve sıralama çubukları kontrol edilecektir.<br>
<b>Ön koşullar :</b> Test ortamı çalışır ve hazır durumda olmalıdır. ‘’ https://tobeto.com/platform’’ sayfası erişilebilir olmalıdır.<br><br>

<h4>Test case 1: “Duyuru ve Haberlerim” Butonu Kontrolü</h4>
<b>Açıklama:</b>Kullanıcının duyuru ve haberlerini takip edeceği panel test edilecektir.<br>
<b>Ön Koşul:</b>Kullanıcı başarılı bir şekilde sisteme giriş yapmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve Haberlerim başlığını tıkla.<br>
<b>3-</b>Aşağıdaki görseldeki gibi max 3 adet duyuru gösterildiğini kontrol et.<br>
<img src="images/Picture1.png" alt="picture1">  
<b>4-</b>”Devamını Oku”  tıkla.<br>
<img src="images/Picture2.png" alt="picture2">   
<b>5-</b>Açılan Duyuru X butonuna tıkla.<br><br>
<img src="images/Picture3.png" alt="picture3">
<b>Beklenen Sonuç:</b> Duyuru kapanmalıdır.<br><br>
<h4>Test case 2:”Daha Fazla Göster “ butonun kontrolü</h4>
<b>Açıklama:</b> “Daha Fazla Göster “ butonuna basarak yeni pencerenin açılması durumu test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/platform hazır çalışır durumda olması gerekir.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi<br>
<b>2-</b>“Daha Fazla Göster” butonuna tıkla<br><br>
<img src="images/Picture4.png" alt="picture4"> 
<b>Beklenen Sonuç:</b> “Daha Fazla Göster” butonuna basarak yeni pencere açılır.<br><br>
<img src="images/Picture5.png" alt="picture5"> 

<h4>Test case 3: “Arama” Butonun Kontrolü</h4>
<b>Açıklama:</b> Arama çubuğunda aratılan kritere uygun duyuru bulunması test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/duyurular sayfası hazır ve çalışır olması gerekir.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve haberlerim butonuna tıkla<br>
<b>3-</b>“Daha fazla göster” butonuna tıkla<br>
<b>4-</b>Arama butonuna input gir.<br>
input:Önemli<br><br> 
<img src="images/Picture6.png" alt="picture6"> 
<b>Beklenen Sonuç:</b> Görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture7.png" alt="picture7"> 

<h4>Test case 4: Arama filtresinde “Bir Duyuru Bulunmamaktadır” Butonun Kontrolü</h4>
<b>Açıklama:</b> Arama çubuğunda aratılan kritere uygun duyuru bulunmaması test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/duyurular sayfası hazır ve çalışır olması gerekir.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve haberlerim butonuna tıkla<br>
<b>3-</b>“Daha fazla göster” butonuna tıkla<br>
<b>4-</b>Arama butonuna input gir.<br>
<b>input:Sınav</b><br><br>
<img src="images/Picture8.png" alt="picture8"> 
<b>Beklenen sonuç:</b> “Bir duyuru bulunmamaktadır”yazısı gelir.<br><br>
<img src="images/Picture9.png" alt="picture9"> 
<h4>Test case 5:”Tür” Başlığının Kontrolü</h4>
<b>Açıklama:</b>Kullanıcının “tür” filtrelemesini kullanarak “Haber” ve “Duyuru” başlıkları test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/duyurular sayfası hazır olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve haberlerim butonuna tıkla<br>
<b>3-</b>daha fazla göster butonuna tıkla<br>
<b>4-</b>tür filtresine tıkla<br><br>
<img src="images/Picture10.png" alt="picture10"> 
<b>Beklenen Sonuç:</b>Aşağıdaki görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture11.png" alt="picture11"> 

<h4>Test case 6:”Organizasyon” Başlığının Kontrolü</h4>
<b>Açıklama:</b>Kullanıcının “Organizasyon” filtreleme çubuğunun organizasyonları filtrelemesi test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/duyurular sayfası hazır olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve haberlerim butonuna tıkla<br>
<b>3-</b>“Daha fazla göster” butonuna tıkla<br>
<b>4-</b>“Organizasyon”Filtreleme çubuğunu göster.<br><br>
<img src="images/Picture12.png" alt="picture12"> 
<b>Beklenen Sonuç:</b>Görseldeki gibi gelmelidir.<br><br>
<img src="images/Picture13.png" alt="picture13">

<h4>Test case 7:Organizasyon filtresinde ”Seçenek Bulunamadı”Başlığının Kontrolü</h4>
<b>Açıklama:</b>Kullanıcının “Organizasyon” filtreleme çubuğunun organizasyonları filtrelemesi test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/duyurular sayfası hazır olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve haberlerim butonuna tıkla<br>
<b>3-</b>“Daha fazla göster” butonuna tıkla<br>
<b>4-</b>“Organizasyon “filtre çubuğunu göster<br>
<img src="images/Picture14.png" alt="picture14"> 
<b>5-</b>input gir<br><br>
<img src="images/Picture15.png" alt="picture15"> 
<b>Beklenen Sonuç:</b> Girilen karakterlerle eşleşen organizasyon bulunmadığında aşağıdaki görseldeki gibi “Seçenek Bulunamadı” yazısı gelmelidir.<br><br>
<img src="images/Picture16.png" alt="picture16">
<h4>Test case 8:”Sıralama” Başlığının Kontrolü</h4>
<b>Açıklama:</b> Kullanıcının “Sıralama” filtreleme çubuğunun açılır kapanır listede “Tarihe Göre(Y-E)” ve “Tarihe Göre (E-Y) seçenekleri test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/duyurular sayfası hazır olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>Call test(test senaryosu: Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b>Duyuru ve haberlerim butonuna tıkla<br>
<b>3-</b>“Daha fazla göster” butonuna tıkla<br>
<b>4-</b>“Sıralama” butonunu göster.<br>
<img src="images/Picture17.png" alt="picture17"> 
<b>5-</b>“Tarihe Göre(Y-E)” göre sırala.<br>
<img src="images/Picture18.png" alt="picture18">
<b>6-</b>“Tarihe Göre (E-Y)” göre sırala.<br><br>
<img src="images/Picture19.png" alt="picture19"> 
<b>Beklenen Sonuç:</b> Duyurular filtrelemeye göre sıralanmalıdır.<br><br>

<h4>Test Case 9: Anketlerim kontrolü</h4>
<b>Açıklama:</b> Anketlerim butonuna tıklayarak kendisine atanmamış anket durumu test edilecektir.<br>
<b>Ön Koşul:</b> https://tobeto.com/platform hazır çalışır durumda olması gerekir.<br><br>
<b>Adımlar</b>:<br>
<b>1-</b>Call test(test senaryosu:Giriş kontrol/ test case1:Başarılı panel girişi)<br>
<b>2-</b> Anketlerim” başlığını tıkla.<br><br>
<b>Beklenen Sonuç:</b>Kullanıcı kendisine anket tanımlanmadığında aşağıdaki görseldeki gibi bir mesajı alacaktır.<br><br>
<img src="images/Picture20.png" alt="picture20">

<h2>PYTEST TEST SONUÇLARI</h2> 
<img src="images/pytest-result.png" alt="pytest-result">

 

