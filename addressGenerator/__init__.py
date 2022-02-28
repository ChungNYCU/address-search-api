import random


def getRandomValue(addr):
    n = random.randint(0, len(addr))
    print(addr[n - 1])


def getRandomNumber(title, num):
    print(title + str(random.randint(10000, 99950)))

def getJapanZip():
    print(str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999)))


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
                    "Hiroshima", "Hokkaidō", "Hyōgo", "Ibaraki", "Ishikawa",
                    "Iwate", "Kagawa", "Kagoshima", "Kanagawa", "Kumamoto", "Kyōto", "Kōchi", "Mie", "Miyagi", "Tokyo",
                    "Niigata", "Yamanashi", "Nagasaki", "Saga", "Nagano",
                    "Miyazaki", "Nara", "Okayama", "Okinawa", "Saitama", "Shiga", "Shimane", "Shizuoka", "Tochigi",
                    "Tokushima", "Tottori", "Toyama", "Wakayama", "Yamagata",
                    "Yamaguchi", "Ōita", "Ōsaka"]

japanCities = ['Tokyo', 'Ōsaka', 'Nagoya', 'Yokohama', 'Fukuoka', 'Sapporo', 'Kyōto', 'Kōbe', 'Kawanakajima', 'Saitama',
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
    , 'Hachiōji'
    , 'Utsunomiya'
    , 'Matsuyama'
    , 'Matsudo'
    , 'Higashi-ōsaka'
    , 'Nishinomiya-hama'
    , 'Ōita'
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
    , 'Ōtsu'
    , 'Tokorozawa'
    , 'Tamuramachi-moriyama'
    , 'Kawagoe'
    , 'Iwaki'
    , 'Maebashi'
    , 'Asahikawa'
    , 'Kōchi'
    , 'Naha'
    , 'Yokkaichi'
    , 'Kasugai'
    , 'Akita'
    , 'Ōakashichō'
    , 'Toshima'
    , 'Morioka'
    , 'Fukushima'
    , 'Tsu'
    , 'Aomori'
    , 'Mito'
    , 'Ichihara'
    , 'Fuchū'
    , 'Fukui'
    , 'Minato'
    , 'Hiratsuka'
    , 'Tokushima'
    , 'Shinozaki'
    , 'Hakodate'
    , 'Sōka'
    , 'Yamagata'
    , ',Tsukuba-kenkyūgakuen-toshi'
    , 'Fuji'
    , 'Chigasaki'
    , 'Chōfugaoka'
    , 'Yato'
    , 'Hachimanchō'
    , 'Sato'
    , 'Saga'
    , 'Neya'
    , 'Ageoshimo'
    , 'Minamiōzuma'
    , 'Arakawa'
    , 'Kure'
    , 'Taitō'
    , 'Matsue'
    , 'Yachiyo'
    , 'Ashino'
    , 'Higashi-Hiroshima'
    , 'Naka'
    , 'Suzuka'
    , 'Kamirenjaku'
    , 'Kumagaya'
    , 'Hino'
    , 'Anjōmachi'
    , 'Tottori'
    , 'Jōetsu'
    , 'Kōfu'
    , 'Izuo'
    , 'Tachikawa'
    , 'Narashino'
    , 'Ōbiraki'
    , 'Takaoka'
    , ',Beppuchō'
    , ',Hitachi'
    , 'Izumo'
    , 'Nishio'
    , 'Takaoka'
    , 'Iwata'
    , 'Niiza'
    , 'Ube'
    , 'Matsuzaka'
    , 'Ōgaki'
    , 'Hitachi-Naka'
    , 'Tochigi'
    , 'Kariya'
    , 'Ueda'
    , 'Higashimurayama'
    , 'Kukichūō'
    , 'Sayama'
    , 'Komaki'
    , 'Tama'
    , 'Yonago'
    , 'Iruma'
    , 'Kakamigahara'
    , 'Kusatsu'
    , 'Shimotoda'
    , 'Misato'
    , 'Fukayachō'
    , 'Ishizaki'
    , ',Kuwana'
    , 'Koga'
    , 'Kisarazu'
    , 'Yaizu'
    , 'Inazawa'
    , 'Ōme'
    , 'Zama'
    , 'Narita'
    , 'Abiko'
    , 'Onomichi'
    , 'Kokubunji'
    , 'Seto'
    , 'Ōmiyachō'
    , 'Iizuka'
    , 'Ise'
    , 'Kashiwara'
    , 'Tsuruoka'
    , 'Ebetsu'
    , 'Daitōchō'
    , 'Kadoma'
    , 'Nobeoka'
    , 'Kōnosu']

japanTowns = ['Zaō',
'Yuzawa',
'Yuza',
'Yūsui',
'Yusuhara',
'Yurihama',
'Yura',
'Yunomae',
'Yuni',
'Yugawara',
'Yūbetsu',
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
'Yōrō',
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
'Uryū',
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
'Tōyō',
'Tōyako',
'Tosa',
'Tōnoshō',
'Tonoshō',
'Tone',
'Tomioka',
'Tomika',
'Tomamae',
'Tōma',
'Tokunoshima',
'Tokigawa',
'Tōin',
'Tōhoku',
'Tōgō',
'Togitsu',
'Tōei',
'Tōbetsu',
'Tobe',
'Teshio',
'Teshikaga',
'Tawaramoto',
'Tatsuno',
'Tatsugō',
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
'Suōōshima',
'Sumita',
'Sugito',
'Sue',
'Sotogahama',
'Soeda',
'Sōbetsu',
'Shōwa',
'Shōō',
'Shōnai',
'Shōdoshima',
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
'Shinkamigotō',
'Shinhidaka',
'Shingū',
'Shinchi',
'Shinano',
'Shin',
'Shimosuwa',
'Shimonita',
'Shimokawa',
'Shimoichi',
'Shimogō',
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
'Seirō',
'Seika',
'Saza',
'Sayō',
'Satsuma',
'Satoshō',
'Sasaguri',
'Saroma',
'Sannohe',
'Sangō',
'Samukawa',
'Samani',
'Sakuho',
'Sakawa',
'Sakaki',
'Sakai',
'Sakahogi',
'Sakae',
'Saka',
'Ryūō',
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
'Ōzu',
'Ōzora',
'Ōyodo',
'Ōyamazaki',
'Oyama',
'Ōwani',
'Ōtsuki',
'Ōtsuchi',
'Ōtoyo',
'Otofuke',
'Otobe',
'Ōtō',
'Ōtaki',
'Ōshima',
'Oshamambe',
'Ōsato',
'Ōsakikamijima',
'Ōsaki',
'Ōra',
'Ōno',
'Ono',
'Onjuku',
'Onga',
'Ōnan',
'Onagawa',
'Ōmu',
'Ōmachi',
'Ōma',
'Okutama',
'Okushiri',
'Ōkuma',
'Okuizumo',
'Okoppe',
'Okinoshima',
'Ōki',
'Oketo',
'Okagaki',
'Ojika',
'Ōji',
'Ōizumi',
'Ōiso',
'Ōishida',
'Oirase',
'Ōi',
'Ōi',
'Ōharu',
'Oguni',
'Oguni',
'Ōguchi',
'Ogose',
'Ōgawara',
'Ogawa',
'Ogano',
'Ōe',
'Ōdai',
'Ochi']

for x in range(200):
    #getRandomValue(japanTowns)
    #getRandomNumber("", 200)
    getJapanZip()
