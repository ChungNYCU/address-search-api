import random


def getRandomValue(addr):
    n = random.randint(0, len(addr))
    print(addr[n - 1])
def getRandomNumber(title, num):
    print(title + str(random.randint(0, 100)))
def getRandomEvenNumber():
    print(random.randrange(0, 1000, 2))
def getJapanZip():
    print(str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999)))
def getBrazilZip():
    print(str(random.randint(10000, 99999)) + "-" + str(random.randint(100, 999)))
def getCanadaUnit():
    print(str(random.randint(10, 99)) + "-" + str(random.randint(100, 999)))
def getRandomPostalCode():
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num = len(abc)-1
    randstr = abc[random.randint(0,num)]
    randstr1 = abc[random.randint(0, num)]
    randstr2 = abc[random.randint(0, num)]
    randstr3 = abc[random.randint(0, num)]
    randstr4 = abc[random.randint(0, num)]
    randstr5 = abc[random.randint(0, num)]
    randstr6 = abc[random.randint(0, num)]

    print(randstr+randstr1+randstr2+randstr6+ " " +randstr3+randstr4+randstr5)
def getKoreaZip():
    print(str(random.randint(100, 999)) + "-" + str(random.randint(100, 999)))
countries = ["Brazil", "Canada", "Germany", "India", "Japan", "North and South Korea", "Mexico", "Spain", "UK", "USA"]
usaStates = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN",
             "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM",
             "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA",
             "WI", "WV", "WY"]
usaCities = ["New York", "Los Angelos", "Chicago", "Houston", "Phoenix", "San Antonio", "Philadelphia", "San Diego",
             "Dallas", "Austin", "San Jose", "Fort Worth", "Jacksonville", "Charlotte", "Columbus", "Indianapolis",
             "San Francisco", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", "Oklahoma City",
             "Las Vegas", "Portland", "Detroit", "Memphis"]
japanPrefectures = ["Aichi", "Akita", "Aomori", "Chiba", "Ehime", "Fukui", "Fukuoka", "Fukushima", "Gifu", "Gunma",
                    "Hiroshima", "Hokkaid??", "Hy??go", "Ibaraki", "Ishikawa",
                    "Iwate", "Kagawa", "Kagoshima", "Kanagawa", "Kumamoto", "Ky??to", "K??chi", "Mie", "Miyagi", "Tokyo",
                    "Niigata", "Yamanashi", "Nagasaki", "Saga", "Nagano",
                    "Miyazaki", "Nara", "Okayama", "Okinawa", "Saitama", "Shiga", "Shimane", "Shizuoka", "Tochigi",
                    "Tokushima", "Tottori", "Toyama", "Wakayama", "Yamagata",
                    "Yamaguchi", "??ita", "??saka"]
