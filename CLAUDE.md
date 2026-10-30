# Árulók – Halálos kastély: munkakönyvtár

Magyar nyelvű fikciós sorozat. A szabályokat, a hangnemet és a határokat lásd: `projekt/projekt-utasitasok.md`, a szereplők modorát: `projekt/stilusjegyzet.md`, a teendőket: `projekt/teendok.md`.

## Felépítés
- `fejezetek/`: a megjelent fejezetek (`NN-cim.md`), publikusak.
- `projekt/`: nyilvános háttéranyag.
- `privat/`: helyi, git által figyelmen kívül hagyott mappa. Itt van a titkos terv (`titkos-terv.md`), a feliratok (`*.srt`), a feliratokból készült jegyzetek és a szerkesztői javaslatok. Spoilert tartalmaz.

## Szabályok
- A GitHub Pages oldalt a `site/build.py` építi a `fejezetek/` mappából, a `site/menetrend.txt` dátumai szerint (`.github/workflows/pages.yml`, naponta újraépül). A repó nyilvános, az előreolvasás nem gond, de a titkos terv továbbra sem kerülhet bele.
- A `privat/` tartalmát soha ne commitold, ne idézd a nyilvános fájlokban, és ne szivárogtasd ki az olvasói szövegben. Commit előtt nézd meg a `git status` kimenetét.
- Új fejezetnél ellenőrizd a szöveget a `privat/titkos-terv.md` ellen (fair play nyomok, ki mikor esik ki).
- Zoli semmilyen spoilert nem akar kapni, sem a válaszokban, sem munka közben, sem az összegzésekben. Nem nevezhetsz meg árulót, éjszakai áldozatot, nyomot, azt, hogy melyik nyom kihez tartozik, hány áruló szerepel valahol, és semmit, ami a későbbi fejezetekben történik. Az összegzésben csak azt írd le, ami az olvasói szövegben is látszik. Ha egy szöveg a titkos terv miatt nem módosítható, legfeljebb azt mondd: „ezt a részt a titkos terv miatt nem változtathatjuk", név, ok és indoklás nélkül.
- A fejezetek gondolatjele az en-dash (–).
- A tévéműsor nevét és logóját nem használjuk, a Játékmester Szerafin Barnabás.

## Munkamód új fejezethez (tokentakarékos, lépésenként)
A felhasználó ingyenes Claude-ot használ, ezért kevés a token. Ezért: ne olvasd újra a feliratokat és a már megírt fejezeteket, csak amit az adott lépés igényel. Kis módosításhoz Edit-et használj, ne írd újra a teljes fájlt.

A repó **nyilvános**, ezért a `temporary/` mappába és a commit üzenetekbe csak olvasói szöveg és spoilermentes haladási jegyzet kerülhet. A vázlat és a titkos terv módosításai nem.

A titkos terv, a vázlatok és a feliratok jegyzetei a claude.ai Projectben vannak (`claude/titkos-terv.md`, `claude/jegyzetek.md`), nem a repóban. **Két privát fájl van, és minden vázlat és fejezet előtt mindkettőt együtt kell olvasni:** a titkos terv (mi történik) és a jegyzetek (hogyan: minták a feliratokból és cikkekből, Zoli észrevételei és döntései, hangulati ív, tiltások). Minden új input (új felirat, cikk, Zoli észrevétele) a `claude/jegyzetek.md` megfelelő szakaszába kerül, új jegyzetfájl nem készül; ha mintát vagy döntést tartalmaz, a titkos tervbe is beépítjük. Ha két forrás ütközik, az újabb érvényes. Felhőmunkamenetben a `privat/` mappa nincs meg: a Projects eszközzel (`project_search`, `project_read`, `project_write`) érd el őket.

