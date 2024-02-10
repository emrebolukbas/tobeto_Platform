<h1>TEST SENERYOSU 1 GİRİŞ KONTROL </h1>
<b>Açıklama :</b> Tobeto eğitim platformuna kullanıcıların e-posta ve şifre ile sisteme giriş yapabilmesi kontrol edilecektir.<br>
<b>Ön koşullar :</b> Test ortamı çalışır ve hazır durumda olmalıdır. ‘’https://tobeto.com/giris’’ sayfası erişilebilir olmalıdır.<br><br>

<h4>Test Case 1 : Giriş yap alanının görüntülenebilmesi.</h4>
<b>Açıklama :</b> Giriş yap alanı görüntülenebilir ve işlevselliği test edilecektir.<br>
<b>Ön koşul :</b> Giriş yap paneli erişilebilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Giriş yap alanının içerisinde Tobeto amblemi, E-posta alanı, Şifre alanı, "Giriş Yap" butonu, "Şifremi Unuttum" bağlantısı, "Henüz Üye Değil misin? Kayıt Ol" bağlantısı alanlarını kontrol et. <br><br>
<b>Beklenen Sonuç :</b> Giriş yap alanı görseldeki gibi olmalıdır .<br><br>
<img src="images/Picture1.png" alt="picture1">                        

<h4>Test Case 2 : Başarılı panel girişi.</h4>
<b>Açıklama :</b> Kullanıcının sistemde kayıtlı e-posta ve şifre bilgileriyle  giriş yapabilmesi test edilecektir.<br>
<b>Ön koşul :</b> Kullanıcının giriş yaptığı e-posta ve şifre sisteme kayıtlı olmalıdır .<br><br>
<b>Adımlar:</b><br>
<b>1-</b> E-posta adresi gir.<br>
İnput: basarili@test.com<br>
<b>2-</b>Şifre gir.<br>
İnput: basarilisifre<br>
<b>3-</b>Giriş yap butonuna tıkla<br><br>
<b>Beklenen Sonuç :</b> Panele giriş yapılmış ve sistem tarafından görseldeki gibi bildirme mesajı gelmelidir.<br><br>
<img src="images/Picture2.png" alt="picture2">
<h4>Test Case 3 : Boş bilgi girişi.</h4>
<b>Açıklama :</b> Kullanıcının e-posta veya şifre bilgilerini boş girerek sisteme giriş yapabilmesi test edilecektir.<br>
<b>Ön koşul :</b> E-posta veya şifre boş bırakılmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>E-posta adresi gir.<br>
      1.1- E-posta adresi gir.<br>
      İnput: test@test.com<br>
      1.2- E-posta adresini boş bırak.<br>
      İnput: <br>
      1.3-E-posta adresini boş bırak.<br>
      İnput:<br>
<b>2-</b>Şifre gir.<br>
     2.1-Şifre alanını boş bırak.<br>
     İnput: <br>
     2.2-test123<br>
     İnput:sifretest<br>
     2.3-Şifre alanını boş bırak.<br>
       İnput:<br>
<b>3-</b>Giriş yap butonuna tıkla<br><br>
<b>Beklenen Sonuç :</b> E-posta veya şifre alanları boş bırakıldığında alanların alt kısmında görseldeki hata mesajlarını vermelidir.<br><br>
<img src="images/Picture3.png" alt="picture3">                                 
 
                    
<h4>Test Case 4 : Başarısız panel girişi.</h4>
<b>Açıklama :</b> Kullanıcının e-posta ve şifre bilgilerini yanlış girerek sisteme giriş yapması  test edilecektir.<br>
<b>Ön koşul :</b> E-posta veya şifre eksik yada geçersiz olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b>E-posta adresi gir.<br>
      1.1- Geçersiz e-posta adresi gir.<br>
      İnput: basarisiz@test.com<br>
      1.2- Geçerli e-posta adresi gir.<br>
      İnput: basarili@test.com<br>
<b>2-</b>Şifre gir.<br>
     2.1-Geçerli bir şifre gir.<br>
     İnput: basarilisifre<br>
     2.2-Geçersiz bir şifre gir.<br>
     İnput:basarisizsifre<br>
<b>3-</b>Giriş yap butonuna tıkla<br><br>
<b>Beklenen Sonuç :</b>  Sistemde kayıtlı olmayan yada geçersiz e-posta veya şifre girildiğinde  görseldeki hata mesajlarını vermelidir.<br><br>
<img src="images/Picture4.png" alt="picture4">                  


                    
<h4>Test Case 5 : Giriş yap sayfası içerisindeki butonların işlevselliği .</h4>
<b>Açıklama :</b> Kullanıcının giriş yap sayfasındaki butonların işlevselliği test edilecektir.<br>
<b>Ön koşul :</b> Giriş yap sayfası görüntülenebilir ve butonlar tıklanabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> E-posta ve Şifre inputlarının işlevselliğini kontrol et.  <br>
<b>2-</b>Giriş yap butonunun işlevselliğini kontrol et.<br>
<b>3-</b>Şifremi unuttum bağlantısı,’’Henüz üye değilmisiniz?Kayıt ol’’ bağlantılarının işlevselliğini kontrol et.<br><br>

<b>Beklenen Sonuç :</b>  İnput,buton ve bağlantı alanları tıklanabilir olmalıdır.<br><br>

<h2>PYTEST TEST SONUÇLARI</h2> 
<img src="images/pytest-result.png" alt="pytest-result">