print("""
Abone tipi kodu
1:konut
2:İşyeri
3:Resmi Daire
4:Organize Sanayi 
5:İlçe Tarımsal ve Hayvan Sulama
""")
kademe1=13
kademe2=7
kademe3=20
abone_tipi_adı=""
Dönemlik_su_tüketim_miktarı=0
Dönemlik_su_tüketim_ücreti=0
Dönemlik_atık_su_ücreti=0
Dönemli_toplam_su_tüketim_ve_atık_su_ücreti=0
Dönemlik_ÇTV_tutarı=0
Dönemlik_katı_atık_toplama_ücreti=0
Dönemlik_katı_atık_bertaraf_ücreti=0
Dönemlik_toplam_fatura_tutarı=0
Dönemlik_devlete_aktarılacak_KDV_tutarı=0
Dönemlik_ilçe_belediyesine_aktarılacak_tutar=0
Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar=0
Dönemlik_İZSU_payı=0
toplam_su_tüketim_miktarı=0
konut_su_tüketim_miktarı=0
işyeri_su_tüketim_miktarı=0
resmidaire_su_tüketim_miktarı=0
organizesanayi_su_tüketim_miktarı=0
İlçeTarımsal_su_tüketim_miktarı=0
konutların_aylık_toplam_su_tüketim_miktarı=0
konut_aylık_ort_su_tüketim_miktarı=0
konut_toplam_hane_sayıları=0
işyeri_aylık_su_tüketim_miktarı=0
işyerinin_aylık_toplam_su_tüketim_miktarı=0
işyeri_sayısı=0
resmidaire_aylık_su_tüketim_miktarı=0
resmidaire_aylık_toplam_su_tüketim_miktarı=0
resmidaire_sayısı=0
organizesanayi_aylık_su_tüketim_miktarı=0
organizesanayi_aylık_toplam_su_tüketim_miktarı=0
organizesanayi_sayısı=0
İlçeTarımsal_aylık_su_tüketim_miktarı=0
İlçeTarımsal_aylık_toplam_su_tüketim_miktarı=0
İlçeTarımsal_sayısı=0
kademe1_hane_sayısı=0
kademe2_hane_sayısı=0
kademe3_hane_sayısı=0
kademe1_su_tüketim=0
kademe2_su_tüketim=0
kademe3_su_tüketim=0
kademe1_aylık_su_tüketim=0
kademe1_aylık_toplam_su_tüketim=0
kademe2_aylık_su_tüketim=0
kademe2_aylık_toplam_su_tüketim=0
kademe3_aylık_su_tüketim=0
kademe3_aylık_toplam_su_tüketim=0
godoman=0
konut_godoman=0
şehitgazispor=0
engellli=0
resmi_daire_liste=[]
resmi_daire_abone_no=[]
resmi_daire_aylık_tüketim_miktarı=[]
genel_ücret_liste=[]
genel_ücret_abone_no=[]
genel_ücret_abone_tipi=[]
genel_ücret_aylıktüketim_miktarı=[]
bornova_toplam_su_tüketim_miktarı=0
bornova_toplam_su_tüketim_ücreti=0
konut_dönemlik_su_tüketim_ücreti=0
işyeri_dönemlik_su_tüketim_ücreti=0
resmi_dönemlik_su_tüketim_ücreti=0
organize_dönemlik_su_tüketim_ücreti=0
ilçe_dönemlik_su_tüketim_ücreti=0
izsu_toplam=0
ilçebelediye_toplam=0
büyükşehirbelediye_toplam=0
belediye_toplam=0