japanCities = ['Tokyo', '??saka', 'Nagoya', 'Yokohama', 'Fukuoka', 'Sapporo', 'Ky??to', 'K??be', 'Kawanakajima', 'Saitama',
               'Hiroshima', 'Sendai', 'Kitaku'
    , 'Chiba'
    , 'Niigata'
    , 'Hamamatsu'
    , 'Kumamoto'
    , 'Sagamihara'
    , 'Okayama'
    , 'Edogawa'
    , 'Shizuoka'
    , 'Adachi'
    , 'Kagoshima'
    , 'Hachi??ji'
    , 'Utsunomiya'
    , 'Matsuyama'
    , 'Matsudo'
    , 'Higashi-??saka'
    , 'Nishinomiya-hama'
    , '??ita'
    , 'Kanazawa'
    , 'Fukuyama'
    , 'Machida'
    , 'Toyota'
    , 'Takamatsu'
    , 'Toyama'
    , 'Nagasaki'
    , 'Gifu'
    , 'Miyazaki'
    , 'Okazaki'
    , 'Ichinomiya'
    , 'Toyohashi'
    , 'Nagano'
    , 'Wakayama'
    , 'Nara'
    , 'Koshigaya'
    , '??tsu'
    , 'Tokorozawa'
    , 'Tamuramachi-moriyama'
    , 'Kawagoe'
    , 'Iwaki'
    , 'Maebashi'
    , 'Asahikawa'
    , 'K??chi'
    , 'Naha'
    , 'Yokkaichi'
    , 'Kasugai'
    , 'Akita'
    , '??akashich??'
    , 'Toshima'
    , 'Morioka'
    , 'Fukushima'
    , 'Tsu'
    , 'Aomori'
    , 'Mito'
    , 'Ichihara'
    , 'Fuch??'
    , 'Fukui'
    , 'Minato'
    , 'Hiratsuka'
    , 'Tokushima'
    , 'Shinozaki'
    , 'Hakodate'
    , 'S??ka'
    , 'Yamagata'
    , ',Tsukuba-kenky??gakuen-toshi'
    , 'Fuji'
    , 'Chigasaki'
    , 'Ch??fugaoka'
    , 'Yato'
    , 'Hachimanch??'
    , 'Sato'
    , 'Saga'
    , 'Neya'
    , 'Ageoshimo'
    , 'Minami??zuma'
    , 'Arakawa'
    , 'Kure'
    , 'Tait??'
    , 'Matsue'
    , 'Yachiyo'
    , 'Ashino'
    , 'Higashi-Hiroshima'
    , 'Naka'
    , 'Suzuka'
    , 'Kamirenjaku'
    , 'Kumagaya'
    , 'Hino'
    , 'Anj??machi'
    , 'Tottori'
    , 'J??etsu'
    , 'K??fu'
    , 'Izuo'
    , 'Tachikawa'
    , 'Narashino'
    , '??biraki'
    , 'Takaoka'
    , ',Beppuch??'
    , ',Hitachi'
    , 'Izumo'
    , 'Nishio'
    , 'Takaoka'
    , 'Iwata'
    , 'Niiza'
    , 'Ube'
    , 'Matsuzaka'
    , '??gaki'
    , 'Hitachi-Naka'
    , 'Tochigi'
    , 'Kariya'
    , 'Ueda'
    , 'Higashimurayama'
    , 'Kukich????'
    , 'Sayama'
    , 'Komaki'
    , 'Tama'
    , 'Yonago'
    , 'Iruma'
    , 'Kakamigahara'
    , 'Kusatsu'
    , 'Shimotoda'
    , 'Misato'
    , 'Fukayach??'
    , 'Ishizaki'
    , ',Kuwana'
    , 'Koga'
    , 'Kisarazu'
    , 'Yaizu'
    , 'Inazawa'
    , '??me'
    , 'Zama'
    , 'Narita'
    , 'Abiko'
    , 'Onomichi'
    , 'Kokubunji'
    , 'Seto'
    , '??miyach??'
    , 'Iizuka'
    , 'Ise'
    , 'Kashiwara'
    , 'Tsuruoka'
    , 'Ebetsu'
    , 'Dait??ch??'
    , 'Kadoma'
    , 'Nobeoka'
    , 'K??nosu']
