<h1>TEST SENERYOSU: İLETİŞİM FORMU</h1>
<b>Açıklama :</b> Tobeto eğitim platformuna kullanıcıların e-posta ve şifre ile sisteme giriş yapmış olduğu platform üzerinde ‘’Bize Ulaşın’’ paneli kontrol edilecektir.<br>
<b>Ön koşullar :</b> Kullanıcı panale başarılı bir şekilde giriş yapmış olmalıdır. <br><br>

<h4>Test Case 1: Bize ulaşın butonu</h4>
<b>Açıklama :</b> “Bize Ulaşın’’ sekmesi görüntülenmesi test edilecektir.<br>
<b>Ön koşul :</b> Kullanıcı sistemde oturum açmış olmalıdır. Sayfada “Bize Ulaşın’’ butonu tıklanabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Ana sayfa üzerinde en alta in.<br>
<b>2-</b> 'Bize Ulaşın' butonuna tıkla.  <br>
<img src="images/Picture1.png" alt="picture1"><br><br>
<b>Beklenen sonuç:</b> 'İletişim' paneline yönlendirilmelidir.<br>

<h4>Test Case 2:İletişim formunun görüntülenmesi</h4>
<b>Açıklama :</b> “İletişim’’ paneli görüntülenmesi test edilecektir.<br>
<b>Ön koşul :</b> Kullanıcı sistemde oturum açmış olmalıdır. . “Bize Ulaşın’’ butonu tıklanabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Bize ulaşın butonuna tıkla.<br>
<b>2-</b> 'İletişim' panelinin görüntülendiğini ve sayfasının içeriğini kontrol et.<br><br>
<b>Beklenen sonuç:</b> 'İletişim' paneli görüntülenmelidir.Aşağıda görseli verilmiştir.<br><br>
<img src="images/Picture2.png" alt="picture2"> 

<h4>Test Case 3:İletişim formu başarılı</h4>
<b>Açıklama :</b> “İletişim Formu’’ panelde görüntülenebilir ve tıklanabilir olmalıdır.<br>
<b>Ön koşul :</b> Kullanıcı sistemde oturum açmış olmalıdır. İletişim paneli açık olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Bize ulaşın butonuna tıkla.<br>
<b>2-</b> 'İletişim Formu' panelinin görüntülendiğini ve tıklanabilirliğini kontrol et.<br>
<b>3-</b> 'Adınız Soyadınız' alanına isim ve soyisim gir.<br>
İnput : Tobeto<br>
<b>4-</b> 'E-Mail' alanına bir mail adresi gir.<br>
İnput : tobeto@test.com<br>
<b>5</b>-Mesaj kutusuna bir veri gir.<br>
İnput:Merhaba tobeto<br>
<b>6-</b>Gönder butonuna tıkla.<br>
<b>7-</b>“İletişim formu başarıyla gönderilmiştir.”uyarısı geldiğini kontrol et.<br><br>

<b>Beklenen sonuç:</b> 'İletişim Formu' istenildiği gibi çalışmalıdır.Ekrana iletişim formu başarıyla gönderilmiştir yazısı gelmelidir aşağıda görseli verilmiştir.<br><br>
<img src="images/Picture3.png" alt="picture3">
 
<h4>Test Case 4: İletişim formu başarısız</h4>

<b>Açıklama :</b> “İletişim Formu’’ panelde görüntülenebilir ve tıklanabilir olmalıdır.Yanlış bilgilerle test et.<br>
<b>Ön koşul :</b> Kullanıcı sistemde oturum açmış olmalıdır. Sayfada “Bize Ulaşın’’ butonu tıklanabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Bize ulaşın butonuna tıkla.<br>
<b>2-</b> 'İletişim Formu' panelinin görüntülendiğini ve tıklanabilirliğini kontrol et.<br>
<b>3-</b> 'Adınız Soyadınız' alanına geçersiz isim ve soyisim gir.<br>
İnput : geçersizisim<br>
<b>4-</b> 'E-Mail' alanına geçersiz bir mail adresi gir.<br>
İnput : tobeto@tobeto<br>
<b>5-</b>Mesaj kutusuna bir veri gir.<br>
İnput:geçersiz mesaj<br>
<b>6-</b>Gönder butonuna tıkla.<br>
<b>7-</b>“Mesaj gönderilemedi...”uyarısı geldiğini kontrol et.<br><br>

<b>Beklenen sonuç:</b> 'İletişim Formu' istenildiği gibi çalışmamalıdır bize bir mesaj gönderilemedi uyarısı vermelidir.Aşağıda görseli verilmiştir.<br><br>
<img src="images/Picture4.png" alt="picture4"> 

<h4>Test Case 5:İletişim formu boş bırak</h4>

<b>Açıklama :</b> “İletişim Formu’’ panelde görüntülenebilir ve tıklanabilir olmalıdır.Doldurulacak alanları boş bırakıp test edilecektir.<br>
<b>Ön koşul :</b> Kullanıcı sistemde oturum açmış olmalıdır. Sayfada “Bize Ulaşın’’ butonu tıklanabilir olmalıdır.<br>
<b>Adımlar:</b><br>
<b>1-</b> Bize ulaşın butonuna tıkla.<br>
<b>2-</b> 'İletişim Formu' panelinin görüntülendiğini ve tıklanabilirliğini kontrol et.<br>
<b>3-</b> 'Adınız Soyadınız' alanına isim ve soyisim gir.<br>
İnput : <br>
<img src="images/Picture5.png" alt="picture5"> <br>
<b>4-</b> 'E-Mail' alanına bir mail adresi gir.<br>
İnput : <br>
<img src="images/Picture6.png" alt="picture6"><br> 
<b>5-</b>Mesaj kutusuna bir veri gir.<br>
İnput:<br>
<img src="images/Picture7.png" alt="picture7"><br> 
<b>6-</b>Gönder butonuna tıkla.<br>
<b>7-</b>“Doldurulması zorunlu alan*”uyarısı geldiğini kontrol et.<br><br>
<b>Beklenen sonuç:</b> 'İletişim Formu'da alanlar boş bırakıldığında  bize doldurulması zorunlu alan  uyarısı vermelidir.Aşağıda görseli verilmiştir.<br><br>
<img src="images/Picture8.png" alt="picture8"><br>
 