while True:
    while True:
        abone_no=input("abone no:")
        basamak=len(abone_no)
        if basamak==7:
            break
        print("eksik abone no girdiniz lütfen tekrar deneyiniz")
    while True:
        abone_tipi=int(input("abone tipi kodu:"))
        if 0<abone_tipi<6:
            break
        print("yanlış kodlama girdiniz")
    while True:
        önceki_sayaç=float(input("önceki sayaç değeri:"))
        şimdiki_sayaç=float(input("şimdiki sayaç değeri:"))
        if önceki_sayaç<0 or şimdiki_sayaç<0:
            print("sayaç değerleri 0 dan küçük olamaz ")
            continue
        önceki_şimdiki_sayaçlar_arası_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısı:"))
        if önceki_şimdiki_sayaçlar_arası_gün_sayısı<0:
            print("sayaçlar arasındaki gün sayısı 0 dan küçük olmaz")
            continue
        if şimdiki_sayaç>=önceki_sayaç:
            Dönemlik_su_tüketim_miktarı = şimdiki_sayaç - önceki_sayaç
            toplam_su_tüketim_miktarı += Dönemlik_su_tüketim_miktarı
            ölçek=önceki_şimdiki_sayaçlar_arası_gün_sayısı/30
            break
        print("önceki sayaç değeri şimdiki sayaç değerinden büyük olamaz")
    if abone_tipi==1:
        abone_tipi_adı="Konut"
        hane_sayısı=int(input("hane sayısı:"))
        konut_toplam_hane_sayıları += hane_sayısı
        hane_ortalaması = Dönemlik_su_tüketim_miktarı / hane_sayısı
        konut_su_tüketim_miktarı += Dönemlik_su_tüketim_miktarı  # konut için toplam su tüketim miktarı
        konut_aylık_su_tüketim_miktarı = (Dönemlik_su_tüketim_miktarı / önceki_şimdiki_sayaçlar_arası_gün_sayısı) * 30
        konut_aylık_su_tüketim_miktarı2 = hane_ortalaması/önceki_şimdiki_sayaçlar_arası_gün_sayısı*30    #konut sayısı 1den falza ise kullanılacak denklem
        konutların_aylık_toplam_su_tüketim_miktarı += konut_aylık_su_tüketim_miktarı
        if hane_sayısı==1:
            while True:
                indirim_durumu=input("indirim durumu giriniz Yok/Şehit/Gazi/Sporcu/Engelli (Y/Ş/G/S/E karakterleri)").upper()
                if indirim_durumu=="Ş" or indirim_durumu=="G" or indirim_durumu=="S":
                    if Dönemlik_su_tüketim_miktarı<kademe1*ölçek:
                        Dönemlik_su_tüketim_ücreti=(Dönemlik_su_tüketim_miktarı*2.89)*5/10
                        Dönemlik_atık_su_ücreti=(Dönemlik_su_tüketim_miktarı*1.44)*5/10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı=Dönemlik_su_tüketim_miktarı*0.39
                        Dönemlik_katı_atık_toplama_ücreti=hane_sayısı*13
                        Dönemlik_katı_atık_bertaraf_ücreti=hane_sayısı*2.54
                        Dönemlik_toplam_fatura_tutarı=Dönemli_toplam_su_tüketim_ve_atık_su_ücreti+Dönemlik_ÇTV_tutarı+Dönemlik_katı_atık_toplama_ücreti+Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı=(Dönemlik_toplam_fatura_tutarı-Dönemlik_ÇTV_tutarı)*8/100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar=Dönemlik_ÇTV_tutarı+Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar=Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı=Dönemlik_toplam_fatura_tutarı-(Dönemlik_devlete_aktarılacak_KDV_tutarı+Dönemlik_ilçe_belediyesine_aktarılacak_tutar+Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe1_hane_sayısı+=1
                        kademe1_su_tüketim+=Dönemlik_su_tüketim_miktarı
                        kademe1_aylık_su_tüketim=kademe1_su_tüketim/önceki_şimdiki_sayaçlar_arası_gün_sayısı*30
                        kademe1_aylık_toplam_su_tüketim+=kademe1_aylık_su_tüketim
                        şehitgazispor+=1
                        konut_dönemlik_su_tüketim_ücreti+=Dönemlik_su_tüketim_ücreti
                        izsu_toplam+=Dönemlik_İZSU_payı
                        ilçebelediye_toplam+=Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam+=Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam+=Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif kademe1*ölçek<Dönemlik_su_tüketim_miktarı<kademe3*ölçek:
                        Dönemlik_su_tüketim_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe1*ölçek)*3.13)+((kademe1*ölçek)*2.89))*5/10
                        Dönemlik_atık_su_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe1*ölçek)*1.56)+((kademe1*ölçek)*1.44))*5/10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe2_hane_sayısı+=1
                        kademe2_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe2_aylık_su_tüketim = kademe2_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe2_aylık_toplam_su_tüketim += kademe2_aylık_su_tüketim
                        şehitgazispor += 1
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif Dönemlik_su_tüketim_miktarı>kademe3*ölçek:
                        Dönemlik_su_tüketim_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe3*ölçek)*6.43)+((kademe2*ölçek)*3.13)+((kademe1*ölçek)*2.89))*5/10
                        Dönemlik_atık_su_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe3*ölçek)*3.22)+((kademe2*ölçek)*1.56)+((kademe1*ölçek)*1.44))*5/10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı =(Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe3_hane_sayısı+=1
                        kademe3_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe3_aylık_su_tüketim = kademe3_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe3_aylık_toplam_su_tüketim += kademe3_aylık_su_tüketim
                        şehitgazispor += 1
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    break
                elif indirim_durumu=="E":
                    if Dönemlik_su_tüketim_miktarı<kademe1*ölçek:
                        Dönemlik_su_tüketim_ücreti=(Dönemlik_su_tüketim_miktarı*2.89)*5/10
                        Dönemlik_atık_su_ücreti=(Dönemlik_su_tüketim_miktarı*1.44)*5/10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe1_hane_sayısı+=1
                        kademe1_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe1_aylık_su_tüketim = kademe1_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe1_aylık_toplam_su_tüketim += kademe1_aylık_su_tüketim
                        engellli+=1
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif kademe1*ölçek<Dönemlik_su_tüketim_miktarı<kademe3*ölçek:
                        Dönemlik_su_tüketim_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe1*ölçek)*3.13)+((kademe1*ölçek)*2.89))*5/10
                        Dönemlik_atık_su_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe1*ölçek)*1.56)+((kademe1*ölçek)*1.44))*5/10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = ( Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe2_hane_sayısı+=1
                        kademe2_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe2_aylık_su_tüketim = kademe2_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe2_aylık_toplam_su_tüketim += kademe2_aylık_su_tüketim
                        engellli += 1
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif Dönemlik_su_tüketim_miktarı>kademe3*ölçek:
                        Dönemlik_su_tüketim_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe3*ölçek)*6.43)+((kademe2*ölçek)*3.13)+((kademe1*ölçek)*2.89))
                        Dönemlik_atık_su_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe3*ölçek)*3.22)+((kademe2*ölçek)*1.56)+((kademe1*ölçek)*1.44))
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe3_hane_sayısı+=1
                        kademe3_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe3_aylık_su_tüketim = kademe3_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe3_aylık_toplam_su_tüketim += kademe3_aylık_su_tüketim
                        engellli += 1
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    break
                elif indirim_durumu=="Y":
                    if Dönemlik_su_tüketim_miktarı<kademe1*ölçek:
                        Dönemlik_su_tüketim_ücreti=(Dönemlik_su_tüketim_miktarı*2.89)
                        Dönemlik_atık_su_ücreti=(Dönemlik_su_tüketim_miktarı*1.44)
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe1_hane_sayısı+=1
                        kademe1_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe1_aylık_su_tüketim = kademe1_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe1_aylık_toplam_su_tüketim += kademe1_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif kademe1*ölçek<Dönemlik_su_tüketim_miktarı<kademe3*ölçek:
                        Dönemlik_su_tüketim_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe1*ölçek)*3.13)+((kademe1*ölçek)*2.89))
                        Dönemlik_atık_su_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe1*ölçek)*1.56)+((kademe1*ölçek)*1.44))
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe2_hane_sayısı+=1
                        kademe2_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe2_aylık_su_tüketim = kademe2_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe2_aylık_toplam_su_tüketim += kademe2_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif Dönemlik_su_tüketim_miktarı>kademe3*ölçek:
                        Dönemlik_su_tüketim_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe3*ölçek)*6.43)+((kademe2*ölçek)*3.13)+((kademe1*ölçek)*2.89))
                        Dönemlik_atık_su_ücreti=(((Dönemlik_su_tüketim_miktarı-kademe3*ölçek)*3.22)+((kademe2*ölçek)*1.56)+((kademe1*ölçek)*1.44))
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe3_hane_sayısı+=1
                        kademe3_su_tüketim += Dönemlik_su_tüketim_miktarı
                        kademe3_aylık_su_tüketim = kademe3_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe3_aylık_toplam_su_tüketim += kademe3_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    break
                else:
                    print("hatalı kodlama girdiniz")
        if hane_sayısı>1:
            while True:
                şehit_gazi_spor=int(input("şehit,gazi veya sporcu sayısı:"))
                engelli=int(input("engelli sayısı:"))
                toplam=engelli+şehit_gazi_spor
                if şehit_gazi_spor<0 or engelli<0:
                    print("hatalı sayı girdiniz")
                    continue
                if toplam>hane_sayısı:
                    print("şehit,gazi,sporcu ve engelli sayısı hane sayısından fazla olamaz")
                else:
                    break
            while True:
                indirim_durumu = input("indirim durumu giriniz Yok/Şehit/Gazi/Sporcu/Engelli (Y/Ş/G/S/E karakterleri)").upper()
                if indirim_durumu == "Ş" or indirim_durumu == "G" or indirim_durumu == "S":
                    if hane_ortalaması < kademe1 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (hane_ortalaması * 2.89) * 5 / 10
                        Dönemlik_atık_su_ücreti = (hane_ortalaması * 1.44) * 5 / 10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe1_hane_sayısı+=hane_sayısı
                        kademe1_su_tüketim += hane_ortalaması
                        kademe1_aylık_su_tüketim = kademe1_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe1_aylık_toplam_su_tüketim += kademe1_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif kademe1 * ölçek < hane_ortalaması < kademe3 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (((hane_ortalaması - 13 * ölçek) * 3.13) + ((13 * ölçek) * 2.89)) * 5 / 10
                        Dönemlik_atık_su_ücreti = (((hane_ortalaması - 13 * ölçek) * 1.56) + ((13 * ölçek) * 1.44)) * 5 / 10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe2_hane_sayısı+=hane_sayısı
                        kademe2_su_tüketim += hane_ortalaması
                        kademe2_aylık_su_tüketim = kademe2_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe2_aylık_toplam_su_tüketim += kademe2_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif hane_ortalaması > kademe3 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (((hane_ortalaması - 20 * ölçek) * 6.43) + ((7 * ölçek) * 3.13) + ((13 * ölçek) * 2.89)) * 5 / 10
                        Dönemlik_atık_su_ücreti = (((hane_ortalaması - 20 * ölçek) * 3.22) + ((7 * ölçek) * 1.56) + ((13 * ölçek) * 1.44)) * 5 / 10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe3_hane_sayısı+=hane_sayısı
                        kademe3_su_tüketim += hane_ortalaması
                        kademe3_aylık_su_tüketim = kademe3_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe3_aylık_toplam_su_tüketim += kademe3_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    break
                elif indirim_durumu == "E":
                    if hane_ortalaması < kademe1 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (hane_ortalaması * 2.89) * 5 / 10
                        Dönemlik_atık_su_ücreti = (hane_ortalaması * 1.44) * 5 / 10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe1_hane_sayısı+=hane_sayısı
                        kademe1_su_tüketim += hane_ortalaması
                        kademe1_aylık_su_tüketim = kademe1_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe1_aylık_toplam_su_tüketim += kademe1_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif kademe1 * ölçek < hane_ortalaması < kademe3 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (((hane_ortalaması - 13 * ölçek) * 3.13) + ((13 * ölçek) * 2.89)) * 5 / 10
                        Dönemlik_atık_su_ücreti = (((hane_ortalaması - 13 * ölçek) * 1.56) + ((13 * ölçek) * 1.44)) * 5 / 10
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe2_hane_sayısı+=hane_sayısı
                        kademe2_su_tüketim += hane_ortalaması
                        kademe2_aylık_su_tüketim = kademe2_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe2_aylık_toplam_su_tüketim += kademe2_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif hane_ortalaması > kademe3 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (((hane_ortalaması - 20 * ölçek) * 6.43) + ((7 * ölçek) * 3.13) + ((13 * ölçek) * 2.89))
                        Dönemlik_atık_su_ücreti = (((hane_ortalaması - 20 * ölçek) * 3.22) + ((7 * ölçek) * 1.56) + ((13 * ölçek) * 1.44))
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe3_hane_sayısı+=hane_sayısı
                        kademe3_su_tüketim += hane_ortalaması
                        kademe3_aylık_su_tüketim = kademe3_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe3_aylık_toplam_su_tüketim += kademe3_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    break
                elif indirim_durumu == "Y":
                    if hane_ortalaması < kademe1 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (hane_ortalaması * 2.89)
                        Dönemlik_atık_su_ücreti = (hane_ortalaması * 1.44)
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe1_hane_sayısı+=hane_sayısı
                        kademe1_su_tüketim += hane_ortalaması
                        kademe1_aylık_su_tüketim = kademe1_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe1_aylık_toplam_su_tüketim += kademe1_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif kademe1 * ölçek < hane_ortalaması < kademe3 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (((hane_ortalaması - kademe1 * ölçek) * 3.13) + ((kademe1 * ölçek) * 2.89))
                        Dönemlik_atık_su_ücreti = (((hane_ortalaması - kademe1 * ölçek) * 1.56) + ((kademe1 * ölçek) * 1.44))
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe2_hane_sayısı+=hane_sayısı
                        kademe2_su_tüketim += hane_ortalaması
                        kademe2_aylık_su_tüketim = kademe2_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe2_aylık_toplam_su_tüketim += kademe2_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti += Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    elif hane_ortalaması > kademe3 * ölçek:
                        Dönemlik_su_tüketim_ücreti = (((hane_ortalaması - kademe3 * ölçek) * 6.43) + ((kademe2 * ölçek) * 3.13) + ((kademe1 * ölçek) * 2.89))
                        Dönemlik_atık_su_ücreti = (((hane_ortalaması - kademe3 * ölçek) * 3.22) + ((kademe2 * ölçek) * 1.56) + ((kademe1 * ölçek) * 1.44))
                        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
                        Dönemlik_ÇTV_tutarı = hane_ortalaması * 0.39
                        Dönemlik_katı_atık_toplama_ücreti = hane_sayısı * 13
                        Dönemlik_katı_atık_bertaraf_ücreti = hane_sayısı * 2.54
                        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
                        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
                        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
                        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
                        kademe3_hane_sayısı+=hane_sayısı
                        kademe3_su_tüketim += hane_ortalaması
                        kademe3_aylık_su_tüketim = kademe3_su_tüketim / önceki_şimdiki_sayaçlar_arası_gün_sayısı * 30
                        kademe3_aylık_toplam_su_tüketim += kademe3_aylık_su_tüketim
                        konut_dönemlik_su_tüketim_ücreti+=Dönemlik_su_tüketim_ücreti
                        izsu_toplam += Dönemlik_İZSU_payı
                        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
                        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
                        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
                    break
                else:
                    print("hatalı kodlama girdiniz")
        if konut_aylık_su_tüketim_miktarı>100 or Dönemlik_toplam_fatura_tutarı>500:
            konut_godoman+=1
        bornova_toplam_su_tüketim_miktarı +=konutların_aylık_toplam_su_tüketim_miktarı
        bornova_toplam_su_tüketim_ücreti+=konut_dönemlik_su_tüketim_ücreti

    elif abone_tipi==2:
        abone_tipi_adı="İşyeri"

        Dönemlik_su_tüketim_ücreti = Dönemlik_su_tüketim_miktarı * 7.38
        Dönemlik_atık_su_ücreti = Dönemlik_su_tüketim_miktarı * 3.68
        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
        Dönemlik_katı_atık_toplama_ücreti =  13
        Dönemlik_katı_atık_bertaraf_ücreti =  2.54
        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
        işyeri_su_tüketim_miktarı+=Dönemlik_su_tüketim_miktarı
        işyeri_aylık_su_tüketim_miktarı=(Dönemlik_su_tüketim_miktarı/önceki_şimdiki_sayaçlar_arası_gün_sayısı)*30
        işyerinin_aylık_toplam_su_tüketim_miktarı+=işyeri_aylık_su_tüketim_miktarı
        işyeri_sayısı+=1
        genel_ücret_liste.append(Dönemlik_su_tüketim_ücreti)
        genel_ücret_abone_no.append(abone_no)
        genel_ücret_abone_tipi.append(abone_tipi_adı)
        genel_ücret_aylıktüketim_miktarı.append(işyeri_aylık_su_tüketim_miktarı)
        bornova_toplam_su_tüketim_miktarı+=işyerinin_aylık_toplam_su_tüketim_miktarı
        işyeri_dönemlik_su_tüketim_ücreti+=Dönemlik_su_tüketim_ücreti
        bornova_toplam_su_tüketim_ücreti+=işyeri_dönemlik_su_tüketim_ücreti
        izsu_toplam += Dönemlik_İZSU_payı
        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı

    elif abone_tipi==3:
        abone_tipi_adı="Resmi Daire"
        Dönemlik_su_tüketim_ücreti = Dönemlik_su_tüketim_miktarı * 4.34
        Dönemlik_atık_su_ücreti = Dönemlik_su_tüketim_miktarı * 2.16
        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
        Dönemlik_katı_atık_toplama_ücreti =  13
        Dönemlik_katı_atık_bertaraf_ücreti =  2.54
        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
        resmidaire_su_tüketim_miktarı+=Dönemlik_su_tüketim_miktarı
        resmidaire_aylık_su_tüketim_miktarı=(Dönemlik_su_tüketim_miktarı/önceki_şimdiki_sayaçlar_arası_gün_sayısı)*30
        resmidaire_aylık_toplam_su_tüketim_miktarı+=resmidaire_aylık_su_tüketim_miktarı
        resmidaire_sayısı+=1
        resmi_daire_liste.append(resmidaire_aylık_su_tüketim_miktarı)
        resmi_daire_abone_no.append(abone_no)
        genel_ücret_liste.append(Dönemlik_su_tüketim_ücreti)
        genel_ücret_abone_no.append(abone_no)
        genel_ücret_abone_tipi.append(abone_tipi_adı)
        genel_ücret_aylıktüketim_miktarı.append(resmidaire_aylık_su_tüketim_miktarı)
        bornova_toplam_su_tüketim_miktarı+=resmidaire_aylık_toplam_su_tüketim_miktarı
        resmi_dönemlik_su_tüketim_ücreti+=Dönemlik_su_tüketim_ücreti
        bornova_toplam_su_tüketim_ücreti+=resmi_dönemlik_su_tüketim_ücreti
        izsu_toplam += Dönemlik_İZSU_payı
        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı

    elif abone_tipi==4:
        abone_tipi_adı="Organize Sanayi"
        Dönemlik_su_tüketim_ücreti = Dönemlik_su_tüketim_miktarı * 5.00
        Dönemlik_atık_su_ücreti = Dönemlik_su_tüketim_miktarı * 2.50
        Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
        Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
        Dönemlik_katı_atık_toplama_ücreti = 13
        Dönemlik_katı_atık_bertaraf_ücreti = 2.54
        Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
        Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
        Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
        Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
        Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
        organizesanayi_su_tüketim_miktarı+=Dönemlik_su_tüketim_miktarı
        organizesanayi_aylık_su_tüketim_miktarı=(Dönemlik_su_tüketim_miktarı/önceki_şimdiki_sayaçlar_arası_gün_sayısı)*30
        organizesanayi_aylık_toplam_su_tüketim_miktarı+=organizesanayi_aylık_su_tüketim_miktarı
        organizesanayi_sayısı+=1
        genel_ücret_liste.append(Dönemlik_su_tüketim_ücreti)
        genel_ücret_abone_no.append(abone_no)
        genel_ücret_abone_tipi.append(abone_tipi_adı)
        genel_ücret_aylıktüketim_miktarı.append(organizesanayi_aylık_su_tüketim_miktarı)
        bornova_toplam_su_tüketim_miktarı +=organizesanayi_aylık_toplam_su_tüketim_miktarı
        organize_dönemlik_su_tüketim_ücreti+=Dönemlik_su_tüketim_ücreti
        bornova_toplam_su_tüketim_ücreti+=organize_dönemlik_su_tüketim_ücreti
        izsu_toplam += Dönemlik_İZSU_payı
        ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
        büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
        belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı

    elif abone_tipi==5:
        abone_tipi_adı="İlçe Tarımsal ve Hayvan Sulama"
        if Dönemlik_su_tüketim_miktarı < kademe1*ölçek:
            Dönemlik_su_tüketim_ücreti = (Dönemlik_su_tüketim_miktarı * 1.45)
            Dönemlik_atık_su_ücreti = (Dönemlik_su_tüketim_miktarı * 0.72)
            Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
            Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
            Dönemlik_katı_atık_toplama_ücreti = 13
            Dönemlik_katı_atık_bertaraf_ücreti = 2.54
            Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
            Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
            Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
            Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
            Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
            izsu_toplam += Dönemlik_İZSU_payı
            ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
            büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
            belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
        elif kademe1*ölçek < Dönemlik_su_tüketim_miktarı < kademe3*ölçek:
            Dönemlik_su_tüketim_ücreti = ((Dönemlik_su_tüketim_miktarı - kademe1*ölçek)*2.89)+(kademe1*ölçek*1.45)
            Dönemlik_atık_su_ücreti = ((Dönemlik_su_tüketim_miktarı - kademe1*ölçek)*1.44)+(kademe1*ölçek*0.72)
            Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
            Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
            Dönemlik_katı_atık_toplama_ücreti =  13
            Dönemlik_katı_atık_bertaraf_ücreti =  2.54
            Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
            Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
            Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
            Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
            Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
            izsu_toplam += Dönemlik_İZSU_payı
            ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
            büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
            belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
        elif Dönemlik_su_tüketim_miktarı > kademe3*ölçek:
            Dönemlik_su_tüketim_ücreti = ((Dönemlik_su_tüketim_miktarı - kademe3*ölçek)*6.43)+(kademe2*ölçek*2.89)+(kademe1*ölçek*1.45)
            Dönemlik_atık_su_ücreti = ((Dönemlik_su_tüketim_miktarı - kademe3*ölçek)*3.22)+(kademe2*ölçek*1.44)+(kademe1*ölçek*0.72)
            Dönemli_toplam_su_tüketim_ve_atık_su_ücreti = Dönemlik_su_tüketim_ücreti + Dönemlik_atık_su_ücreti
            Dönemlik_ÇTV_tutarı = Dönemlik_su_tüketim_miktarı * 0.39
            Dönemlik_katı_atık_toplama_ücreti = 13
            Dönemlik_katı_atık_bertaraf_ücreti = 2.54
            Dönemlik_toplam_fatura_tutarı = Dönemli_toplam_su_tüketim_ve_atık_su_ücreti + Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti + Dönemlik_katı_atık_bertaraf_ücreti
            Dönemlik_devlete_aktarılacak_KDV_tutarı = (Dönemlik_toplam_fatura_tutarı - Dönemlik_ÇTV_tutarı) * 8 / 100
            Dönemlik_ilçe_belediyesine_aktarılacak_tutar = Dönemlik_ÇTV_tutarı + Dönemlik_katı_atık_toplama_ücreti
            Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar = Dönemlik_katı_atık_bertaraf_ücreti
            Dönemlik_İZSU_payı = Dönemlik_toplam_fatura_tutarı - (Dönemlik_devlete_aktarılacak_KDV_tutarı + Dönemlik_ilçe_belediyesine_aktarılacak_tutar + Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar)
            izsu_toplam += Dönemlik_İZSU_payı
            ilçebelediye_toplam += Dönemlik_ilçe_belediyesine_aktarılacak_tutar
            büyükşehirbelediye_toplam += Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar
            belediye_toplam += Dönemlik_devlete_aktarılacak_KDV_tutarı
        İlçeTarımsal_su_tüketim_miktarı+=Dönemlik_su_tüketim_miktarı
        İlçeTarımsal_aylık_su_tüketim_miktarı=(Dönemlik_su_tüketim_miktarı/önceki_şimdiki_sayaçlar_arası_gün_sayısı)*30
        İlçeTarımsal_aylık_toplam_su_tüketim_miktarı+=İlçeTarımsal_aylık_su_tüketim_miktarı
        İlçeTarımsal_sayısı+=1
        genel_ücret_liste.append(Dönemlik_su_tüketim_ücreti)
        genel_ücret_abone_no.append(abone_no)
        genel_ücret_abone_tipi.append(abone_tipi_adı)
        genel_ücret_aylıktüketim_miktarı.append(İlçeTarımsal_aylık_su_tüketim_miktarı)
        bornova_toplam_su_tüketim_miktarı +=İlçeTarımsal_aylık_toplam_su_tüketim_miktarı
        işyeri_dönemlik_su_tüketim_ücreti+=Dönemlik_su_tüketim_ücreti
        bornova_toplam_su_tüketim_ücreti+=işyeri_dönemlik_su_tüketim_ücreti
        if İlçeTarımsal_aylık_su_tüketim_miktarı>50:      #ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı ve ilçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi
            godoman+=1
    print("abone no :",abone_no)
    print("abone tipi adı:",abone_tipi_adı)
    print("dönemlik su tüketim miktarı:",format(Dönemlik_su_tüketim_miktarı,".2f"),"Ton")
    print("dönemlik su tüketim ücreti:",format(Dönemlik_su_tüketim_ücreti,".2f"),"TL")
    print("dönemlik atık su ücreti:",format(Dönemlik_atık_su_ücreti,".2f"),"TL")
    print("Dönemlik toplam su tüketim ve atık su ücreti:",format(Dönemli_toplam_su_tüketim_ve_atık_su_ücreti,".2f"),"TL")
    print("Dönemlik ÇTV tutarı:",format(Dönemlik_ÇTV_tutarı,".2f"),"TL")
    print("Dönemlik katı atık toplama ücreti:",format(Dönemlik_katı_atık_toplama_ücreti,".2f"),"TL")
    print("Dönemlik katı atık bertaraf ücreti:",format(Dönemlik_katı_atık_bertaraf_ücreti,".2f"),"TL")
    print("Dönemlik toplam fatura tutarı:",format(Dönemlik_toplam_fatura_tutarı,".2f"),"TL")
    print("Dönemlik devlete aktarılacak KDV tutarı:",format(Dönemlik_devlete_aktarılacak_KDV_tutarı,".2f"),"TL")
    print("Dönemlik ilçe belediyesine aktarılacak tutar:",format(Dönemlik_ilçe_belediyesine_aktarılacak_tutar,".2f"),"TL")
    print("Dönemlik büyükşehir belediyesine aktarılacak tutar:",format(Dönemlik_büyükşehir_belediyesine_aktarılacak_tutar,".2f"),"TL")
    print("Dönemlik İZSU payı:",format(Dönemlik_İZSU_payı,".2f",),"TL")
    while True:
        başka_abone=input("başka abone varsa giriniz E (evet) veya H (hayır):").upper()
        if başka_abone=="E" or başka_abone=="H":
            break
        print("hatalı kod girdiniz")
    if başka_abone=="H":
        break