japanTowns = ['Za??',
              'Yuzawa',
              'Yuza',
              'Y??sui',
              'Yusuhara',
              'Yurihama',
              'Yura',
              'Yunomae',
              'Yuni',
              'Yugawara',
              'Y??betsu',
              'Yuasa',
              'Yoshitomi',
              'Yoshioka',
              'Yoshinogari',
              'Yoshino',
              'Yoshimi',
              'Yoshika',
              'Yoshida',
              'Yosano',
              'Yoron',
              'Y??r??',
              'Yorii',
              'Yonaguni',
              'Yonabaru',
              'Yokoze',
              'Yokoshibahikari',
              'Yokohama',
              'Yoichi',
              'Yazu',
              'Yasuda',
              'Yaotsu',
              'Yanaizu',
              'Yamatsuri',
              'Yamato',
              'Yamanouchi',
              'Yamanobe',
              'Yamamoto',
              'Yamakita',
              'Yamada',
              'Yakushima',
              'Yakumo',
              'Yakage',
              'Yahaba',
              'Yaese',
              'Yachiyo',
              'Yabuki',
              'Wazuka',
              'Watari',
              'Watarai',
              'Wassamu',
              'Wanouchi',
              'Wakuya',
              'Waki',
              'Wake',
              'Wakasa',
              'Wakasa',
              'Wadomari',
              'Utazu',
              'Ury??',
              'Urausu',
              'Urakawa',
              'Urahoro',
              'Umi',
              'Ujitawara',
              'Ugo',
              'Uchinada',
              'Uchiko',
              'Tsuwano',
              'Tsuruta',
              'Tsurugi',
              'Tsuno',
              'Tsuno',
              'Tsunan',
              'Tsunagi',
              'Tsukigata',
              'Tsubetsu',
              'Tsubata',
              'Toyoyama',
              'Toyoura',
              'Toyotomi',
              'Toyosato',
              'Toyono',
              'Toyokoro',
              'T??y??',
              'T??yako',
              'Tosa',
              'T??nosh??',
              'Tonosh??',
              'Tone',
              'Tomioka',
              'Tomika',
              'Tomamae',
              'T??ma',
              'Tokunoshima',
              'Tokigawa',
              'T??in',
              'T??hoku',
              'T??g??',
              'Togitsu',
              'T??ei',
              'T??betsu',
              'Tobe',
              'Teshio',
              'Teshikaga',
              'Tawaramoto',
              'Tatsuno',
              'Tatsug??',
              'Tateyama',
              'Tateshina',
              'Tarui',
              'Taragi',
              'Tara',
              'Tano',
              'Tanagura',
              'Tamamura',
              'Tamaki',
              'Tako',
              'Takko',
              'Takinoue',
              'Taki',
              'Taketoyo, Mihama',
              'Taketomi',
              'Takatori',
              'Takasu',
              'Takanezawa',
              'Takanabe',
              'Takamori',
              'Takamori',
              'Takahata',
              'Takaharu',
              'Takahama',
              'Takachiho',
              'Taka',
              'Tajiri',
              'Taiwa',
              'Taishi',
              'Taishi',
              'Taiki',
              'Taiki',
              'Taiji',
              'Tagami',
              'Taga',
              'Tadotsu',
              'Tadaoka',
              'Tadami',
              'Tachiarai',
              'Tabuse',
              'Suttsu',
              'Susami',
              'Su????shima',
              'Sumita',
              'Sugito',
              'Sue',
              'Sotogahama',
              'Soeda',
              'S??betsu',
              'Sh??wa',
              'Sh????',
              'Sh??nai',
              'Sh??doshima',
              'Shizukuishi',
              'Shiwa',
              'Shitara',
              'Shisui',
              'Shirosato',
              'Shiroishi',
              'Shiriuchi',
              'Shirataka',
              'Shiraoi',
              'Shiranuka',
              'Shirako',
              'Shirakawa',
              'Shirahama',
              'Shioya',
              'Shintotsukawa',
              'Shintomi',
              'Shintoku',
              'Shinkamigot??',
              'Shinhidaka',
              'Shing??',
              'Shinchi',
              'Shinano',
              'Shin',
              'Shimosuwa',
              'Shimonita',
              'Shimokawa',
              'Shimoichi',
              'Shimog??',
              'Shimizu',
              'Shimizu',
              'Shime',
              'Shimanto',
              'Shimamoto',
              'Shikaoi',
              'Shikama',
              'Shikabe',
              'Shika',
              'Shihoro',
              'Shichinohe',
              'Shichikashuku',
              'Shichigahama',
              'Shibetsu',
              'Shibecha',
              'Shibayama',
              'Shibata',
              'Shari',
              'Shakotan',
              'Setouchi',
              'Setana',
              'Sera',
              'Sekigahara',
              'Seir??',
              'Seika',
              'Saza',
              'Say??',
              'Satsuma',
              'Satosh??',
              'Sasaguri',
              'Saroma',
              'Sannohe',
              'Sang??',
              'Samukawa',
              'Samani',
              'Sakuho',
              'Sakawa',
              'Sakaki',
              'Sakai',
              'Sakahogi',
              'Sakae',
              'Saka',
              'Ry????',
              'Rokunohe',
              'Rishirifuji',
              'Rishiri',
              'Rikubetsu',
              'Rifu',
              'Reihoku',
              'Rebun',
              'Rausu',
              'Ranzan',
              'Rankoshi',
              'Pippu',
              '??zu',
              '??zora',
              '??yodo',
              '??yamazaki',
              'Oyama',
              '??wani',
              '??tsuki',
              '??tsuchi',
              '??toyo',
              'Otofuke',
              'Otobe',
              '??t??',
              '??taki',
              '??shima',
              'Oshamambe',
              '??sato',
              '??sakikamijima',
              '??saki',
              '??ra',
              '??no',
              'Ono',
              'Onjuku',
              'Onga',
              '??nan',
              'Onagawa',
              '??mu',
              '??machi',
              '??ma',
              'Okutama',
              'Okushiri',
              '??kuma',
              'Okuizumo',
              'Okoppe',
              'Okinoshima',
              '??ki',
              'Oketo',
              'Okagaki',
              'Ojika',
              '??ji',
              '??izumi',
              '??iso',
              '??ishida',
              'Oirase',
              '??i',
              '??i',
              '??haru',
              'Oguni',
              'Oguni',
              '??guchi',
              'Ogose',
              '??gawara',
              'Ogawa',
              'Ogano',
              '??e',
              '??dai',
              'Ochi']
