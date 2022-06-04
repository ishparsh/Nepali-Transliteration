from collections import OrderedDict

dict_value=OrderedDict([
#missing of S
('सा','sa'),
('सि','si'),
('सी','si'),
('सु','su'),
('सू','su'),
('से','se'),
('सै','sai'),
('सो','so'),
('सौ','sau'),
('सं','sam'),
#districts
('भोजपुर', 'Bhojpur'),
 ('धनकुटा', 'Dhankuta'),
 ('इलाम', 'Ilam'),
 ('झापा', 'Jhapa'),
 ('खोटाङ', 'Khotang'),
 ('मोरङ', 'Morang'),
 ('ओखलढुंगा', 'Okhaldhunga'),
 ('पाँचथर', 'Panchthar'),
 ('संखुवासभा', 'Sankhuwasabha'),
 ('सोलुखुम्बु', 'Solukhumbu'),
 ('सुनसरी', 'Sunsari'),
 ('ताप्लेजुङ', 'Taplejung'),
 ('तेह्रथुम', 'Terhathum'),
 ('उदयपुर', 'Udayapur'),
 ('बारा', 'Bara'),
 ('धनुषा', 'Dhanusa'),
 ('महोत्तरी', 'Mahottari'),
 ('पर्सा', 'Parsa'),
 ('आज','aaja'),
 ('रौतहट', 'Rautahat'),
 ('सप्तरी', 'Saptari'),
 ('सर्लाही', 'Sarlahi'),
 ('सिरहा', 'Siraha'),
 ('भक्तपुर', 'Bhaktapur'),
 ('चितवन', 'Chitwan'),
 ('धादिङ', 'Dhading'),
 ('दोलखा', 'Dolakha'),
 ('काठमाडौं', 'Kathmandu'),
 ('काभ्रेपलाञ्चोक', 'Kavrepalanchok'),
 ('ललितपुर', 'Lalitpur'),
 ('मकवानपुर', 'Makawanpur'),
 ('नुवाकोट', 'Nuwakot'),
 ('रामेछाप', 'Ramechhap'),
 ('रसुवा', 'Rasuwa'),
 ('सिन्धुली', 'Sindhuli'),
 ('सिन्धुपाल्चोक', 'Sindhupalchok'),
 ('बाग्लुङ', 'Baglung'),
 ('गोरखा', 'Gorkha'),
 ('कास्की', 'Kaski'),
 ('लमजुङ', 'Lamjung'),
 ('मनाङ', 'Manang'),
 ('मुस्ताङ', 'Mustang'),
 ('म्याग्दी', 'Myagdi'),
 ('नवलपुर', 'Nawalpur'),
 ('पर्वत', 'Parbat'),
 ('स्याङ्जा', 'Syangja'),
 ('तनहुँ', 'Tanahu'),
 ('अर्घाखाँची', 'Arghakhanchi'),
 ('बाँके', 'Banke'),
 ('बर्दिया', 'Bardiya'),
 ('दाङ', 'Dang'),
 ('गुल्मी', 'Gulmi'),
 ('कपिलवस्तु', 'Kapilvastu'),
 ('परासी', 'Parasi'),
 ('पाल्पा', 'Palpa'),
 ('प्युठान', 'Pyuthan'),
 ('रोल्पा', 'Rolpa'),
 ('रुकुम', 'Rukum'),
 ('रुपन्देही', 'Rupandehi'),
 ('दैलेख', 'Dailekh'),
 ('डोल्पा', 'Dolpa'),
 ('हुम्ला', 'Humla'),
 ('जाजरकोट', 'Jajarkot'),
 ('जुम्ला', 'Jumla'),
 ('कालिकोट', 'Kalikot'),
 ('मुगु', 'Mugu'),
('रुकुम पश्चिम','Rukum Paschim') ,
('सल्यान','Salyan'), 
('सुर्खेत','Surkhet'), 
('अछाम','Achham'),
('बैतडी','Baitadi'),
('बझाङ','Bajhang'),
('बाजुरा','Bajura'),
('डडेल्धुरा','Dadeldhura'),
('दार्चुला','Darchula'),
('डोटी','Doti'),
('कैलाली','Kailali'),
('कञ्चनपुर','Kanchanpur'),
#municipality prov1
('भोजपुर','Bhojpur'),
('षडानन्द','Sadananda'),
('टेम्केमैयुङ','Tyamkemaiyum'),
('रामप्रसाद राई','Ramprasadrai'),
('अरुण','Arun'),
('पौवादुङ्मा','Pauwadungma'),
('साल्पासिलिछो','Salpasilichho'),
('आमचोक','Aamchowk'),
('हतुवागढी','Hatuwagadhi'),
('पाख्रिवास','Pakhribaas'),
('धनकुटा','Dhankuta'),
('महालक्ष्मी','Mahalaxmi'),
('साँगुरीगढी','Sagurigadhi'),
('सहिदभुमि','Khalsa Chhintang Sahidbhumi'),
('छथर जोरपाटी','Chhathar Jorpati'),
('चौबिसे','Chaubise'),
('ईलाम','Illam'),
('देउमाई','Deumai'),
('माई','Mai'),
('सुर्योदय','Suryodaya'),
('फाकफोकथुम','Fakfokthum'),
('चुलाचुली','Chulachuli'),
('माईजोगमाई','Maijogmai'),
('माङसेबुङ','Mangsebung'),
('रोङ','Rong'),
('सन्दकपुर','Sandakpur'),
('मेचीनगर','Mechinagar'),
('दमक','Damak'),
('कन्काई','Kankai'),
('भद्रपुर','Bhadrapur'),
('अर्जुनधारा','Arjundhara'),
('शिवसताक्षी','Shivasatakshi'),
('गौरादह','Gauradaha'),
('विर्तामोड','Birtamod'),
('कमल','Kamal'),
('गौरिगंज','Gaurigunj'),
('बाह्रदशी','Barhadashi'),
('झापा','Jhapa'),
('बुद्धशान्ति','Buddhasanti'),
('हल्दिबारी','Haldibari'),
('कचनकवल','Kachankawal'),
('हलेसी तुवाचुङ','Halesituwachung'),
('दिक्तेल रुपाकोट मझुवागढी','Rupakot Majhuwagadhi'),
('ऐसेलुखर्क','Aiselukharka'),
('लामिडाडा','Lamidada'),
('जन्तेढुंगा','Jantedhunga'),
('खोटेहाङ','Khotehang'),
('केपिलासगढी','Kepilasgadhi'),
('दिप्रुङ','Diprung'),
('साकेला','Sakela'),
('वराहपोखरी','Barahpokhari'),
('विराटनगर','Biratnagar'),
('बेलवारी','Belbaari'),
('लेटाङ','Letang'),
('पथरी शनिश्चरे','Pathari Sanischare'),
('रंगेली','Rangeli'),
('रतुवामाई','Ratuwamai'),
('सुनवर्षी','Sunawarsi'),
('उर्लाबारी','Urlabaari'),
('सुन्दर हरैचा','Sundarharaincha'),
('बुढीगंगा','Budhiganga'),
('धनपालथान','Dhanpalthan'),
('ग्रामथान','Gramthan'),
('जहदा','Jahada'),
('कानेपोखरी','Kanepokhari'),
('कटहरी','Katahari'),
('केराबारी','Kerabaari'),
('मिक्लाजुङ','Miklajung'),
('सिद्धिचरण','Siddhicharan'),
('खिजीदेम्वा','Khijidemwa'),
('चम्पादेवी','Champadevi'),
('चिशंखुगढी','Chisankhugadhi'),
('मानेभञ्याङ','Manebhanjyang'),
('मोलुङ','Molung'),
('लिखु','Likhu'),
('सुनकोशी','Sunkoshi'),
('फिदिम','Fidim'),
('फालेलुङ','Falelung'),
('फाल्गुनन्द','Falgunanda'),
('हिलिहाङ','Hilihang'),
('कुम्मायक','Kummayek'),
('मिक्लाजुङ','Miklajung'),
('तुम्वेवा','Tumwewa'),
('याङवरक','Yangwarak'),
('चैनपुर','Chainpur'),
('धर्मदेवी','Dharmadevi'),
('खाँदवारी','Khaadbaari'),
('मादी','Madi'),
('पाँचखपन','Paanchkhapan'),
('भोटखोला','Bhotkhola'),
('चिचिला','Chichila'),
('मकालु','Makalu'),
('सभापोखरी','Sabhapokhari'),
('सिलीचोङ','Silichong'),
('सोलुदुधकुण्ड','Solududhkunda'),
('दुधकोशी','Dudhkoshi'),
('खुम्वु पासाङल्हामु','Khumbu Pasang Lhamu'),
('दुधकौसिका','Dudhkausika'),
('नेचासल्यान','Nechasalyan'),
('माहाकुलुङ','Mahakulung'),
('लिखु पिके','Likhu Pike'),
('सोताङ','Sotang'),
('इटहरी','Itahari'),
('धरान','Dharan'),
('इनरुवा','Inaruwa'),
('दुहवी','Duhabi'),
('रामधुनी','Ramdhuni'),
('बराह','Barah'),
('देवानगञ्ज','Dewangunj'),
('कोशी','Koshi'),
('गढी','Gadhi'),
('बर्जु','Barju'),
('भोक्राहा','Bhokraha'),
('हरिनगर','Harinagara'),
('फुङलिङ','Fungling'),
('आठराई त्रिवेणी','Athrai Tribeni'),
('सिदिङ्वा','Sidingwa'),
('फक्ताङलुङ','Faktanglung'),
('मिक्वाखोला','Mikhwakhola'),
('मेरिङदेन','Meringden'),
('मैवाखोला','Maiwakhola'),
('याङ्वरक','Yangwarak'),
('सिरीजङ्घा','Sirijunga'),
('म्याङलुङ','Myanglung'),
('लालीगुराँस','Laligurans'),
('आठराई','Athrai'),
('छथर','Chhathar'),
('फेदाप','Fedaap'),
('मेन्छयायेम','Menchhayayem'),
('कटारी','Katari'),
('चौदण्डीगढी','Chaudandagadhi'),
('त्रियुगा','Triyuga'),
('वेलका','Belaka'),
('उदयपुरगढी','Udaypurgadhi'),
('ताप्ली','Tapli'),
('रौतामाई','Rautamai'),
('सुनकोशी','Sunkoshi'),
('नेवार','Newar'),
('राम','ram'),
('नेपालटार',"Nepaltar"),
#municipality prov2
('कलैया','Kalaiya'),
('जितपुर-सिमरा','Jitpursimara'),
('कोल्हवी','Kolhawi'),
('निजगढ','Nijgadh'),
('महागढीमाई','Mahagadimai'),
('सिम्रौनगढ','Simraungadh'),
('आदर्श कोतवाल','Adarsha Kotwal'),
('आदर्श','Adarsha'),
('करैयामाई','Karaiyamai'),
('देवताल','Devtaal'),
('पचरौता','Pachrauta'),
('परवानीपुर','Parwanipur'),
('प्रसौनी','Prasauni'),
('फेटा','Pheta'),
('बारागढी','Baragadhi'),
('सुवर्ण','Subarna'),
('विश्रामपुर','bishrampur'),
('जनकपुर','Janakpur'),
('क्षिरेश्वरनाथ','Chhireshwor'),
('गणेशमान–चारनाथ','Ganeshman Charnath'),
('धनुषाधाम','Dhanusadham'),
('नगराइन','Nagarain'),
('विदेह','Videha'),
('मिथिला','Mithila'),
('शहिदनगर','Sahidnagar'),
('सबैला','Sabaila'),
('सिद्धिदात्री','Siddidatri'),
('जनकनन्दिनी','Janaknandini'),
('बटेश्वर','Bateshwor'),
('मिथिला विहारी','Mithila Bihari'),
('मुखियापट्टि मुसहरमिया','Mukhiyapatti musaharmiya'),
('लक्ष्मीनिया','Laxminiya'),
('हंसपुर','Hansapur'),
('कमला','kamala'),
('औरही','Aurahi'),
('जलेश्वर','Jaleshwor'),
('बर्दिबास','Bardibas'),
('गौशाला','Gausala'),
('एकडारा','Ekdara'),
('सोनमा','Sonama'),
('साम्सी','Samsi'),
('लोहरपट्टी','Loharpatti'),
('रामगोपालपुर','Ramgopalpur'),
('महोत्तरी','Mahottari'),
('मनरा','Manara'),
('मटिहानी','Matihani'),
('भँगाहा','Bhanggaha'),
('बलवा','Balawa'),
('पिपरा','Pipara'),
('औरही','Aurahi'),
('वीरगञ्ज','Birgunj'),
('पोखरिया','Pokhariya'),
('सुवर्णपुर','Subarnapur'),
('जगरनाथपुर','Jagarnathpur'),
('धोबीनी','Dhobini'),
('छिपहरमाई','Chhipaharmai'),
('पकाहा मैनपुर','Pakaha Mainapur'),
('बिन्दबासिनी','Bindabasini'),
('बहुदरमाई','Bahudarmai'),
('बेलवा','Belawa'),
('पर्सागढी','Parsagadhi'),
('सखुवा प्रसौनी','Sakhuwa Prasauni'),
('पटेर्वा सुगौली','Paterwa Sugauli'),
('चन्द्रपुर','Chandrapur'),
('गरुडा','Garuda'),
('गौर','Gaur'),
('बौधीमाई','Baudhimai'),
('वृन्दावन','Brindaban'),
('देवाही गोनाही','Dewahi Gonahi'),
('दुर्गाभगवती','Durga Bhagwati'),
('दुर्गा भगवती','Durga Bhagwati'),
('गढीमाई','Gadhimai'),
('गुजरा','Gujara'),
('कटहरीया','Katahariya'),
('माधवनारायण','Madhav Narayan'),
('मौलापुर','Maulapur'),
('फतुवा विजयपुर','Fatuwa Bijayapur'),
('ईशनाथ','Ishanath'),
('परोहा','Paroha'),
('राजपुर','Rajpur'),
('यमुनामाई','yamunamai'),
('राजविराज','rajbiraj'),
('कञ्चनरुप','Kanchanrup'),
('डाक्नेश्वरी','Dakneshwori'),
('बोदेबरसाईन','Bodebarsain'),
('खडक','Khadak'),
('शम्भुनाथ','Sambhunath'),
('सुरुगां','Surunga'),
('हनुमाननगर कंकालिनी','hanumannagar kankalini'),
('कृष्णासवरन','Krishna sabaran'),
('छिन्नमस्ता','Chhinnamasta'),
('महादेवा','Mahadeva'),
('राजगढ','rajgadh'),
('सप्तकोशी','Saptakosi'),
('तिरहुत','Tirahut'),
('तिलाठी कोईलाडी','Tilathi Koiladi'),
('रुपनी','Rupani'),
('बेल्ही चपेना','Belhi Chapena'),
('बिष्णुपुर','Bishnupur'),
('ईश्वरपुर','Ishworpur'),
('लालबन्दी','Lalbandi'),
('हरिपुर','Haripur'),
('हरिपुर्वा','Haripurba'),
('हरिवन','Hariban'),
('बरहथवा','Barahathawa'),
('बलरा','Balara'),
('गोडैटा','Godaita'),
('मलंगवा','Malangwa'),
('बागमती','Bagmati'),
('कबिलासी','Kabilasi'),
('चक्रघट्टा','Chakraghatta'),
('चन्द्रनगर','Chandranagar'),
('धनकौल','Dhankaul'),
('बसबरीया','basbariya'),
('ब्रह्मपुरी','Bramhapuri'),
('रामनगर','Ramnagar'),
('विष्णु','Bishnu'),
('लहान','Lahan'),
('धनगढीमाई','Dhangadimai'),
('धनगढी','Dhangadi'),
('सिरहा','Siraha'),
('गोलबजार','Golbazar'),
('मिर्चैया','Mirchaiya'),
('कल्याणपुर','Kalyanpur'),
('भगवानपुर','Bhagawanpur'),
('विष्णु','Bishnu'),
('सुखीपुर','Sukhipur'),
('कर्जन्हा','Karjanha'),
('बरियारपट्टी','Bariyarpatti'),
('लक्ष्मीपुर पतारी','Laxmipur Patari'),
('नरहा','Naraha'),
('सखुवानान्कारकट्टी','Sakhuwanankarkatti'),
('अर्नमा','Arnama'),
('नवराजपुर','Nawarajpur'),
#Municipality province 3
('चाँगुनारायण','Changu Narayan'),
('भक्तपुर','Bhaktapur'),
('मध्यपुर','Madhyepur'),
('थिमी','Thimi'),
('सूर्यविनायक','Suryebinayak'),
('भरतपुर','Bharatpur'),
('कालिका','Kalika'),
('खैरहनी','Khairhani'),
('माडी','Madi'),
('रत्ननगर','Ratnanagar'),
('राप्ती','Rapti'),
('इच्छाकामना','Echyakamana'),
('धुनीबेंसी','Dhunibenshi'),
('नीलकण्ठ','Nilkantha'),
('खनियाबास','Khaniyabash'),
('गजुरी','Gajuri'),
('गल्छी','Galchi'),
('गङ्गाजमुना','Gangajamuna'),
('ज्वालामूखी','Jwalamukhi'),
('थाक्रे','Thakre'),
('नेत्रावती','Netrabati'),
('बेनीघाट रोराङ्ग','Benighat Rorang'),
('रुवी भ्याली','Rubi Valley'),
('सिद्धलेक','Sidhlake'),
('त्रिपुरासुन्दरी','Tripurasundari'),
('जिरी','Jiri'),
('भिमेश्वर','Bhimeshwor'),
('कालिन्चोक','Kalinchowk'),
('गौरीशङ्कर','Gaurishankar'),
('तामाकोशी','Tamakoshi'),
('मेलुङ्ग','Melung'),
('विगु','Bigu'),
('वैतेश्वर','Baiteshwor'),
('शैलुङ्ग','Shailung'),
('धुलिखेल','Dhulikhel'),
('बनेपा','Banepa'),
('पनौती','Panauti'),
('पांचखाल','Panchkhaal'),
('नमोबुद्ध','Namobuddha'),
('खानीखोला','Khanikhola'),
('चौंरीदेउराली','Chaurideurali'),
('तेमाल','Temaal'),
('बेथानचोक','Bethanchowk'),
('भुम्लु','Bhumlu'),
('मण्डनदेउपुर','Mandandeupur'),
('महाभारत','Mahabharat'),
('रोशी','Roshi'),
('काठमाण्डौं','Kathmandu'),
('कागेश्वरी','Kageshwori'),
('कीर्तिपुर','Kirtipur'),
('गोकर्णेश्वर','Gokarneshwor'),
('चन्द्रागिरी','Chandragiri'),
('टोखा','Tokha'),
('तारकेश्वर','Tarkeshwor'),
('दक्षिणकाली','Dakchinkali'),
('नागार्जुन','Nagarjun'),
('बुढानिलकण्ठ','Budhanilkantha'),
('शंखरापुर','Shankharapur'),
('ललितपुर','Lalitpur'),
('गोदावरी','Godawari'),
('महालक्ष्मी','Mahalaxmi'),
('कोन्ज्योसोम','Konjyosom'),
('बाग्मती','Bagmati'),
('महाङ्काल','Mahankaal'),
('हेटौंडा','Hetauda'),
('थाहा','Thaha'),
('ईन्द्रसरोवर','Indrasarobar'),
('कैलाश','Kailash'),
('बकैया','Bakaiya'),
('भिमफेदी','Bhimfedi'),
('मकवानपुरगढी','Makwanpurgadhi'),
('मनहरी','Manhari'),
('राक्सिराङ्ग','Raksirang'),
('विदुर','Bidur'),
('बेलकोटगढी','Belkotgadhi'),
('ककनी','Kakani'),
('किस्पाङ','Kispang'),
('तादी','Tadi'),
('दुप्चेश्वर','Dupcheshwor'),
('पञ्चकन्या','Panchakanya'),
('लिखु','Likhu'),
('म्यागङ','Meghang'),
('शिवपुरी','Shivapuri'),
('सुर्यगढी','Suryegadhi'),
('मन्थली','Manthali'),
('रामेछाप','Ramechhap'),
('उमाकुण्ड','Umakunda'),
('खाँडादेवी','Khandadevi'),
('गोकुलगङ्गा','Gokulganga'),
('दोरम्बा','Doramba'),
('सुनापति','Sunapati'),
('उत्तरगया','Uttargaya'),
('कालिका','Kalika'),
('गोसाईंकुण्ड','Gosainkunda'),
('नौकुण्ड','Naukunda'),
('कमलामाई','Kamalamaai'),
('दुधौली','Dudhauli'),
('गोलन्जोर','Golanjor'),
('घ्याङ','Ghyan'),
('तीनपाटन','Tinpatan'),
('फिक्कल','Fikkal'),
('मरिण','Marin'),
('सुनकोशी','Sunkoshi'),
('हरिहरपुरगढी','Hariharpurgadhi'),
('सागाचोकगढी','Sangachowkgadhi'),
('वाह्रविसे','Barabise'),
('मेलम्ची','Melamchi'),
('ईन्द्रावती','Indrabati'),
('जुगल','Jugal'),
('थाङपाल','Thanpal'),
('बलेफी','Balephi'),
('भोटेकोशी','Botekoshi'),
('लिसंखुपाखर','Lisankhu Pakhar'),
('हेलम्बु','Helambhu'),
('त्रिपुरासुन्दरी','Tripurasundari'),
#province 4 Municipality
('बाग्लुङ', 'Baglung'),
 ('गल्कोट', 'Galkot'),
 ('जैमिनी', 'Jaimini'),
 ('ढोरपाटन', 'Dhorpatan'),
 ('वरेङ', 'Bareng'),
 ('काठेखोला', 'Kathekhola'),
 ('तमानखोला', 'Tamankhola'),
 ('ताराखोला', 'Tarakhola'),
 ('निसीखोला', 'Nisikhola'),
 ('वडिगाड', 'Badigad'),
 ('गोरखा', 'Gorkha'),
 ('पालुङटार', 'Palungtar'),
 ('सुलिकोट', 'Sulikot'),
 ('सिरानचोक', 'Siranchok'),
 ('अजिरकोट', 'Ajirkot'),
 ('आरुघाट', 'Aarughat'),
 ('गण्डकी', 'Gandaki'),
 ('चुमनुव्री', 'Chumnubri'),
 ('धार्चे', 'Dharche'),
 ('भीमसेन', 'Bhimsen'),
 ('सहिद लखन', 'Sahid Lakhan'),
 ('पोखरा', 'Pokhara'),
 ('अन्नपूर्णा', 'Annapurna'),
 ('ममाछापुछ्रे', 'Machhapuchhre'),
 ('माडी', 'Madi'),
 ('रुपा', 'Rupa'),
 ('बेसीशहर', 'Beshisahar'),
 ('मध्यनेपाल', 'Madhyanepal'),
 ('राईनास', 'Rainas'),
 ('सुन्दरबजार', 'Sundarbajar'),
 ('क्व्होलासोथार', 'Kobholasothar'),
 ('दुधपोखरी', 'Dudhpokhari'),
 ('दोर्दी', 'Dordi'),
 ('मर्स्याङदी', 'Marsyandi'),
 ('नार्पा', 'Narpa'),
 ('नासोँ', 'Nashon'),
 ('ङिस्याङ', 'Ngisyang'),
 ('चामे', 'Chame'),
 ('घरपझोङ', 'Gharpajhong'),
 ('थासाङ', 'Thasang'),
 ('लो-घेकर दामोदरकुण्ड', 'Lo-Ghekar Damodarkunda'),
 ('लोमन्थाङ', 'Lomanthang'),
 ('वारागुङ मुक्तिक्षेत्र', 'Barhagaun Muktichhetra'),
 ('बेनी', 'Beni'),
 ('अन्नपूर्णा', 'Annapurna'),
 ('धौलागिरी', 'Dhaulagiri'),
 ('मंगला', 'Mangala'),
 ('मालिका', 'Malika'),
 ('रघुगंगा', 'Raghuganga'),
 ('कावासोती', 'Kawasoti'),
 ('गैंडाकोट', 'Gaindakot'),
 ('देवचुली', 'Devchuli'),
 ('मध्यविन्दु', 'Madhyabindu'),
 ('बौदीकाली', 'Bungdikali'),
 ('बुलिङटार', 'Bulingtar'),
 ('बिनयी', 'Binaie'),
 ('हुप्सेकोट', 'Hupsekot'),
 ('कुश्मा', 'Kushma'),
 ('फलेवास', 'Phalewas'),
 ('जलजला', 'Jaljala'),
 ('पैयूं', 'paiyu'),
 ('महाशिला', 'Mahashila'),
 ('मोदी', 'Modi'),
 ('विहादी', 'Bihadi'),
 ('गल्याङ', 'Galyang'),
 ('चापाकोट', 'Chapkot'),
 ('पुतलीबजार', 'Putalibazar'),
 ('विरकोट', 'Virkot'),
 ('वालिङ', 'Waling'),
 ('अर्जुनचौपरी', 'Arjunchaupari'),
 ('आँधिखोला', 'Aadhikhola'),
 ('कालीगण्डकी', 'Kaligandaki'),
 ('फेदीखोला', 'Fedikhola'),
 ('बिरुवा', 'Biruwa'),
 ('हरिनास', 'Harinas'),
 ('भानु', 'Bhanu'),
 ('भिमाद', 'Bhimad'),
 ('व्यास', 'Byas'),
 ('शुक्लागण्डकी', 'Shuklagandaki'),
 ('आँबुखैरेनी', 'Ambukhaireni'),
 ('ऋषिङ्ग', 'Rhishing'),
 ('घिरिङ', 'Ghiring'),
 ('देवघाट', 'Devghat'),
 ('म्याग्दी', 'Myagdi'),
 ('बन्दिपुर', 'Bandipur'),
  #muncipality of province 5
 ('सन्धिखर्क', 'Sandhikharka'),
 ('शितगंगाा', 'Sitganga'),
 ('भुमिकास्थान', 'Bhumikasthan'),
 ('छत्रदेव', 'Chhatradev'),
 ('पाणिनी', 'Pandini'),
 ('मालारानी', 'Malarani'),
 ('नेपालगञ्ज', 'Nepalgunj'),
 ('कोहोलपुर', 'Koholpur'),
 ('नरैनापुर', 'Narainapur'),
 ('राप्तीसोनारीी', 'Raptisonari'),
 ('बैजनाथ', 'Baijanath'),
 ('खजुरा', 'Khajura'),
 ('डुडुवाा', 'Duduwa'),
 ('जानकी', 'Janaki'),
 ('गुलरिया', 'Gulariya'),
 ('मधुवन', 'Madhuban'),
 ('राजापुर', 'Rajapur'),
 ('ठाकुरबाबा', 'Thakurbaba'),
 ('बाँसगढी', 'Bansgadhi'),
 ('बारबर्दिया', 'Barbardiya'),
 ('बढैयाताल', 'Badhaiyatal'),
 ('गेरुवा', 'Geruwa'),
 ('तुल्सीपुर', 'Tulsipur'),
 ('घोराही', 'Ghorahi'),
 ('लमही', 'Lamahi'),
 ('बंगलाचुली', 'Bangalichuli'),
 ('दंगीशरण', 'Dangisaran'),
 ('गढवा', 'Gadhawa'),
 ('राजपुर', 'Rajpur'),
 ('राप्ती', 'Rapti'),
 ('शान्तिनगर', 'Santinagar'),
 ('बबई', 'Babai'),
 ('मुसिकोट', 'Musikot'),
 ('रेसुंगा', 'Resunga'),
 ('इस्मा', 'Ishma'),
 ('कालीगण्डकी', 'Kaligandaki'),
 ('गुल्मीदरबार', 'Gulmidarbar'),
 ('सत्यवती', 'Satyawoti'),
 ('चन्द्रकोट', 'Chandrakot'),
 ('रुरु', 'Ruru'),
 ('छत्रकोट', 'Chhatrakot'),
 ('धुर्कोट', 'Dhurkot'),
 ('मदाने', 'Madane'),
 ('मालिका', 'Malika'),
 ('कपिलवस्तु', 'Kapilvastu'),
 ('बुद्धभुमी', 'Buddhabhumi'),
 ('शिवराज', 'Shivaraj'),
 ('महाराजगञ्ज', 'Maharajgang'),
 ('कृष्णनगर', 'Krishnanagar'),
 ('बाणगंगा', 'Bandganga'),
 ('मायादेवी', 'Mayadevi'),
 ('यसोधरा', 'Yesodhara'),
 ('विजयनगर', 'Bijayanagar'),
 ('शुद्धोधन', 'Suddhodhan'),
 ('सरावल', 'Sarawal'),
 ('रामग्राम', 'Ramgram'),
 ('सुनवल', 'Sunwal'),
 ('ट्रिबेनिसुस्ता', 'Tribenisusta'),
 ('पाल्हीनन्दन', 'Palhinandan'),
 ('प्रतापपुर', 'Pratappur'),
 ('बर्दघाट', 'Bardghat'),
 ('रामपुर', 'Rampur'),
 ('तानसेन', 'Tansen'),
 ('निस्दी', 'Nisdi'),
 ('पूर्वखोला', 'Purbakhola'),
 ('रम्भा', 'Rambha'),
 ('माथागढी', 'Mathagadi'),
 ('तिनाउ', 'Tinau'),
 ('बगनासकाली', 'Baganaskali'),
 ('रिब्दीकोट', 'Ribdikot'),
 ('रैनादेवी छहरा', 'Rainadevi Chhahara'),
 ('रोल्पा', 'Rolpa'),
 ('त्रिवेणी', 'Tribeni'),
 ('दुईखोली', 'Duikholi'),
 ('माडी', 'Madi'),
 ('रुन्टीगढी', 'Runtigadhi'),
 ('लुङग्री', 'Lungri'),
 ('सुकिदह', 'Sukidaha'),
 ('सुनछहरी', 'Sunchhahari'),
 ('सुवर्णवती', 'Subarnawoti'),
 ('थबाङ', 'Thabang'),
 ('पुथा उत्तरगंगा', 'Putha Uttarganga'),
 ('भूमे', 'Bhume'),
 ('सिस्ने', 'Sisne'),
 ('बुटवल', 'Butwal'),
 ('लुम्बिनी सांस्कृतिक', 'Lumbini Saskritik'),
 ('सिद्धार्थनगर', 'Sidharthanager'),
 ('सम्मरीमाई', 'Sammarimai'),
 ('देवदह', 'Debdaha'),
 ('सैनामैना', 'Sainamaina'),
 ('तिलोत्तमा', 'Tilottma'),
 ('सियारी', 'Siyari'),
 ('गैडहवा', 'Gaidahawa'),
 ('कन्चन', 'Kanchan'),
 ('कोटहीमाई', 'Kotahimai'),
 ('मर्चवारी', 'Marchawari'),
 ('मायादेवी', 'Mayadevi'),
 ('ओमसतिया', 'Omsatiya'),
 ('रोहिणी', 'Rohindi'),
 ('शुद्धोधन', 'Suddodhan'),
 #province 6 muncipalities
('नारायण', 'Narayan'),
 ('दुल्लु', 'Dullu'),
 ('चामुण्डा बिन्द्रासैनी', 'Chamunda Bindrasaini'),
 ('आठबीस', 'Aathbis'),
 ('भगवतीमाई', 'Bhagawatimai'),
 ('गुराँस', 'Gurash'),
 ('डुंगेश्वर', 'Dungeshwar'),
 ('नौमुले', 'Naumule'),
 ('महाबु', 'Mahabu'),
 ('भैरवी', 'Bhairabi'),
 ('ठाँटीकाँध', 'Thatikadh'),
 ('ठूलीभेरी', 'Thuli veri'),
 ('त्रिपुरासुन्दरी', 'Tripurasundari'),
 ('डोल्पा बुद्ध', 'Dolpa buddha'),
 ('शे फोक्सुन्डो', 'She phoksundo'),
 ('जगदुल्ला', 'Jagdulla'),
 ('मुड्केचुला', 'Mudkechula'),
 ('काइके', 'Kaike'),
 ('छार्का ताङसोङ', 'Chharka tangsong'),
 ('सिमकोट', 'Simkot'),
 ('नाम्खा', 'Namkha'),
 ('खार्पुनाथ', 'kharpunath'),
 ('सर्केगाड', 'Surkegad'),
 ('चंखेली', 'Chankheli'),
 ('अदानचुली', 'Adanchuli'),
 ('ताँजाकोट', 'Tajakot'),
 ('भेरी', 'Veri'),
 ('छेडागाड', 'Chhedagad'),
 ('त्रिवेणी नलगाड', 'Tribeni nalgad'),
 ('कुसे', 'Kuse'),
 ('जुनीचाँदे', 'Junichande'),
 ('बारेकोट', 'Barekot'),
 ('शिवालय', 'Shibalaya'),
 ('चन्दननाथ', 'Chandannath'),
 ('कनकासुन्दरी', 'Kankasundari'),
 ('सिंजा', 'Sinja'),
 ('हिमा', 'Hima'),
 ('तिला', 'Tila'),
 ('गुठीचौर', 'Guthichaur'),
 ('तातोपानी', 'Tatopani'),
 ('पातारासी', 'Patarasi'),
 ('खाँडाचक्र', 'Khadachakra'),
 ('रास्कोट', 'Raskot'),
 ('तिलागुफा', 'Tilagupha'),
 ('पाचलझरना', 'Pachaljharana'),
 ('सान्नी त्रिवेणी', 'Sanni tribeni'),
 ('नरहरीनाथ', 'Naraharinath'),
 ('कालिका', 'Kalika'),
 ('महावै', 'Mahabai'),
 ('पलाता', 'Palata'),
 ('मुसिकोट', 'Musikot'),
 ('चौरजहारी', 'Chaurjahari'),
 ('आठबिसकोट', 'Aathabiskot'),
 ('बाँफिकोट', 'Baphikot'),
 ('त्रिवेणी', 'Tribeni'),
 ('सानीभेरी', 'Sanibheri'),
 ('शारदा', 'Sarada'),
 ('बागचौर', 'Bagchaur'),
 ('बनगाँड', 'Bangad'),
 ('कालिमाटी', 'Kalimati'),
 ('त्रिवेणी', 'Tribeni'),
 ('कपुरकोट', 'Kapurkot'),
 ('छत्रेश्वरी', 'Chhatreswori'),
 ('ढोरचौर', 'Dhorchaur'),
 ('कुमाखमालिका', 'Kumakhamalika'),
 ('दार्मा', 'Darma'),
 ('बीरेन्द्र', 'Birendra'),
 ('भेरीगंगा', 'Bheriganga'),
 ('गुर्भाकोट', 'Gurbhakot'),
 ('पञ्चपुरी', 'Pabchapuri'),
 ('लेकबेसी', 'Lekbesi'),
 ('चौकुने', 'Chaukune'),
 ('बराहताल', 'Barahatal'),
 ('चिङ्गाड', 'Chingad'),
 ('सिम्ता', 'Simta'),
#province 7 muncipalities
('मंगलसेन', 'Mangalsen'),
 ('कमलबजार', 'Kamalbajar'),
 ('साँफेवगर', 'Sanphebagar'),
 ('पंचदेवल विनायक', 'Panchadewal Binayak'),
 ('चौरपाटी', 'Chaurpati'),
 ('मेल्लेख', 'Mellekh'),
 ('बान्नीगढी जयगढ', 'Bannigadi Jayagadh'),
 ('रामारोशन', 'Ramaroshan'),
 ('ढकारी', 'Dhakari'),
 ('तुर्माखाँद', 'Turmakhad'),
 ('दशरथचन्द', 'Dashrathachanda'),
 ('पाटन', 'Patan'),
 ('मेलौली', 'Melauli'),
 ('पुर्चौडी', 'Purchaudi'),
 ('सुर्नया', 'Surnaya'),
 ('सिगास', 'Sisag'),
 ('शिवनाथ', 'Shivanath'),
 ('पंचेश्वर', 'Pancheshwar'),
 ('दोगडाकेदार', 'Dogdakedar'),
 ('डीलासैनी', 'Dilasaini'),
 ('जयपृथ्वी', 'jayaprithvi'),
 ('बुंगल', 'Bungal'),
 ('तालकोट', 'Talkot'),
 ('मष्टा', 'Masta'),
 ('खप्तडछान्ना', 'Khaptadchhanna'),
 ('थलारा', 'Thalara'),
 ('वित्थडचिर', 'Bitthadchir'),
 ('सूर्मा', 'Surma'),
 ('छबिसपाथिभेरा', 'Chhabispathibhera'),
 ('दुर्गाथली', 'Durgathali'),
 ('केदारस्युँ', 'Kedarsyun'),
 ('काण्ड', 'Kanda'),
 ('बडिमालिका', 'Badimalika'),
 ('त्रिवेणी', 'Tribeni'),
 ('बुढीगंगा', 'Budhiganga'),
 ('बुढीनन्दा', 'Budhinanda'),
 ('गौमुल', 'Gaumun'),
 ('पाण्डव', 'Pandav'),
 ('स्वामीकार्तिक', 'Swamikartik'),
 ('छेडेदह', 'Chhededaha'),
 ('हिमाली', 'Himali'),
 ('अमरगढी', 'Amargadhi'),
 ('परशुराम', 'Parsuram'),
 ('आलिताल', 'Aalital'),
 ('भागेश्वर', 'Bhageshwar'),
 ('नवदुर्गा', 'nabadurga'),
 ('अजयमेरु', 'Ajayameru'),
 ('गन्यापधुरा', 'Ganyapdhura'),
 ('महाकाली', 'Mahakali'),
 ('शैल्यशिखर', 'Shailyashikar'),
 ('मालिकार्जुन', 'Malikarjun'),
 ('अपिहिमाल', 'Apihimal'),
 ('दुहुँ', 'Duhu'),
 ('नौगाड', 'Naugad'),
 ('मार्मा', 'Marma'),
 ('लेकम', 'Lekam'),
 ('व्याँस', 'Byash'),
 ('दिपायल सिलगढी', 'Dipayal siladhi'),
 ('शिखर', 'Shikhar'),
 ('पूर्वीचौकी', 'Purbichauki'),
 ('बडीकेदार', 'Badikedar'),
 ('जोरायल', 'Jorayal'),
 ('सायल', 'Sayal'),
 ('आदर्श', 'Aadarsh'),
 ('के.आई.सिंह', 'K.I.Singh'),
 ('बोगाटन', 'Bogatan'),
 ('धनगढी', 'Dhangadhi'),
 ('टिकापुर', 'Tikapur'),
 ('घोडाघोडी', 'Ghodaghodi'),
 ('लम्किचुहा', 'Lamkichuha'),
 ('भजनी', 'bhajani'),
 ('गोदावरी', 'Godawari'),
 ('गौरीगंगा', 'Gauriganga'),
 ('जानकी', 'Janaki'),
 ('बर्दगोरिया', 'Bardagoriya'),
 ('मोहन्याल', 'Mohanyal'),
 ('कैलारी', 'Kailari'),
 ('जोशीपुर', 'Joshipur'),
 ('चुरे', 'Chure'),
 ('भिमदत्त', 'bhimdatta'),
 ('पुनर्वास', 'Punarbas'),
 ('बेदकोट', 'Bedkot'),
 ('महाकाली', 'Mahakali'),
 ('शुक्लाफाँट', 'Shuklaphata'),
 ('बेलौरी', 'Belauri'),
 ('कृष्णपुर', 'Krishnapur'),
 ('बेलडाँडी', 'Beldandi'),
 ('लालझाडी', 'Laljhadi'),
#updates on Nepali Letters
('क्','k'),
('ख्','kh'),
('ग्','g'),
('घ्','gh'),
('ङ्','n'),
('च्','ch'),
('छ्','chh'),
('ज्','j'),
('झ्','jh'),
('ञ्','n'),
('ट्','t'),
('ठ्','th'),
('ड्','d'),
('ढ्','dh'),
('ण्','n'),
('त्','t'),
('थ्','th'),
('द्','d'),
('ध्','dh'),
('न्','n'),
('प्','p'),
('फ्','ph'),
('ब्','b'),
('भ्','bh'),
('म्','m'),
('य्','y'),
('र्','r'),
('ल्','l'),
('व्','w'),
('श्','s'),
('ष्','s'),
('स्','s'),
('ह्','h'),
('ष','श'),
('का','ka'),
('को','ko'),
('कौ','kau'),
('कि','ki'),
('की','ki'),
('कु','ku'),
('कू','ku'),
('के','ke'),
('कै','kai'),
('कं','kum'),
('खा','kha'),
('खो','kho'),
('खौ','khau'),
('खि','khi'),
('खी','khi'),
('खु','khu'),
('खू','khu'),
('खे','khe'),
('खै','khai'),
('खं','khum'),
('गा','ga'),
('गो','go'),
('गौ','gau'),
('गि','gi'),
('गी','gi'),
('गु','gu'),
('गू','gu'),
('गे','ge'),
('गै','gai'),
('गं','gum'),
('घा','gha'),
('घो','gho'),
('घौ','ghau'),
('घि','ghi'),
('घी','ghi'),
('घु','ghu'),
('घू','ghu'),
('घे','ghe'),
('घै','ghai'),
('घं','ghum'),
('ङा','na'),
('ङो','no'),
('ङौ','nau'),
('ङि','ni'),
('ङी','ni'),
('ङु','nu'),
('ङू','nu'),
('ङे','ne'),
('ङै','nai'),
('ङं','num'),
('चा','cha'),
('चो','cho'),
('चौ','chau'),
('चि','chi'),
('ची','chi'),
('चु','chu'),
('चू','chu'),
('चे','che'),
('चै','chai'),
('चं','chum'),
('छा','chha'),
('छो','chho'),
('छौ','chhau'),
('छि','chhi'),
('छी','chhi'),
('छु','chhu'),
('छू','chhu'),
('छे','chhe'),
('छै','chhai'),
('छं','chhum'),
('जा','ja'),
('जो','jo'),
('जौ','jau'),
('जि','ji'),
('जी','ji'),
('जु','ju'),
('जू','ju'),
('जे','je'),
('जै','jai'),
('जं','jum'),
('झा','jha'),
('झो','jho'),
('झौ','jhau'),
('झि','jhi'),
('झी','jhi'),
('झु','jhu'),
('झू','jhu'),
('झे','jhe'),
('झै','jhai'),
('झं','jhum'),
('ञा','na'),
('ञो','no'),
('ञौ','nau'),
('ञि','ni'),
('ञी','ni'),
('ञु','nu'),
('ञू','nu'),
('ञे','ne'),
('ञै','nai'),
('ञं','num'),
('टा','ta'),
('टो','to'),
('टौ','tau'),
('टि','ti'),
('टी','ti'),
('टु','tu'),
('टू','tu'),
('टे','te'),
('टै','tai'),
('टं','tum'),
('ठा','tha'),
('ठो','tho'),
('ठौ','thau'),
('ठि','thi'),
('ठी','thi'),
('ठु','thu'),
('ठू','thu'),
('ठे','the'),
('ठै','thai'),
('ठं','thum'),
('डा','da'),
('डो','do'),
('डौ','dau'),
('डि','di'),
('डी','di'),
('डु','du'),
('डू','du'),
('डे','de'),
('डै','dai'),
('डं','dum'),
('ढा','dha'),
('ढो','dho'),
('ढौ','dha'),
('ढि','dhi'),
('ढी','dhi'),
('ढु','dhu'),
('ढू','dhu'),
('ढे','dhe'),
('ढै','dhai'),
('ढं','dhum'),
('ता','ta'),
('तो','to'),
('तौ','tau'),
('ति','ti'),
('ती','ti'),
('तु','tu'),
('तू','tu'),
('ते','te'),
('तै','tai'),
('तं','tum'),
('था','tha'),
('थो','tho'),
('थौ','thau'),
('थि','thi'),
('थी','thi'),
('थु','thu'),
('थू','thu'),
('थे','the'),
('थै','thai'),
('थं','thum'),
('दा','da'),
('दो','do'),
('दौ','dau'),
('दि','di'),
('दी','di'),
('दु','du'),
('दू','du'),
('दे','de'),
('दै','dai'),
('दं','dum'),
('धा','dha'),
('धो','dho'),
('धौ','dhau'),
('धि','dhi'),
('धी','dhi'),
('धु','dhu'),
('धू','dhu'),
('धे','dhe'),
('धै','dhai'),
('धं','dhum'),
('ना','na'),
('नो','no'),
('नौ','nau'),
('नि','ni'),
('नी','ni'),
('नु','nu'),
('नू','nu'),
('ने','ne'),
('नै','nai'),
('नं','num'),
('पा','pa'),
('पो','po'),
('पौ','pau'),
('पि','pi'),
('पी','pi'),
('पु','pu'),
('पू','pu'),
('पे','pe'),
('पै','pai'),
('पं','pum'),
('फा','pha'),
('फो','pho'),
('फौ','phau'),
('फि','phi'),
('फी','phi'),
('फु','phu'),
('फू','phu'),
('फे','phe'),
('फै','phai'),
('फं','phum'),
('बा','ba'),
('बो','bo'),
('बौ','bau'),
('बि','bi'),
('बी','bi'),
('बु','bu'),
('बू','bu'),
('बे','be'),
('बै','bai'),
('बं','bum'),
('भा','bha'),
('भो','bho'),
('भौ','bhau'),
('भि','bhi'),
('भी','bhi'),
('भु','bhu'),
('भू','bhu'),
('भे','bhe'),
('भै','bhai'),
('भं','bhum'),
('मा','ma'),
('मो','mo'),
('मौ','mau'),
('मि','mi'),
('मी','mi'),
('मु','mu'),
('मू','mu'),
('मे','me'),
('मै','mai'),
('मं','mum'),
('या','ya'),
('यो','yo'),
('यौ','yau'),
('यि','yi'),
('यी','yi'),
('यु','yu'),
('यू','yu'),
('ये','ye'),
('यै','yai'),
('यं','yum'),
('रा','ra'),
('रो','ro'),
('रौ','rau'),
('रि','ri'),
('री','ri'),
('रु','ru'),
('रू','ru'),
('रे','re'),
('रै','rai'),
('रं','rum'),
('ला','la'),
('लो','lo'),
('लौ','lau'),
('लि','li'),
('ली','li'),
('लु','lu'),
('लू','lu'),
('ले','le'),
('लै','lai'),
('लं','lum'),
('वा','wa'),
('वो','wo'),
('वौ','wau'),
('वि','wi'),
('वी','wi'),
('वु','wu'),
('वू','wu'),
('वे','we'),
('वै','wai'),
('वं','wum'),
('शा','sha'),
('शो','sho'),
('शौ','shau'),
('शि','shi'),
('शी','shi'),
('शु','shu'),
('शू','shu'),
('शे','she'),
('शै','shai'),
('शं','shum'),
('हा','ha'),
('हो','ho'),
('हौ','hau'),
('हि','hi'),
('ही','hi'),
('हु','hu'),
('हू','hu'),
('हे','he'),
('है','hai'),
('हं','hum'),
('क','ka'),
('ख','kha'),
('ग','ga'),
('घ','gha'),
('ङ','na'),
('च','cha'),
('छ','chha'),
('ज','ja'),
('झ','jha'),
('ञ','na'),
('ट','ta'),
('ठ','tha'),
('ड','da'),
('ढ','dha'),
('ण','na'),
('त','ta'),
('थ','tha'),
('द','da'),
('ध','dha'),
('न','na'),
('प','pa'),
('फ','pha'),
('ब','ba'),
('भ','bha'),
('म','ma'),
('य','ya'),
('र','ra'),
('ल','la'),
('व','wa'),
('स','sa'),
('श','sha'),
('ष','श'),
('ह','ha'),
('ँ','n'),
('ं','m'),
('ः','h'),
('अ','a'),
('आ','aa'),
('इ','i'),
('ई','i'),
('उ','u'),
('ऊ','u'),
('ऋ','ri'),
('ए','e'),
('ऐ','ai'),
('ओ','o'),
('औ','au'),
('ा',''),
('ि','i'),
('ी','i'),
('ु','u'),
('ू','u'),
('ृ','ri'),
('े','e'),
('ै','ai'),
('ो','o'),
('ौ','au'),
('०', '0'),
('१', '1'),
('२', '2'),
('३', '3'),
('४', '4'),
('५', '5'),
('६', '6'),
('७', '7'),
('८', '8'),
('९', '9'),
('।', '.')
])