print("konut için;"
      "hane sayısı:",konut_toplam_hane_sayıları,
      "yüzdesi :",format(konut_su_tüketim_miktarı/toplam_su_tüketim_miktarı*100,".2f"),
      "aylık ortalama su tüketim miktarı:",format(konutların_aylık_toplam_su_tüketim_miktarı/konut_toplam_hane_sayıları,".2f"))
print("işyeri için;"
      "hane sayısı ",işyeri_sayısı,
      "yüzdesi:",format(işyeri_su_tüketim_miktarı/toplam_su_tüketim_miktarı*100,".2f"),
      "aylık ortalama su tüketim miktarı:",format(işyerinin_aylık_toplam_su_tüketim_miktarı/işyeri_sayısı,".2f"))
print("resmi daire için;"
      "hane sayısı ",resmidaire_sayısı,
      "yüzdesi: ",format(resmidaire_su_tüketim_miktarı/toplam_su_tüketim_miktarı*100,".2f"),
      "aylık ortalama su tüketim miktarı:",format(resmidaire_aylık_toplam_su_tüketim_miktarı/resmidaire_sayısı,".2f"))
print("organize sanayi için;"
      "hane sayısı ",organizesanayi_sayısı,
      "yüzdesi: ",format(organizesanayi_su_tüketim_miktarı/toplam_su_tüketim_miktarı*100,".2f"),
      "aylık ortalama su tüketim miktarı:",format(organizesanayi_aylık_toplam_su_tüketim_miktarı/organizesanayi_sayısı,".2f"))