brazilProvinces = ['AC',
                   'AL',
                   'AM',
                   'AP',
                   'BA',
                   'CE',
                   'DF',
                   'ES',
                   'GO',
                   'MA',
                   'MG',
                   'MS',
                   'MT',
                   'PA',
                   'PB',
                   'PE',
                   'PI',
                   'PR',
                   'RJ',
                   'RN',
                   'RO',
                   'RR',
                   'RS',
                   'SC',
                   'SE',
                   'SP',
                   'TO']
brazilCities = ['S??o Paulo',
                'Rio de Janeiro',
                'Bras??lia',
                'Salvador',
                'Fortaleza',
                'Belo Horizonte',
                'Manaus',
                'Curitiba',
                'Recife',
                'Goi??nia',
                'Bel??m',
                'Porto Alegre',
                'Guarulhos',
                'Campinas',
                'S??o Lu??s',
                'S??o Gon??alo',
                'Macei??',
                'Duque de Caxias',
                'Campo Grande',
                'Natal',
                'Teresina',
                'S??o Bernardo do Campo',
                'Jo??o Pessoa',
                'Nova Igua??u',
                'S??o Jos?? dos Campos',
                'Santo Andr??',
                'Ribeir??o Preto',
                'Jaboat??o dos Guararapes',
                'Uberl??ndia',
                'Osasco',
                'Sorocaba',
                'Contagem',
                'Aracaju',
                'Feira de Santana',
                'Cuiab??',
                'Joinville',
                'Aparecida de Goi??nia',
                'Londrina',
                'Juiz de Fora',
                'Porto Velho',
                'Ananindeua',
                'Serra',
                'Caxias do Sul',
                'Macap??',
                'Niter??i',
                'Florian??polis',
                'Belford Roxo',
                'Campos dos Goytacazes',
                'Vila Velha',
                'Mau??',
                'S??o Jo??o de Meriti',
                'S??o Jos?? do Rio Preto',
                'Mogi das Cruzes',
                'Betim',
                'Boa Vista',
                'Maring??',
                'Santos',
                'Diadema',
                'Jundia??',
                'Rio Branco',
                'Montes Claros',
                'Campina Grande',
                'Piracicaba',
                'Carapicu??ba',
                'An??polis',
                'Olinda',
                'Cariacica',
                'Bauru',
                'Itaquaquecetuba',
                'S??o Vicente',
                'Vit??ria',
                'Caruaru',
                'Caucaia',
                'Blumenau',
                'Petrolina',
                'Ponta Grossa',
                'Franca',
                'Canoas',
                'Pelotas',
                'Vit??ria da Conquista',
                'Ribeir??o das Neves',
                'Uberaba',
                'Paulista',
                'Praia Grande',
                'Cascavel',
                'S??o Jos?? dos Pinhais',
                'Guaruj??',
                'Taubat??',
                'Palmas',
                'Limeira',
                'Cama??ari',
                'Santar??m',
                'Petr??polis',
                'Mossor??',
                'Suzano',
                'Tabo??o da Serra',
                'Versa Grande',
                'Sumar??',
                'Marab??',
                'Gravata??']
