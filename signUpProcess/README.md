<h1>TEST SENERYOSU 3 KAYIT OL İŞLEMİ</h1>
<b>Açıklama :</b> Tobeto eğitim platformuna kullanıcının kayıt olabilmesi kontrol edilecektir.
<b>Ön koşullar :</b> Test ortamı çalışır ve hazır durumda olmalıdır. ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.

<h4>Test Case 1 : Başarılı kayıt olma işlemi.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b></b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b></b>AD gir.<br/>
İnput:test1<br/>
<b>3-</b></b>Soyad gir.<br/>
İnput:test2<br/>
<b>4-</b></b>E-posta gir.<br/>
İnput:12345@test.com<br/>
<b>5-</b>Şifre gir.<br/>
İnput:123456<br/>
<b>6-</b>Şifre tekrar gir.<br/>
İnput:123456<br/>
<b>7-</b>Kayıt ol butonuna tıkla.<br/>
<b>8-</b>Kayıt oluşturmak için gerekli sözleşmeler sayfası ekteki gibi  geldiğini kontrol et.<br/>
<img src="images/Picture1.png" alt="picture1">                              
<b>9-</b> ‘’Kişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.’’ Başlığı altında bulunan ;
Açık Rıza  HYPERLINK "https://tobeto.com/yasal-metinler/acik-riza-metni"Metni’ni okudum ve anladım.*
Üyelik Sözleşmesi ve Kullanım  HYPERLINK "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi"Koşulları’nı okudum ve anladım.*
Checkboxlarını işaretle.<br/>
<b>10-</b>E-posta gönderim izni checkboxını işaretle.<br/>
<b>11-</b>Arama izni checkboxını işaretle.<br/>
<b>12-</b>Altta ki görselde görünen panelin açıldığını kontrol et.<br/>
<img src="images/Picture2.png" alt="picture2">
<b>13-</b>Telefon numarası gir.<br/>
İnput:+90 312 123 45 67<br/>
<b>14-</b>Ben robot değilim checkboxını işaretle.<br/>
<b>15-</b>Devam et butonuna tıkla.<br/><br/>
<b>Beklenen Sonuç :</b> Panele başarılı bir şekilde kayıt yapabilmelidir.Ekte görülen görsel görüntülenmelidir.<br/><br/>
<img src="images/Picture3.png" alt="picture3"> 
<h4>Test Case 2 : Başarısız kayıt olma işlemi şifre en az altı karakter olmalı.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>AD gir, Soyad gir.<br/>
İnput:test1<br/>
<b>3-</b>Soyad gir.<br/>
İnput:test2<br/>
<b>4-</b>E-posta gir.<br/>
İnput:12345@test.com<br/>
<b>5-</b>Şifre gir.<br/>
İnput:123<br/>
<b>6-</b>Şifre tekrar gir.<br/>
İnput:123<br/>
<b>7-</b>Kayıt ol butonuna tıkla.<br/>
<b>8-</b>Kayıt oluşturmak için gerekli sözleşmeler sayfası ekteki gibi  geldiğini kontrol et.<br/>
<img src="images/Picture1.png" alt="picture1">                             
<b>9-</b> ‘’Kişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.’’ Başlığı altında bulunan ;
Açık Rıza  HYPERLINK "https://tobeto.com/yasal-metinler/acik-riza-metni"Metni’ni okudum ve anladım.*
Üyelik Sözleşmesi ve Kullanım  HYPERLINK "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi"Koşulları’nı okudum ve anladım.*
Checkboxlarını işaretle.<br/>
<b>10-</b>E-posta gönderim izni checkboxını işaretle.<br/>
<b>11-</b>Arama izni checkboxını işaretle.<br/>
<b>12-</b>Altta ki görselde görünen panelin açıldığını kontrol et. <br/>
<img src="images/Picture2.png" alt="picture2">
<b>13-</b>Telefon numarası gir.<br/>
İnput:+90 312 123 45 67<br/>
<b>14-</b>Ben robot değilim checkboxını işaretle.<br/>
<b>15-</b>Devam et butonuna tıkla.<br/><br/>
<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture4.png" alt="picture4">                    
                    