print("ilçe tarımsal ve hayvan sulama için;"
      "hane sayısı",İlçeTarımsal_sayısı,
      "yüzdesi:}",format(İlçeTarımsal_su_tüketim_miktarı/toplam_su_tüketim_miktarı*100,".2f"),
      "aylık ortalama su tüketim miktarı:".format(İlçeTarımsal_aylık_toplam_su_tüketim_miktarı/İlçeTarımsal_sayısı,".2f"))

print("1.kademe hane sayısı",kademe1_hane_sayısı,"yüzdesi:",format(kademe1_su_tüketim/konut_su_tüketim_miktarı*100,".2f"),"ortalama su tüketim miktarı:",format(kademe1_aylık_toplam_su_tüketim/kademe1_hane_sayısı,".2f"))
print("2.kademe hane sayısı",kademe2_hane_sayısı,"yüzdesi:",format(kademe2_su_tüketim/konut_su_tüketim_miktarı*100,".2f"),"ortalama su tüketim miktarı:",format(kademe2_aylık_toplam_su_tüketim/kademe2_hane_sayısı,".2f"))
print("3.kademe hane sayısı",kademe3_hane_sayısı,"yüzdesi:",format(kademe3_su_tüketim/konut_su_tüketim_miktarı*100,".2f"),"ortalama su tüketim miktarı:",format(kademe3_aylık_toplam_su_tüketim/kademe3_hane_sayısı,".2f"))
print("aylık su tüketim miktarı 50 tonun üstünde olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı:",godoman,"yüzdesi",format(godoman/İlçeTarımsal_sayısı*100,".2f"))
print("aAylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin sayısı",konut_godoman)
print("Şehit, gazi veya devlet sporcusu olan ve engelli olan konut tipi hanelerin sayısı:",şehitgazispor+engellli,"yüzdesi:",format((şehitgazispor+engellli)/konut_toplam_hane_sayıları*100,".2f"))
en_büyük=max(resmi_daire_liste)
indeks=resmi_daire_liste.index(en_büyük)
resmi_abone_no_adı=resmi_daire_abone_no[indeks]
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su:",resmi_abone_no_adı,"aylık su tüketim miktarı:",en_büyük)
genel_en_büyük=max(genel_ücret_liste)
genel_indeks=genel_ücret_liste.index(genel_en_büyük)
genel_abone_no_adı=genel_ücret_abone_no[genel_indeks]
genel_abone_tipi_adı=genel_ücret_abone_tipi[genel_indeks]
genel_aylıktüketim_miktarı=genel_ücret_aylıktüketim_miktarı[genel_indeks]
print("Aylık su tüketim ücreti en yüksek olan abonenın abone no su:",genel_abone_no_adı,"abone tipi adı:",genel_abone_tipi_adı,"aylık su tüketim miktarı:",genel_aylıktüketim_miktarı,"ödediği ücret:",genel_en_büyük)
print("konut için;"
      "aylık toplam su tüketim miktarları:",konutların_aylık_toplam_su_tüketim_miktarı,
      "yüzdesi :",format(konutların_aylık_toplam_su_tüketim_miktarı/bornova_toplam_su_tüketim_miktarı*100,".2f")),