brazilNeighborhood = ['Falc??o',
                      'Favela',
                      'Mangueira',
                      'Morro da Babil??nia',
                      'Morro da Mineira',
                      'Morro da Provid??ncia',
                      'Morro do Estado',
                      'Vidigal, Rio de Janeiro',
                      'Vig??rio Geral',
                      'Vila do Jo??o',
                      'Vila Parisi',
                      'Cantagalo???Pav??o???Pav??ozinho',
                      'Cidade de Deus, Rio de Janeiro',
                      'Complexo do Alem??o',
                      'Ondina, Salvador',
                      'Paju??ara',
                      'Ponta Verde',
                      'Praia do Gunga',
                      'Jati??ca',
                      'Parangaba',
                      'Rodolfo Te??filo, Fortaleza']

canadaProvince = ['AB',
                  'BC',
                  'MB',
                  'NB',
                  'NL',
                  'NT',
                  'NS',
                  'NU',
                  'ON',
                  'PE',
                  'QC',
                  'SK',
                  'YT']
canadaCities = ['Abbotsford',
                'Armstrong',
                'Burnaby',
                'Campbell River',
                'Castlegar',
                'Chilliwack',
                'Colwood',
                'Coquitlam',
                'Courtenay',
                'Cranbrook',
                'Dawson Creek',
                'Delta',
                'Duncan',
                'Enderby',
                'Fernie',
                'Fort St. John',
                'Grand Forks',
                'Greenwood',
                'Kamloops',
                'Kelowna',
                'Kimberley',
                'Langford',
                'Langley',
                'Maple Ridge',
                'Merritt',
                'Mission',
                'Nanaimo',
                'Nelson',
                'New Westminster',
                'North Vancouver',
                'Parksville',
                'Penticton',
                'Pitt Meadows',
                'Port Alberni',
                'Port Coquitlam',
                'Port Moody',
                'Powell River',
                'Prince George',
                'Prince Rupert',
                'Quesnel',
                'Revelstoke',
                'Richmond',
                'Rossland',
                'Salmon Arm',
                'Surrey',
                'Terrace',
                'Trail',
                'Vancouver[a]',
                'Vernon',
                'Victoria[b]',
                'West Kelowna',
                'White Rock',
                'Williams Lake']

germanyCities =['Berlin',
'Hamburg',
'M??nchen',
'K??ln',
'Frankfurt',
'Essen',
'Dortmund',
'Stuttgart',
'D??sseldorf',
'Bremen',
'Hannover',
'Duisburg',
'N??rnberg',
'Leipzig',
'Dresden',
'Bochum',
'Wuppertal',
'Bielefeld',
'Bonn',
'Mannheim',
'Karlsruhe',
'Gelsenkirchen',
'Wiesbaden',
'M??nster',
'M??nchengladbach',
'Chemnitz',
'Augsburg',
'Braunschweig',
'Aachen',
'Krefeld',
'Halle',
'Kiel',
'Magdeburg',
'Oberhausen',
'L??beck',
'Freiburg',
'Hagen',
'Erfurt',
'Kassel',
'Rostock',
'Mainz',
'Hamm',
'Saarbr??cken',
'Herne',
'M??lheim',
'Solingen',
'Osnabr??ck',
'Ludwigshafen',
'Leverkusen',
'Oldenburg',
'Neuss',
'Paderborn',
'Heidelberg',
'Darmstadt',
'Potsdam',
'W??rzburg',
'G??ttingen',
'Regensburg',
'Recklinghausen',
'Bottrop',
'Wolfsburg',
'Heilbronn',
'Ingolstadt',
'Ulm',
'Remscheid',
'Pforzheim',
'Bremerhaven',
'Offenbach',
'F??rth',
'Reutlingen',
'Salzgitter',
'Siegen',
'Gera',
'Koblenz',
'Moers',
'Bergisch Gladbach',
'Cottbus',
'Hildesheim',
'Witten',
'Zwickau',
'Erlangen',
'Iserlohn',
'Trier',
'Kaiserslautern',
'Jena',
'Schwerin',
'G??tersloh',
'Marl',
'L??nen',
'Esslingen',
'Velbert',
'Ratingen',
'D??ren',
'Ludwigsburg',
'Wilhelmshaven',
'Hanau',
'Minden',
'Flensburg',
'Dessau',
'Villingen-Schwenningen']

for x in range(200):
    #getRandomValue(germanyCities)
    # getRandomNumber("", 200)
     #getRandomNumber("Flat No. ",1000)
    # getCanadaUnit()
    #getRandomNumber("Postfach ",999)
    #getKoreaZip()
    getRandomPostalCode();


