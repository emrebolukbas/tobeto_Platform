<h1>TEST SENERYOSU 5 :CHATBOT</h1>
<b>Açıklama :</b>  Ana sayfa üzerinde  sağ alt kısımdaki "Chatbot" kısmına tıkladığında chatbot beklenildiği gibi çalışmalıdır.<br>
<b>Ön koşul :</b> ‘’https://tobeto.com’’ url adresinin erişilebilir olması gerekmektedir.<br><br>

<h4>Test Case 1 : Chatbot kontrolü</h4>
<b>Açıklama :</b> Kullanıcı sayfanın sağ alt kısmındaki "Chatbot" kısmına tıkladığında chatbotun görüntülenmesi test edilecektir.<br>
<b>Ön koşul :</b> ‘’https://tobeto.com’’ url adresinin erişilebilir olması gerekmektedir.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>‘’https://tobeto.com’’ url sayfasına git.<br>
<b>2-</b> Sayfanın sağ alt kısmındaki "Chatbot" simgesine tıkla.<br>
<b>3-</b>Chatbot sayfasının açıldığını kontrol et.<br><br>
<b>Beklenen Sonuç :</b> "Chatbot" açılıp sayfanın sağ alt kısmında görüntülenebilir olmalıdır.<br>
<img src="images/Picture1.png" alt="picture1">                                                             
<h4>Test Case 2 : Mesaj Gönderim Bölümü Kontrolü</h4>
<b>Açıklama:</b> Kullanıcının Ad Soyad kısmında metin girişi yapabilmesi ve hazır mesajla yönlendirilmesi  kontrol edilecektir.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>‘’https://tobeto.com’’ url sayfasına git.<br>
<b>2-</b> Sayfanın sağ alt kısmındaki "Chatbot" simgesine tıkla.<br>
<b>3-</b>Chatbot sayfasının açıldığını kontrol et.<br>
<b>4-</b>Ad Soyad kısmına metin girişi yapılabildiğini kontrol et.<br>
İnput: TEST<br>
<img src="images/Picture2.png" alt="picture2">  
<b>5-</b>Ad Soyad girişi yapıldıktan sonra kullanıcının hazır mesajla yönlendirildiğini kontrol et.<br>
<img src="images/Picture3.png" alt="picture3">  
<b>6-</b>Hazır mesajlardan Tobeto Hakkında butonuna tıkla<br>
<b>7-</b>Bir mesaj yazın bölümünde ataç butonuna tıkla<br>
<img src="images/Picture4.png" alt="picture4">  
<b>8-</b>Dosyanın sürükle bırak bölümünün geldiğini kontrol et<br><br>
<img src="images/Picture5.png" alt="picture5">  
<b>Beklenen Sonuç :</b>  Kullanıcı Ad Soyad kısmında metin girişi yapıp  hazır mesaja yönlendirilmelidir.<br><br>

<h4>Test Case 3 : Görüşme Sonlandırma Butonu Kontrolü</h4>
<b>Açıklama:</b> Kullanıcının görüşmeyi sonlandırma butonuna tıkladığında görüşmenin sonlandırılması kontrol edilecektir.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>‘’https://tobeto.com’’ url sayfasına git.<br>
<b>2-</b> Sayfanın sağ alt kısmındaki "Chatbot" simgesine tıkla.<br>
<b>3-</b> Görüşme sonlandırma butonuna tıkla.<br>
<img src="images/Picture6.png" alt="picture6">   
<b>4-</b> Görüşmeyi sonlandırma butonuna tıklandığında “Görüşmeyi bitirmek istediğinize emin misiniz?” mesajının geldiğini kontrol et<br>
<img src="images/Picture7.png" alt="picture7">  
<b>5-</b>Evet butonuna tıkla<br>
<b>6-</b> “Bize puan vermek ister misiniz?” 5 farklı emoji geldiğini kontrol et ve birine tıkla.<br><br>
<img src="images/Picture8.png" alt="picture8">  
<b>Beklenen Sonuç :</b>  Görüşmeyi sonlandırma butonuna tıklandığında 5 farklı butondan biri seçilerek kullanıcı bize puan verip görüşmeyi sonlandırabilmelidir.<br><br>

<h2>PYTEST TEST SONUÇLARI</h2> 
<img src="images/pytest-result.png" alt="pytest-result">