### Lépések
1. **Vázlat.** Előbb olvasd el a `claude/titkos-terv.md`-t és a `claude/jegyzetek.md`-t (együtt, a jegyzetek ellenőrzőlistájával és a titkos terv „Hangulati ív" szakaszának ellenőrzőlistájával). Dolgozd ki a fejezet vázlatát, és minden döntést (próbatétel, szereplők sorsa, a titkos terv módosítása) magad hozz meg a saját belátásod szerint. Ne kérdezd meg Zolit, és ne adj neki lehetőségeket, amelyek közül választania kell, sem a vázlat közben, sem utána. A vázlatot és a titkos terv módosításait a Projectbe mentsd (`claude/NN-vazlat.md`, `claude/titkos-terv.md`), a repóba nem kerülhet, mert spoilert tartalmaz, és a nyilvános repó előzményei a törölt fájlokat is megőrzik. Ha megszakad a munka, a vázlatot onnan olvasd vissza.
2. **Részenkénti írás.** A fejezetet részenként írd a `temporary/NN-cim.md` fájlba. Minden rész után commitold és pushold. A `temporary/allapot.md` spoilermentesen jelzi, hol tartunk (melyik rész kész, mi jön következőként, néhány szóban),, hogy új beszélgetésben (például a tokenek elfogyása után) onnan lehessen folytatni. A vázlatot a Projectben találod. Írás közben is használd együtt a titkos tervet és a `claude/jegyzetek.md`-t (hangulati ív, árulói viszály, minták), ne csak a vázlatnál.
3. **Átolvasás.** Ha a fejezet kész, olvasd át egyszer, és javítsd a következetlenségeket, a nyelvtani hibákat és a magyartalan mondatokat (Edit-tel). Ellenőrizd a szöveget a titkos terv megfelelő részével (fair play nyomok, ki esik ki) és a jegyzetek hangulati ívével is (stressz-szint, árulói viszály, tiltások). Ha lehet, össze kell vonni bekezdéseket, hogy ne legyen túl tagolt a szöveg, mert arról lerí, hogy AI írta.
4. **Lezárás.** Mentsd a kész fejezetet a `fejezetek/` mappába (`NN-cim.md`), frissítsd a `README.md` fejezettáblázatát, a `projekt/teendok.md`-t és vedd fel az új fejezetet a `site/menetrend.txt`-be (heti megjelenési dátummal; az oldal csak az elérkezett dátumú fejezeteket mutatja). A módosult privát jegyzeteket (titkos terv stb.) a Projectben frissítsd. Végül töröld a `temporary/` mappát (`git rm -r temporary`), és commitold, pushold.
5. **Szerzői átolvasás (Zoli).** Zoli átolvassa a kész fejezetet, és rákérdez azokra a mondatokra, amelyek számára rossz magyarsággal íródtak vagy nem értelmezhetők. Minden jelzett mondatnál nézd meg a szövegkörnyezetet (néhány sort előtte és utána, ne az egész fejezetet), mondd el röviden, mi a hiba, és adj egy-két javítási javaslatot, amely a jelenet tartalmához illik. Ha a mondat nyomot hordoz (titkos terv, fair play), a javítás a nyomot ne változtassa meg. Zolinak csak annyit mondj, hogy az adott részt a titkos terv miatt nem változtathatjuk, anélkül, hogy megneveznéd, kihez tartozik a nyom, és mit jelent. Edit-tel csak akkor javíts, ha Zoli kiválasztotta a változatot. A javításokat ne commitold külön, csak ha Zoli kéri. Mielőtt az illusztrációk jönnek, Zoli jelzi, hogy az átolvasással végzett.

A felhasználó kérése: új fejezetet csak akkor kezdj el, ha ő kéri, és ne kérdezgesd, hogy jöhet-e a következő. Ha egy fejezet már folyamatban van, ne kérdezd meg minden lépés után, hogy mehet-e tovább: haladj a lépéseken. A döntéseket (például új szereplő sorsa, a titkos terv módosítása) magad hozod meg, és csak akkor állj meg, ha a fejezet elkészült.

### Illusztrációk
A `kepek/` mappában vannak az illusztrációk promptjai (`FF-SS-cim.md`) és a kész képek. A felhasználó a képeket külső AI-val készíti. Minden kép egy konkrét mondathoz kapcsolódik, a promptfájl ezt idézi. Új fejezetnél a szöveg elkészülte és a szerzői átolvasás (5. lépés) után javasolj és írj 2–4 promptot ugyanebben a formában, és vedd fel a `kepek/README.md` táblázatába. A képeket a fejezet szövegébe nem a lezáráskor, hanem a 6. lépésben szerkesztjük bele (lásd alább).

### 6. lépés: a kész képek beillesztése
Ha Zoli feltöltötte a képeket a `kepek/` mappába (a fájlnév `FF-SS-cim` alapú, a kiterjesztés lehet `.jfif` vagy más), ezt kell tenni:
1. `git pull`, majd nézd meg a `git status` és a `ls kepek` kimenetét, hogy mely képek érkeztek.
2. Nevezd át őket `.jpg`-re (`git mv`; a `.jfif` valódi JPEG, a build `.png` fájlt nem másol ki, `.md`-t és `.svg`-t sem), hogy egységesek legyenek a korábbi képekkel.
3. Nézd meg a képeket (Read): rendben vannak-e, illenek-e a kapcsolódó mondathoz. Ha nem, szólj Zolinak, és ne szerkeszd be.
4. Szerkeszd be a képeket a `fejezetek/NN-cim.md` fájlba, a promptfájl „Kapcsolódó mondat" sorában idézett mondatot tartalmazó bekezdés alá (`![Rövid leírás](../kepek/FF-SS-cim.jpg)`, előtte és utána üres sor). A mondatnak szó szerint meg kell lennie a fejezetben.
5. A `kepek/README.md` táblázatában a „Kész" oszlopba írd: „kész, beszerkesztve". A `projekt/teendok.md` illusztrációs sorát pipáld ki.
6. Futtasd le a `python3 site/build.py` parancsot (a `_site/` mappa git által figyelmen kívül hagyott), ellenőrizd, hogy a képek a `_site/kepek/` alatt ott vannak, majd commit és push.
Zoli kérte: ez a lépés a szerzői átolvasás és az illusztrációk promptjai után jön; akkor kezdd el, amikor a képek megérkeztek, és ne kérdezd meg, hogy jöhet-e.

### Commit
Minden commit üzenete a `Co-Authored-By` és a `Claude-Session` sorokkal végződik, ahogy a környezet előírja. Commit előtt nézd meg a `git status` kimenetét, `privat/` vagy jegyzet ne kerüljön bele.