<h4>Test Case 3 : Başarısız kayıt olma işlemi çift error hatası.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>AD gir, Soyad gir.<br/>
İnput:test1<br/>
<b>3-</b>Soyad gir.<br/>
İnput:test2<br/>
<b>4-</b>E-posta gir.<br/>
İnput:tobeto@test.com<br/>
<b>5-</b>Şifre gir.<br/>
İnput:123<br/>
<b>6-</b>Şifre tekrar gir.<br/>
İnput:123<br/>
<b>7-</b>Kayıt ol butonuna tıkla.<br/>
<b>8-</b>Kayıt oluşturmak için gerekli sözleşmeler sayfası ekteki gibi  geldiğini kontrol et.<br/>
<img src="images/Picture1.png" alt="picture1">                             
<b>9-</b> ‘’Kişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.’’ Başlığı altında bulunan ;<br/>
Açık Rıza  HYPERLINK "https://tobeto.com/yasal-metinler/acik-riza-metni"Metni’ni okudum ve anladım.*
Üyelik Sözleşmesi ve Kullanım  HYPERLINK "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi"Koşulları’nı okudum ve anladım.*
Checkboxlarını işaretle.<br/>
<b>10-</b>E-posta gönderim izni checkboxını işaretle.<br/>
<b>11-</b>Arama izni checkboxını işaretle.<br/>
<b>12-</b>Altta ki görselde görünen panelin açıldığını kontrol et. <br/>
<img src="images/Picture2.png" alt="picture2">
<b>13-</b>Telefon numarası gir.<br/>
İnput:+90 312 123 45 67<br/>
<b>14-</b>Ben robot değilim checkboxını işaretle.<br/>
<b>15-</b>Devam et butonuna tıkla.<br/><br/>
<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture5.png" alt="picture5">                                       
<h4>Test Case 4 : Başarısız kayıt olma işlemi kayıtlı e-posta adresi.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>AD gir, Soyad gir.<br/>
İnput:test1<br/>
<b>3-</b>Soyad gir.<br/>
İnput:test2<br/>
<b>4-</b>E-posta gir.<br/>
İnput:tobeto@test.com<br/>
<b>5-</b>Şifre gir.<br/>
İnput:123456<br/>
<b>6-</b>Şifre tekrar gir.<br/>
İnput:123456<br/>
<b>7-</b>Kayıt ol butonuna tıkla.<br/>
<b>8-</b>Kayıt oluşturmak için gerekli sözleşmeler sayfası ekteki gibi  geldiğini kontrol et.<br/>
<img src="images/Picture1.png" alt="picture1">                             
<b>9-</b> ‘’Kişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.’’ Başlığı altında bulunan ;
Açık Rıza  HYPERLINK "https://tobeto.com/yasal-metinler/acik-riza-metni"Metni’ni okudum ve anladım.*
Üyelik Sözleşmesi ve Kullanım  HYPERLINK "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi"Koşulları’nı okudum ve anladım.*
Checkboxlarını işaretle.<br/>
<b>10-</b>E-posta gönderim izni checkboxını işaretle.<br/>
<b>11-</b>Arama izni checkboxını işaretle.<br/>
<b>12-</b>Altta ki görselde görünen panelin açıldığını kontrol et. <br/>
<img src="images/Picture2.png" alt="picture2">
<b>13-</b>Telefon numarası gir.<br/>
İnput:+90 312 123 45 67<br/>
<b>14-</b>Ben robot değilim checkboxını işaretle.<br/>
<b>15-</b>Devam et butonuna tıkla.<br/><br/>
<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture6.png" alt="picture6">                                       

<h4>Test Case 5: Başarısız kayıt olma işlemi eşleşmeyen şifre.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>AD gir, Soyad gir.<br/>
İnput:test1<br/>
<b>3-</b>Soyad gir.<br/>
İnput:test2<br/>
<b>4-</b>E-posta gir.<br/>
İnput:tobeto@test.com<br/>
<b>5-</b>Şifre gir.<br/>
İnput:1234566<br/>
<b>6-</b>Şifre tekrar gir.<br/>
İnput:1234567<br/>
<b>7-</b>Kayıt ol butonuna tıkla.<br/>
<b>8-</b>Kayıt oluşturmak için gerekli sözleşmeler sayfası ekteki gibi  geldiğini kontrol et.<br/>
<img src="images/Picture1.png" alt="picture1">                             
<b>9-</b> ‘’Kişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.’’ Başlığı altında bulunan ;
Açık Rıza  HYPERLINK "https://tobeto.com/yasal-metinler/acik-riza-metni"Metni’ni okudum ve anladım.*
Üyelik Sözleşmesi ve Kullanım  HYPERLINK "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi"Koşulları’nı okudum ve anladım.*
Checkboxlarını işaretle.<br/>
<b>10-</b>E-posta gönderim izni checkboxını işaretle.<br/>
<b>11-</b>Arama izni checkboxını işaretle.<br/>
<b>12-</b>Altta ki görselde görünen panelin açıldığını kontrol et. <br/>
<img src="images/Picture2.png" alt="picture2">
<b>13-</b>Telefon numarası gir.<br/>
İnput:+90 312 123 45 67<br/>
<b>14-</b>Ben robot değilim checkboxını işaretle.<br/>
<b>15-</b>Devam et butonuna tıkla.<br/><br/>
<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture7.png" alt="picture7">                                      
                          

