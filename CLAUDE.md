# Árulók – Halálos kastély: munkakönyvtár

Magyar nyelvű fikciós sorozat. A szabályokat, a hangnemet és a határokat lásd: `projekt/projekt-utasitasok.md`, a szereplők modorát: `projekt/stilusjegyzet.md`, a teendőket: `projekt/teendok.md`.

## Felépítés
- `fejezetek/`: a megjelent fejezetek (`NN-cim.md`), publikusak.
- `projekt/`: nyilvános háttéranyag.
- `privat/`: helyi, git által figyelmen kívül hagyott mappa. Itt van a titkos terv (`titkos-terv.md`), a feliratok (`*.srt`), a feliratokból készült jegyzetek és a szerkesztői javaslatok. Spoilert tartalmaz.

## Szabályok
- A `privat/` tartalmát soha ne commitold, ne idézd a nyilvános fájlokban, és ne szivárogtasd ki az olvasói szövegben. Commit előtt nézd meg a `git status` kimenetét.
- Új fejezetnél ellenőrizd a szöveget a `privat/titkos-terv.md` ellen (fair play nyomok, ki mikor esik ki).
- A fejezetek gondolatjele az en-dash (–).
- A tévéműsor nevét és logóját nem használjuk, a Játékmester Szerafin Barnabás.

## Munkamód új fejezethez (tokentakarékos, lépésenként)
A felhasználó ingyenes Claude-ot használ, ezért kevés a token. Ezért: ne olvasd újra a feliratokat és a már megírt fejezeteket, csak amit az adott lépés igényel. Kis módosításhoz Edit-et használj, ne írd újra a teljes fájlt.

A repó **nyilvános**, ezért a `temporary/` mappába és a commit üzenetekbe csak olvasói szöveg és spoilermentes haladási jegyzet kerülhet. A vázlat és a titkos terv módosításai nem.

A titkos terv, a vázlatok és a feliratok jegyzetei a claude.ai Projectben vannak (`claude/titkos-terv.md`, `claude/jegyzet-*.md`), nem a repóban. Felhőmunkamenetben a `privat/` mappa nincs meg: a Projects eszközzel (`project_search`, `project_read`, `project_write`) érd el őket.

### Lépések
1. **Vázlat.** Dolgozd ki a fejezet vázlatát, és minden döntést (próbatétel, szereplők sorsa, a titkos terv módosítása) magad hozz meg a saját belátásod szerint. Ne kérdezd meg Zolit, és ne adj neki lehetőségeket, amelyek közül választania kell, sem a vázlat közben, sem utána. A vázlatnak két változata van: a teljes, spoileres vázlat és a titkos terv módosításai a Projectbe kerülnek (`claude/NN-vazlat.md`, `claude/titkos-terv.md`), a spoilermentes vázlat a repóba (`temporary/NN-vazlat.md`). A spoilermentes vázlatban csak az szerepel, ami az olvasói szövegben is elhangzik vagy látszik majd: a jelenetek sorrendje, a próbatétel szabályai, ki mit csinál a jelenetben, a Kerekasztal eredménye. Nem szerepel benne, hogy kik az árulók, ki az éjszakai áldozat, melyik nyom melyik árulóhoz tartozik, és mi következik a későbbi fejezetekben. A repó nyilvános, és a git előzmények a törölt fájlokat is megőrzik, ezért spoiler egyszer sem kerülhet fel. A spoilermentes vázlatot commitold és told fel, mielőtt írni kezdesz, és frissítsd, ahogy a fejezet halad.
2. **Részenkénti írás.** A fejezetet részenként írd a `temporary/NN-cim.md` fájlba. Minden rész után commitold és pushold. A `temporary/allapot.md` spoilermentesen jelzi, hol tartunk (melyik rész kész, mi jön következőként, néhány szóban), és a `temporary/NN-vazlat.md` is ott van, hogy új beszélgetésben (például a tokenek elfogyása után) onnan lehessen folytatni. A teljes vázlatot a Projectben találod.
3. **Átolvasás.** Ha a fejezet kész, olvasd át egyszer, és javítsd a következetlenségeket, a nyelvtani hibákat és a magyartalan mondatokat (Edit-tel). Ellenőrizd a szöveget a titkos terv megfelelő részével (fair play nyomok, ki esik ki).
4. **Lezárás.** Mentsd a kész fejezetet a `fejezetek/` mappába (`NN-cim.md`), frissítsd a `README.md` fejezettáblázatát és a `projekt/teendok.md`-t. A módosult privát jegyzeteket (titkos terv stb.) a Projectben frissítsd. Végül töröld a `temporary/` mappát (`git rm -r temporary`), és commitold, pushold.
5. **Szerzői átolvasás (Zoli).** Zoli átolvassa a kész fejezetet, és rákérdez azokra a mondatokra, amelyek számára rossz magyarsággal íródtak vagy nem értelmezhetők. Minden jelzett mondatnál nézd meg a szövegkörnyezetet (néhány sort előtte és utána, ne az egész fejezetet), mondd el röviden, mi a hiba, és adj egy-két javítási javaslatot, amely a jelenet tartalmához illik. Ha a mondat nyomot hordoz (titkos terv, fair play), szólj, és a javítás a nyomot ne változtassa meg. Edit-tel csak akkor javíts, ha Zoli kiválasztotta a változatot. A javításokat ne commitold külön, csak ha Zoli kéri. Mielőtt az illusztrációk jönnek, Zoli jelzi, hogy az átolvasással végzett.

A felhasználó kérése: új fejezetet csak akkor kezdj el, ha ő kéri, és ne kérdezgesd, hogy jöhet-e a következő. Ha egy fejezet már folyamatban van, ne kérdezd meg minden lépés után, hogy mehet-e tovább: haladj a lépéseken. A döntéseket (például új szereplő sorsa, a titkos terv módosítása) magad hozod meg, és csak akkor állj meg, ha a fejezet elkészült.

### Illusztrációk
A `kepek/` mappában vannak az illusztrációk promptjai (`FF-SS-cim.md`) és a kész képek. A felhasználó a képeket külső AI-val készíti. Minden kép egy konkrét mondathoz kapcsolódik, a promptfájl ezt idézi. Új fejezetnél a szöveg elkészülte és a szerzői átolvasás (5. lépés) után javasolj és írj 2–4 promptot ugyanebben a formában, és vedd fel a `kepek/README.md` táblázatába. A képeket a fejezet szövegébe csak a lezáráskor szerkesszük bele, a kapcsolódó mondat alá.

### Commit
Minden commit üzenete a `Co-Authored-By` és a `Claude-Session` sorokkal végződik, ahogy a környezet előírja. Commit előtt nézd meg a `git status` kimenetét, `privat/` vagy jegyzet ne kerüljön bele.