print("işyeri için;"
      "aylık toplam su tüketim miktarları ",işyerinin_aylık_toplam_su_tüketim_miktarı,
      "yüzdesi:",format(işyerinin_aylık_toplam_su_tüketim_miktarı/bornova_toplam_su_tüketim_miktarı*100,".2f")),
print("resmi daire için;"
      "aylık toplam su tüketim miktarları: ",resmidaire_aylık_toplam_su_tüketim_miktarı,
      "yüzdesi: ",format(resmidaire_aylık_toplam_su_tüketim_miktarı/bornova_toplam_su_tüketim_miktarı*100,".2f")),
print("organize sanayi için;"
      "aylık toplam su tüketim miktarları: ",organizesanayi_aylık_toplam_su_tüketim_miktarı,
      "yüzdesi: ",format(organizesanayi_aylık_toplam_su_tüketim_miktarı/bornova_toplam_su_tüketim_miktarı*100,".2f")),
print("ilçe tarımsal ve hayvan sulama için;"
      "aylık toplam su tüketim miktarları",İlçeTarımsal_aylık_toplam_su_tüketim_miktarı,
      "yüzdesi: ",format(İlçeTarımsal_aylık_toplam_su_tüketim_miktarı/bornova_toplam_su_tüketim_miktarı*100,".2f")),