<h4>Test Case 6 :Eksik telefon numarası girmesi.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>AD gir, Soyad gir.<br/>
İnput:test1<br/>
<b>3-</b>Soyad gir.<br/>
İnput:test2<br/>
<b>4-</b>E-posta gir.<br/>
İnput:tobeto@test.com<br/>
<b>5-</b>Şifre gir.<br/>
İnput:1234566<br/>
<b>6-</b>Şifre tekrar gir.<br/>
İnput:1234567<br/>
<b>7-</b>Kayıt ol butonuna tıkla.<br/>
<b>8-</b>Kayıt oluşturmak için gerekli sözleşmeler sayfası ekteki gibi  geldiğini kontrol et.<br/>
<img src="images/Picture1.png" alt="picture1">                             
<b>9-</b> ‘’Kişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.’’ Başlığı altında bulunan ;
Açık Rıza  HYPERLINK "https://tobeto.com/yasal-metinler/acik-riza-metni"Metni’ni okudum ve anladım.*
Üyelik Sözleşmesi ve Kullanım  HYPERLINK "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi"Koşulları’nı okudum ve anladım.*
Checkboxlarını işaretle.<br/>
<b>10-</b>E-posta gönderim izni checkboxını işaretle.<br/>
<b>11-</b>Arama izni checkboxını işaretle.<br/>
<b>12-</b>Altta ki görselde görünen panelin açıldığını kontrol et. <br/>
<img src="images/Picture2.png" alt="picture2">
<b>13-</b>Telefon numarası gir.<br/>
İnput:+05 <br/><br/>
 
<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture8.png" alt="picture8">

<h4>Test Case 7 : Geçersiz e-posta adresi.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (E-posta) alanını doldurulup sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.İstenilen bilgilerin doldurulması zorunlu olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>E-posta gir.<br/>
İnput:e<br/><br/>
<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture9.png" alt="picture9">                                      
                 
<h4>Test Case 8: Doldurulması gereken zorunlu alan.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,Şifre,Şifre Tekrar) alanları boş bırakılıp sisteme kayıt olma işlemi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1- </b>Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>AD gir sil.<br/>
İnput: <br/>
<b>3-</b>Soyad gir sil.<br/>
İnput:<br/>
<b>4-</b>E-posta gir.<br/>
İnput:e<br/>
<b>5-</b>Şifre gir sil.<br/>
İnput:<br/>
<b>6-</b>Şifre tekrar gir sil.<br/>
İnput:<br/><br/>

<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
<img src="images/Picture10.png" alt="picture10">                                        

<h4>Test Case 9: E-posta girip silme durumu.</h4>
<b>Açıklama :</b> Kullanıcının istenilen bilgiler doğrultusunda (E-posta) alanı girilip silinmesi test edilecektir.<br/>
<b>Ön koşul :</b> ‘’https://tobeto.com/kayit-ol’’ sayfası erişilebilir olmalıdır.<br/><br/>
<b>Adımlar:</b><br/><br/>
<b>1-</b> Call test ( test senaryosu 1/ Test Case 5 )<br/>
<b>2-</b>E-posta gir.<br/>
İnput:e<br/>
<b>3-</b>E-posta sil.<br/>
İnput:<br/><br/>

<b>Beklenen Sonuç :</b> Ekrana hata mesajı gelmelidir.Ekte bulunan görseldeki gibi olmalıdır.<br/><br/>
 <img src="images/Picture11.png" alt="picture11">                                 

