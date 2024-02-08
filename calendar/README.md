<h1>TEST SENERYOSU 6 TAKVİM KISMININ KONTROLÜ</h1>
<b>Açıklama :</b> “Takvim” sayfası , “Eğitim arama”,”Eğitmen”,”Eğitim Durumu”,başlıklarına sahip eğitim filtreleri alanından , “Bugün” butonu ,yön butonları ,
“Ay”, “Hafta”,”Gün” filtreleme butonlarına sahip zaman filtreleri alanından ve bu zaman filtrelerine göre değişen başlıkların kontrol edilecektir.<br>
<b>Ön koşullar :</b> Test ortamı çalışır ve hazır durumda olmalıdır. “https://tobeto.com/platform’’ sayfası erişilebilir olmalıdır.<br><br>

<h4>Test Case 1: Takvimine  Butonuna Erişim</h4>
<b>Açıklama:</b> sayfanın üst kısmındaki takvim butonuna tıklayarak “Takvim" sayfasına erişebilmesi ve sayfanın açılması test edilecektir.<br>
<b>Ön koşul:</b> ‘’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Takvim butonunu tıkla<br><br>
<img src="images/Picture.png" alt="picture">   
<b>Beklenen Sonuç:</b> Takvim butonuna tıklanıldığında aşağıdaki sayfa açılmalıdır.<br><br>
<img src="images/Picture1.png" alt="picture1">   
<h4>Test Case 2: “Eğitim Arama “butonun  test edilmesi</h4>
<b>Açıklama:</b> “Eğitim arama” filtresinden “eğitimi arayın “başlığının  doldurulması ve eğitime uygun tarih ve saat gösterilmesi test edilecektir.<br>
<b>Ön koşul:</b> ’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır. Takvim  penceresi açılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Takvim butonunu tıkla<br>
<b>3-</b>“Eğitim arama” butonunu göster<br>
<img src="images/Picture2.png" alt="picture2">   
<b>4-</b>input gir:test<br><br>
<img src="images/Picture3.png" alt="picture3">   
<b>Beklenen sonuç:</b> Girilen değere göre başarılı bir şekilde filtrelenmelidir.Takvim ve saat görüntülenmelidir.<br><br>
<img src="images/Picture4.png" alt="picture4">   

<h4>Test Case 3: “Bugün“ butonun kontrol edilmesi</h4>
<b>Açıklama:</b> ‘Bugün’ butonuna tıklandığında takvim üzerinde, güncel günü belirtmesi test edilecektir.<br>
<b>Ön koşul:</b> ’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır. Takvim  penceresi açılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Call test(takvim test senaryosu1/test case1)<br><br>
<b>Beklenen Sonuç:</b>Görseldeki gibi olmalıdır.<br><br>
<img src="images/Picture5.png" alt="picture5">   
<h4>Test Case 4: “Yön“ butonun kontrol edilmesi</h4>
<b>Açıklama:</b>  yön oklarını kullanarak gelecek ve geçmiş eğitim takvimini görüntülenmesi test edilecektir.<br>
<b>Ön koşul:</b> ’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır. Takvim  penceresi açılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Call test(takvim test senaryosu1/test case1)<br>
<b>3-</b>Yön okları tıkla<br><br>
<img src="images/Picture6.png" alt="picture6">   
<b>Beklenen Sonuç:</b>  yön oklarını kullanarak gelecek ve geçmiş eğitim takvimini görüntüleyebilmelidir.<br><br>
<img src="images/Picture7.png" alt="picture7">   
<img src="images/Picture8.png" alt="picture8">  
 
<h4>Test Case 5: “Ay“ butonun kontrol edilmesi</h4>
<b>Açıklama:</b> ‘Ay’ butonuna tıklandığında takvim üzerinde, güncel “ay”belirtmesi test edilecektir.<br>
<b>Ön koşul:</b> ’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır. Takvim  penceresi açılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Call test(takvim test senaryosu1/test case1)<br>
<b>3-</b>Ay butonuna tıkla<br><br>
<img src="images/Picture9.png" alt="picture9">   
<b>Beklenen Sonuç:</b>Ay butonuna tıklanıldığında takvim görseldeki gibi olur.<br><br>
<img src="images/Picture10.png" alt="picture10">   

<h4>Test Case 6: “Hafta“ butonun kontrol edilmesi</h4>
<b>Açıklama:</b> ‘Gün’ butonuna tıklandığında takvim üzerinde, güncel “hafta”belirtmesi test edilecektir.<br>
<b>Ön koşul:</b> ’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır. Takvim  penceresi açılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1- </b>Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Call test(takvim test senaryosu1/test case1)<br>
<b>3-</b>Hafta butonuna tıkla<br><br>
<img src="images/Picture11.png" alt="picture11">   
<b>Beklenen Sonuç: </b>Hafta butonuna tıklanıldığında takvim görseldeki gibi olur.<br><br>
<img src="images/Picture12.png" alt="picture12">   
<h4>Test Case 7: “Gün“ butonun kontrol edilmesi</h4>
<b>Açıklama:</b> ‘Gün’ butonuna tıklandığında takvim üzerinde, güncel “gün”belirtmesi test edilecektir.<br>
<b>Ön koşul:</b> ’ https://tobeto.com/takvim ’’ sayfası erişilebilir olmalıdır. Takvim  penceresi açılabilir olmalıdır.<br><br>
<b>Adımlar:</b><br>
<b>1-</b> Call test(test senaryosu1/ test case1)<br>
<b>2-</b>Call test(takvim test senaryosu1/test case1)<br>
<b>3-</b>Gün butonuna tıkla<br><br>
<img src="images/Picture13.png" alt="picture13">   
<b>Beklenen Sonuç:</b>Gün butonuna tıklanıldığında takvim görseldeki gibi olur.<br>
<img src="images/Picture14.png" alt="picture14">  
 