print("bornovanın toplam su tüketim miktarı:",bornova_toplam_su_tüketim_miktarı)
print("konut için;"
      "aylık toplam su tüketim ücreti:",format(konut_dönemlik_su_tüketim_ücreti,".2f"))
print("işyeri için;"
      "aylık toplam su tüketim ücreti ",format(işyeri_dönemlik_su_tüketim_ücreti,".2f"))
print("resmi daire için;"
      "aylık toplam su tüketim ücreti: ",format(resmi_dönemlik_su_tüketim_ücreti,".2f"))
print("organize sanayi için;"
      "aylık toplam su tüketim ücreti: ",format(organize_dönemlik_su_tüketim_ücreti,".2f"))
print("ilçe tarımsal ve hayvan sulama için;"
      "aylık toplam su tüketim ücreti",format(ilçe_dönemlik_su_tüketim_ücreti,".2f"))
print("bornovanın toplam su tüketim ücreti:",format(bornova_toplam_su_tüketim_ücreti,".2f"))
print("izsu elde ettiği gelir:",format(izsu_toplam,".2f"))
print("ilçe belediyesinin elde ettiği gelir:",format(ilçebelediye_toplam,".2f"))
print("büyükşehir belediyesini elde ettiği gelir:",format(büyükşehirbelediye_toplam,".2f"))
print("belediyenin elde ettiği gelir:",format(belediye_toplam,".2f"))


















































































